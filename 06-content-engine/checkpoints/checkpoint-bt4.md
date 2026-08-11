# Checkpoint TH4 — Đóng gói: n8n + app duyệt (GV/TA)

> TH nặng nhất buổi, 30 phút cho hai prompt. Chạy chậm thì cắt Q&A, đừng cắt TH4.

## Nhịp 30 phút

| Phút | Việc |
|------|------|
| 0–18 | **bt4a** — agent dựng workflow n8n 4 lớp, in ra 3 webhook URL (`/b6/angles`, `/b6/generate`, `/b6/approve`) |
| 18–30 | **bt4b** — agent dựng app duyệt, dán 3 URL, sinh ý tưởng → chọn → viết → duyệt, mở Sheets kiểm |

Mốc chặn: **phút 18 chưa có webhook URL thì cấp workflow solution ngay**, đừng để học viên mất luôn phần app — app mới là sản phẩm của buổi.

---

## Phần A — bt4a (backend n8n)

### Expected state

- [ ] Agent đã đọc 3 artifact và xác nhận `brief_id` khớp, schema PASS.
- [ ] Workflow có 4 vùng, mỗi vùng một sticky note tiếng Việt.
- [ ] `/b6/angles` là webhook RIÊNG, chỉ chạy Lớp 1, trả về danh sách ý tưởng — KHÔNG tự chạy tiếp Lớp 2.
- [ ] `/b6/generate` KHÔNG tự chạy Lớp 1 và KHÔNG tự lấy ý tưởng đầu tiên — nhận ý tưởng đã chọn qua `$json.body.angle`.
- [ ] Lớp 3 có node gọi API sinh ảnh, dùng chính trường `image_prompt` của TH3.
- [ ] Có webhook `/b6/approve` riêng, ghi Content_Queue + Publish_Log.
- [ ] Status mặc định `Needs Review`. **Không có** trạng thái `Published`, không có node đăng bài.
- [ ] Cả BA webhook bật CORS `Allowed Origins = *`.
- [ ] Workflow Inactive, đã validate, đã export JSON.
- [ ] Đã in ra 3 webhook URL production.

### Rescue map

| Lỗi | Câu lệnh cứu hộ |
|---|---|
| Agent dựng workflow mà chưa đọc artifact | `Đọc content-angles.json, content-draft.json, content-assets.json trước. Xác nhận ba brief_id khớp rồi mới cấu hình node.` |
| App báo lỗi CORS | `Mở cả BA node Webhook, Options, đặt Allowed Origins = *, Save rồi Activate lại.` |
| Bấm "Viết nội dung đầy đủ" mà báo thiếu ý tưởng / n8n nhận `angle` rỗng | `App phải gửi nguyên object ý tưởng đã chọn trong field "angle" của body khi gọi /b6/generate — không phải chỉ gửi angle_id. Kiểm lại payload gửi đi bằng Console trình duyệt.` |
| n8n nhận request nhưng field rỗng | `Dữ liệu webhook nằm ở $json.body.xxx, không phải $json.xxx. Sửa mọi expression.` |
| Lỗi 404 khi gọi webhook | `URL production không có /webhook-test/. Activate workflow rồi copy lại URL.` |
| Node Sheets không thấy cột | Tên cột phải khớp `content-workbook.xlsx`: `Post ID`, `Angle ID`, `Kênh`, `Nội dung`, `Status`, `Người duyệt`, `Ghi chú`, `Ảnh (Drive)` (thêm 2026-08-11). |
| Ảnh lưu Drive nhưng link không mở ra ảnh (ra trang xin quyền) | `File chưa share "Anyone with the link". Kiểm node "Chia sẻ ảnh" đã chạy chưa, hoặc tự vào Drive bật share tay. Link đúng dạng phải là drive.google.com/uc?export=view&id=..., không phải .../file/d/.../view.` |
| Node Google Drive báo lỗi thiếu tham số khi import | `Tên tham số node Drive khác nhau giữa các phiên bản n8n. Mở node trong UI, n8n thường tự gợi ý ánh xạ lại field cũ sang field mới — chọn đúng thư mục Drive + đúng field nhị phân ("data") rồi lưu lại.` |
| Sheets báo lỗi quyền | Nối lại credential Google Sheets, chọn đúng account đã dùng ở B1. |
| Node ảnh trả lỗi (mọi loại) | `Kiểm credential của node sinh ảnh. Nếu không gọi được, để trống image_url, image_ok=false, vẫn ghi Content_Queue — không chặn cả luồng.` |
| Google báo quota=0 khi sinh ảnh dù model chữ chạy bình thường | `Sinh ảnh Google (Imagen/Gemini image) hầu như luôn cần billing paid-tier riêng, khác model chữ. Đổi sang GeminiGen.ai (credential httpHeaderAuth riêng, key trả phí khác) — xem node mẫu trong n8n-content-engine-solution.json.` |
| GeminiGen báo "Invalid model" | `API bên thứ 3 đổi model liên tục. Gọi GET history/{uuid} hoặc thử submit với model khác trong danh sách hợp lệ GeminiGen trả về (thường: nano-banana-pro, nano-banana-2).` |
| Ảnh GeminiGen chưa xong sau 55s (status vẫn =1) | `Bình thường — nano-banana-pro có lúc cần gần 2 phút, nhưng "thêm cứng vòng chờ thứ 2" TỪNG bị coi nhầm là "không phải lỗi" — thực ra là lỗi thiết kế thật, đã sửa 2026-08-10 bằng vòng lặp IF/Wait thật (Wait 55s → Poll → IF kiểm status, quay lại nếu chưa xong, tối đa 3 lần ~165s). Xem đúng chi tiết ở gotcha #5 trong mục "Đã validate trên instance thật" bên dưới.` |
| Agent viết API key vào workflow | `Bỏ key khỏi workflow JSON. Dùng credential đã có trên n8n.` |
| Agent nói đã chạy được nhưng mới validate | `Bạn mới validate cấu trúc. Nói rõ phần nào đã chạy thật, phần nào chưa.` |
| Quá phút 18 | Cấp `checkpoints/n8n-content-engine-solution.json` để import, học viên chỉ gắn credential và activate. |
| Lỗi 429 "Quota exceeded... free_tier_requests, limit: 0" | `Model đã bị Google đưa free-tier về 0. Đổi sang model Gemini mới nhất còn free tier (kiểm ở Google AI Studio), không phải lỗi credential.` |
| Ghi Sheets báo "document must not be an Office file" | `Spreadsheet đang là file .xlsx thô trên Drive. Mở file → File → Save as Google Sheets → dùng ID của file MỚI tạo ra.` |

---

## Phần B — bt4b (app duyệt)

### Expected state

- [ ] Một file `index.html`, không thư viện ngoài, mở trực tiếp là chạy.
- [ ] Ba ô nhập webhook URL (`angles`, `generate`, `approve`), không hardcode.
- [ ] Có bước chọn ý tưởng TRƯỚC màn viết đầy đủ: nút "Sinh ý tưởng" (gọi `/b6/angles`, hiện 5 thẻ để chọn) và nút "Tự đưa ý tưởng" (gõ tay, không qua AI) — cả hai đều dẫn tới nút "Viết nội dung đầy đủ" mới gọi `/b6/generate`.
- [ ] Hiện được: ảnh, image brief, bài Fanpage, kịch bản TikTok 4 dòng, 5 seeding.
- [ ] Bài Fanpage và cột hình ảnh / lời thoại sửa trực tiếp được.
- [ ] Có cảnh báo `[cần bổ sung]`, từ cấm, cột hình ảnh trống — **chỉ cảnh báo, không chặn**.
- [ ] Nút Approved và Needs Review, bắt buộc điền người duyệt.
- [ ] **Không có nút đăng bài.**
- [ ] Trong file không có API key nào.
- [ ] Bấm duyệt → nhận Log ID → mở Google Sheets thấy một dòng Publish_Log.

### Rescue map

| Lỗi | Câu lệnh cứu hộ |
|---|---|
| App đẹp nhưng không gọi được webhook | `Kiểm CORS ở n8n trước. Sau đó mở Console trình duyệt đọc lỗi thật rồi sửa.` |
| Agent nhét API key vào app để gọi thẳng AI | `Bỏ mọi API key khỏi app. Mọi thứ đi qua webhook n8n.` |
| Agent thêm nút đăng bài | `Bỏ nút đăng. Trạng thái cao nhất app này ghi được là Approved.` |
| Cảnh báo tự sửa nội dung | `Chỉ cảnh báo, không tự sửa và không chặn nút duyệt. Quyết định thuộc người duyệt.` |
| Không sửa được nội dung trên màn hình | `Cho bài Fanpage và cột hình ảnh, lời thoại sửa trực tiếp bằng contenteditable, blur thì lưu lại.` |
| Ảnh không hiện | `Kiểm URL ảnh workflow trả về. Nếu rỗng, hiện ô giữ chỗ kèm dòng "chưa có ảnh" thay vì để trống.` |
| Agent nói xong nhưng chưa gọi webhook lần nào | `Chạy thử một lần: bấm Cần sửa, cho tôi biết Log ID nhận về.` |
| Quá giờ | Cấp `checkpoints/app-duyet-solution.html`, học viên chỉ dán 3 URL của mình. **Từ 2026-08-11: app đọc trực tiếp `templates/*.md` qua `fetch()` nên KHÔNG mở được bằng double-click file — phải chạy `python -m http.server 8000` trong thư mục `06-content-engine` rồi mở `http://localhost:8000/checkpoints/app-duyet-solution.html`.** GV nên chạy sẵn lệnh này trước giờ học, chỉ đưa link localhost cho học viên quá giờ, đỡ mất thời gian giải thích. |

---

## Nghiệm thu cuối buổi

Chạy engine trên chính brief Sunrise Kids, từ đầu tới cuối:

1. App sinh 5 ý tưởng (hoặc người tự đưa 1 ý tưởng riêng), chọn 1.
2. Workflow viết nội dung và ảnh mới từ đúng ý tưởng đã chọn.
3. App hiện bài, ảnh, seeding.
4. Bấm **Approved**.
5. Mở Google Sheets: `Content_Queue` có dòng Status `Approved`, `Publish_Log` có một dòng kèm ngày và người duyệt.

Học viên phải nói được: ba artifact chứng minh logic đúng, workflow đóng gói logic đó để chạy lại trên brief mới, app là chỗ người thật ra quyết định.

## Câu chốt cho GV

> Nội dung thì AI viết trong ba phút. Cái mất ba mươi phút vừa rồi là dựng chỗ cho một người thật ngồi xuống, nhìn bài, nhìn ảnh, rồi chịu trách nhiệm bấm nút. Đó là khác biệt giữa một mẻ nội dung và một cỗ máy giao được cho đội marketing.

## ✅ Đã validate trên instance thật (2026-08-09)

`n8n-content-engine-solution.json` đã chạy thật end-to-end trên 1 instance n8n thật — cả `/b6/generate` lẫn `/b6/approve` đều `finished: true, status: success`, ghi được `Content_Queue`/`Publish_Log` thật. 5 lỗi thật đã gặp và đã sửa vào file solution, GV nên biết trước khi lên lớp:

1. **Model Gemini đổi tên định kỳ.** `gemini-2.0-flash` từng dùng nay bị Google đưa free-tier về 0 (deprecated). File đã đổi sang `gemini-3.1-flash-lite`, nhưng **kiểm lại tên model còn đúng không** trước mỗi lần dạy — vào Google AI Studio xem model nào đang active.
2. **Spreadsheet phải là Google Sheets gốc, không phải file .xlsx nằm trên Drive.** Học viên hay chỉ upload rồi lấy ID luôn — phải bấm thêm **File → Save as Google Sheets** để ra file mới (ID khác), thì n8n Sheets node mới ghi được. Nếu gặp lỗi "document must not be an Office file" thì đúng chỗ này.
3. **Node Sheets phiên bản mới đòi khai báo `columns.schema` rõ ràng** — đã thêm sẵn trong file, nhưng nếu học viên tự dựng bằng tay theo `bt4a-prompt.md` mà dùng giao diện kéo-thả thì không cần lo, n8n UI tự sinh schema khi bấm chọn cột.
4. **Sinh ảnh bằng Google (Imagen/Gemini image) hầu như luôn đòi billing paid-tier riêng, khác hẳn model chữ** — thử cả `gemini-3.1-flash-image` lẫn đổi model qua UI, project vẫn báo quota=0 dù model chữ đã chạy free tier bình thường. Đây là giới hạn billing phía Google cho khả năng sinh ảnh, không sửa được bằng cách đổi cấu hình. **Giải pháp cuối cùng đã áp dụng: đổi hẳn sang GeminiGen.ai** (dịch vụ trung gian trả phí riêng, tách khỏi billing Google Cloud — cùng dịch vụ dùng ở dự án `Agent_Video_AI`). Cần thêm credential `httpHeaderAuth` riêng (header `x-api-key`, tài khoản GeminiGen.ai trả phí). Model dùng: `nano-banana-pro` (LƯU Ý: `imagen-4` từng hợp lệ nhưng bị GeminiGen từ chối ở lần test này — API bên thứ 3 cũng đổi liên tục, kiểm model hợp lệ trước mỗi lần dùng).
5. **GeminiGen sinh ảnh bất đồng bộ, có lúc mất gần 2 phút.** ~~File solution đã chờ 2 vòng (55s + 55s) rồi mới kiểm — 1 vòng không đủ khi test thật.~~ **Sửa lại 2026-08-10** (bị chê đúng — hardcode "chờ-kiểm 2 lần" không hợp lý): giờ là vòng lặp thật — Wait 55s → Poll → node IF `Ảnh xong chưa?` kiểm `status===2`, đúng thì đi tiếp, sai thì quay lại Wait, tối đa 3 lần (~165s). Thoát sớm nếu ảnh xong sớm, thay vì luôn tốn đủ ~110s như bản cũ. Nếu ảnh vẫn chưa xong sau 3 lần, workflow vẫn tiếp tục (không sập), chỉ thiếu ảnh — HV duyệt phần chữ trước, ảnh bổ sung sau. Test thật `--full` xác nhận vòng lặp hoạt động đúng.
6. **`angle_id` AI đôi khi trả sai format** (vd `"ANGLE-01"` thay vì `"A-01"`) vì n8n runtime không có bước validate schema tất định như bài tay TH1-TH3. Không chặn workflow, nhưng nếu muốn kiểm chặt, cần thêm Code node validate riêng — hiện chưa có.
7. **Đã tách `/b6/generate` thành 2 webhook** (`/b6/angles` + `/b6/generate`) để người dùng biết ý tưởng TRƯỚC khi tốn phí ảnh — ban đầu bản đầu tiên tự động lấy cứng `angles[0]`, không cho người chọn. Đã sửa cả n8n (Lớp 1 giờ đứng sau webhook riêng, trả thẳng ra; Lớp 2 đọc `$json.body.angle` thay vì `$json.output.angles[0]`) và App (thêm Bước 1 "Sinh ý tưởng"/"Tự đưa ý tưởng" trước Bước 2 "Viết nội dung đầy đủ"). Test thật ngày 2026-08-09: gọi `/b6/angles` trả đúng 5 ý tưởng (~10s, không tốn ảnh); gọi `/b6/generate` với 1 ý tưởng chọn tay (`ANGLE-01`) ra đúng `angle_id` đó trong kết quả (không lệch sang ý tưởng khác), ảnh thật tải được (HTTP 200, `image/png`, 1.36MB).
8. **Ảnh AI được phép có người/trẻ em (2026-08-09).** Bỏ `no human faces, no children` khỏi prompt Lớp 3 — ảnh AI sinh hoàn toàn, không tham chiếu ai thật nên không phát sinh vấn đề quyền riêng tư (khác ảnh chụp thật). Prompt giờ khuyến khích có người để tăng độ thu hút. (Câu "chỉ còn giữ cấm chữ" ở đây đã lỗi thời — xem gotcha #10 ngay dưới, đổi hướng lần 2 cùng ngày.)
9. **Đã build thật Judge Lớp 2b (văn phong) + Lớp 3b (ảnh, vision) vào n8n** — trước đây chỉ là thiết kế trên giấy ở `prompts/judge-extension-prompt.md`. Test thật ngày 2026-08-09: Judge văn phong trả đúng `{confidence, reason, nghi_bia_so}`; Judge ảnh **phát hiện thật** một lần ảnh có chữ mờ/logo lẫn vào (dù prompt lúc đó chưa yêu cầu chữ nào) và tự động xoá `image_url` trước khi ghi Content_Queue — đúng thiết kế "chỉ chặn riêng ảnh, không dừng cả luồng". Lỗi thật đã gặp: `jsonBody` dựng bằng expression n8n lồng quá sâu (object literal nhiều tầng ngay trong `{{ }}`) báo lỗi `"invalid syntax"` — sửa bằng cách dựng JSON body thật trong Code node (`JSON.stringify` JS thuần), HTTP node chỉ tham chiếu `{{ $json.gemini_body }}` — nếu học viên tự dựng bằng tay và gặp lỗi tương tự, đây chính là nguyên nhân.
10. **Chữ trong ảnh KHÔNG còn bị cấm hoàn toàn (2026-08-09, đổi hướng lần 2, cùng ngày với gotcha #8).** Giả định gốc "model sinh ảnh viết sai chính tả tiếng Việt gần như chắc chắn" **đã sai** với model hiện tại. Test thật trực tiếp qua GeminiGen (`nano-banana-pro`, không qua n8n) với 2 cụm từ có dấu phức tạp ("Học thử miễn phí", "Gò Vấp & Tân Bình") ra đúng 100% — không lỗi chính tả nào. Đã sửa prompt Lớp 3 cho phép TỐI ĐA 1 dòng tiêu đề/CTA ngắn (≤8 từ) hiển thị thẳng trong ảnh, khớp `image_brief.chu_tren_anh`. Judge Lớp 3b đổi vai trò tương ứng: từ "có chữ hay không" sang "chữ có đúng — không thiếu/thừa/lặp/sai chính tả — so với dự kiến". Test thật lần 2 xác nhận rủi ro còn lại có thật: model **lặp thừa** 1 dòng chữ (vẽ "Tiếng Anh" rồi vẽ lại đầy đủ "Tiếng Anh tự nhiên cho bé" ngay dưới) dù prompt chỉ yêu cầu đúng 1 dòng — Judge chặn đúng, đã tải ảnh gốc xác nhận không phải báo nhầm. **Lưu ý encoding Windows:** gõ tiếng Việt có dấu trực tiếp trên dòng lệnh `curl -F` qua Git Bash có thể bị mangle (`?` thay dấu) — phải ghi prompt ra file UTF-8 rồi dùng `curl -F "prompt=<file"` để tránh lỗi giả (không phải lỗi model).
11. **Judge Lớp 3b mở rộng thành 4 tiêu chí (2026-08-09).** Từ 1 field `vi_pham_chinh_sach` đơn lẻ, mở rộng thành `{chu_dung, khong_co_yeu_to_cam, phong_cach_khop, bo_cuc_khop, reason}` — 1 lần gọi vision chấm đủ cả 4, không cần gọi nhiều lần. `vi_pham_chinh_sach` KHÔNG lấy model tự trả — tính tất định trong Code node (`= !chu_dung || !khong_co_yeu_to_cam`) để tránh model tự ý nới lỏng quy tắc cứng. Chỉ 2 tiêu chí đầu (chữ đúng, không có yếu tố cấm) chặn cứng xoá ảnh; `phong_cach_khop`/`bo_cuc_khop` chỉ đưa vào `judge_anh` để App cảnh báo mềm, không chặn — vì đây là đánh giá chủ quan, khác vi phạm khách quan đo được. Test thật: ảnh đạt cả 4 tiêu chí, đã tải ảnh xác nhận Judge không chặn nhầm khi ảnh thực sự tốt (giáo viên bản ngữ + trợ giảng + học sinh đọc sách cùng nhau, chữ "Tiếng Anh tự nhiên cho bé" đúng 100%).
12. **Ethnicity trong ảnh + bỏ ước lượng tuổi khỏi Judge (2026-08-09).** Thêm chỉ dẫn vào prompt Lớp 3: học sinh mô tả là trẻ em người Việt Nam, giáo viên được phép mô tả là người nước ngoài (đúng mô hình "giáo viên bản ngữ"), trợ giảng là người Việt — test thật ra đúng ảnh (giáo viên tóc vàng phương Tây, học sinh + trợ giảng châu Á, xác nhận qua 2 lần tải ảnh xem trực tiếp). Đồng thời phát hiện lỗi thật: Lớp 3 từng tự thêm ước lượng tuổi trẻ em (vd "trẻ dưới 6 tuổi") vào `khong_duoc_xuat_hien` — Judge Lớp 3b đọc danh sách này rồi đoán tuổi trẻ em qua ảnh tĩnh, đoán SAI (nói 4-5 tuổi trong khi ảnh thật trông như 8-9 tuổi) và chặn oan 1 ảnh đạt. Đã sửa cả 2 lớp: Lớp 3 bị cấm liệt kê ước lượng tuổi vào `khong_duoc_xuat_hien` (chỉ được liệt kê điều khách quan như logo/bảng điểm/chữ tiếng Anh), Judge Lớp 3b được dặn bỏ qua nếu lỡ còn sót — phòng hờ 2 lớp. Test thật lại xác nhận: `khong_duoc_xuat_hien` không còn mục nào về tuổi, và lần chặn tiếp theo (nếu có) là vì lý do khách quan thật (vd đã gặp: poster tường giống tài liệu luyện thi) — đã tải ảnh xác nhận đúng.
13. **Sự cố thật: workflow bị GHI ĐÈ về bản cũ giữa lúc đang sửa qua API (2026-08-09).** Đang sửa Judge/prompt qua API thì workflow tụt từ 35 xuống 25 node — mất sạch mọi thay đổi trong ngày (kể cả tách webhook `/b6/angles` từ đầu). Nguyên nhân xác nhận: có người mở tab n8n UI cũ (chưa refresh) và bấm Save cùng lúc — n8n không merge, ai save sau đè hoàn toàn lên bản mới hơn, không cảnh báo conflict. **Bài học cho GV/HV:** nếu vừa sửa workflow qua Coding Agent (API) vừa có người mở workflow đó trên n8n UI, phải đóng/refresh tab UI trước khi Agent sửa tiếp, hoặc không làm song song 2 đường trên cùng 1 workflow. **Cứu được nhờ:** đã đồng bộ `checkpoints/n8n-content-engine-solution.json` từ workflow thật ngay sau mỗi vòng thay đổi lớn trong ngày — khi bị đè, phục hồi lại được từ file JSON đã lưu (chỉ mất phần chưa kịp đồng bộ, tự sửa lại tay được). Nếu không có checkpoint mới, sẽ phải làm lại từ đầu toàn bộ Judge + angle-split.
14. **Gap "TH4a/TH4b không có test tự động" đã đóng một phần (2026-08-10).** `giao_trinh/scripts/validate-b6-n8n-app.py` kiểm TĨNH (không cần n8n đang chạy) trên `n8n-content-engine-solution.json` + `app-duyet-solution.html`: đọc `$json.body.` đúng chỗ, cả 3 webhook bật CORS `*`, Status Content_Queue chỉ trong 5 giá trị hợp lệ (không có `Published`), không key hardcode, node ảnh + cả 2 Judge có `onError`, schema Judge đúng field, app không có nút đăng bài, bắt buộc người duyệt, cảnh báo không khoá nút, lỗi mạng hiện rõ thay vì im lặng. Riêng logic "Judge ảnh chặn thì xoá `image_url`" được chạy THẬT qua Node.js (2 kịch bản đạt/chặn, không phải đoán bằng regex). **Vẫn CHƯA thay được:** hành vi mạng thật (CORS preflight qua trình duyệt thật, double-submit, lỗi mạng thật khi bấm Duyệt) — những cái đó vẫn phải làm theo Nghiệm thu cuối buổi + checklist thủ công ở trên. Chạy: `python giao_trinh/scripts/validate-b6-n8n-app.py`.
15. **Thêm live E2E runner giống B4/B5 (2026-08-10) — `test/interactive_b6_runner.py` + `checkpoints/test-cases.json` (8 case).** Khác B4/B5 ở 2 điểm có lý do thật (không phải làm tắt): (a) không có docker-compose n8n cục bộ dùng chung — workflow B6 gọi LLM + sinh ảnh THẬT trả phí, không tự-chứa được trong container dùng-rồi-bỏ như workflow B5 (B5 định tuyến bằng Code node JS thuần, tất định, miễn phí); script gọi thẳng 3 webhook URL production của một instance đang chạy thật, qua biến môi trường `B6_WEBHOOK_ANGLES/GENERATE/APPROVE` — đúng 3 ô mà app cũng cần. (b) `ky_vong` trong test-cases chỉ kiểm bất biến cấu trúc (số lượng, có/không field, brief_id echo, không bịa chân dung ngoài input) chứ không so khớp chuỗi 1-1 kiểu B5 (`expected_route == actual_route`) — vì nội dung sinh bằng LLM thật không tất định. TC05 (đường đầy đủ Lớp 2→3→4) tốn phí ảnh thật + ~2 phút nên mặc định SKIP, chỉ chạy khi thêm `--full`.
   **Chạy live lần đầu bắt được BUG THẬT:** TC04 (gọi `/b6/generate` thiếu field `angle`) phát hiện workflow KHÔNG báo lỗi mà LLM tự **bịa** `angle_id` (vd `"TUYEN-SINH-MAM-NON"`) rồi viết cả bài từ ý tưởng không ai chọn — vi phạm đúng nguyên tắc cốt lõi cả buổi "không được tự bịa". Giả định tĩnh trước đó (prompt thiếu `||` fallback ⇒ n8n sẽ tự báo lỗi expression) **sai trong thực tế**. Sửa 2 lần: lần 1 dùng Code node `throw Error` — hoá ra n8n vẫn trả **HTTP 200 rỗng** (không đủ rõ ràng, đã tự phát hiện qua `curl` kiểm status code, không chỉ tin JSON). Lần 2 (đúng): thêm node **IF thật** (`Có angle hợp lệ?`, kiểm `$json.body.angle && .angle_id`) chèn giữa Webhook và Lớp 2 — nhánh sai đi tới node Respond riêng (`Trả lỗi — thiếu angle`, `responseCode` phải đặt trong `options.responseCode`, đặt ở gốc `parameters.responseCode` bị n8n bỏ qua âm thầm — cũng tự bắt qua kiểm `curl` status thật). Test lại xác nhận cả 2 nhánh: thiếu `angle` → HTTP 400 + thông báo rõ; có `angle` hợp lệ → chạy `--full` lại vẫn PASS, không gãy luồng chính. Bài học: **test live mới lộ bug live** — test tĩnh chỉ kiểm được cấu hình/code, không kiểm được hành vi runtime thật của n8n. Chạy: `B6_WEBHOOK_ANGLES=... B6_WEBHOOK_GENERATE=... B6_WEBHOOK_APPROVE=... python test/interactive_b6_runner.py [--full]`.
   **Kèm `test/06_content_engine_lab_demo.ipynb`** (song song với runner, giống `05_cskh_bot_lab_demo.ipynb`) — 7 bước GV trình chiếu trên lớp, output baked-in là output THẬT chạy ngày 2026-08-10 (không dán số liệu giả), bước tốn phí (đường đầy đủ Lớp 2→3→4) mặc định tắt qua cờ `CHAY_FULL = False`. **Lưu ý:** mỗi lần chạy notebook/runner sẽ ghi thêm dòng thật vào `Content_Queue`/`Publish_Log` (post_id tiền tố `NOTEBOOK-DEMO-`/`AUTOTEST-` để dễ nhận ra và dọn sau).

16. **Lưu ảnh vào Google Drive, ghi link bền vào Sheets (2026-08-11) — ✅ đã test thật, chạy đúng end-to-end.** Trước đây `image_url` chỉ là link tạm của GeminiGen.ai — không ghi vào Content_Queue/Publish_Log, chỉ sống trong localStorage trình duyệt và log thực thi n8n, mất khi đóng app. Đã thêm vào workflow: sau khi Judge ảnh duyệt, node IF `Có ảnh để lưu Drive?` → tải ảnh về (`Tải ảnh để lưu Drive`) → upload Google Drive (`Lưu ảnh vào Google Drive`) → share "ai có link đều xem được" (`Chia sẻ ảnh (ai có link đều xem được)`) → ghép lại URL trực tiếp dạng `drive.google.com/uc?export=view&id=...` (`Chuẩn hoá link Drive`), rồi ghi vào field `image_url` như cũ — không cần đổi App hiển thị. Cột mới thêm vào cả `Lớp 4 — Ghi Content_Queue` và `Ghi Publish_Log` (Publish_Log lấy qua field `anh_url` mới trong `Chuẩn hóa quyết định`, do App giờ gửi kèm `image_url` khi bấm Duyệt/Cần sửa).

    **⚠️ Tên cột thật trong Sheets là `Ảnh Drive` — KHÔNG có ngoặc đơn.** Bản thiết kế đầu ghi `Ảnh (Drive)`, nhưng khi tạo cột thật trong Content_Queue/Publish_Log, tên gõ vào sheet là `Ảnh Drive` (không dấu ngoặc) — lệch với tên trong node, gây lỗi n8n UI "Column names were updated after the node's setup... Missing columns: Ảnh (Drive)". Thêm nữa: lần bấm "refresh columns" đầu tiên trong n8n UI vô tình xoá mất field `Người duyệt` khỏi mapping của `Lớp 4 — Ghi Content_Queue` (n8n reset toàn bộ `columns.value` về đúng những field còn khớp schema mới, không cảnh báo field nào bị rớt). Đã sửa cả 2: đổi tên field trong node thành `Ảnh Drive` (khớp sheet thật), thêm lại `Người duyệt: ""`. **Bài học:** sau khi đổi tên cột trong Sheets, đừng chỉ bấm refresh rồi tin — mở lại `columns.value` kiểm đủ tất cả field cũ, không chỉ field mới.

    **Đã đẩy thẳng lên workflow thật đang chạy (2026-08-11, qua n8n REST API `n8n-mcp` .mcp.json, không phải qua UI):** workflow `[B6-TEST] Content Engine Sunrise Kids` (id `UW8TZvSg1ZzlcE3b`) trên instance `n8n-qns0.srv1741374.hstgr.cloud`. Quy trình: GET workflow live → so khớp tên node với bản `n8n-content-engine-solution.json` trước khi vá (37/37 khớp, chỉ lệch 4 chỗ cosmetic) → áp bản vá → PUT qua API → GET lại xác nhận đủ 43 node, `active: true`.

    **Test thật end-to-end (2026-08-11), không phải chỉ validate cấu trúc:** gọi `/b6/angles` → chọn 1 angle thật → gọi `/b6/generate` (Lớp 2→3→4, sinh ảnh thật qua GeminiGen, tốn phí + ~2 phút) → response trả `image_url: "https://drive.google.com/uc?export=view&id=..."`, `image_ok: true`, Judge ảnh đạt cả 4 tiêu chí. Dùng `curl -L` xác nhận link trả về `Content-Type: image/png`, HTTP 200 (không phải trang xin quyền — share "anyone/reader" hoạt động đúng). Đọc lại Google Sheet qua Drive xác nhận dòng `Content_Queue` mới có đúng link Drive ở đúng cột `Ảnh Drive`. Gọi tiếp `/b6/approve` (status `Approved`) → dòng `Publish_Log` mới cũng có đúng link Drive ở cột cuối. Cả 2 sheet, cả 2 node đều ghi đúng.

    Còn lại phía GV chỉ cần: dọn 2 dòng test (`POST-260811182056` / `LOG-260811182216`, người duyệt "Claude Code (test Drive integration)") khỏi Sheets trước khi dạy thật.
