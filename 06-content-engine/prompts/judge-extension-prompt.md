# Mở rộng — LLM-as-Judge cho văn phong + ảnh

> Tham khảo tư duy buổi 5 (`../../05-cskh-bot/thuc-hanh-3-llm-fallback-judge-hitl.md`): một LLM THỨ HAI, độc lập với LLM sinh nội dung, chấm `confidence`/`reason` trước khi nội dung tới người. Nguyên tắc gốc: *"LLM-judge = đo, không tin — separation: LLM trả lời (thực thi) ≠ LLM judge (kiểm chứng)"*.
>
> **Vị trí trong buổi học:** đây KHÔNG phải bài tập học viên tự build trong 120 phút của TH4 — không tính vào Expected state/rescue map của `checkpoints/checkpoint-bt4.md`, không ảnh hưởng mốc chặn phút 18. Tài liệu này dùng để **GV giảng tư duy + demo** (GV tự chạy bằng Coding Agent trên lớp, học viên xem và hỏi), hoặc **giao học viên tự làm sau giờ** — cùng nhóm với bài tập về nhà ở `../lab.md` §8. Vì không bị time-box, thiết kế dưới đây làm đầy đủ, không cắt gọn vì thời gian.
>
> **✅ Đã build + test thật trên instance n8n (2026-08-09).** Không còn là thiết kế trên giấy — cả Lớp 2b lẫn Lớp 3b đã chạy thật trong `checkpoints/n8n-content-engine-solution.json`. Judge ảnh từng **phát hiện thật 2 lần khác nhau**: (1) chữ mờ/logo lẫn vào ảnh dù chưa được yêu cầu, và (2) sau khi đổi hướng cho phép tiêu đề ngắn trong ảnh — model **lặp thừa một dòng chữ** (vẽ "Tiếng Anh" rồi lại vẽ "Tiếng Anh tự nhiên cho bé" ngay dưới) — cả hai lần Judge đều chặn đúng, đã xác nhận bằng cách tải ảnh gốc trước khi bị chặn để xem trực tiếp. GV demo trên lớp giờ có thể trỏ thẳng vào file solution thay vì phải tự dựng từ đầu.

## Vì sao cần — 2 lỗ hổng thật mà quy tắc cứng không bắt được

Toàn bộ nghiệm thu hiện tại của buổi 6 (`giao_trinh/scripts/validate-b6-artifacts.py`, cảnh báo brand-voice trong app) đều là **quy tắc cứng**: regex, đếm chuỗi, so khớp từ khoá. Quy tắc cứng mạnh ở chỗ tất định, dễ kiểm — nhưng có 2 việc nó không làm được:

1. **AI bịa số mà quên đánh dấu thiếu.** `validate-b6-artifacts.py` chỉ đếm số ô `[cần bổ sung]` có khớp mảng `thieu_thong_tin` không (dòng 108-112) — nếu AI viết sai mà KHÔNG đánh dấu gì cả (ví dụ ngầm định học phí "chỉ từ 2 triệu" dù brief không hề có số này, và không có ô `[cần bổ sung]` nào để đếm), quy tắc đếm chuỗi không phát hiện được. Cần một bên đọc hiểu ngữ nghĩa: so bài viết với brief gốc, tự hỏi "câu này có thật sự tra được từ brief không".
2. **Ảnh sinh ra không đảm bảo đúng như prompt yêu cầu.** `image_prompt` mô tả đúng 1 dòng tiêu đề/CTA ngắn cần hiển thị (`chu_tren_anh`) — nhưng đó là kiểm **chuỗi prompt**, không phải kiểm **ảnh thật**. Model sinh ảnh có thể vẫn vẽ sai/lặp thừa/thiếu chữ so với đúng những gì đã yêu cầu, dù đã ghi rõ trong prompt. Hiện tại tuyến phòng thủ duy nhất cho việc này là người duyệt tự nhìn bằng mắt ở app — không có gì tự động cảnh báo trước.

> **Lưu ý (2026-08-09, 2 lần đổi hướng):** (1) Ảnh có người/trẻ em KHÔNG còn là vi phạm — ảnh do AI sinh hoàn toàn, không tham chiếu ai thật, nên không phát sinh vấn đề quyền riêng tư như ảnh chụp thật. (2) Chữ trong ảnh KHÔNG còn bị cấm hoàn toàn — model hiện tại (`nano-banana-pro`) render dấu tiếng Việt đúng gần như tuyệt đối (test thật xác nhận), nên cho phép TỐI ĐA 1 dòng tiêu đề/CTA ngắn (≤8 từ) hiển thị thẳng trong ảnh. Judge ảnh dưới đây đổi vai trò: từ "có chữ hay không" sang **"chữ có đúng — không thiếu/thừa/lặp/sai chính tả — so với dự kiến hay không"**.

Cả 2 việc này cần đánh giá **ngữ nghĩa/thị giác**, đúng loại việc LLM-as-Judge sinh ra để giải.

## Khác gì với buổi 5 — không copy nguyên, có lý do

| | Buổi 5 (CSKH) | Buổi 6 (Content Engine) |
|---|---|---|
| Judge dùng để làm gì | Tự động định tuyến: confidence thấp → auto tạo ticket, phần lớn case KHÔNG cần người xem | Làm giàu cảnh báo cho người xem — **không tự chặn** ghi vào hàng đợi (trừ ảnh vi phạm chính sách, luôn phải chặn riêng ảnh đó) |
| Vì sao khác | Trả lời khách cần nhanh, không phải mọi case đáng để người xem | Mọi bài marketing đã bắt buộc người duyệt trước khi Approved (100% HITL) — Judge không thay được bước đó, chỉ giúp người duyệt quyết nhanh và đúng hơn |

## Thiết kế đầy đủ

### Lớp 2b — Judge văn phong (chèn sau Lớp 2 trong workflow n8n của bt4a)

Gọi Gemini **lần thứ hai**, là một AI node hoàn toàn riêng biệt với node Lớp 2 (không phải sửa lại cùng một lệnh gọi để "tự chấm mình").

**Input:** `content_draft` vừa sinh ở Lớp 2 + `product-brief-sunrise-kids.md` + `brand-voice.md`.

**Output JSON bắt buộc:**
```json
{
  "confidence": 0.0,
  "reason": "vì sao tin/không tin, tối đa 2 câu, tiếng Việt",
  "nghi_bia_so": false
}
```

**Quy tắc:**
- Judge KHÔNG được sửa bài — chỉ chấm.
- `nghi_bia_so=true` khi bài không có ô `[cần bổ sung]` nào nhưng đọc kỹ thấy có chi tiết (học phí, ngày khai giảng, ưu đãi, sĩ số...) không tra được từ brief gốc — đây chính là lỗ hổng #1 ở trên.
- `confidence` thấp khi giọng văn lệch chân dung đã chọn (ví dụ angle nhắm phụ huynh "lo con nhút nhát" nhưng bài lại nói về "tăng tốc luyện thi").
- Ép output đúng JSON — nếu model trả lời tự do/giải thích dài, coi là lỗi cấu hình node, không phải "Judge nói không sao".

### Lớp 3b — Judge ảnh (chèn sau Lớp 3, sau khi ảnh đã sinh)

Cần model đọc được ảnh (Gemini vision). Gọi **sau khi có URL ảnh thật**, không phải chấm trên prompt.

**Input:** ảnh vừa sinh ở Lớp 3 + 4 thứ dự kiến lấy thẳng từ `image_brief` của chính Lớp 3: `chu_tren_anh`, `phong_cach`, `bo_cuc`, `khong_duoc_xuat_hien`. Một lần gọi vision chấm đủ cả 4 tiêu chí, không cần 4 lần gọi riêng.

> **Lưu ý (2026-08-09):** `khong_duoc_xuat_hien` chỉ được phép chứa điều NHÌN THẤY RÕ RÀNG, khách quan (logo, bảng điểm, chữ tiếng Anh...) — Lớp 3 bị cấm liệt kê ước lượng tuổi trẻ em (vd "trẻ dưới 6 tuổi") vào đây, và Judge cũng được dặn bỏ qua nếu lỡ còn sót. Lý do: vision model đoán tuổi trẻ em qua ảnh tĩnh không đáng tin — test thật từng đoán nhầm trẻ 8-9 tuổi thành 4-5 tuổi rồi chặn oan 1 ảnh đạt (đã xác nhận bằng cách tải ảnh gốc so sánh). Việc kiểm tuổi hợp lý để lại cho người duyệt tự nhìn ở App, không phải điều kiện chặn tự động.
>
> **Gợi ý thêm cho prompt sinh ảnh (không phải việc của Judge, việc của Lớp 3):** nếu ảnh có học sinh, mô tả rõ là trẻ em người Việt Nam; nếu có giáo viên, được phép mô tả là người nước ngoài (đúng mô hình "giáo viên bản ngữ" của brief) — đã thêm vào prompt Lớp 3, test thật ra đúng ảnh (giáo viên phương Tây, học sinh + trợ giảng châu Á).

**Output JSON bắt buộc (2026-08-09, mở rộng từ 1 tiêu chí lên 4 — xem lý do ở bảng dưới):**
```json
{
  "chu_dung": true,
  "khong_co_yeu_to_cam": true,
  "phong_cach_khop": true,
  "bo_cuc_khop": true,
  "reason": "mô tả ngắn tiếng Việt, nêu rõ tiêu chí nào không đạt"
}
```
`vi_pham_chinh_sach` **không** để model tự trả — tính tất định trong Code node: `vi_pham_chinh_sach = !chu_dung || !khong_co_yeu_to_cam`. Đây là quy tắc cứng của hệ thống, không phải phán đoán của LLM — không tin model tự tính đúng bấy chấp responseSchema.

| Tiêu chí | Chấm gì | Chặn cứng (xoá ảnh)? |
|---|---|---|
| `chu_dung` | Chữ trong ảnh có đúng CHÍNH XÁC `chu_tren_anh` không — đúng chính tả/dấu, không thiếu/thừa/lặp, không có chữ lạ khác lẫn vào. Nếu `chu_tren_anh` rỗng thì chỉ đạt khi ảnh KHÔNG có chữ nào. | **Có** |
| `khong_co_yeu_to_cam` | Ảnh có chứa bất kỳ điều nào trong `khong_duoc_xuat_hien` không (danh sách chỉ gồm điều khách quan, KHÔNG có ước lượng tuổi trẻ em). | **Có** |
| `phong_cach_khop` | Ảnh có đúng `phong_cach` mô tả không (ấm/lạnh, sáng/tối, chất liệu...). | Không — chỉ cảnh báo ở App |
| `bo_cuc_khop` | Ảnh có đúng `bo_cuc` mô tả không (góc chụp, vị trí, khoảng trống chừa chữ...). | Không — chỉ cảnh báo ở App |

**Vì sao chỉ 2/4 tiêu chí chặn cứng:** đúng tinh thần "chỉ cảnh báo, không chặn" đã giữ xuyên suốt buổi 6 (mục 6, `bt4b-prompt.md`) — phong cách/bố cục là đánh giá **chủ quan**, lệch nhẹ không có nghĩa ảnh không dùng được, người duyệt tự quyết là đủ. Chữ sai và yếu tố cấm là **vi phạm khách quan, đo được** — mới đáng chặn cứng và tốn phí sinh lại.

**Quy tắc:**
- Nếu `vi_pham_chinh_sach=true` (từ 2 tiêu chí cứng): **không dùng ảnh đó**. Xoá `image_url` (để rỗng) trước khi ghi Content_Queue — App tự hiện ô "chưa có ảnh, duyệt phần chữ trước". Luồng vẫn đi tiếp tới Lớp 4 — chỉ chặn riêng ảnh, không dừng cả workflow.
- Nếu model không đọc được ảnh (không hỗ trợ vision, lỗi API): coi như Lớp 3b không chạy được ở brief này — quay lại hành vi gốc (ảnh đi thẳng tới người duyệt, người tự nhìn bằng mắt). Đây là fallback hợp lệ, không phải lỗi phải sửa bằng mọi giá.
- **Đã test thật:** cả 4 tiêu chí trả đúng schema; đã tải ảnh thật xác nhận Judge chấm đúng khi ảnh thực sự đạt (không chặn nhầm) lẫn khi ảnh thực sự lỗi (chặn đúng, xem 2 ví dụ ở mục "Vì sao cần" phía trên).
- **Đã test thật hai lần, Judge chấm đúng cả hai:** lần 1 phát hiện chữ mờ/logo lạ lẫn vào (khi chưa yêu cầu chữ nào); lần 2 phát hiện model **lặp thừa** dòng chữ (vẽ "Tiếng Anh" rồi lại vẽ đầy đủ "Tiếng Anh tự nhiên cho bé" ngay dưới) — cả hai lần đã tải ảnh gốc để xác nhận Judge không báo nhầm.

### Tích hợp vào workflow n8n đã có (bt4a) — không phá cấu trúc gốc

- **Không thêm cột mới vào Google Sheets.** Cột `Ghi chú` có sẵn trong `Content_Queue` (đã khớp `content-workbook.xlsx` của học viên) dùng để chứa `reason` của cả 2 Judge — ghép lại, bỏ qua cái nào không chạy. Nếu cả 2 đều pass (confidence cao, không nghi bịa, không vi phạm) thì để `Ghi chú` rỗng như thiết kế gốc.
- **Không đổi 3 schema JSON của TH1-TH3** (`schemas/content-angles.schema.json`, `content-draft.schema.json`, `content-assets.schema.json`). Judge sống hoàn toàn trong n8n runtime của TH4a — không ghi ngược output của nó vào `content-draft.json`/`content-assets.json`, nên không ảnh hưởng `validate-b6-artifacts.py` hay các bài tập TH1-TH3 đã kiểm chứng.
- Webhook "sinh nội dung" (đường trigger 4 lớp gốc) trả về thêm 2 field `judge_van_phong` và `judge_anh` trong response cho app — Judge chấm mà không ai thấy thì vô nghĩa.

### Hiển thị ở App duyệt (bt4b) — vẫn chỉ cảnh báo, không chặn

Nếu payload nạp vào có `judge_van_phong`/`judge_anh`: hiện `reason` như một dòng cảnh báo riêng, có nhãn rõ "AI đã chấm: ...". Vẫn đúng nguyên tắc đã có sẵn của app (mục 6, `bt4b-prompt.md`): **chỉ cảnh báo, KHÔNG tự sửa, KHÔNG chặn nút Duyệt** — người xem rồi tự quyết. Nếu payload không có 2 field này (Judge không chạy), không hiện ô cảnh báo rỗng.

## Cách dạy trên lớp (nếu GV chọn demo thay vì giao về nhà)

1. Sau khi HV hoàn thành TH4a/TH4b theo đúng bản gốc (không Judge), GV mở lại chính workflow đã build, chèn thêm Lớp 2b/3b trực tiếp bằng Coding Agent trước lớp — học viên xem quá trình, không tự gõ.
2. Nhấn mạnh đúng 1 câu tổng kết: *"LLM trả lời và LLM chấm phải là hai lệnh gọi khác nhau — nếu để cùng một lệnh vừa viết vừa tự khen, Judge vô nghĩa."*
3. Chỉ ra 2 ví dụ cụ thể có thật (bịa số không đánh dấu; ảnh lặp thừa một dòng chữ dù prompt chỉ yêu cầu đúng 1 dòng) để học viên thấy quy tắc cứng đã có (schema, regex) không bắt được, còn Judge thì có — đây là bài học chính, quan trọng hơn việc build được hay không.

## Nghiệm thu nếu học viên tự làm ở nhà (không chấm trong buổi chính khoá)

- Judge là node Gemini riêng, không phải node sinh nội dung tự chấm lại chính nó.
- Judge văn phong trả đúng JSON `confidence`/`reason`/`nghi_bia_so`.
- Judge ảnh trả đúng JSON `chu_dung`/`khong_co_yeu_to_cam`/`phong_cach_khop`/`bo_cuc_khop`/`reason`; `vi_pham_chinh_sach` tính tất định trong Code node từ 2 tiêu chí đầu, không lấy model tự trả; nếu `true` thì ảnh gốc không lọt vào `Content_Queue`.
- App hiện được `reason` nhưng nút Duyệt vẫn bấm được bình thường (không bị Judge chặn).
- Giải thích được vì sao Judge không thay thế người duyệt — vẫn đúng tinh thần HITL 100% của buổi 6.
