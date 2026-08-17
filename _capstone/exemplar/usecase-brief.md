# Usecase Brief — Xử lý đơn xin nghỉ phép (exemplar GV)

> Exemplar minh họa cho buổi 8 — GV dùng demo 15'. Mức tối thiểu đủ 4 deliverable.

## [BẮT BUỘC] Bài toán
Nhóm 25 người, nhân viên xin nghỉ phép qua Zalo/email cho trưởng nhóm. Trưởng nhóm tự ghi vào file chung, check lại chính sách (loại phép, số ngày còn, deadline báo trước), rồi trả lời duyệt/từ chối. Mỗi tuần ~8 đơn, mỗi đơn 10–15 phút, hay quên ghi sổ và trả lời trễ.

## [BẮT BUỘC] Người dùng
Người nộp: nhân viên nhóm. Người xử lý: trưởng nhóm (người duyệt cuối). Người nhận output: trưởng nhóm + nhân viên (kết quả duyệt).

## [BẮT BUỘC] Input hàng ngày
Tin nhắn/email đơn nghỉ phép dạng tự nhiên: ai, loại phép (annual/sick/không lương), từ ngày–đến ngày, lý do. Tần suất ~8 đơn/tuần. Ví dụ: "Chào sếp, em xin nghỉ phép annual 2 ngày 21-22/08, việc đang làm em đã bàn giao cho Lan."

## [BẮT BUỘC] Output mong muốn
File `leave-requests/approved|rejected-YYYY-MM-DD.md`: kết quả duyệt + lý do + điều kiện (ai cover việc). Kèm `leave-log.csv` 1 dòng/đơn (ngày, người, loại, số ngày, kết quả).

## [BẮT BUỘC] Quy trình xử lý
1. (Cứng) Trích thông tin đơn: tên, loại phép, ngày, lý do → JSON.
2. (Cứng) Đối chiếu chính sách: annual ≥3 ngày báo trước 3 ngày; sick có thể báo sáng hôm đó; không lương cần duyệt riêng.
3. (AI phán đoán) Kiểm tra lời bàn giao có nêu người cover hay không; thiếu → flag.
4. (Người duyệt) Trưởng nhóm duyệt cuối (HITL) — tool chỉ đề xuất duyệt/từ chối.
5. (Cứng) Ghi log + trả lời nhân viên.

## [BẮT BUỘC] Tiêu chí thành công (đo được)
- 100% đơn được trả lời trong 4 giờ làm việc, có entry `leave-log.csv`
- Đơn đủ điều kiện chính sách: đề xuất "duyệt" đúng 10/10 mẫu test
- Đơn vi phạm (thiếu báo trước): đề xuất "từ chối" kèm điều khoản vi phạm, 10/10 mẫu

## Ràng buộc & công cụ sẵn có
Không dùng tên/dữ liệu thật — dùng dữ liệu mô phỏng theo mẫu B6 fallback-inputs. Có n8n local, AI Studio, Claude Code. Ngân sách 0 đồng.
