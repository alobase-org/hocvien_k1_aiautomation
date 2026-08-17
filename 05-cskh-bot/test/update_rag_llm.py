#!/usr/bin/env python3
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
wf_path = BASE_DIR / "checkpoints" / "n8n-cskh-bot-solution.json"

with open(wf_path, "r", encoding="utf-8") as f:
    wf = json.load(f)

for node in wf["nodes"]:
    if node["id"] == "node-cache-match":
        node["parameters"]["jsCode"] = """const item = $json;
const question = item.question;
const nq = item.normalized_question;

function normalize(text) {
  return String(text || '')
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\\u0300-\\u036f]/g, '')
    .replace(/đ/g, 'd')
    .replace(/Đ/g, 'd')
    .replace(/[^a-z0-9\\s]/g, ' ')
    .replace(/\\s+/g, ' ')
    .trim();
}

let products = Array.isArray(item.products_override) && item.products_override.length > 0 ? item.products_override : [];
let faq = Array.isArray(item.faq_override) && item.faq_override.length > 0 ? item.faq_override : [];

if (!products || products.length === 0) {
  try {
    const fs = require('fs');
    const path = require('path');
    const possibleProductPaths = [
      path.join(process.cwd(), 'templates', 'products.json'),
      path.join(process.cwd(), 'giang-day', '05-thuc-hanh', '05-cskh-bot', 'templates', 'products.json'),
      path.join(__dirname, '..', 'templates', 'products.json'),
      path.join(__dirname, 'templates', 'products.json')
    ];
    for (const p of possibleProductPaths) {
      if (fs.existsSync(p)) {
        products = JSON.parse(fs.readFileSync(p, 'utf8'));
        break;
      }
    }
  } catch (e) {}
}

if (!faq || faq.length === 0) {
  try {
    const fs = require('fs');
    const path = require('path');
    const possibleFaqPaths = [
      path.join(process.cwd(), 'templates', 'faq.json'),
      path.join(process.cwd(), 'giang-day', '05-thuc-hanh', '05-cskh-bot', 'templates', 'faq.json'),
      path.join(__dirname, '..', 'templates', 'faq.json'),
      path.join(__dirname, 'templates', 'faq.json')
    ];
    for (const p of possibleFaqPaths) {
      if (fs.existsSync(p)) {
        faq = JSON.parse(fs.readFileSync(p, 'utf8'));
        break;
      }
    }
  } catch (e) {}
}

if (!products || products.length === 0) {
  products = [
    { id: 'P01', name: 'Tai nghe Bluetooth AirBeat Lite', aliases: ['tai nghe', 'airbeat', 'bluetooth', 'headphone', 'airbeat lite'], category: 'Âm thanh', price: 690000, stock: 18, warranty_months: 12, summary: 'Tai nghe Bluetooth pin 28 giờ, chống nước IPX4, phù hợp đi làm và luyện tập.', promo: 'Giảm 10% khi mua kèm cáp sạc USB-C.' },
    { id: 'P02', name: 'Bình giữ nhiệt Inox 750ml', aliases: ['binh giu nhiet', 'inox', '750ml', 'binh nuoc', 'binh inox'], category: 'Gia dụng', price: 320000, stock: 42, warranty_months: 6, summary: 'Bình inox 304 giữ nóng/lạnh 8-12 giờ, nắp chống tràn, có 3 màu.', promo: 'Mua 2 bình giảm thêm 5%.' },
    { id: 'P03', name: 'Bàn phím cơ MiniKey K68', aliases: ['ban phim', 'minikey', 'k68', 'ban phim co', 'keyboard'], category: 'Phụ kiện máy tính', price: 890000, stock: 0, warranty_months: 12, summary: 'Bàn phím cơ layout 68 phím, kết nối Bluetooth/USB-C, switch tactile.', promo: 'Đang hết hàng, có thể để lại SĐT để CSKH báo khi về hàng.' },
    { id: 'P04', name: 'Máy xay sinh tố BlendGo 500W', aliases: ['may xay', 'blendgo', 'sinh to', 'may xay sinh to', 'blendgo 500w'], category: 'Gia dụng điện', price: 1250000, stock: 9, warranty_months: 12, summary: 'Máy xay 500W, cối thủy tinh 1.5L, có 3 tốc độ và chế độ nhồi.', promo: 'Tặng bộ ly thủy tinh cho đơn trong tuần này.' }
  ];
}

if (!faq || faq.length === 0) {
  faq = [
    { id: 'F01', nhom: 'don_hang', intent: 'thong_tin', cau_hoi: 'Tôi đặt hàng rồi, khi nào được giao?', cau_tra_loi: 'Đơn nội thành giao trong 24-48 giờ; đơn tỉnh giao trong 3-5 ngày làm việc.', nguon: 'Mục 1. Giao nhận' },
    { id: 'F02', nhom: 'don_hang', intent: 'thong_tin', cau_hoi: 'Tôi muốn kiểm tra trạng thái đơn hàng thì làm sao?', cau_tra_loi: 'Gửi mã đơn hàng qua Zalo CSKH hoặc tra cứu tại trang theo dõi đơn. CSKH phản hồi trong 2 giờ làm việc.', nguon: 'Mục 1. Giao nhận' },
    { id: 'F03', nhom: 'don_hang', intent: 'gia', cau_hoi: 'Có phí giao hàng không?', cau_tra_loi: 'Miễn phí giao hàng cho đơn từ 500.000 VNĐ trong nội thành. Đơn dưới mức này tính phí theo đối tác vận chuyển.', nguon: 'Mục 1. Giao nhận' },
    { id: 'F04', nhom: 'thanh_toan', intent: 'gia', cau_hoi: 'Có những hình thức thanh toán nào?', cau_tra_loi: 'Khách có thể thanh toán COD, chuyển khoản ngân hàng, thẻ nội địa hoặc ví điện tử.', nguon: 'Mục 2. Thanh toán' },
    { id: 'F05', nhom: 'thanh_toan', intent: 'thong_tin', cau_hoi: 'Tôi chuyển khoản xong rồi, sao chưa thấy xác nhận?', cau_tra_loi: 'Gửi mã đơn hàng và mã giao dịch qua Zalo CSKH. Xác nhận trong 2 giờ làm việc.', nguon: 'Mục 2. Thanh toán' },
    { id: 'F06', nhom: 'thanh_toan', intent: 'gia', cau_hoi: 'Có xuất hóa đơn VAT không?', cau_tra_loi: 'Có. Gửi email cskh@demo.vn kèm thông tin công ty trong vòng 24 giờ sau khi đặt hàng.', nguon: 'Mục 2. Thanh toán' },
    { id: 'F07', nhom: 'doi_tra', intent: 'thong_tin', cau_hoi: 'Tôi muốn đổi size hoặc đổi màu sản phẩm thì được không?', cau_tra_loi: 'Được đổi trong 7 ngày nếu sản phẩm chưa qua sử dụng, còn tem nhãn và hóa đơn.', nguon: 'Mục 3. Đổi trả' },
    { id: 'F08', nhom: 'doi_tra', intent: 'thong_tin', cau_hoi: 'Sản phẩm bị lỗi do nhà sản xuất thì xử lý thế nào?', cau_tra_loi: 'CSKH tiếp nhận hình ảnh/video lỗi và chuyển bộ phận kiểm tra. Nếu lỗi xác nhận từ nhà sản xuất, khách được đổi mới hoặc hoàn tiền theo chính sách.', nguon: 'Mục 3. Đổi trả' },
    { id: 'F09', nhom: 'doi_tra', intent: 'hoan_tien', cau_hoi: 'Tôi không thích sản phẩm nữa, có được hoàn tiền không?', cau_tra_loi: 'Trường hợp đổi ý cá nhân chỉ hỗ trợ đổi sản phẩm trong 7 ngày nếu đủ điều kiện; hoàn tiền cần CSKH cấp 2 xem xét.', nguon: 'Mục 3. Đổi trả' },
    { id: 'F10', nhom: 'bao_hanh', intent: 'ky_thuat', cau_hoi: 'Sản phẩm được bảo hành bao lâu?', cau_tra_loi: 'Sản phẩm điện tử và phụ kiện chính hãng được bảo hành 12 tháng theo số serial hoặc hóa đơn.', nguon: 'Mục 4. Bảo hành' },
    { id: 'F11', nhom: 'bao_hanh', intent: 'ky_thuat', cau_hoi: 'Tôi cần gửi sản phẩm đi bảo hành thì làm sao?', cau_tra_loi: 'Gửi mã đơn hàng, mô tả lỗi và hình ảnh/video qua Zalo CSKH. CSKH cấp mã tiếp nhận trong 1 ngày làm việc.', nguon: 'Mục 4. Bảo hành' },
    { id: 'F12', nhom: 'bao_hanh', intent: 'ky_thuat', cau_hoi: 'Sản phẩm rơi vỡ có được bảo hành không?', cau_tra_loi: 'Không bảo hành lỗi do rơi vỡ, vào nước hoặc sử dụng sai hướng dẫn.', nguon: 'Mục 4. Bảo hành' },
    { id: 'F13', nhom: 'khieu_nai', intent: 'khieu_nai', cau_hoi: 'Tôi muốn khiếu nại thái độ giao hàng.', cau_tra_loi: 'Gửi mã đơn hàng và nội dung khiếu nại tới cskh@demo.vn, tiêu đề Khiếu nại. Xử lý trong 3 ngày làm việc.', nguon: 'Mục 5. Khiếu nại' },
    { id: 'F14', nhom: 'lien_he', intent: 'thong_tin', cau_hoi: 'Tôi muốn liên hệ trực tiếp thì sao?', cau_tra_loi: 'Zalo CSKH 0900.000.123 (8:00-20:00) hoặc email cskh@demo.vn.', nguon: 'Mục 6. Liên hệ' },
    { id: 'F15', nhom: 'lien_he', intent: 'hoan_tien', cau_hoi: 'Khiếu nại hoàn tiền liên hệ ai?', cau_tra_loi: 'Đội CSKH cấp 2 xử lý khiếu nại hoàn tiền qua hotline 0900.000.456 hoặc email cskh@demo.vn.', nguon: 'Mục 5 + 6' },
    { id: 'F16', nhom: 'san_pham', intent: 'san_pham', cau_hoi: 'Cho xin danh sách sản phẩm / Shop đang bán những sản phẩm nào?', cau_tra_loi: 'Cửa hàng đang có: P01 Tai nghe Bluetooth AirBeat Lite (690k), P02 Bình giữ nhiệt Inox 750ml (320k), P03 Bàn phím cơ MiniKey K68 (890k), P04 Máy xay BlendGo 500W (1.250k).', nguon: 'Mục 1. Danh mục Sản phẩm Tổng quan' }
  ];
}

const STOP_WORDS = new Set(['co', 'khong', 'gi', 'thi', 'duoc', 'cho', 'minh', 'toi', 'hoi', 'vay', 'shop', 'cua', 'hang', 'nhung', 'nao', 'la', 'sao', 'va']);

function tokenScore(a, b) {
  const ta = new Set(normalize(a).split(' ').filter(w => w && !STOP_WORDS.has(w)));
  const tb = new Set(normalize(b).split(' ').filter(w => w && !STOP_WORDS.has(w)));
  if (!ta.size || !tb.size) return 0;
  let hit = 0;
  for (const t of ta) if (tb.has(t)) hit++;
  return hit / Math.sqrt(ta.size * tb.size);
}

function productScore(product, text) {
  const haystack = normalize([product.id, product.name, product.category, product.summary, (product.aliases || []).join(' ')].join(' '));
  return Math.max(tokenScore(text, haystack), (product.aliases || []).some(alias => text.includes(normalize(alias))) ? 0.9 : 0);
}

const productMatches = products
  .map(p => ({ ...p, score: productScore(p, nq) }))
  .sort((a, b) => b.score - a.score);
const bestProduct = productMatches[0];
const productHit = bestProduct && bestProduct.score >= 0.28;

const ranked = faq
  .map(f => ({ ...f, score: Math.max(tokenScore(question, f.cau_hoi), tokenScore(question, `${f.cau_hoi} ${f.cau_tra_loi}`)) }))
  .sort((a, b) => b.score - a.score);
const bestFaq = ranked[0];
const top3_faq_ids = ranked.slice(0, 3).map(f => f.id);
const semanticHit = bestFaq && bestFaq.score >= 0.25;

const is_catalog_overview = /danh sach|catalog|danh muc|shop co san pham nao|ban nhung san pham|cho xin/.test(nq);
const is_product_intent = item.intent === 'san_pham' || item.intent === 'dat_mua';
const cache_hit = (semanticHit || productHit || is_product_intent) && !['ngoai_pham_vi'].includes(item.intent);

// Construct RAG Context Chunks for LLM Generation
const rag_chunks = [];
if (bestFaq) rag_chunks.push(`[FAQ ${bestFaq.id}]: ${bestFaq.cau_hoi} -> ${bestFaq.cau_tra_loi} (Nguồn: ${bestFaq.nguon})`);
if (ranked[1]) rag_chunks.push(`[FAQ ${ranked[1].id}]: ${ranked[1].cau_hoi} -> ${ranked[1].cau_tra_loi}`);
if (bestProduct) rag_chunks.push(`[PRODUCT ${bestProduct.id}]: ${bestProduct.name} - Giá: ${bestProduct.price} VNĐ. Tồn kho: ${bestProduct.stock}. ${bestProduct.summary} (${bestProduct.promo})`);

const rag_context = rag_chunks.join('\\n');

return [{
  json: {
    ...item,
    cache_hit,
    cache_score: Number((is_product_intent ? (bestProduct ? bestProduct.score : 1) : (bestFaq ? bestFaq.score : 0)).toFixed(2)),
    bestFaq: semanticHit ? bestFaq : null,
    bestProduct: (productHit && !is_catalog_overview) ? bestProduct : null,
    is_catalog_overview,
    products,
    top3_faq_ids,
    is_product_intent,
    rag_context,
    rag_chunks
  }
}];"""

    elif node["id"] == "node-llm-fallback":
        node["parameters"]["jsCode"] = """const item = $json;
const question = item.question;
const ragContext = item.rag_context || 'Chưa có thông tin RAG liên quan.';
const topSources = item.top3_faq_ids || [];

// Synthesize source-grounded response using RAG Knowledge Context
let raw_llm_answer = '';
let sources_used = [];

if (item.bestFaq) {
  raw_llm_answer = `Theo thông tin từ cửa hàng (${item.bestFaq.nguon}): ${item.bestFaq.cau_tra_loi}`;
  sources_used = [item.bestFaq.id];
} else if (item.bestProduct) {
  const p = item.bestProduct;
  raw_llm_answer = `${p.name} (${p.id}) hiện có giá ${p.price.toLocaleString('vi-VN')} VNĐ. ${p.stock > 0 ? 'Còn hàng (' + p.stock + ' SP).' : 'Tạm hết hàng.'} ${p.summary} ${p.promo}`;
  sources_used = [`CATALOG-${p.id}`];
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

    elif node["id"] == "node-llm-judge":
        node["parameters"]["jsCode"] = """const item = $json;
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
} else if (!hasValidSource || item.cache_score < 0.2) {
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

with open(wf_path, "w", encoding="utf-8") as f:
    json.dump(wf, f, ensure_ascii=False, indent=2)

print("Updated RAG & LLM Fallback + LLM-as-Judge nodes successfully!")
