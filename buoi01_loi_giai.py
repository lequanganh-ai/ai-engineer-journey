# BUỔI 1 · LỜI GIẢI THAM KHẢO — chỉ xem SAU KHI đã tự làm.
# Chấm thử lời giải:  python buoi01_cham_diem.py buoi01_loi_giai.py

# ===== BÀI 1 =====
print("Xin chào, thế giới!")

# ===== BÀI 2 =====
print("Tôi đang học Python.")
print("Mục tiêu: trở thành AI Engineer.")
print("Bắt đầu: 06/10/2026")

# ===== BÀI 3 =====
ngon_ngu = "Python"
khoa_hoc = "CS50P"
print("Tôi học", ngon_ngu, "qua khóa", khoa_hoc + ".")
# Cách khác: print(f"Tôi học {ngon_ngu} qua khóa {khoa_hoc}.")

# ===== BÀI 4 =====
ten = input("Tên bạn là gì? ")
print("Xin chào, " + ten + "!")

# ===== BÀI 5 =====
ten = input("Tên: ")
que = input("Quê: ")
print(ten, "đến từ", que + ".")

# ===== BÀI 6 =====
print("2026", "10", "06", sep="-")

# ===== BÀI 7 =====
mon_1 = "phở"
mon_2 = "bún chả"
mon_1, mon_2 = mon_2, mon_1   # đổi chỗ trong một dòng
print(mon_1)
print(mon_2)

# ===== BÀI 8 =====
mon = input("Món yêu thích: ")
print(f"Món yêu thích của tôi là {mon}.")

# ===== BÀI 9 =====
ho_ten = input("Họ tên: ").strip().title()
print(f"Xin chào, {ho_ten}")

# ===== BÀI 10 · THỬ THÁCH =====
ten = input("Tên: ")
print("=" * 20)
print(f"Học viên: {ten}")
print("=" * 20)
