# Prompt 04 — Test skill trên input mẫu (chạy trong agent đã cài skill)

> Chạy cái này TRONG agent sau khi cài skill (không phải chat AI thường). Mục đích: chứng minh skill chạy được + có bằng chứng PASS.

---

Hãy thực hiện skill `[tên skill của bạn]` với input sau:

[DÁN INPUT MẪU CỦA USE CASE BẠN — file hoặc nội dung]

Yêu cầu khi chạy:
1. Theo đúng workflow trong SKILL.md, không bỏ bước. Với mỗi kết luận, nêu điều khoản/quy tắc nào trong kb được áp dụng (trích nguyên văn) — không kết luận suông.
2. Ghi lại từng bước thực hiện vào `test-run.md`: bước làm gì, input/output trung gian.
3. Nếu thiếu dữ liệu theo rule của skill: dừng đúng quy định, ghi cờ thiếu — đó là hành vi ĐÚNG, không phải lỗi.
4. Cuối `test-run.md`, tự đối chiếu với test-case: mỗi tiêu chí ghi PASS hay FAIL kèm evidence (trích output thật).
5. KHÔNG tuyên bố PASS nếu output chưa thật sự sinh ra file/kết quả — trung thực runtime-test.

## Tiêu chuẩn đầu ra
- File output đúng contract của skill (tên file + định dạng)
- `test-run.md` có bảng kết quả từng tiêu chí, ≥1 tiêu chí PASS trên use case của tôi
- Nếu FAIL: ghi rõ lỗi gì, tôi sẽ sửa skill và chạy lại (đó là vòng loop bình thường)
