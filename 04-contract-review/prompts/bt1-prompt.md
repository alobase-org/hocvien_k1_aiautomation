# Prompt Thực hành 1 — Vận hành n8n trong Docker & Chạy Unit Test local

> Thực hành 1/5 — Cài đặt, đóng gói n8n local bằng Docker và chạy kiểm thử tự động.
> Input: Dockerfile, docker-compose.yml, unit test scripts. Output: Báo cáo Unit Test PASSED.

## 1. Lệnh khởi chạy Container n8n với Docker Compose

```bash
# Di chuyển tới thư mục test
cd test

# Khởi chạy container n8n tester
docker compose up --build
```

## 2. Lệnh thực thi trực tiếp bộ Unit Test Runner bằng Python

```bash
# Chạy bộ test suite kiểm định 7 test cases
python3 test/run_tests.py
```

## 3. Lệnh chạy chi tiết bằng pytest (nếu có)

```bash
pytest test/test_n8n_workflows.py -v
```
