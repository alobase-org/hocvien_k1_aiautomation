# Prompt TH3 — Media canary: storyboard → clip có audio

```text
BỐI CẢNH:
Ba content artifact đã PASS. Giờ kiểm chứng runtime bằng canary 2 scene trước khi batch 6–9.

INPUT:
- video-script.json
- storyboard.json
- video-plan.json
- Công cụ tạo ảnh/video hiện có (Google Flow là đường demo; có thể dùng công cụ khác)

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
   không lấn thoại, không có âm thanh cấm.
8. Cập nhật status/asset ref, không xóa kết quả scene khác nếu một scene lỗi.
9. Ghi media-run-log.json gồm run_id, tool, model nếu biết, project_id, từng scene, input ref,
   start/end, status, error, retry_count, output ref và runtime_evidence.
10. Nêu rõ phần nào chạy thật, phần nào dùng fallback hoặc chưa runtime-test.

QUY TẮC:
- Không batch toàn bộ trước khi canary PASS.
- Không clone mặt/giọng người thật thiếu consent.
- Không tuyên bố SUCCESS nếu chỉ có URL giả/placeholder.
```

**Chaining line:** TH4A đọc cả artifact và run log để thiết kế engine từ bằng chứng đã chạy.

