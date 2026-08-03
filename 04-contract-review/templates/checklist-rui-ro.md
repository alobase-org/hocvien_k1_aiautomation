# KHO TRI THỨC RED FLAGS & CÁC DẠNG CÀI CẮM, BẪY HỢP ĐỒNG THỰC TẾ
## (Contract Review Knowledge Base — Red Flags & Subversive Clauses)

> **Dành cho**: AI Contract Review Agent (n8n Workflow) & Chuyên viên Thẩm định Hợp đồng / Pháp chế Doanh nghiệp.
> **Mục tiêu**: Cung cấp cơ sở dữ liệu tri thức số hóa chuẩn (Knowledge Base) phục vụ rà soát hợp đồng tự động, phát hiện các điều khoản bất lợi, bẫy gài cắm pháp lý và gợi ý sửa đổi (Redline).

---

## I. CẤU TRÚC KHO TRI THỨC (KNOWLEDGE BASE SPECIFICATION)

Mỗi tiêu chí rà soát được quy chuẩn theo 6 thành phần:
1. **Mã Tiêu Chí (ID)**: TC01 - TC12.
2. **Tên Hạng Mục Rà Soát**: Tên nhóm điều khoản thương mại / pháp lý.
3. **Từ khóa Kích hoạt (Trigger Words)**: Nhận diện điều khoản liên quan trong văn bản.
4. **Các Dạng Bẫy Thực Tế & Kịch bản Cài Cắm (Real-world Contract Traps)**: Mô tả chi tiết cách đối tác thường lồng ghép bẫy.
5. **Mức độ Rủi ro (Risk Severity)**:
   - 🔴 **HIGH (Cao)**: Nguy cơ thiệt hại tài chính lớn, mất quyền sở hữu tài sản/IP, hoặc gánh trách nhiệm pháp lý vô hạn.
   - 🟡 **MED (Trung bình)**: Gây bất lợi về tiến độ, thủ tục phức tạp, mất cân bằng nghĩa vụ.
   - 💡 **LOW (Thấp)**: Thiếu sót thủ tục hành chính, cần làm rõ từ ngữ mập mờ.
6. **Mẫu Điều khoản Đối ứng / Đề xuất Redline (Counter-clause Standard)**: Mẫu câu sửa đổi chuẩn doanh nghiệp để đàm phán lại.

---

## II. KHO DỮ LIỆU RED FLAGS & CÁC BẪY HỢP ĐỒNG THỰC TẾ (12 TIÊU CHÍ)

### TC01: Đối tượng & Phạm vi Hợp đồng (Scope of Work & Deliverables)

- **Phân loại**: Tiêu chí Bắt buộc (`bat_buoc = true`).
- **Từ khóa trigger**: `phạm vi`, `bàn giao`, `hạng mục`, `phát sinh`, `không giới hạn`, `phối hợp`, `kèm theo`, `theo yêu cầu của bên A`.
- **Dạng bẫy & Kịch bản cài cắm thực tế**:
  - 🔴 **Bẫy 1.1 — Scope Creep mở (Mập mờ phát sinh)**:
    - *Dấu hiệu*: Thêm câu *"Bên B có nghĩa vụ thực hiện các công việc khác theo yêu cầu thực tế của Bên A mà không tính thêm chi phí"*.
    - *Rủi ro*: Bên B bị ép làm khối lượng công việc gấp đôi/gấp ba ban đầu mà không được thanh toán phụ phí.
  - 🟡 **Bẫy 1.2 — Phụ thuộc một chiều (Dependency Trap)**:
    - *Dấu hiệu*: *"Bên B cam kết hoàn thành đúng tiến độ bất kể thời gian Bên A cung cấp thông tin/mặt bằng"*.
    - *Rủi ro*: Bên A chậm bàn giao tài nguyên/dữ liệu nhưng Bên B vẫn bị phạt trễ hạn.
  - 🔴 **Bẫy 1.3 — Bẫy thiếu Phụ lục Kỹ thuật/SLA (Omission)**:
    - *Dấu hiệu*: Hợp đồng không đính kèm Phụ lục mô tả tiêu chí chấp nhận (Acceptance Criteria) hoặc SLA.
    - *Rủi ro*: Bên A từ chối nghiệm thu với lý do "chưa đúng kỳ vọng" bất kỳ lúc nào.
- **Đề xuất Redline**:
  > *"Mọi công việc phát sinh nằm ngoài Phụ lục 01 phải được hai bên thống nhất bằng Phụ lục bổ sung trước khi triển khai và được tính phí riêng. Trường hợp Bên A chậm cung cấp thông tin/mặt bằng quá 03 ngày làm việc, tiến độ của Bên B sẽ được tự động gia hạn tương ứng."*

---

### TC02: Giá trị, Đồng tiền & Điều khoản Thanh toán (Payment Terms & Financials)

- **Phân loại**: Tiêu chí Bắt buộc (`bat_buoc = true`).
- **Từ khóa trigger**: `giá trị hợp đồng`, `đợt thanh toán`, `nghiệm thu`, `hài lòng`, `hóa đơn`, `chậm thanh toán`, `lãi suất`, `tài khoản`.
- **Dạng bẫy & Kịch bản cài cắm thực tế**:
  - 🔴 **Bẫy 2.1 — Nghiệm thu theo cảm tính Bên A**:
    - *Dấu hiệu*: *"Đợt thanh toán cuối chỉ được thực hiện sau khi Bên A nghiệm thu và hoàn toàn hài lòng với chất lượng dịch vụ"*.
    - *Rủi ro*: Bên A kéo dài nghiệm thu vô thời hạn để hoãn giải ngân đợt cuối (thường là 10-30% lợi nhuận).
  - 🔴 **Bẫy 2.2 — Không có lãi phạt chậm thanh toán cho Bên A (Omission/Unfair)**:
    - *Dấu hiệu*: Hợp đồng phạt Bên B nếu giao hàng chậm, nhưng KHÔNG có điều khoản phạt Bên A nếu thanh toán trễ.
    - *Rủi ro*: Bên A trễ hạn 6 tháng - 1 năm mà Bên B không có cơ sở đòi tiền lãi quá hạn.
  - 🟡 **Bẫy 2.3 — Ma trận chứng từ thanh toán (Documentation Trap)**:
    - *Dấu hiệu*: Yêu cầu quá nhiều chứng từ hành chính phức tạp (xác nhận của bên thứ 3, hóa đơn gốc nhiều bản) mới giải ngân.
    - *Rủi ro*: Bên A lấy cớ thiếu 1 tờ xác nhận nhỏ để từ chối chuyển tiền.
- **Đề xuất Redline**:
  > *"Bên A có trách nhiệm phản hồi Biên bản Nghiệm thu trong vòng 05 ngày làm việc kể từ khi nhận được. Quá thời hạn trên mà không có ý kiến bằng văn bản, sản phẩm/dịch vụ được coi là đã nghiệm thu đạt chuẩn. Nếu Bên A chậm thanh toán quá 07 ngày, Bên A chịu lãi phạt 0.05%/ngày trên số tiền chậm trả."*

---

### TC03: Nghĩa vụ các Bên & Điểm phụ thuộc (Obligations & Dependencies)

- **Phân loại**: Tiêu chí Bắt buộc (`bat_buoc = true`).
- **Từ khóa trigger**: `nghĩa vụ bên A`, `nghĩa vụ bên B`, `cam kết`, `đảm bảo`, `bố trí nhân sự`, `phối hợp`.
- **Dạng bẫy & Kịch bản cài cắm thực tế**:
  - 🟡 **Bẫy 3.1 — Độc quyền nhân sự (Key-person Lockout)**:
    - *Dấu hiệu*: *"Bên B không được thay đổi nhân sự dự án trong suốt thời hạn hợp đồng. Mỗi lượt thay đổi nhân sự phạt 50.000.000 VNĐ"*.
    - *Rủi ro*: Nhân sự Bên B nghỉ việc là yếu tố khách quan, quy định phạt cứng gây tổn thất phi lý.
  - 🔴 **Bẫy 3.2 — Đổ toàn bộ nghĩa vụ pháp lý sang Bên B**:
    - *Dấu hiệu*: *"Bên B chịu toàn bộ trách nhiệm và chi phí phát sinh nếu dự án bị cơ quan nhà nước kiểm tra hoặc xử phạt"*.
    - *Rủi ro*: Lỗi có thể do giấy phép/mặt bằng của Bên A, nhưng Bên B gánh toàn bộ trách nhiệm.
- **Đề xuất Redline**:
  > *"Trong trường hợp cần thay đổi nhân sự, Bên B có trách nhiệm thông báo trước 05 ngày làm việc và bố trí nhân sự có trình độ tương đương thay thế. Mỗi bên chịu trách nhiệm pháp lý đối với các vi phạm thuộc phạm vi thẩm quyền và nghĩa vụ của mình."*

---

### TC04: Thời hạn, Tiến độ & Mốc bàn giao (Duration & Milestones)

- **Phân loại**: Tiêu chí Bắt buộc (`bat_buoc = true`).
- **Từ khóa trigger**: `thời hạn hợp đồng`, `ngày có hiệu lực`, `tiến độ`, `mốc bàn giao`, `milestone`, `gia hạn`.
- **Dạng bẫy & Kịch bản cài cắm thực tế**:
  - 🔴 **Bẫy 4.1 — Tiến độ đóng đinh (Fixed-date Trap)**:
    - *Dấu hiệu*: Quy định ngày hoàn tất cố định (ví dụ: 30/12/2026) mà không trừ đi thời gian tạm dừng do lỗi Bên A hoặc bất khả kháng.
    - *Rủi ro*: Bên B chắc chắn vi phạm hợp đồng nếu có rủi ro khách quan xảy ra.
  - 🟡 **Bẫy 4.2 — Thời hạn hợp đồng mập mờ**:
    - *Dấu hiệu*: KHÔNG ghi rõ ngày bắt đầu có hiệu lực (ví dụ: "có hiệu lực từ ngày ký" nhưng ngày ký để trống).
- **Đề xuất Redline**:
  > *"Thời hạn thực hiện hợp đồng được tính từ ngày Bên B nhận đủ tiền tạm ứng đợt 1 và nhận đầy đủ bàn giao mặt bằng/dữ liệu từ Bên A. Mọi sự chậm trễ từ phía Bên A sẽ làm kéo dài thời gian thực hiện của Bên B tương ứng."*

---

### TC05: Điều khoản Chấm dứt & Đơn phương Chấm dứt (Termination & Exit Strategy)

- **Phân loại**: Tiêu chí Bắt buộc (`bat_buoc = true`). *(Lưu ý: Hợp đồng mẫu B4 thường cố ý bỏ sót TC05 để kiểm tra Omission)*.
- **Từ khóa trigger**: `chấm dứt hợp đồng`, `đơn phương`, `hủy bỏ`, `thông báo trước`, `hậu quả chấm dứt`, `hoàn trả`.
- **Dạng bẫy & Kịch bản cài cắm thực tế**:
  - 🔴 **Bẫy 5.1 — Đơn phương hủy hợp đồng bất bình đẳng (One-sided Termination)**:
    - *Dấu hiệu*: *"Bên A có quyền đơn phương chấm dứt hợp đồng bất kỳ lúc nào bằng việc thông báo trước 03 ngày và không phải bồi thường. Bên B đơn phương chấm dứt chịu phạt 100% giá trị hợp đồng"*.
    - *Rủi ro*: Bên B đầu tư máy móc/nhân sự xong thì Bên A hủy ngang, Bên B trắng tay.
  - 🔴 **Bẫy 5.2 — Thiếu quy định về hậu quả tài chính khi chấm dứt (Exit Financial Trap)**:
    - *Dấu hiệu*: Chấm dứt hợp đồng nhưng không ghi rõ Bên A phải thanh toán phần khối lượng Bên B đã làm dở dang.
- **Đề xuất Redline**:
  > *"Mỗi bên có quyền đơn phương chấm dứt hợp đồng nếu bên kia vi phạm nghiêm trọng nghĩa vụ và không khắc phục trong vòng 15 ngày kể từ khi nhận được thông báo. Trường hợp Bên A đơn phương chấm dứt không do lỗi của Bên B, Bên A phải thanh toán toàn bộ chi phí cho phần công việc Bên B đã thực hiện cùng khoản tiền phạt bằng 10% giá trị hợp đồng."*

---

### TC06: Bảo mật Thông tin & Dữ liệu (Confidentiality / NDA)

- **Phân loại**: Tiêu chí Bắt buộc (`bat_buoc = true`).
- **Từ khóa trigger**: `bảo mật`, `thông tin bảo mật`, `NDA`, `tiết lộ`, `bên thứ ba`, `thời hạn bảo mật`, `chế tài bảo mật`.
- **Dạng bẫy & Kịch bản cài cắm thực tế**:
  - 🔴 **Bẫy 6.1 — Bảo mật vô thời hạn & Phạm vi tràn lan**:
    - *Dấu hiệu*: Định nghĩa "Thông tin bảo mật" là *mọi thông tin Bên B tiếp cận được* và nghĩa vụ bảo mật kéo dài *vĩnh viễn (vô thời hạn)*.
    - *Rủi ro*: Bên B dễ vô tình vi phạm NDA nhiều năm sau khi hợp đồng kết thúc.
  - 🔴 **Bẫy 6.2 — Phạt chế tài phạt bảo mật siêu ngạch không chứng minh thiệt hại**:
    - *Dấu hiệu*: *"Mỗi vi phạm bảo mật phạt 5.000.000.000 VNĐ bất kể có gây thiệt hại thực tế hay không"*.
- **Đề xuất Redline**:
  > *"Nghĩa vụ bảo mật có hiệu lực trong thời hạn hợp đồng và tiếp tục kéo dài 02 năm kể từ ngày hợp đồng chấm dứt. Thông tin bảo mật không bao gồm các thông tin đã được công khai hợp pháp hoặc do bên nhận thông tin tự nghiên cứu độc lập."*

---

### TC07: Sở hữu Trí tuệ & Sản phẩm phái sinh (Intellectual Property - IP Rights)

- **Phân loại**: Tiêu chí Bắt buộc (`bat_buoc = true`).
- **Từ khóa trigger**: `sở hữu trí tuệ`, `bản quyền`, `quyền tác giả`, `sản phẩm phái sinh`, `chuyển giao quyền`, `source code`, `bí quyết`.
- **Dạng bẫy & Kịch bản cài cắm thực tế**:
  - 🔴 **Bẫy 7.1 — Cướp IP trước khi hoàn tất thanh toán**:
    - *Dấu hiệu*: *"Tất cả mã nguồn, thiết kế, quyền sở hữu trí tuệ phát sinh trong quá trình thực hiện thuộc về Bên A ngay từ thời điểm tạo ra"*.
    - *Rủi ro*: Bên A lấy mã nguồn/thiết kế rồi xùng xằng không thanh toán tiền đợt cuối, Bên B mất trắng IP.
  - 🟡 **Bẫy 7.2 — Tước đoạt IP nền tảng (Background IP Trap)**:
    - *Dấu hiệu*: Bên A đòi sở hữu cả thư viện/công cụ sẵn có (Background IP) mà Bên B đã dùng để tạo ra sản phẩm.
- **Đề xuất Redline**:
  > *"Quyền sở hữu trí tuệ đối với các sản phẩm/kết quả công việc chỉ được chuyển giao hoàn toàn cho Bên A sau khi Bên A đã hoàn tất 100% nghĩa vụ thanh toán theo hợp đồng. Bên B giữ nguyên quyền sở hữu đối với các tài sản trí tuệ có trước (Background IP)."*

---

### TC08: Bảo hành & Giới hạn Trách nhiệm (Warranty & Limitation of Liability)

- **Phân loại**: Tiêu chí Bắt buộc (`bat_buoc = true`).
- **Từ khóa trigger**: `bảo hành`, `sửa chữa`, `giới hạn trách nhiệm`, `bồi thường tối đa`, `thiệt hại gián tiếp`, `lost profits`.
- **Dạng bẫy & Kịch bản cài cắm thực tế**:
  - 🔴 **Bẫy 8.1 — Bồi thường thiệt hại gián tiếp không giới hạn (Consequential Damages Trap)**:
    - *Dấu hiệu*: KHÔNG loại trừ thiệt hại gián tiếp, bắt Bên B bồi thường "mất doanh thu, mất cơ hội kinh doanh, suy giảm uy tín thương hiệu" của Bên A.
    - *Rủi ro*: Một sự cố nhỏ có thể dẫn tới khoản bồi thường hàng chục tỷ đồng, gây phá sản Bên B.
  - 🔴 **Bẫy 8.2 — Giới hạn trách nhiệm lệch cán cân**:
    - *Dấu hiệu*: Trách nhiệm bồi thường của Bên A giới hạn ở 0 VNĐ, nhưng Bên B chịu trách nhiệm vô hạn.
- **Đề xuất Redline**:
  > *"Trong mọi trường hợp, tổng trách nhiệm bồi thường thiệt hại của Bên B theo hợp đồng này không vượt quá 100% tổng giá trị thực tế Bên B đã nhận được từ Hợp đồng. Hai bên nhất trí loại trừ toàn bộ trách nhiệm đối với các thiệt hại gián tiếp, thiệt hại hệ quả hoặc lợi nhuận bị mất."*

---

### TC09: Gia hạn Tự động (Auto-renewal Traps)

- **Phân loại**: Tiêu chí Mở rộng (`bat_buoc = false`).
- **Từ khóa trigger**: `tự động gia hạn`, `auto-renew`, `thời hạn báo hủy`, `thông báo không gia hạn`.
- **Dạng bẫy & Kịch bản cài cắm thực tế**:
  - 🟡 **Bẫy 9.1 — Cửa sổ báo hủy quá ngắn (Opt-out Window Trap)**:
    - *Dấu hiệu*: *"Hợp đồng tự động gia hạn thêm 01 năm trừ khi Bên B gửi thông báo không gia hạn bằng văn bản trước đúng 60 ngày so với ngày hết hạn"*.
    - *Rủi ro*: Quên báo trước 60 ngày (ví dụ trễ 1 ngày) khiến hợp đồng bị trói buộc thêm 1 năm với chi phí cao.
- **Đề xuất Redline**:
  > *"Hợp đồng chỉ được gia hạn khi hai bên thống nhất bằng văn bản (Phụ lục hợp đồng) trước khi hết hạn ít nhất 30 ngày. Không áp dụng cơ chế tự động gia hạn mặc định."*

---

### TC10: Bất khả kháng (Force Majeure)

- **Phân loại**: Tiêu chí Bắt buộc (`bat_buoc = true`).
- **Từ khóa trigger**: `bất khả kháng`, `dịch bệnh`, ` thiên tai`, `chiến tranh`, `thay đổi luật`, `thủ tục thông báo`, `miễn trừ`.
- **Dạng bẫy & Kịch bản cài cắm thực tế**:
  - 🟡 **Bẫy 10.1 — Loại trừ dịch bệnh / chính sách nhà nước ra khỏi Bất khả kháng**:
    - *Dấu hiệu*: Định nghĩa Bất khả kháng chỉ gồm thiên tai/động đất, loại trừ việc thay đổi chính sách pháp luật hoặc phong tỏa/dịch bệnh.
  - 🟡 **Bẫy 10.2 — Thời hạn thông báo bất khả kháng quá ngặt nghèo**:
    - *Dấu hiệu*: Bắt thông báo sự kiện bất khả kháng trong vòng 24 giờ, nếu quá hạn thì mất quyền miễn trừ trách nhiệm.
- **Đề xuất Redline**:
  > *"Sự kiện Bất khả kháng bao gồm nhưng không giới hạn ở thiên tai, dịch bệnh, đình công, sự cố hạ tầng quốc gia hoặc sự thay đổi chính sách/pháp luật của nhà nước. Bên gặp sự kiện có trách nhiệm thông báo cho bên kia trong vòng 07 ngày làm việc."*

---

### TC11: Phạt Vi phạm & Bồi thường Thiệt hại (Penalties & Statutory Caps)

- **Phân loại**: Tiêu chí Bắt buộc (`bat_buoc = true`).
- **Từ khóa trigger**: `phạt vi phạm`, `mức phạt`, `bồi thường thiệt hại`, `8%`, `vi phạm hợp đồng`, `phạt trùng`.
- **Dạng bẫy & Kịch bản cài cắm thực tế**:
  - 🔴 **Bẫy 11.1 — Phạt vi phạm vượt trần Luật Thương mại (Statutory Cap Violation)**:
    - *Dấu hiệu*: Quy định phạt vi phạm 20% - 50% giá trị hợp đồng (Trong khi Điều 301 Luật Thương mại 2005 khống chế tối đa **8%** giá trị phần nghĩa vụ bị vi phạm).
    - *Rủi ro*: Điều khoản bị tuyên vô hiệu khi tranh chấp, hoặc gánh khoản phạt phi lý nếu không nắm luật.
  - 🔴 **Bẫy 11.2 — Phạt trùng lắp (Double Penalty)**:
    - *Dấu hiệu*: Vừa áp dụng phạt vi phạm max trần, vừa phạt tiền theo ngày không giới hạn mà không khấu trừ.
- **Đề xuất Redline**:
  > *"Mức phạt vi phạm hợp đồng do hai bên thỏa thuận nhưng không vượt quá 8% giá trị phần nghĩa vụ hợp đồng bị vi phạm theo quy định của Luật Thương mại Việt Nam."*

---

### TC12: Giải quyết Tranh chấp & Luật Áp dụng (Dispute Resolution & Governing Law)

- **Phân loại**: Tiêu chí Bắt buộc (`bat_buoc = true`).
- **Từ khóa trigger**: `giải quyết tranh chấp`, `thương lượng`, `hòa giải`, `trọng tài`, `tòa án`, `luật áp dụng`, `thẩm quyền`.
- **Dạng bẫy & Kịch bản cài cắm thực tế**:
  - 🔴 **Bẫy 12.1 — Thẩm quyền Tòa án tỉnh xa / Bất lợi địa lý**:
    - *Dấu hiệu*: Cả 2 bên ở Hà Nội nhưng hợp đồng ghi *"Mọi tranh chấp do Tòa án nhân dân tỉnh Cà Mau giải quyết"*.
    - *Rủi ro*: Tốn kém chi phí đi lại, ăn ở, tố tụng vượt xa giá trị tranh chấp.
  - 🔴 **Bẫy 12.2 — Ép xử lý tại Trọng tài Quốc tế đắt đỏ (SIAC/HKIAC)**:
    - *Dấu hiệu*: Hợp đồng giá trị 500 triệu VNĐ nhưng bắt giải quyết tại Trọng tài SIAC (Singapore) với phí khởi kiện tối thiểu hàng chục nghìn USD.
- **Đề xuất Redline**:
  > *"Tranh chấp trước hết được giải quyết thông qua thương lượng, hòa giải. Nếu không thành công, tranh chấp sẽ do Tòa án nhân dân có thẩm quyền tại nơi Bên B đặt trụ sở chính giải quyết."*

---

## III. HƯỚNG DẪN ỨNG DỤNG CHO AI AGENT & WORKFLOW (N8N INTEGRATION)

1. **AI Node Context**: Chèn toàn bộ file `checklist-rui-ro.md` vào System Prompt / Context Window của AI Node trong n8n để AI đối chiếu từng `clause` bóc tách từ hợp đồng.
2. **Omission Check (Kiểm tra Bỏ sót)**: Đếm xem 10/10 tiêu chí Bắt buộc (`bat_buoc = true`) có xuất hiện trong hợp đồng hay không. Tiêu chí nào thiếu → Gán cờ `omission = true` (Severity: 🔴 HIGH).
3. **Severity Mapping**:
   - Khớp Bẫy 🔴 HIGH → Gợi ý Redline đàm phán ngay lập tức.
   - Khớp Bẫy 🟡 MED → Đề xuất làm rõ điều khoản.
