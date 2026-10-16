# =================================================================
# BUỔI 1 · BÀI TẬP: print(), input(), BIẾN, f-string
# =================================================================
# Cách làm:
#   1. Viết code của bạn ngay bên dưới mỗi đề bài (dưới dòng "# Viết code ở đây").
#   2. KHÔNG xóa các dòng "# ===== BÀI ..." — máy chấm dựa vào chúng để tách bài.
#   3. Chấm điểm: mở terminal trong thư mục này và chạy
#          python buoi01_cham_diem.py
#      Máy sẽ tự "gõ" dữ liệu cho input() và kiểm tra kết quả bạn in ra.
#   4. Muốn tự thử một bài: chạy  python buoi01_bai_tap.py  (máy sẽ hỏi lần lượt các input).
#
# Mẹo: in ra phải GIỐNG CHÍNH XÁC đề bài, kể cả dấu câu và chữ hoa.
# =================================================================


# ===== BÀI 1 =====
# In ra đúng dòng chữ:
#   Xin chào, thế giới!
# Viết code ở đây:
print("Xin chào, thế giới!")



# ===== BÀI 2 =====
# Dùng 3 lệnh print để in ra đúng 3 dòng:
#   Tôi đang học Python.
#   Mục tiêu: trở thành AI Engineer.
#   Bắt đầu: 06/10/2026
# Viết code ở đây:
print("Tôi đang học Python.")
print("Mục tiêu: trở thành AI Engineer.")
print("Bắt đầu: 06/10/2026")



# ===== BÀI 3 =====
# Tạo biến ngon_ngu có giá trị "Python" và biến khoa_hoc có giá trị "CS50P".
# Sau đó dùng 2 biến này (không gõ trực tiếp chữ) để in ra:
#   Tôi học Python qua khóa CS50P.
# Gợi ý: print("Tôi học", ngon_ngu, ...) — print tự thêm dấu cách giữa các phần.
#        Chú ý dấu chấm cuối câu dính liền chữ CS50P.
# Viết code ở đây:
ngon_ngu = "Python"
khoa_hoc = "CS50P"
print("Tôi học", ngon_ngu,"qua khóa", khoa_hoc + ".")



# ===== BÀI 4 =====
# Hỏi tên người dùng bằng input("Tên bạn là gì? ") rồi in ra:
#   Xin chào, <tên>!
# Ví dụ người dùng gõ Lan  →  in ra  Xin chào, Lan!
# Viết code ở đây:
ten = input("Tên bạn là gì? ")
print("Xin chào, "+ ten + "!")


# ===== BÀI 5 =====
# Hỏi 2 lần: tên (input("Tên: ")) và quê (input("Quê: ")), rồi in ra:
#   <tên> đến từ <quê>.
# Ví dụ: Lan, Bắc Ninh  →  Lan đến từ Bắc Ninh.
# Viết code ở đây:
ten = input("Tên: ")
que = input("Quê: ")
print(ten,"đến từ",que + ".")



# ===== BÀI 6 =====
# Dùng MỘT lệnh print với 3 giá trị "2026", "10", "06" và tham số sep
# để in ra:
#   2026-10-06
# Gợi ý: print("a", "b", sep="?")
# Viết code ở đây:
print("2026","10","06", sep="-")



# ===== BÀI 7 =====
# Tạo biến mon_1 = "phở" và mon_2 = "bún chả".
# Hãy ĐỔI CHỖ giá trị của 2 biến (sau khi đổi, mon_1 là "bún chả", mon_2 là "phở"),
# rồi in mon_1 trên dòng đầu, mon_2 trên dòng sau:
#   bún chả
#   phở
# Gợi ý: cần một biến tạm, hoặc tìm cách viết  a, b = b, a
# Viết code ở đây:
mon_1 = "phở"
mon_2 = "bún chả"
mon_1,mon_2=mon_2,mon_1
print(mon_1)
print(mon_2)

# ===== BÀI 8 =====
# Hỏi món ăn yêu thích bằng input("Món yêu thích: ") rồi dùng f-string để in:
#   Món yêu thích của tôi là <món>.
# Gợi ý: print(f"...{mon}...")
# Viết code ở đây:
mon = input("Món ăn yêu thích: ")
print(f"Món yêu thích của tôi là {mon}.")


# ===== BÀI 9 =====
# Người dùng hay gõ thừa dấu cách và viết thường, ví dụ:  "   lê quang anh  "
# Hỏi tên bằng input("Họ tên: "), làm sạch tên bằng .strip() và .title(), rồi in:
#   Xin chào, Lê Quang Anh
# (không có dấu chấm than ở cuối)
# Viết code ở đây:
name = input("Họ tên: ").strip().title()
print(f"Xin chào, {name}")


# ===== BÀI 10 · THỬ THÁCH =====
# Hỏi tên bằng input("Tên: ") và in ra một "thẻ học viên" đúng 3 dòng:
#   ====================
#   Học viên: <tên>
#   ====================
# Dòng trên và dưới là 20 dấu "=". Thử viết gọn bằng  "=" * 20
# Viết code ở đây:
ten = input("Tên: ")
print("=" * 20)
print(f"Học viên: {ten}")
print("=" * 20)


