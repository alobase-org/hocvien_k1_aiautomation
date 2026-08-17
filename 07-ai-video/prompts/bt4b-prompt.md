# Prompt TH4B — Build app node-based (lớp hỗ trợ)

> Có thể dùng Google Flow custom tool, AI Studio, Coding Agent hoặc nền tảng khác.

```text
BỐI CẢNH:
Content/Video Engine đã được đặc tả và validate. Hãy build một app node-based để vận hành trực
quan. App là lớp hỗ trợ, phải bảo toàn engine-spec và data contract.

INPUT PHẢI ĐỌC:
- engine-spec.json và engine-spec.schema.json
- Ba schema nghiệp vụ
- Ba artifact mẫu
- media-run-log.json
- Google Flow Automation Workflow Resource (chỉ lấy scaffold canvas/node/edge/status/preview;
  không lấy pipeline quảng cáo, asset giả, 16:9 cố định, mute audio hay lời gọi API chưa xác minh)

YÊU CẦU:
1. Dùng canvas node-based có pan/zoom/minimap, port/edge theo data type, sidebar và status bar.
2. Render đúng các node trong engine-spec: Input, Scene Planner, Storyboard, Review,
   Video Generator tổng, Clip Review/Export.
3. Input cho phép import B6 hoặc nhập kịch bản tay. Cả hai normalize về cùng video-script.
4. Storyboard hiển thị 6–9 cards; sửa prompt/regenerate từng scene; Approved/Needs Review.
5. Video Generator tổng chỉ nhận APPROVED, chạy tuần tự. Hiện progress tổng và status riêng
   từng clip; Retry Scene không chạy lại toàn bộ.
6. Preview cả ảnh và video; audio bật theo mặc định nhưng có control mute ở trình phát, không
   tắt audio ở model level.
7. Các trạng thái IDLE/RUNNING/SUCCESS/ERROR phải phản ánh runtime thật.
8. Không hardcode API key, model hoặc pseudo API. Dùng native integration/adapter thực sự có
   trong nền tảng; nếu chưa xác minh, tạo interface và ghi NOT_RUNTIME_TESTED.
9. Build từ engine-spec; không tự đổi node, schema, số scene hay approval gate.
10. Chạy test 2 scene. Báo bằng chứng: input ref → frame ref → clip ref. Nếu không chạy được,
    ghi lỗi thật và prompt sửa lỗi ngắn, cụ thể.

TIÊU CHUẨN BÀN GIAO:
- Master prompt đã dùng.
- Link/file app nếu có.
- Danh sách phần tái sử dụng từ resource.
- Kết quả runtime thật và known limitations.
- Không tuyên bố hoàn thành chỉ vì giao diện render đẹp.
```

