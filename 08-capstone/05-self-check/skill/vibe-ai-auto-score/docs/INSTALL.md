# Cài đặt vibe-ai-auto-score

## Yêu cầu
- Claude Code CLI (phiên bản mới nhất) hoặc bất kỳ client tương thích SKILL.md
- Python 3.8+ (cho scripts validate/aggregate/dashboard)
- Python package: `python-docx` (cho render docx qua vibe-humanizer)
- Skill phụ thuộc (tuỳ chọn): `vibe-humanizer` (render docx), `deep-research` (tiêu chí khó cần fact)

## Cài đặt (Claude Code)

### Option 1: Personal (áp dụng mọi project)
```bash
unzip vibe-ai-auto-score.zip -d ~/.claude/skills/
```

### Option 2: Project-only (chỉ project hiện tại)
```bash
unzip vibe-ai-auto-score.zip -d .claude/skills/
```

## Cài hooks (tuỳ chọn — bảo vệ template/archive khỏi ghi nhầm)
```bash
bash ~/.claude/skills/vibe-ai-auto-score/script/install_hooks.sh
```

## Xác nhận cài đặt
Khởi động lại Claude Code, rồi gõ:
```
/vibe-ai-auto-score
```

## Gỡ cài đặt
```bash
rm -rf ~/.claude/skills/vibe-ai-auto-score
```
