# Prompt mở rộng — Đổi sang dự án video của bạn

```text
Đọc engine-spec, schema và app hiện tại trước khi sửa. Tôi muốn thay input bằng kịch bản của tôi.

1. Chỉ thay source adapter và dữ liệu dự án; giữ nguyên ID chain, approval gate, sequential
   generator, retry và logging.
2. Cho tôi biết kịch bản cần bao nhiêu scene trong khoảng 6–9 và lý do.
3. Sinh lại artifact theo schema, validate, rồi chỉ chạy canary 2 scene.
4. Trước khi tạo media, báo số lượt ảnh/video dự kiến.
5. Không dùng hình/giọng người thật nếu tôi chưa xác nhận có quyền.
6. Báo file đã sửa, test đã chạy và phần chưa runtime-test.
```

