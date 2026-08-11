#!/usr/bin/env python3
import argparse
import hashlib
import json
import math
import re
import sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

TEST_DIR = Path(__file__).parent.resolve()
BASE_DIR = TEST_DIR.parent.resolve()
DB_PATH = TEST_DIR / "cskh_vector_store.sqlite3"
FAQ_PATH = BASE_DIR / "templates" / "faq.json"
PRODUCTS_PATH = BASE_DIR / "templates" / "products.json"
DIM = 192
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8095

STOP_WORDS = {
    "co", "khong", "gi", "thi", "duoc", "cho", "minh", "toi", "hoi",
    "vay", "shop", "cua", "hang", "nhung", "nao", "la", "sao", "va",
}


def normalize(text):
    value = str(text or "").lower()
    replacements = {
        "đ": "d",
        "á": "a", "à": "a", "ả": "a", "ã": "a", "ạ": "a",
        "ă": "a", "ắ": "a", "ằ": "a", "ẳ": "a", "ẵ": "a", "ặ": "a",
        "â": "a", "ấ": "a", "ầ": "a", "ẩ": "a", "ẫ": "a", "ậ": "a",
        "é": "e", "è": "e", "ẻ": "e", "ẽ": "e", "ẹ": "e",
        "ê": "e", "ế": "e", "ề": "e", "ể": "e", "ễ": "e", "ệ": "e",
        "í": "i", "ì": "i", "ỉ": "i", "ĩ": "i", "ị": "i",
        "ó": "o", "ò": "o", "ỏ": "o", "õ": "o", "ọ": "o",
        "ô": "o", "ố": "o", "ồ": "o", "ổ": "o", "ỗ": "o", "ộ": "o",
        "ơ": "o", "ớ": "o", "ờ": "o", "ở": "o", "ỡ": "o", "ợ": "o",
        "ú": "u", "ù": "u", "ủ": "u", "ũ": "u", "ụ": "u",
        "ư": "u", "ứ": "u", "ừ": "u", "ử": "u", "ữ": "u", "ự": "u",
        "ý": "y", "ỳ": "y", "ỷ": "y", "ỹ": "y", "ỵ": "y",
    }
    for src, dst in replacements.items():
        value = value.replace(src, dst)
    value = re.sub(r"[^a-z0-9\s]", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def tokens(text):
    return [t for t in normalize(text).split() if t and t not in STOP_WORDS]


def embed(text):
    vec = [0.0] * DIM
    for token in tokens(text):
        digest = hashlib.sha256(token.encode("utf-8")).digest()
        idx = int.from_bytes(digest[:2], "big") % DIM
        sign = 1.0 if digest[2] % 2 == 0 else -1.0
        vec[idx] += sign
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [round(v / norm, 6) for v in vec]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute(
        """
        create table if not exists documents (
          id text primary key,
          doc_type text not null,
          text text not null,
          metadata_json text not null,
          vector_json text not null,
          updated_at text default current_timestamp
        )
        """
    )
    return conn


def upsert_document(doc_id, doc_type, text, metadata):
    vector = embed(text)
    with connect() as conn:
        conn.execute(
            """
            insert into documents(id, doc_type, text, metadata_json, vector_json, updated_at)
            values (?, ?, ?, ?, ?, current_timestamp)
            on conflict(id) do update set
              doc_type=excluded.doc_type,
              text=excluded.text,
              metadata_json=excluded.metadata_json,
              vector_json=excluded.vector_json,
              updated_at=current_timestamp
            """,
            (doc_id, doc_type, text, json.dumps(metadata, ensure_ascii=False), json.dumps(vector)),
        )


def delete_document(doc_id):
    with connect() as conn:
        cur = conn.execute("delete from documents where id = ?", (doc_id,))
        return cur.rowcount


def all_documents():
    with connect() as conn:
        rows = conn.execute("select * from documents order by doc_type, id").fetchall()
    return [row_to_doc(row) for row in rows]


def row_to_doc(row):
    return {
        "id": row["id"],
        "doc_type": row["doc_type"],
        "text": row["text"],
        "metadata": json.loads(row["metadata_json"]),
        "vector": json.loads(row["vector_json"]),
        "updated_at": row["updated_at"],
    }


def seed(reset=False):
    if reset and DB_PATH.exists():
        DB_PATH.unlink()
    with connect() as conn:
        count = conn.execute("select count(*) from documents").fetchone()[0]
    if count and not reset:
        return count

    faq = json.loads(FAQ_PATH.read_text(encoding="utf-8"))
    products = json.loads(PRODUCTS_PATH.read_text(encoding="utf-8"))
    for item in faq:
        text = f"{item['cau_hoi']}\n{item['cau_tra_loi']}\nNguồn: {item['nguon']}"
        upsert_document(item["id"], "faq", text, item)
    for item in products:
        aliases = " ".join(item.get("aliases", []))
        text = (
            f"{item['id']} {item['name']} {aliases}\n"
            f"Danh mục: {item.get('category')}\n"
            f"Giá: {item.get('price')} VNĐ. Tồn kho: {item.get('stock')}. "
            f"Bảo hành {item.get('warranty_months')} tháng. "
            f"{item.get('summary')} {item.get('promo')}"
        )
        upsert_document(item["id"], "product", text, item)
    return len(faq) + len(products)


def product_score(product, query_text):
    nq = normalize(query_text)
    fields = [
        product.get("id"),
        product.get("name"),
        product.get("category"),
        product.get("summary"),
        " ".join(product.get("aliases", [])),
    ]
    hay = " ".join(tokens(" ".join(str(f or "") for f in fields)))
    query_tokens = set(tokens(nq))
    hay_tokens = set(hay.split())
    overlap = len(query_tokens & hay_tokens) / math.sqrt((len(query_tokens) or 1) * (len(hay_tokens) or 1))
    alias_hit = any(normalize(alias) in nq for alias in product.get("aliases", []))
    id_hit = normalize(product.get("id")) in nq
    return max(overlap, 0.9 if alias_hit or id_hit else 0.0)


def search(payload):
    question = str(payload.get("question") or "")
    intent = payload.get("intent") or "thong_tin"
    top_k = int(payload.get("top_k") or 3)
    query_vec = embed(question)
    docs = all_documents()
    scored = []
    for doc in docs:
        score = cosine(query_vec, doc["vector"])
        scored.append({**doc, "score": score})
    scored.sort(key=lambda d: d["score"], reverse=True)

    faq_hits = [d for d in scored if d["doc_type"] == "faq"]
    product_docs = [d for d in scored if d["doc_type"] == "product"]
    products = [d["metadata"] for d in docs if d["doc_type"] == "product"]
    best_faq_doc = faq_hits[0] if faq_hits else None
    product_matches = sorted(
        [{**p, "score": product_score(p, question)} for p in products],
        key=lambda p: p["score"],
        reverse=True,
    )
    best_product = product_matches[0] if product_matches else None
    product_hit = bool(best_product and best_product["score"] >= 0.28)
    is_catalog_overview = bool(
        re.search(r"danh sach|catalog|danh muc|shop co san pham nao|ban nhung san pham|cho xin", normalize(question))
    )
    is_product_intent = intent in {"san_pham", "dat_mua"}
    semantic_hit = bool(best_faq_doc and best_faq_doc["score"] >= 0.25)
    cache_hit = (semantic_hit or product_hit or is_product_intent) and intent != "ngoai_pham_vi"

    top_faq = faq_hits[:top_k]
    rag_chunks = []
    if best_faq_doc:
        meta = best_faq_doc["metadata"]
        rag_chunks.append(f"[FAQ {meta['id']}]: {meta['cau_hoi']} -> {meta['cau_tra_loi']} (Nguồn: {meta['nguon']})")
    for doc in top_faq[1:top_k]:
        meta = doc["metadata"]
        rag_chunks.append(f"[FAQ {meta['id']}]: {meta['cau_hoi']} -> {meta['cau_tra_loi']}")
    if best_product:
        rag_chunks.append(
            f"[PRODUCT {best_product['id']}]: {best_product['name']} - Giá: {best_product['price']} VNĐ. "
            f"Tồn kho: {best_product['stock']}. {best_product.get('summary')} ({best_product.get('promo')})"
        )

    return {
        **payload,
        "cache_hit": cache_hit,
        "cache_score": round(best_product["score"] if is_product_intent and best_product else (best_faq_doc["score"] if best_faq_doc else 0), 2),
        "bestFaq": best_faq_doc["metadata"] if semantic_hit and best_faq_doc else None,
        "bestProduct": best_product if product_hit and not is_catalog_overview else None,
        "is_catalog_overview": is_catalog_overview,
        "products": products,
        "top3_faq_ids": [d["metadata"]["id"] for d in top_faq],
        "is_product_intent": is_product_intent,
        "rag_context": "\n".join(rag_chunks),
        "rag_chunks": rag_chunks,
        "vector_db": {
            "provider": "local_sqlite_vector_store",
            "db_path": str(DB_PATH),
            "documents": len(docs),
            "top_k": top_k,
        },
    }


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body):
        encoded = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def _read_json(self):
        length = int(self.headers.get("Content-Length") or "0")
        raw = self.rfile.read(length).decode("utf-8") if length else "{}"
        return json.loads(raw or "{}")

    def log_message(self, fmt, *args):
        return

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/health":
            self._send(200, {"ok": True, "documents": len(all_documents())})
        elif path == "/documents":
            self._send(200, {"documents": [{k: v for k, v in doc.items() if k != "vector"} for doc in all_documents()]})
        else:
            self._send(404, {"error": "not_found"})

    def do_POST(self):
        path = urlparse(self.path).path
        try:
            body = self._read_json()
            if path == "/search":
                self._send(200, search(body))
            elif path == "/upsert":
                doc_id = body["id"]
                doc_type = body.get("doc_type", "faq")
                text = body.get("text") or json.dumps(body.get("metadata", {}), ensure_ascii=False)
                metadata = body.get("metadata", {})
                upsert_document(doc_id, doc_type, text, metadata)
                self._send(200, {"ok": True, "id": doc_id, "doc_type": doc_type})
            elif path == "/seed":
                self._send(200, {"ok": True, "documents": seed(reset=bool(body.get("reset")))})
            else:
                self._send(404, {"error": "not_found"})
        except Exception as exc:
            self._send(400, {"error": str(exc)})

    def do_DELETE(self):
        path = urlparse(self.path).path
        prefix = "/documents/"
        if path.startswith(prefix):
            doc_id = unquote(path[len(prefix):])
            deleted = delete_document(doc_id)
            self._send(200, {"ok": True, "id": doc_id, "deleted": deleted})
        else:
            self._send(404, {"error": "not_found"})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--reset", action="store_true")
    args = parser.parse_args()
    count = seed(reset=args.reset)
    print(f"CSKH vector DB ready: {count} docs at http://{args.host}:{args.port}", flush=True)
    ThreadingHTTPServer((args.host, args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
