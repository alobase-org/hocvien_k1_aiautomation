# Thiết kế Chi tiết Use-case: Hệ thống Tự động hóa Chấm điểm & Cá nhân hóa Bài tập về nhà cho Học sinh

## 1. Mô tả bài toán & Usecase
* **Bối cảnh:** Tại các cơ sở giáo dục, trung tâm đào tạo hoặc lớp học, việc kiểm tra bài tập về nhà (homework) là một phần thiết yếu trong quá trình học tập. Học sinh thường hoàn thành bài tập viết tay trên giấy, chụp ảnh lại bằng điện thoại và nộp qua các kênh giao tiếp phổ biến như Google Drive, Zalo, Telegram hoặc các cổng LMS (Learning Management System).
* **Vấn đề tồn tại:**
  - **Tốn thời gian chấm điểm thủ công:** Giáo viên phải căng mắt đọc chữ viết tay trên từng bức ảnh điện thoại (thường bị mờ, lệch góc, thiếu sáng), đối chiếu với đáp án mẫu, ghi điểm số và viết lời nhận xét cho từng học sinh. Quy trình này mất trung bình 5-10 phút/học sinh, tức là khoảng 3-6 tiếng cho một lớp 40 học sinh.
  - **Thời gian phản hồi chậm:** Do quá tải công việc, giáo viên thường mất từ 2-3 ngày để trả bài. Điều này làm giảm hiệu quả sửa sai khi học sinh đã quên mất nội dung bài làm và tư duy giải bài trước đó.
  - **Không cá nhân hóa được bài tập về nhà:** Do hạn chế về thời gian, giáo viên buộc phải giao chung một bộ đề bài tập cho cả lớp. Kết quả là học sinh khá giỏi cảm thấy quá dễ, trong khi học sinh yếu cảm thấy quá tải và nản lòng. Giáo viên không có đủ nguồn lực để thiết kế đề bài riêng phù hợp với lỗ hổng kiến thức của từng học sinh.
  - **Dữ liệu phân mảnh:** Điểm số và nhận xét nằm rải rác trên file ảnh, tin nhắn Chat hoặc sổ tay cá nhân của giáo viên, gây khó khăn cho việc theo dõi tiến độ học tập lâu dài và báo cáo cho phụ huynh.
* **Mục tiêu tự động hóa:** Xây dựng một quy trình tự động hóa tích hợp AI (gồm 2 luồng chính):
  - **Luồng 1 (Chấm điểm & Phản hồi tự động):** Tự động thu thập ảnh chụp bài làm, sử dụng AI Vision để số hóa chữ viết tay, so sánh với đáp án chuẩn, tự động chấm điểm chi tiết từng câu, viết nhận xét mang tính sư phạm và cập nhật trực tiếp vào sổ điểm Google Sheets.
  - **Luồng 2 (Cá nhân hóa bài tập về nhà):** Phân tích kết quả học tập của từng học sinh từ Luồng 1, xác định phần kiến thức học sinh bị hổng, từ đó tự động sinh đề bài tập về nhà cá nhân hóa (hoặc theo nhóm năng lực học tập) để củng cố lỗ hổng kiến thức trước khi gửi giáo viên phê duyệt và giao bài.

---

## 2. Dữ liệu đầu vào (Input) & Đầu ra (Output)

| Quy trình | Dữ liệu đầu vào (Input) & Nguồn | Kết quả đầu ra (Output) & Trạng thái |
| :--- | :--- | :--- |
| **Luồng 1: Chấm điểm bài làm qua ảnh chụp** | - Ảnh chụp bài làm của học sinh (`.jpg`, `.png`, hoặc `.pdf` dạng scan) được nộp vào thư mục Google Drive chung.<br>- Tên file được đặt theo quy chuẩn: `[MãHọcSinh]_[TênHọcSinh]_[MãBàiTập].[ĐuôiFile]`.<br>- File đáp án mẫu (Rubric/Answer Key) do giáo viên cung cấp (`.txt`, `.docx` hoặc `.md`).<br>- Danh sách lớp học chứa thông tin học sinh (`.xlsx`/Google Sheets). | - Nội dung bài làm đã số hóa thành văn bản dạng Markdown (`.md`).<br>- Báo cáo chấm điểm chi tiết (Điểm số từng câu, lỗi sai, lời giải thích) được cập nhật vào Sổ điểm Google Sheets.<br>- File ảnh bài làm gốc được vẽ thêm ghi chú khoanh vùng lỗi sai (nếu sử dụng thư viện xử lý ảnh).<br>- Bản nháp nhận xét gửi học sinh/phụ huynh. |
| **Luồng 2: Tạo bài tập về nhà cá nhân hóa** | - Báo cáo điểm số và phân tích lỗ hổng kiến thức của học sinh từ Luồng 1.<br>- Ngân hàng câu hỏi/đề bài mẫu hoặc tài liệu giáo trình chuẩn của môn học.<br>- Yêu cầu về cấu trúc đề của giáo viên (ví dụ: Số lượng câu, tỷ lệ Nhận biết/Thông hiểu/Vận dụng, thời gian làm bài). | - File đề bài tập về nhà cá nhân hóa cho từng học sinh (hoặc nhóm học lực) dưới dạng file PDF/Markdown.<br>- File đáp án chi tiết tương ứng để giáo viên đối chiếu.<br>- Email hoặc tin nhắn nháp thông báo giao bài tự động gửi qua hệ thống. |

---

## 3. Giá trị kỳ vọng (Expected Value)
* **Định lượng (Quantitative):**
  - **Tiết kiệm thời gian chấm bài:** Tiết kiệm từ **6 - 8 giờ làm việc/tuần** cho mỗi giáo viên nhờ loại bỏ việc kiểm tra thủ công và ghi chép sổ điểm.
  - **Rút ngắn tốc độ xử lý bài nộp:** Thời gian phản hồi bài làm cho học sinh giảm từ **48-72 giờ xuống dưới 10 phút** kể từ lúc học sinh tải ảnh lên hệ thống.
  - **Tỷ lệ cá nhân hóa đề bài:** Đảm bảo **100% học sinh** gặp khó khăn về kiến thức được giao đề bài ôn tập củng cố riêng biệt mà không làm phát sinh thêm giờ soạn bài của giáo viên.
* **Định tính (Qualitative):**
  - Giảm tải áp lực công việc hành chính cho giáo viên, nâng cao sự hài lòng và giúp họ tập trung vào công tác chuyên môn, kèm cặp học sinh trực tiếp.
  - Tăng độ chính xác và tính khách quan trong chấm điểm nhờ tiêu chí (Rubric) được AI áp dụng nhất quán.
  - Cải thiện trải nghiệm học tập của học sinh nhờ nhận được phản hồi tức thì, đúng trọng tâm kiến thức bị hổng và làm bài tập vừa sức.

---

## 4. Rủi ro cần quản lý (Risks & Mitigation)

| # | Rủi ro | Mức độ | Phương án giảm thiểu (Mitigation) |
|---|--------|:---:|----------------------|
| 1 | AI nhận diện sai chữ viết tay của học sinh do chữ quá ẩu, viết nháp đè lên nhau, hoặc ảnh chụp bị mờ, mất góc. | Cao | - Đưa ra hướng dẫn chuẩn cho học sinh về cách chụp ảnh bài làm (chụp thẳng góc, đủ ánh sáng, viết rõ ràng).<br>- Sử dụng mô hình Vision LLM chất lượng cao (Gemini 1.5 Pro hoặc GPT-4o) được tối ưu hóa cho nhận diện chữ viết tay đa ngôn ngữ.<br>- Thiết lập ngưỡng tin cậy (Confidence Score): Nếu AI đánh giá độ chính xác của nội dung OCR dưới 80%, hệ thống tự động gắn cờ đỏ và chuyển bài làm sang thư mục chờ chấm thủ công. |
| 2 | AI chấm điểm sai hoặc đưa ra lời nhận xét thiếu tính sư phạm, gây ức chế cho học sinh. | Trung bình | - Cung cấp prompt chấm điểm có kèm theo Rubric chi tiết và các ví dụ mẫu chấm (Few-shot Prompting).<br>- Áp dụng cơ chế **Human-in-the-loop (HITL)**: Điểm số và nhận xét từ AI chỉ ở trạng thái "Bản nháp" (Draft). Giáo viên phải xem lại và phê duyệt trước khi gửi kết quả đi. |
| 3 | AI sinh đề bài tập về nhà bị lỗi kiến thức (Hallucination - ảo tưởng) hoặc vượt quá chương trình học chính thống. | Trung bình | - Áp dụng phương pháp **RAG (Retrieval-Augmented Generation)**: Hạn chế nguồn ngữ cảnh của AI, chỉ cho phép AI sinh đề dựa trên ngân hàng câu hỏi sẵn có hoặc tài liệu giáo trình chính thống do nhà trường cung cấp.<br>- Định nghĩa rõ ràng độ khó của câu hỏi theo khung phân loại Bloom trong prompt. |
| 4 | Rò rỉ thông tin cá nhân và kết quả học tập của học sinh lên môi trường cloud công cộng. | Cao | - Ẩn danh hóa thông tin trước khi gửi lên API của LLM (thay thế tên học sinh bằng ID ẩn danh như `HS001`, `HS002`).<br>- Sử dụng các API phiên bản Enterprise có cam kết bảo mật dữ liệu doanh nghiệp (không lưu trữ dữ liệu người dùng để huấn luyện mô hình). |

---

## 5. Điểm chạm Con người (Human-in-the-Loop - HITL)
* **Kiểm duyệt và Duyệt điểm (Approve Grades & Feedback):** Sau khi AI chấm bài và soạn nhận xét, hệ thống hiển thị giao diện Dashboard so sánh trực quan cho giáo viên: `[Ảnh bài làm gốc của học sinh]` vs `[Nội dung AI trích xuất & Điểm/Nhận xét đề xuất]`. Giáo viên có thể nhanh chóng chỉnh sửa lại điểm hoặc nội dung nhận xét và bấm nút **"Duyệt & Gửi"** để phát hành kết quả.
* **Xử lý bài nộp lỗi (Exception Handling):** Đối với các bài làm bị lỗi ảnh mờ, chữ quá xấu không đọc được hoặc lỗi định dạng, AI Agent tự động di chuyển tệp tin vào thư mục `/Can_Cham_Thu_Cong/` và gửi thông báo trực tiếp đến giáo viên để chấm tay.
* **Duyệt đề bài tập về nhà cá nhân hóa (Approve Homework Generation):** Trước khi đề bài tập về nhà được gửi đến học sinh, giáo viên phải xem qua bộ đề do AI tạo ra (ở trạng thái bản nháp) để kiểm tra tính hợp lý của câu hỏi và bấm xác nhận để giao bài hàng loạt.

---

## 6. Các ràng buộc & Điều kiện biên khác (Constraints & Assumptions)
* **Bảo mật dữ liệu (Data Privacy):** Tuyệt đối không gửi trực tiếp thông tin nhạy cảm của học sinh (như họ tên đầy đủ, ngày sinh, địa chỉ) lên các mô hình LLM công cộng. Quy trình xử lý dữ liệu phải tuân thủ nghiêm ngặt chính sách bảo vệ thông tin cá nhân trong giáo dục.
* **Ràng buộc hạ tầng công nghệ:**
  - Hệ thống chạy tự động dựa trên các script Python kết hợp với nền tảng tự động hóa (như n8n hoặc Make) để kết nối Google Drive, Google Sheets và API của LLM.
  - Yêu cầu kết nối Internet ổn định để gọi API của LLM.
* **Giới hạn kỹ thuật:**
  - Ảnh bài làm đầu vào phải có định dạng phổ biến (`.jpg`, `.png`, `.pdf`) với kích thước không vượt quá 10MB.
  - Phải có file hướng dẫn chấm điểm (Answer Key/Rubric) chi tiết do giáo viên cung cấp trước. AI không thể tự suy diễn barem chấm điểm nếu không có dữ liệu đối chiếu chuẩn xác.
* **Giả định (Assumptions):**
  - Học sinh có thiết bị di động để chụp ảnh bài tập và đã được hướng dẫn quy chuẩn nộp bài.
  - Sổ điểm được lưu trữ tập trung trên Google Sheets hoặc một cơ sở dữ liệu có sẵn kết nối API.
