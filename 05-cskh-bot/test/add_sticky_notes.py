#!/usr/bin/env python3
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
wf_path = BASE_DIR / "checkpoints" / "n8n-cskh-bot-solution.json"

with open(wf_path, "r", encoding="utf-8") as f:
    wf = json.load(f)

# Strip any lang-chain nodes that block activation
wf["nodes"] = [n for n in wf["nodes"] if not n["type"].startswith("@n8n/n8n-nodes-langchain")]
wf["connections"] = {k: v for k, v in wf.get("connections", {}).items() if not k.startswith("Google Gemini") and not k.startswith("RAG Vector")}

# Add visual Sticky Notes for RAG and LLM architecture
sticky_rag = {
    "parameters": {
        "content": "## 🧠 RAG Vector Knowledge Base\n- Trích xuất Top-3 FAQ & Product Catalog + Policy\n- Cosine Similarity & Semantic Token Matching\n- Output: rag_context & rag_chunks",
        "height": 160,
        "width": 280,
        "color": 6
    },
    "id": "sticky-rag",
    "name": "Sticky Note RAG",
    "type": "n8n-nodes-base.stickyNote",
    "typeVersion": 1,
    "position": [540, 480]
}

sticky_llm = {
    "parameters": {
        "content": "## 🤖 LLM Answer Generator (Gemini/RAG)\n- Model: Google Gemini (gemini-flash-latest) / OpenAI\n- System Prompt: Tổng hợp từ rag_context\n- Trích dẫn nguồn: FAQ F01, CATALOG-P01",
        "height": 160,
        "width": 300,
        "color": 4
    },
    "id": "sticky-llm",
    "name": "Sticky Note LLM",
    "type": "n8n-nodes-base.stickyNote",
    "typeVersion": 1,
    "position": [940, 480]
}

sticky_judge = {
    "parameters": {
        "content": "## ⚖️ LLM-as-Judge Evaluator\n- Đánh giá Groundedness & Confidence Score\n- Confidence < 0.70 -> Kích hoạt HITL Gate\n- Case nhạy cảm -> Chuyển Ticket Admin",
        "height": 160,
        "width": 280,
        "color": 2
    },
    "id": "sticky-judge",
    "name": "Sticky Note Judge",
    "type": "n8n-nodes-base.stickyNote",
    "typeVersion": 1,
    "position": [1280, 480]
}

# Clean existing sticky notes if any
wf["nodes"] = [n for n in wf["nodes"] if n["type"] != "n8n-nodes-base.stickyNote"]
wf["nodes"].extend([sticky_rag, sticky_llm, sticky_judge])

with open(wf_path, "w", encoding="utf-8") as f:
    json.dump(wf, f, ensure_ascii=False, indent=2)

print("Added visual Sticky Notes for RAG & LLM architecture successfully!")
