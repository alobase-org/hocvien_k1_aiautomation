# Prompt TH2 — Angle → bài Fanpage + kịch bản TikTok

> Chạy trong cùng phiên chat sau TH1. Thay `A-0X` bằng angle bạn chọn.

```text
BỐI CẢNH:
Đây là LỚP 2 của Content Engine. Lớp 1 đã cho ra danh sách angle và được kiểm chứng.
Giờ chọn một angle và viết nội dung cho hai kênh có định dạng khác hẳn nhau.

INPUT:
- content-angles.json từ TH1 — đọc file này để lấy angle, KHÔNG nghĩ lại ý tưởng từ brief.
- templates/brand-voice.md
- templates/channel-format-spec.md
- templates/product-brief-sunrise-kids.md — chỉ để tra dữ kiện, không để lấy ý tưởng.
- schemas/content-draft.schema.json

ANGLE TÔI CHỌN: A-0X

CHỈ DẪN:
1. Đọc content-angles.json, tìm angle có angle_id đúng bằng mã tôi chọn ở trên.
   Nếu không tìm thấy, dừng lại và báo — đừng tự chọn angle khác.
2. Lấy brief_id và chan_dung từ chính angle đó. brief_id phải giữ y nguyên.
3. Viết bài Fanpage bám đúng angle này, nhắm đúng chân dung này:
   - 120 đến 200 từ.
   - Hai dòng đầu phải đứng được một mình, vì Facebook cắt phần sau nút "Xem thêm".
     Không mở bài bằng tên doanh nghiệp.
   - Đúng 1 CTA đặt cuối bài.
   - Tối đa 2 emoji. Không viết hoa cả câu.
   - Đếm số từ thật và ghi vào trường so_tu.
4. Viết kịch bản TikTok 30 đến 45 giây, đúng 4 khối theo thứ tự:
   HOOK (0-3s), PROBLEM (3-10s), SOLUTION (10-35s), CTA (35-45s).
   - Mỗi khối ghi rõ hình_anh (quay cái gì) và loi_thoai (nói câu gì).
   - Lời thoại viết để NÓI, không phải để đọc. Câu ngắn. Mỗi khối tối đa 2 câu.
   - Số phải đọc thành chữ: "mười lăm bé một lớp", không phải "sĩ số ≤15".
   - Cột hình_anh phải đủ chi tiết để người khác quay được — buổi sau sẽ dựng video từ đây.
   - Không quay mặt trẻ em.
5. Tuân thủ toàn bộ mục CẤM trong brand-voice.md. Đặc biệt: không cam kết kết quả,
   không hù dọa phụ huynh, không nêu tên đối thủ, không dùng câu tuyệt đối.
6. Brief thiếu học phí, ưu đãi, ngày khai giảng và số học viên. KHÔNG bịa.
   Chỗ nào cần thì ghi đúng chuỗi [cần bổ sung], rồi liệt kê tất cả những chỗ đó
   vào mảng thieu_thong_tin.
7. Ghi kết quả thật ra file content-draft.json trong workspace.
8. Validate theo schemas/content-draft.schema.json, tự sửa rồi validate lại cho tới khi PASS.

TIÊU CHUẨN ĐẦU RA:
content-draft.json là JSON hợp lệ gồm:
{
  "brief_id": "",
  "source_angle_id": "A-0X",
  "chan_dung": "",
  "fanpage": { "noi_dung": "", "so_tu": 0, "hook": "", "cta": "" },
  "tiktok": {
    "tong_thoi_luong_giay": 0,
    "khoi": [ { "ten_khoi": "HOOK", "thoi_gian": "0-3s", "hinh_anh": "", "loi_thoai": "" } ]
  },
  "thieu_thong_tin": []
}

Sau khi ghi file, đọc lại và báo: brief_id có khớp TH1 không, số từ bài Fanpage,
tổng thời lượng kịch bản, và những chỗ đã ghi [cần bổ sung].
Không tạo seeding hay image brief ở bước này.
```

**Chaining line:** Giữ nguyên chat và file `content-draft.json`; TH3 đọc chính file này để viết seeding và image brief bám đúng bài đã viết.
