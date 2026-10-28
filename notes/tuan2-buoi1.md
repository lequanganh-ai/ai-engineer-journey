# Tuần 2 · Buổi 1 – 28/10/2026

## Đã làm
- Xem CS50P Lecture 1 đến **34:44** (dừng trước chương Modulo)
- Tự kiểm tra 5 câu: 3/5 đúng hẳn (sai: `5 == 5.0` là True; vì sao `or "Chủ nhật"` luôn đúng)
- Bài tập `t2b1_bai_tap.py`: lần đầu **5/11** (soát đề ghi 11/11) → sửa theo hướng dẫn → 11/11
- Luyện lại `t2b1_luyen_lai.py`: **8/8 ngay lần đầu, soát đề 8/8**
- Gộp thư mục trùng: giờ chỉ còn `tuan2/` ở thư mục gốc

## Học được
- So sánh: `== != < > <= >=` → ra `True`/`False` (kiểu bool). `=` là gán, `==` là so sánh
- `5 == 5.0` → True (cùng giá trị số); `"5" == 5` → False
- `if / elif / else`: chỉ **một** khối chạy — khối đúng đầu tiên
- `and` cần cả hai đúng; `or` cần ít nhất một đúng; `and` tính trước `or`
- So sánh nối liền: `6 <= tuoi <= 17` — **số nhỏ bên trái**
- Thứ tự `elif` với `>=`: điều kiện **chặt nhất đứng đầu** (>= 95 → >= 80 → >= 50)
- `if thu == "A" or "B":` luôn đúng vì chuỗi không rỗng được coi là đúng → phải viết `thu == "A" or thu == "B"`
- Chuẩn hóa chuỗi (`.strip().lower()`) **trước** khi so sánh, rồi so với chuỗi **viết thường**
- Chuỗi rỗng `""` = sai, chuỗi không rỗng = đúng
- Đọc dòng đường dẫn trên vùng code để biết đang sửa file nào

## Lỗi (đánh giá thật)
- Ghi `# Soát đề: OK` khi chưa thử: 6 bài sai vẫn ghi OK (lần thứ 3 trong 2 ngày)
- Khoảng viết ngược `17 <= tuoi <= 6`; thứ tự `elif` sai; đảo True/False
- Gần đúng 1 ký tự: `Xuát`, `300000` vs `30000`, `may_khau_on` — và khi sửa còn sửa luôn số đang đúng
- Tạo thư mục bằng chuột nhưng gõ cả `mkdir tuan2` làm tên; `No such file` lần thứ 6

## Tiến bộ
- Bài luyện lại 8/8 ngay lần đầu, gồm đúng 4 dạng lỗi vừa mắc

## Buổi sau (buổi 2)
- Xem Lecture 1 từ **34:44**: `%`, chẵn/lẻ, hàm trả về bool kiểu Pythonic, `match`
