#!/usr/bin/env python3
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
wf_path = BASE_DIR / "checkpoints" / "n8n-cskh-bot-solution.json"

with open(wf_path, "r", encoding="utf-8") as f:
    wf = json.load(f)

# Define visual RAG Vector Store, Embeddings, and Gemini LLM Model nodes
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

embeddings_node = {
    "parameters": {
        "modelName": "models/text-embedding-004"
    },
    "id": "embeddings-gemini",
    "name": "Google Gemini Embeddings (RAG)",
    "type": "@n8n/n8n-nodes-langchain.embeddingsGoogleGemini",
    "typeVersion": 1,
    "position": [680, 680]
}

llm_model_node_1 = {
    "parameters": {
        "modelName": "models/gemini-flash-latest",
        "options": {
            "temperature": 0.2
        }
    },
    "id": "model-gemini-llm",
    "name": "Google Gemini Chat Model (LLM)",
    "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
    "typeVersion": 1,
    "position": [1080, 520]
}

llm_model_node_2 = {
    "parameters": {
        "modelName": "models/gemini-flash-latest",
        "options": {
            "temperature": 0.1
        }
    },
    "id": "model-gemini-judge",
    "name": "Google Gemini Model (LLM-as-Judge)",
    "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
    "typeVersion": 1,
    "position": [1320, 520]
}

# Ensure nodes are present in workflow
existing_ids = {n["id"] for n in wf["nodes"]}

# Clean out old ones if any
wf["nodes"] = [n for n in wf["nodes"] if n["id"] not in {"vector-store-rag", "embeddings-gemini", "model-gemini-llm", "model-gemini-judge"}]

wf["nodes"].extend([vector_store_node, embeddings_node, llm_model_node_1, llm_model_node_2])

# Add AI connections for visual RAG architecture
connections = wf.get("connections", {})

connections["Google Gemini Embeddings (RAG)"] = {
    "ai_embedding": [
        [
            {
                "node": "RAG Vector Store (FAQ + Catalog + Policy)",
                "type": "ai_embedding",
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

connections["Google Gemini Chat Model (LLM)"] = {
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

connections["Google Gemini Model (LLM-as-Judge)"] = {
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

wf["connections"] = connections

with open(wf_path, "w", encoding="utf-8") as f:
    json.dump(wf, f, ensure_ascii=False, indent=2)

print("Successfully injected visual RAG Vector Store & Gemini LLM nodes into workflow solution!")
