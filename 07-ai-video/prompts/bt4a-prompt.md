# Prompt TH4A — Đóng gói Content/Video Engine độc lập công cụ

```text
BỐI CẢNH:
Schema, content artifact và media canary đã được kiểm chứng. Hãy đóng gói logic thành một
Content/Video Engine specification độc lập nền tảng. Đây là phần bắt buộc; chưa build giao diện.

INPUT PHẢI ĐỌC:
- schemas/*.schema.json
- video-script.json, storyboard.json, video-plan.json
- media-run-log.json
- content-validation-report.md và schema-validation-report.md nếu có

CHỈ DẪN:
1. Xác nhận các invariant và runtime evidence. Nếu canary chưa tạo được clip thật, ghi BLOCKED,
   không tự suy diễn là chạy được.
2. Sinh engine-spec.json có:
   - engine_id/version;
   - hai input adapter B6_APPROVED và MANUAL;
   - nodes[]: id, type, purpose, inputs, outputs, config, state;
   - edges[]: source_node/port, target_node/port, data_type;
   - execution_policy;
   - approval_gates;
   - retry_policy;
   - logging;
   - cost_guard;
   - test_cases;
   - known_limitations.
3. Pipeline bắt buộc: Input Adapter → Scene Planner → Storyboard Generator → Storyboard Review
   → Video Generator tổng → Clip Review/Export.
4. Video Generator nhận danh sách frame APPROVED, chạy SEQUENTIAL, lưu state/progress/error
   theo clip; retry một scene không reset scene khác.
5. Ghi rõ payload từng port và reference IDs. Không truyền một object mơ hồ rồi để node sau đoán.
6. Engine không phụ thuộc Google Flow. Model/tool được cấu hình qua adapter.
7. Sinh engine-spec.schema.json từ đặc tả vừa thiết kế, validate engine-spec.json đến PASS.
8. Ghi engine-validation-report.md và sơ đồ Mermaid ngắn trong engine-spec.md.

TIÊU CHUẨN BÀN GIAO:
- engine-spec.json + engine-spec.schema.json PASS.
- Không có API key/URL bí mật.
- Nêu rõ phần runtime-test và phần chỉ thiết kế.
```

**Chaining line:** TH4B chỉ đóng gói engine spec thành app; không sửa nghiệp vụ/schema.

