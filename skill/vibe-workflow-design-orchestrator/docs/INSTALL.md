# Cài đặt — vibe-workflow-design-orchestrator

## Skill này là gì

Sinh **Workflow Design Package hoàn chỉnh** cho một use-case doanh nghiệp: đi từ
"tôi muốn tự động hoá quy trình X" tới một gói tài liệu sẵn sàng trình lãnh đạo —
as-is→ESIA to-be, hardening production, sơ đồ Mermaid, ảnh infographic, deck tham mưu 30 ngày.

Triết lý: **thiết kế cho đáng tin cậy trước — tự động hoá sau.**

## Yêu cầu

- Claude Code CLI (phiên bản mới nhất), hoặc bất kỳ client tương thích SKILL.md (Antigravity, …).
- Python 3.9+ (chạy `script/validator.py`, `anonymizer.py`, `review_queue.py`).
- Không cần API key hay config gì thêm — skill local-first.

## Cài đặt (Claude Code)

### Option 1: Personal — áp dụng mọi project

```bash
unzip vibe-workflow-design-orchestrator.zip -d ~/.claude/skills/
```

### Option 2: Project-only — chỉ project hiện tại

```bash
unzip vibe-workflow-design-orchestrator.zip -d .claude/skills/
```

> Nếu nhận folder rời (không phải ZIP): copy nguyên folder `vibe-workflow-design-orchestrator/`
> vào `~/.claude/skills/` (hoặc `.claude/skills/`).

## Cài hooks (tuỳ chọn, bảo vệ folder)

Hooks ngăn ghi nhầm vào `output/templates/` và các vùng cố định:

```bash
cd ~/.claude/skills/vibe-workflow-design-orchestrator
bash script/install_hooks.sh
```

## Xác nhận cài đặt

Khởi động lại Claude Code, rồi gõ:

```
/vibe-workflow-design-orchestrator
```

Skill sẽ tự kích hoạt khi bạn đề cập "thiết kế workflow", "tái thiết kế quy trình",
"as-is to-be", "ESIA", "hardening workflow"…

## Gỡ cài đặt

```bash
rm -rf ~/.claude/skills/vibe-workflow-design-orchestrator
```
