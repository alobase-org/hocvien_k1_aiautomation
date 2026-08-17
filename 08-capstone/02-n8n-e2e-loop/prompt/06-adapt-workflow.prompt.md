# Prompt 06 — Bản đồ sửa workflow mượn cho use case của bạn

> Input: e2e-test.md (đã viết) + workflow mượn đã import vào n8n (bạn đang mở nó).

---

Bạn là kỹ sư n8n. Lập bản đồ sửa workflow mượn thành workflow cho use case của tôi — tối thiểu thay đổi, tối đa tái sử dụng.

## Bối cảnh
Workflow mượn từ buổi học trước (thẩm định hợp đồng / chấm CV). Nghiệp vụ khác nhưng pattern giống: nhận input → chuẩn hóa → AI xử lý theo rule → validate → output.

## Chỉ dẫn
1. Đọc e2e-test: các assert dict cái gì phải đúng — bản đồ sửa phải nhắm cho hết assert.
2. Liệt kê từng node của workflow mượn (tôi sẽ dán mô tả node hoặc ảnh chụp cấu trúc): node nào GIỮ nguyên, node nào SỬA (sửa field/prompt/route nào), node nào THÊM, node nào XÓA.
3. Với mỗi node SỬA: ghi cụ thể tham số mới — riêng prompt AI node: viết lại prompt con theo nghiệp vụ use case tôi (giữ cấu trúc prompt cũ: vai trò → chỉ dẫn → tiêu chuẩn đầu ra).
   - Quy tắc nghiệp vụ trong prompt con phải ĐÁNH SỐ, mỗi rule 1 dòng điều kiện exact (vd "2. X: A VÀ B"), kèm 1 ví dụ phủ định (vd "333,777 KHÔNG phải bội 50k → KHONG_RO") — rule viết văn xuôi dễ bị AI bỏ qua điều kiện.
4. Nếu use case cần schema output mới: đề xuất schema theo mẫu `04-contract-review/templates/clause.schema.json` (required + type + enum).
5. Ước lượng thứ tự thao tác trong UI n8n để tôi làm theo từng bước.

## Tiêu chuẩn đầu ra
- File `workflow-plan.md`: bảng node (Giữ/Sửa/Thêm/Xóa) + prompt con mới + schema mới (nếu có) + thứ tự thao tác
- Không thêm node "cho đẹp" — mỗi thay đổi map về 1 assert trong e2e-test
- Không đụng đến credentials/tài khoản — tôi tự cấu hình

## E2e test

[DÁN e2e-test.md]

## Cấu trúc workflow mượn (tôi đang mở trong n8n)

[DÁN tên các node + mô tả ngắn từng node, hoặc ảnh chụp]
