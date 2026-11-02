
---

## NHÓM H+ · BUỔI 4 TUẦN 2 (02/11/2026)

### H10. Số biến ≠ số phần sau split
- **Bằng chứng:** interpreter nhập `1` → `ValueError: not enough values to unpack (expected 3, got 1)`; `ca_lam` dùng `split(".")` cho `"6:00"` → list 1 phần
- **Sửa:** nhìn chuỗi mẫu, ký tự **nằm giữa** các phần mới là dấu cắt; nhập thử **đúng y** ví dụ đề

### H11. Hàm trả về sai kiểu
- **Bằng chứng:** `convert` trả về list → `TypeError: '<=' not supported between 'int' and 'list'`
- **Sửa:** đề ghi "trả về số" → `return` phải là phép tính trên số, sau `int()`

### H12. Câu hỏi input gõ tay (lần 3 cùng 1 dòng)
- **Bằng chứng:** `"what time is it?"` → `"What time is it ?"` → mới đúng `"What time is it? "`
- **Sửa:** bôi đen trong đề → Ctrl + C → dán. Dấu cách **sau** `?`

### H13. "Đã thử thêm" không copy từ màn hình
- **Bằng chứng:** ghi `luch time`, `Ngoài giờ làm` — màn hình in `lunch time`, `ngoài giờ làm`
- **Sửa:** copy từ terminal, không gõ lại
