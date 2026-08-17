# Cấu trúc package nộp chuẩn

```
ho-ten-capstone/
├── README.md                    ← 10 dòng: use case là gì, package chứa gì, mở file nào đầu tiên
├── usecase-brief.md             ← lab 00
├── resource-map.md              ← lab 00
├── d1-agent-skill/
│   ├── SKILL.md
│   ├── [templates/ kb/ theo thiết kế]
│   └── test/                    ← test-run.md + test-case.md
├── d2-n8n-e2e/
│   ├── workflow-[ten-use-case].json   ← export từ n8n
│   ├── e2e-test.md
│   └── run-log.md
├── d3-mvp/
│   ├── spec-kit.md
│   ├── improve-log.md
│   ├── RUN.md                  ← cách chạy lại app trong ≤3 lệnh (hoặc link preview công khai)
│   └── [source + ảnh chụp app]
├── d4-package/
│   └── pitch.html
├── anh-demo/                    ← ảnh chụp: n8n execution, app, output
├── acceptance-checklist.md      ← tick xong
└── risk-log.md
```

Kiểm tra nhanh trước khi zip: mở `pitch.html` từ trong package (đường dẫn tương đối phải còn ăn nhau), mỗi ảnh trong `anh-demo/` được dùng ở chỗ nào đó.
