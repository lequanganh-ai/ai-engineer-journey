# Tuần 2 · Buổi 4 – 02/11/2026

## Đã làm
- Kiểm tra buổi 3: **8/10** (câu 6 sai thứ tự điều kiện, câu 7 thiếu `.strip()`) → sửa lại 10/10
- Problem Set 1 bài 4 `interpreter.py` và bài 5 `meal.py` → **PS1 hoàn thành 5/5**
- Bài luyện `ca_lam.py` (tự viết, không nhìn mẫu): **13/13**

## Học được
- `x, y, z = s.split(" ")`: số phần tách ra phải **bằng** số biến, nếu không sẽ báo `ValueError: not enough values to unpack (expected 3, got 1)`
- Ví dụ đề là `1 + 1` thì phải nhập **đúng y**, có dấu cách
- `match` cho giá trị cụ thể (`+ - * /`); `if/elif` cho **khoảng** (`7 <= gio <= 8`)
- Gán `ket_qua` trong mỗi `case`, rồi **in một lần** sau `match` với `f"{ket_qua:.1f}"` → `2` thành `2.0`
- `case _` không gán biến thì phải `exit()`, nếu không dòng `print` sau sẽ báo `NameError`
- `print(repr(y))` để **dò lỗi**: hiện cả dấu nháy, lộ dấu cách thừa. Xong thì xóa
- Hàm nhỏ `convert(time)`: `"7:30"` → `split(":")` → `int` → `gio + phut / 60` → `return 7.5`
- `main` hỏi, gọi `convert`, `if/elif`, `print`. `convert` **chỉ return**
- Trong code, `7:00` không phải số → viết `7`, `8`, `11.5` (hoặc `11 + 30 / 60`)
- Đọc `TypeError: '<=' not supported between 'int' and 'list'` → hàm trả về **list** thay vì số

## Đánh giá thật
**Tiến bộ có bằng chứng:**
- Bài 4 thử đủ 5 nhánh, có giá trị tự nghĩ (`2 - 3`, `20 * 10`)
- Meal: logic đúng lần đầu, tự thử mốc sát biên `8:01`
- `ca_lam`: `main` đúng hoàn toàn ngay lần đầu; lần đầu tiên **gửi code đang thử kèm lỗi** thay vì xin mẫu

**Còn lặp lại:**
- Câu hỏi input **gõ tay** → sửa 3 lần mới đúng (`what time is it?` → `What time is it ?` → đúng)
- Xin code mẫu khi chưa gửi bản thử (2 lần)
- Sửa thiếu khi được nhắc nhiều điểm (`bieuer`, mẩu rác trong kế hoạch)
- `Đã thử thêm` không đúng màn hình (`luch time`, `Ngoài giờ làm` viết hoa trong khi in `ngoài giờ làm`)
- Quên Ctrl + S (chạy ra kết quả cũ ở interpreter)
- Bỏ qua phần kế hoạch ở `ca_lam.py`

## Buổi sau (buổi 5)
- Kiểm tra buổi 4 trước khi vào
- Mini project "Báo giá NEXORA" bản 1 + ôn tổng kết tuần 2
- Mục tiêu đo được: chuỗi in ra / input **copy-dán** 100%; không xin mẫu trước khi gửi bản thử
