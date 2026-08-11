#!/usr/bin/env python3
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
wf_path = BASE_DIR / "checkpoints" / "n8n-cskh-bot-solution.json"

with open(wf_path, "r", encoding="utf-8") as f:
    wf = json.load(f)

# Define native n8n AI Model and Vector Store sub-nodes
ai_model_node_1 = {
    "parameters": {
        "modelName": "models/gemini-flash-latest",
        "options": {
            "temperature": 0.2,
            "topP": 0.95
        }
    },
    "id": "model-gemini-llm",
    "name": "Google Gemini Model (LLM)",
    "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
    "typeVersion": 1,
    "position": [1080, 520]
}

ai_model_node_2 = {
    "parameters": {
        "modelName": "models/gemini-flash-latest",
        "options": {
            "temperature": 0.1,
            "topP": 0.95
        }
    },
    "id": "model-gemini-judge",
    "name": "Google Gemini Model (Judge Evaluator)",
    "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
    "typeVersion": 1,
    "position": [1320, 520]
}

vector_store_node = {
    "parameters": {
        "mode": "retrieve",
        "options": {
            "topK": 3
        }
    },
    "id": "vector-store-rag",
    "name": "RAG Vector Store (FAQ + Catalog + Policy)",
    "type": "@n8n/n8n-nodes-langchain.vectorStoreInMemory",
    "typeVersion": 1,
    "position": [680, 520]
}

# Add nodes if they don't already exist
node_ids = {n["id"] for n in wf["nodes"]}
if "model-gemini-llm" not in node_ids:
    wf["nodes"].append(ai_model_node_1)
if "model-gemini-judge" not in node_ids:
    wf["nodes"].append(ai_model_node_2)
if "vector-store-rag" not in node_ids:
    wf["nodes"].append(vector_store_node)

# Set node 3 (LLM Generator) & node 4 (LLM Judge) to LLM Chain type
for n in wf["nodes"]:
    if n["id"] == "node-llm-fallback":
        n["type"] = "@n8n/n8n-nodes-langchain.chainLlm"
        n["typeVersion"] = 1.4
        n["name"] = "3. RAG LLM Answer Generator"
        n["parameters"] = {
            "promptType": "define",
            "text": "={{ $json.question }}",
            "hasOutputParser": False,
            "messages": {
                "messageValues": [
                    {
                        "role": "system",
                        "message": "Bạn là trợ lý CSKH Retail Care. Hãy tổng hợp câu trả lời cho khách hàng dựa trên RAG Context được trích xuất từ kho tri thức (FAQ, Catalog, Chính sách):\n\n--- RAG CONTEXT ---\n={{ $json.rag_context }}\n--- END RAG CONTEXT ---\n\nYêu cầu: Trả lời ngắn gọn, lịch sự, chính xác bằng tiếng Việt. Ghi rõ nguồn trích dẫn (ví dụ: [FAQ F01], [CATALOG-P01], [Chính sách Giao nhận]). Nếu không có thông tin trong RAG Context, trả lời lịch sự rằng CSKH sẽ kiểm tra và phản hồi lại."
                    }
                ]
            }
        }
    elif n["id"] == "node-llm-judge":
        n["type"] = "@n8n/n8n-nodes-langchain.chainLlm"
        n["typeVersion"] = 1.4
        n["name"] = "4. LLM-as-Judge Evaluator (RAG)"
        n["parameters"] = {
            "promptType": "define",
            "text": "={{ $json.question }}",
            "hasOutputParser": False,
            "messages": {
                "messageValues": [
                    {
                        "role": "system",
                        "message": "Bạn là LLM-as-Judge đánh giá độ tin cậy (Groundedness & Confidence) của câu trả lời CSKH dựa trên RAG Context.\n\nĐộ tin cậy = 0.85-0.95 nếu có nguồn RAG rõ ràng.\nĐộ tin cậy = 0.45-0.65 (cần chuyển người HITL) nếu là case nhạy cảm (hoàn tiền, khiếu nại) hoặc thiếu nguồn RAG."
                    }
                ]
            }
        }

# Update connections for AI sub-nodes
connections = wf.get("connections", {})
connections["Google Gemini Model (LLM)"] = {
    "ai_languageModel": [
        [
            {
                "node": "3. RAG LLM Answer Generator",
                "type": "ai_languageModel",
                "index": 0
            }
        ]
    ]
}
connections["Google Gemini Model (Judge Evaluator)"] = {
    "ai_languageModel": [
        [
            {
                "node": "4. LLM-as-Judge Evaluator (RAG)",
                "type": "ai_languageModel",
                "index": 0
            }
        ]
    ]
}
connections["RAG Vector Store (FAQ + Catalog + Policy)"] = {
    "ai_vectorStore": [
        [
            {
                "node": "2. RAG Knowledge & Vector Search",
                "type": "ai_vectorStore",
                "index": 0
            }
        ]
    ]
}

wf["connections"] = connections

with open(wf_path, "w", encoding="utf-8") as f:
    json.dump(wf, f, ensure_ascii=False, indent=2)

print("Updated solution workflow with Native n8n LangChain AI & Vector Store nodes!")
