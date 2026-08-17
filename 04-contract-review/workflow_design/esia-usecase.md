# ESIA Use-case — Contract Review (B4)

> Use-case minh hoạ cho workflow_design package. Đây là CỐT LÕI để mini-game (G2) và Track B (G4b) móc vào.

## Use-case chính (GV demo + Track A)
**"Hợp đồng dịch vụ số hoá"** — công ty thuê đối tác cung cấp dịch vụ cloud. Hợp đồng 20 trang, 8 điều khoản. Đã GIẤU 1 omission: không có điều khoản chấm dứt đơn phương. Cài thêm 3 redline vi mô (trách nhiệm mập mờ, BMTT yếu, pháp luật áp dụng mơ hồ).

- File: `templates/contract-mau-hop-dong-dich-vu.docx` (synthetic, zero PII thật).
- Kỳ vọng Agent: omission chấm dứt bị flag (Macro) + 3 redline (Micro) + report có section HITL.

## Use-case holdout (TH4 nghiệm thu)
**`checkpoints/contract-holdout.docx`** — GV cầm, hợp đồng khác (vd thuê mặt bằng), cài omission khác + redline khác. HV chạy Agent TH4 trên file này để nghiệm thu.

## Use-case Track B (HV customize)
HV chọn 1 hợp đồng THẬT ở cơ quan mình (NDA / dịch vụ / lao động), **loại PII trước** (tên đối tác→Bên A/B, giá trị→làm tròn), rồi chạy workflow. Điểm khác vs GV: loại hợp đồng, nghiệp vụ, checklist trọng số (vd NDA nặng BMTT, lao động nặng chấm dứt).

> Nguyên tắc: workflow design package (4 lớp + checklist + HITL) KHÔNG đổi — chỉ đổi use-case/checklist trọng số. Đó là G4b (BR-06).

## 8 điều khoản "bắt buộc phải có" (JIT Macro — subset của checklist 12)
đối tượng · giá trị · thanh toán · nghĩa vụ · chấm dứt · BMTT · giải quyết tranh chấp · pháp luật áp dụng.

> (JIT dạy 8; Agent thật rà 12 tiêu chí trong `templates/checklist-rui-ro.json` TC01-TC12 — 8 là subset).
