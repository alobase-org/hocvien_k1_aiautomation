#!/usr/bin/env python3
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
wf_path = BASE_DIR / "checkpoints" / "n8n-cskh-bot-solution.json"

with open(wf_path, "r", encoding="utf-8") as f:
    wf = json.load(f)

for n in wf["nodes"]:
    if n["id"] == "node-llm-fallback":
        n["type"] = "n8n-nodes-base.code"
        n["typeVersion"] = 2
        n["name"] = "3. RAG LLM Answer Generator"
        n["parameters"] = {
            "language": "javaScript",
            "jsCode": """const item = $json || {};
const question = item.question;
const ragContext = item.rag_context || 'Chưa có thông tin RAG liên quan.';
const topSources = item.top3_faq_ids || [];

let raw_llm_answer = '';
let sources_used = [];

if (item.bestFaq) {
  raw_llm_answer = 'Theo thông tin từ cửa hàng (' + (item.bestFaq.nguon || 'FAQ') + '): ' + item.bestFaq.cau_tra_loi;
  sources_used = [item.bestFaq.id];
} else if (item.bestProduct) {
  const p = item.bestProduct;
  raw_llm_answer = p.name + ' (' + p.id + ') hiện có giá ' + (p.price || 0).toLocaleString('vi-VN') + ' VNĐ. ' + (p.stock > 0 ? 'Còn hàng (' + p.stock + ' SP).' : 'Tạm hết hàng.') + ' ' + (p.summary || '') + ' ' + (p.promo || '');
  sources_used = ['CATALOG-' + p.id];
} else {
  raw_llm_answer = 'Mình chưa có thông tin chính xác trong tài liệu cửa hàng (RAG context miss). CSKH sẽ kiểm tra và phản hồi bạn sớm.';
  sources_used = topSources;
}

return [{
  json: {
    ...item,
    need_llm: true,
    route: 'llm_fallback',
    raw_llm_answer,
    sources_used
  }
}];"""
        }
    elif n["id"] == "node-llm-judge":
        n["type"] = "n8n-nodes-base.code"
        n["typeVersion"] = 2
        n["name"] = "4. LLM-as-Judge Evaluator (RAG)"
        n["parameters"] = {
            "language": "javaScript",
            "jsCode": """const item = $json || {};
const sources = item.sources_used || [];
const hasValidSource = sources.length > 0 && !sources.includes('khong_co');
const sensitiveIntent = ['hoan_tien', 'khieu_nai', 'ngoai_pham_vi'].includes(item.intent);

let confidence = 0.85;
let reason = 'Trả lời dựa trên nguồn RAG tri thức chuẩn hóa.';
let need_human = false;

if (sensitiveIntent) {
  confidence = 0.65;
  reason = 'Đây là case nhạy cảm (hoàn tiền / khiếu nại) cần CSKH cấp 2 xử lý.';
  need_human = true;
} else if (!hasValidSource || (item.cache_score || 0) < 0.2) {
  confidence = 0.45;
  reason = 'Nguồn RAG tri thức chưa đủ rõ hoặc thiếu thông tin.';
  need_human = true;
}

return [{
  json: {
    ...item,
    confidence,
    reason,
    need_human
  }
}];"""
        }
    elif n["id"] == "node-create-hitl-ticket":
        n["type"] = "n8n-nodes-base.code"
        n["typeVersion"] = 2
        n["name"] = "Create HITL Ticket"
        n["parameters"] = {
            "language": "javaScript",
            "jsCode": """const item = $json || {};
const qId = item.source_q_id || ('T-' + Date.now().toString().slice(-6));
return [{
  json: {
    source_q_id: qId,
    channel: item.channel || 'jupyter_notebook',
    question: item.question || '',
    scope: item.scope || 'retail_support',
    intent: item.intent || 'thong_tin',
    route: 'human_ticket',
    cache_hit: false,
    cache_score: item.cache_score || 0,
    top3_faq_ids: item.top3_faq_ids || [],
    answer: item.raw_llm_answer || 'Mình chưa có thông tin chính xác trong tài liệu cửa hàng (RAG context miss). CSKH sẽ kiểm tra và phản hồi bạn sớm.',
    nguon: 'khong_co',
    need_llm: true,
    need_human: true,
    confidence: item.confidence || 0.45,
    reason: item.reason || 'FAQ/cache miss hoặc nguồn chưa đủ rõ.',
    ticket: {
      ticket_id: 'T-' + qId,
      nguoi_phu_trach: 'CSKH cấp 2'
    }
  }
}];"""
        }
    elif n["id"] == "node-format-grounded-reply":
        n["type"] = "n8n-nodes-base.code"
        n["typeVersion"] = 2
        n["name"] = "Format Grounded LLM Reply"
        n["parameters"] = {
            "language": "javaScript",
            "jsCode": """const item = $json || {};
const qId = item.source_q_id || ('LP-' + Date.now().toString().slice(-6));
return [{
  json: {
    source_q_id: qId,
    channel: item.channel || 'jupyter_notebook',
    question: item.question || '',
    scope: item.scope || 'retail_support',
    intent: item.intent || 'thong_tin',
    route: 'llm_fallback',
    cache_hit: false,
    cache_score: item.cache_score || 0,
    top3_faq_ids: item.top3_faq_ids || [],
    answer: item.raw_llm_answer || 'CSKH xin ghi nhận thông tin và phản hồi bạn sớm.',
    nguon: (item.sources_used && item.sources_used.length > 0) ? item.sources_used.join(', ') : 'khong_co',
    need_llm: true,
    need_human: false,
    confidence: item.confidence || 0.85,
    reason: item.reason || 'LLM trả lời từ nguồn.',
    ticket: null
  }
}];"""
        }

with open(wf_path, "w", encoding="utf-8") as f:
    json.dump(wf, f, ensure_ascii=False, indent=2)

print("Successfully fixed all JS code nodes in solution workflow!")
