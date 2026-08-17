# Lab 03 — Deliverable D3: MVP Vibe Coding theo SDD

## Mục tiêu
Biến use case thành **web app MVP chạy được** bằng vibe coding: viết đặc tả trước (SDD — Specification-Driven Development), AI sinh code, bạn chạy thử, cải tiến từng tính năng nhỏ.

## File input cần cung cấp
- `input/INPUT-CHECKLIST.md`
- `input/spec-kit.template.md` — bộ đặc tả rút gọn (PRD + user stories + test scenarios)
- `input/improve-log.template.md` — ghi vòng cải tiến
- `usecase-brief.md` (lab 00)

## Prompt để chạy

| Prompt | Input | Output |
|--------|-------|--------|
| `prompt/08-spec-sdd.prompt.md` | brief | `spec-kit.md` (đặc tả theo prompt 3 phần) |
| `prompt/09-build-improve.prompt.md` | spec-kit | MVP app + `improve-log.md` ≥1 vòng |

## Các bước
1. Chạy prompt 08 sinh spec-kit (PRD rút gọn + user stories + test scenarios). Spec là sản phẩm chính — AI code tốt hay kém do spec.
2. Chạy prompt 09 trong công cụ build (AI Studio Build mode / Coding Agent trong IDE — dùng lại công cụ các buổi trước đã quen).
3. Preview, dùng thử với input thật của use case, ghi lỗi/ghét chỗ nào vào improve-log.
   - **App bấm nút mà không chạy?** Mở Console lỗi: bấm F12 (hoặc chuột phải → Kiểm tra) → tab Console → đọc dòng đỏ, copy nguyên dòng đó đưa lại cho AI yêu cầu sửa. Đa số lỗi nằm ở đó.
4. Cải tiến đúng 1 tính năng mỗi vòng (không sửa loạn xạ), ghi vòng 2 vào improve-log.

## Vòng test + debug tự động (làm sau mỗi lần sửa app)
1. **Test bằng tay theo spec-kit** — mỗi dòng trong bảng Test scenarios: dán input → bấm → đối chiếu "Kỳ vọng". Ghi PASS/FAIL vào improve-log.
2. **App chết im?** F12 → Console → copy dòng ĐỎ đưa cho AI kèm câu: "lỗi này sửa thế nào, chỉ sửa 1 chỗ".
3. **Vòng lặp chuẩn:** Sửa 1 thứ → chạy lại CẢ 3+1 scenario (kể cả cái đã PASS — chống sửa chỗ này hỏng chỗ kia) → ghi vòng mới vào improve-log.
4. **Nâng cao (có Node):** viết file `test.js` copy 3 hàm chính từ app + các case kỳ vọng, chạy `node test.js` — PASS/FAIL tự động từng dòng.

## Nghiệm thu (đếm được)
- [ ] `spec-kit.md` đủ 3 phần: PRD rút gọn (mục tiêu + phạm vi), ≥3 user stories, ≥3 test scenarios
- [ ] App mở được bằng trình duyệt (link preview hoặc chạy local)
- [ ] Thao tác input → output của use case chạy được ít nhất 1 lần đầu cuối
- [ ] `improve-log.md` có ≥1 vòng cải tiến: vấn đề thấy → yêu cầu sửa → kết quả
- [ ] Phần chưa làm xong ghi rõ "chưa runtime-test" — không claim nhiều hơn thực tế

## Tài nguyên mượn (mở thật ra xem trước)
- `04-contract-review/app/` — app React hoàn chỉnh của B4 (exemplar cấu trúc + README chạy app): mượn cách tổ chức src, cách nó gọi nghiệp vụ
- `04-contract-review/app/src/App.jsx` — đọc thử 1 file chính để biết code vibe-coding thật trông thế nào
- `07-ai-video/templates/manual-script-input.md` (B7) — mẫu form input nhập tay nếu use case nhập tay
- Prompt 3 phần (Bối cảnh / Chỉ dẫn / Tiêu chuẩn đầu ra) — dùng nguyên cấu trúc này trong prompt 08/09
