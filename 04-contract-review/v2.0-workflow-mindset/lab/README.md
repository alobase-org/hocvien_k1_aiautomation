# Lab — Webinar #3 v2.0 · Workflow Mindset

> 6 bài tập móc nối (output N = input N+1). HV build dần 1 Workflow Design Doc hoàn chỉnh + deck tham mưu lãnh đạo.
> Tham chiếu pattern: `~/vtn-5days-builders-bootcamp/03-practice/session-02/` (Workflow Thinking).

## Cấu trúc

```
lab/
├── README.md                  ← file này (index)
├── lab.md                     ← 6 bài tập chính
├── prompts/                   ← 6 prompt copy-paste (3 phần BỐI CẢNH/CHỈ DẪN/TIÊU CHUẨN)
│   ├── 01-usecase-impact-matrix.md
│   ├── 02-workflow-design-esia.md
│   ├── 03-production-hardening.md
│   ├── 04-mermaid-diagram.md
│   ├── 05-generate-workflow-image.md
│   └── 06-notebooklm-leadership-deck.md
├── templates/
│   ├── as-is-table-template.md
│   ├── impact-difficulty-matrix-template.md
│   └── workflow-design-doc-template.md
├── checkpoints/               ← rescue khi HV stuck
│   └── checkpoint-bt{1..6}.md
├── fallback-inputs/           ← sample output cho HV chậm
│   ├── sample-problems-list.md
│   ├── sample-as-is.md
│   ├── sample-esia-tobe.md
│   ├── sample-mermaid.mmd
│   └── sample-design-doc.md
└── synthetic-data/
    └── company-dong-duong-thuongmai.md   ← công ty giả + 10 vấn đề DN
```

## Hướng dẫn GV

| Khi nào | Dùng file gì |
|---------|-------------|
| Demo BT1-BT6 trên máy chiếu | `lab.md` + `prompts/0X-*.md` |
| HV không nghĩ ra use-case | `synthetic-data/company-dong-duong-thuongmai.md` |
| HV stuck ở bài N | `checkpoints/checkpoint-btN.md` (rescue map) |
| HV chậm, cần nhảy bài | `fallback-inputs/sample-*.md` |
| 15' cuối HV nộp bài | `../nop-bai/form-nop-bai-webinar3-v2.md` |

## SLI/SLO kiểm soát chất lượng (whole lab)

| # | SLI | SLO | Cách đo |
|---|-----|-----|---------|
| 1 | Hoàn thành ≥1 bài (BT1 hoặc BT2) | 100% HV nộp | Đếm form nộp |
| 2 | Ma trận use-case hợp lệ (4 góc) | 100% | Soi output BT1 |
| 3 | Design doc có as-is + to-be ESIA | 100% | Soi output BT2 |
| 4 | ≥1 bước Automate + ≥1 HITL | 100% | Rà cột AI/người |
| 5 | Mermaid render được | 100% | Paste mermaid.live |
| 6 | Có phần hardening (4 lớp) | 100% HV làm thêm | Soi output BT3 |

## Safety / HITL
- KHÔNG dùng dữ liệu khách hàng thật / PII thật trong demo.
- Công ty "Đông Dương Thương Mại" là synthetic (zero PII thật).
- Bước Automate rủi ro cao (tiền bạc, dữ liệu cá nhân, quyết định ảnh hưởng người dùng) → bắt buộc HITL.
