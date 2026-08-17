# E2E Test — [tên use case]

> Điền xong file này TRƯỚC khi sửa workflow. Test phải FAIL với workflow chưa sửa.

## Workflow dưới test
- Tên workflow n8n: [tên]
- Nguồn mượn: [path workflow mượn, vd `04-contract-review/checkpoints/n8n-contract-review-solution.json`]

## Bộ input mẫu
| # | Input | File/nội dung | Ghi chú |
|---|-------|---------------|---------|
| 1 | [vd: đơn nghỉ phép hợp lệ] | [path] | kỳ vọng PASS |
| 2 | [vd: đơn thiếu ngày] | [path] | kỳ vọng bị từ chối có lý do |

## Asserts (≥3)

| # | Assert | Cách kiểm | PASS khi |
|---|--------|-----------|----------|
| 1 | Workflow chạy hết, không node đỏ | Xem execution trong n8n | Status = success |
| 2 | Artifact output sinh ra đúng tên file | Kiểm file [tên file] | File tồn tại sau chạy |
| 3 | [Nội dung đúng nghiệp vụ] | [so nội dung với kỳ vọng] | [điều kiện] |
| 4 | [Trường hợp xấu xử lý đúng] | [chạy input #2] | [kỳ vọng từ chối/lỗi có thông báo] |

## Kết quả mỗi lần chạy
| Lần | Ngày | Asserts PASS | Verdict | Ghi vào run-log |
|-----|------|---------------|---------|-----------------|
| 1 | | /4 | | vòng 1 |
