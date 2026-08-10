# Checkpoint TH4 — Workflow n8n hoàn chỉnh (GV/TA)

## Expected state

- [ ] Học viên chỉ kết nối Coding Agent với n8n ở bước đóng gói.
- [ ] Agent đã đọc ba artifact TH1–TH3 trước khi xây workflow.
- [ ] Workflow n8n có bốn vùng: bóc tách, chất lượng, rubric, scorecard/HITL.
- [ ] HTTP Request dùng Google AI Studio Header Auth hiện có; không lộ API key.
- [ ] Workflow ghi Google Sheets, bằng chứng là văn bản dễ đọc.
- [ ] Scorecard có cột `Câu hỏi phỏng vấn`, mỗi câu một dòng.
- [ ] Workflow chạy với CV holdout và giữ trạng thái `Chờ HR duyệt`.
- [ ] Agent nói rõ phần nào chỉ validation và phần nào đã runtime-test.
- [ ] Workflow chính ghi `WORKFLOW_COMPLETE/SUCCESS` vào tab `Run Log` sau khi ghi Scorecard.
- [ ] Error Workflow riêng ghi `WORKFLOW_ERROR/ERROR`, đã được liên kết trong Workflow Settings và có ghi chú giới hạn Manual Execution.
- [ ] Log không chứa CV nguyên văn, prompt, credential hoặc API key.

## Rescue map

| Lỗi | Cách cứu hộ |
|---|---|
| Agent tạo workflow không dựa artifact | Yêu cầu đọc lại ba JSON và lập bảng `artifact field → runtime node field` trước khi sửa. |
| Sai Google AI Studio | Tham chiếu workflow đang chạy trong cùng n8n: Generic Credential Type → Header Auth → GoogleAIStudio. |
| Học viên phải viết expression dài | Coding Agent phải tự cấu hình; học viên chỉ review schema và test output. |
| Kẹt quá 10 phút | GV cấp `checkpoints/hr-screening-b2b-junior-solution.json` hoặc workflow solution ID `N33hDcikrV8vlbPK`. |

Khi import solution từ Git, import cả workflow chính và `hr-screening-error-logger-solution.json`; chọn lại credential `GoogleAIStudio`, credential Google Sheets và Spreadsheet ID. Sau đó vào **Workflow Settings → Error workflow** của workflow chính và chọn Error Logger vừa import. Public API của n8n không gán được trường cài đặt này, nên đây là một thao tác UI bắt buộc. Hai file export đã dùng placeholder, không chứa ID nội bộ hoặc API key.

## Nghiệm thu phát biểu

Học viên phải nói được: “Ba JSON là artifact kiểm chứng và data contract; workflow cuối dùng chúng để tái tạo logic trên CV mới, không hard-code kết quả ứng viên mẫu.”
