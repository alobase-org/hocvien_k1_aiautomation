# Prompt TH3 — Media canary: storyboard → clip có audio

```text
BỐI CẢNH:
Ba content artifact đã PASS. Giờ kiểm chứng runtime bằng canary 2 scene trước khi batch 6–9.

INPUT:
- video-script.json
- storyboard.json
- video-plan.json
- Công cụ tạo ảnh/video hiện có (Google Flow là đường demo; có thể dùng công cụ khác)

QUYẾT ĐỊNH CÔNG CỤ VIDEO — có đánh đổi thật, không phải chọn tuỳ ý:
- Nếu công cụ hỗ trợ audio gốc kèm video (không cần TTS/mux rời), kiểm trước 3 điều: (a) duration
  công cụ đó thật sự chấp nhận giá trị nào (có thể chỉ vài giá trị cố định, không phải dải tự do);
  (b) công cụ có xu hướng tự vẽ thêm người/tay vào khung hình khi prompt mô tả lời thoại không —
  nếu có, phải cấm rõ trong negative_prompt + chỉ dẫn narration off-screen trong video_prompt;
  (c) công cụ có gắn watermark/nhãn xác thực nội dung AI-sinh cố định không xoá được bằng prompt
  không — nếu có, đây là đặc tính của công cụ (không phải lỗi cần sửa), phải quyết định chấp nhận
  hay đổi công cụ khác TRƯỚC khi chạy hàng loạt, không phát hiện muộn sau khi đã tốn credit.
- Không giả định 1 công cụ mới chưa test sẽ hoạt động giống công cụ khác đã quen (vd model A cho
  audio gốc miễn phí không có nghĩa model B cũng vậy) — luôn canary 1 lần trước khi tin.

CHỈ DẪN:
1. Đọc ba artifact; xác nhận ID khớp. Không sửa kịch bản hoặc schema.
2. Chọn SC-01 và một scene thuộc SOLUTION làm canary. Báo trước số lượt tạo ảnh/video dự kiến.
3. Dùng image_prompt tương ứng tạo đúng 2 ảnh. Lưu asset reference vào đúng frame.
4. Kiểm ảnh theo continuity, bố cục, safety và mục cấm. Không tự APPROVE. Yêu cầu người dùng
   chọn APPROVED hoặc NEEDS_REVIEW cho từng ảnh.
5. Chỉ với frame APPROVED: cập nhật clip tương ứng thành READY_TO_GENERATE và chép đúng
   image_asset_ref. Frame chưa duyệt giữ clip BLOCKED.
6. Video Generator tổng xử lý tuần tự danh sách READY_TO_GENERATE. Tạo tối thiểu 1 clip bằng
   video_prompt có native audio.
7. Kiểm clip: đúng frame, đúng chuyển động, lời thoại nghe rõ, ngôn ngữ/giọng đúng, ambience/SFX
   không lấn thoại, không có âm thanh cấm. Nếu dùng công cụ audio gốc: kiểm THÊM khung hình có
   xuất hiện người/tay lạ so với ảnh đã duyệt không (dấu hiệu công cụ tự vẽ thêm "người đọc thoại"
   dù prompt không yêu cầu — nếu có, sửa lại negative_prompt/video_prompt và sinh lại), và ghi nhận
   watermark/nhãn AI-sinh nếu công cụ gắn cứng (không cố xoá, chỉ ghi vào báo cáo).
8. Khi API tạo được clip, cập nhật technical status nhưng đặt review status=`NEEDS_REVIEW`; không tự
   coi là `APPROVED`. Cho người dùng xem/nghe clip thật và chọn `APPROVED`, `NEEDS_RETRY` hoặc
   `REJECTED`. Chỉ `APPROVED` mới được phép assemble. Nếu retry, giữ nguyên ID và không xóa kết quả
   scene khác.
9. Ghi media-run-log.json gồm run_id, tool, model nếu biết, project_id, từng scene, input ref,
   technical status, review decision, reviewer note,
   start/end, status, error, retry_count, output ref và runtime_evidence.
10. Nêu rõ phần nào chạy thật, phần nào dùng fallback hoặc chưa runtime-test.

QUY TẮC:
- Không batch toàn bộ trước khi canary PASS.
- Không clone mặt/giọng người thật thiếu consent.
- Không tuyên bố SUCCESS nếu chỉ có URL giả/placeholder.
- Phân biệt `SUCCESS` kỹ thuật (API tạo được asset) với `APPROVED` nghiệp vụ (người đã xem/nghe và duyệt).
```

**Chaining line:** TH4A đọc cả artifact và run log để thiết kế engine từ bằng chứng đã chạy.
