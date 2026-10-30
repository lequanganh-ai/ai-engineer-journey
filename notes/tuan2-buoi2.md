# Tuần 2 · Buổi 2 – 30/10/2026

## Đã làm
- Kiểm tra buổi 1: **9/10 ngay lần đầu** (sai câu 4 `dang_nhap`), soát đề ghi 10/10
- Xem CS50P Lecture 1 từ 34:44 đến hết: `%`, chẵn/lẻ, hàm trả về bool, `match`
- Tự kiểm tra: 3/5 (câu 3 nửa đúng; câu 5 chọn match thay vì if/elif cho khoảng)
- Bài tập `t2b2_bai_tap.py`: lần đầu **6/11** → sửa → 11/11
- Luyện lại 1 `t2b2_luyen_lai.py`: **3/7 thật** (lặp lại đúng các lỗi vừa ghi)
- Luyện lại 2 `t2b2_luyen_lai_2.py`: **5/6 lần đầu** (lỗi gõ thiếu `!= 0`) → 6/6, soát đề 6/6, đã thử thêm 6/6

## Học được
- `a % b` = số dư; `a % b == 0` = chia hết; chẵn `n % 2 == 0`
- Hàm bool viết gọn: `return n % 2 == 0` (không cần if)
- `if la_chan:` — không viết `== True`; tham số bool dùng thẳng
- `match` + `case giá_trị:` + `|` (hoặc) + `case _:` (còn lại, đặt CUỐI)
- `case` phải cùng kiểu với biến: số → `case 2:`, chuỗi → `case "2":`
- Giá trị CỤ THỂ → match; KHOẢNG → if/elif
- Trả chuỗi: chữ cố định → `"..."`; giá trị tính ra → `str(...)`; ghép → f-string
- `and` / `or` có thể trả về chính giá trị (24) chứ không phải True → mỗi vế phải là so sánh đầy đủ
- Hàm bool trả lời đúng/sai → `main` dùng `if` để CHỌN câu in, in con số chứ không in True/False

## Lỗi (đánh giá thật)
- **Chép ví dụ vào code: 4 lần** (`return "7"`, `return "1"`, `case "s"/"l"`, ghi "đã thử" bằng chính ví dụ)
- In True/False thay vì câu (2 lần), so bool với `"True"`
- Soát đề OK cho bài sai: lần thứ 5; viết `Ok` thường
- Sai thư mục `No such file`: lần 7–8 (lần cuối tự sửa được bằng `cd tuan2` ✅)

## Tiến bộ
- Kiểm tra buổi 1 đạt 9/10 lần đầu: sửa hết lỗi khoảng ngược / thứ tự elif / or viết tắt
- Năm nhuận (and + or + %) đúng ngay; match với | đúng ngay
- Luyện lại 2: 5/6 lần đầu, hết lỗi chép ví dụ khi máy chấm thử nhiều giá trị lạ

## Buổi sau
- Làm thêm 1 bài ôn (chép ví dụ · bool · match) → rồi buổi 3: kiểm tra buổi 2 + Problem Set 1 bài 1–3
