# Buổi 07 — Script → Storyboard → Video

## Cách học

Không bắt đầu bằng app. Chạy theo thứ tự:

1. `prompts/bt1-prompt.md` → prompt sinh schema + sample.
2. `prompts/bt2-prompt.md` → schema sinh content artifact 6–9 cảnh.
3. `prompts/bt3-prompt.md` → tạo media canary và run log.
4. `prompts/bt4a-prompt.md` → Content/Video Engine spec bắt buộc.
5. `prompts/bt4b-prompt.md` → build app hỗ trợ.

Giữ cùng một phiên chat và workspace. Output bước trước là input bước sau. Nếu dùng fallback, ghi rõ file nào không do bạn tự tạo.

## Hai đường đầu vào

- Có B6: đặt `SOURCE_MODE=B6_APPROVED`, cung cấp `content-draft.json` và bằng chứng trạng thái Approved nếu có.
- Chưa có B6: đặt `SOURCE_MODE=MANUAL`, dùng `templates/manual-script-input.md`.

## Điều kiện hoàn thành

- 3 schema + 3 sample PASS.
- 6–9 scene, ID nối xuyên suốt.
- 2 ảnh storyboard, 1 ảnh Approved, 1 clip có audio.
- `media-run-log.json` và `engine-spec.json`.
- Master prompt/app là lớp hỗ trợ; không bắt buộc phải dùng Google Flow nếu engine được triển khai bằng cách khác.

## Nguyên tắc

- Không chạy video trước khi ảnh Approved.
- Test 2 scene trước khi batch.
- Không dùng hình/giọng thiếu quyền.
- Không bịa dữ kiện thiếu từ B6.
- Không nói “đã chạy” nếu mới tạo UI hoặc validate JSON.

