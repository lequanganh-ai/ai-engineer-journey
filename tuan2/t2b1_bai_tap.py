# =================================================================
# TUẦN 2 · BUỔI 1 · BÀI TẬP ĐIỀU KIỆN (if / elif / else / and / or)
# =================================================================
# Làm SAU KHI xem video phần 1 + đọc ghi chú.
# Đây là BÀI TẬP (không phải kiểm tra): được mở ghi chú.
# Nhưng KHÔNG dùng AI gợi ý code, KHÔNG xem lời giải trên mạng.
#
# Mỗi bài:
#   1. Đọc đề → 2. viết code → 3. TỰ THỬ đủ ví dụ (thêm print tạm ở cuối file, thử xong xóa)
#   4. Đúng hết mới đổi dòng soát đề thành  # Soát đề: OK   (copy dòng này)
#
# Chấm:  python cham_t2b1.py      (chạy trong thư mục tuan2)
# =================================================================


# BÀI 1
# Viết hàm  so_lon_hon(a, b)  trả về số LỚN HƠN trong 2 số (bằng nhau thì trả về số đó).
# KHÔNG dùng hàm max() — dùng if / else.
#   so_lon_hon(3, 5)  → 5
#   so_lon_hon(7, 2)  → 7
#   so_lon_hon(4, 4)  → 4
# Soát đề: OK
# Viết code dưới đây:
def so_lon_hon(a, b):
    if a > b:
        return a
    else:
        return b


# BÀI 2
# Viết hàm  so_sanh(a, b)  trả về MỘT trong ba chuỗi: "nhỏ hơn", "lớn hơn", "bằng nhau"
# (so sánh a với b). Dùng if / elif / else.
#   so_sanh(1, 2)  → "nhỏ hơn"
#   so_sanh(5, 3)  → "lớn hơn"
#   so_sanh(4, 4)  → "bằng nhau"
# Soát đề: OK
# Viết code dưới đây:
def so_sanh(a ,b):
    if a < b:
        return "nhỏ hơn"
    elif a > b:
        return "lớn hơn"
    else:
        return "bằng nhau"



# BÀI 3
# Viết hàm  ket_qua_thi(diem)
# Điểm từ 5 trở lên → "Đậu", dưới 5 → "Rớt".
#   ket_qua_thi(5)    → "Đậu"
#   ket_qua_thi(4.9)  → "Rớt"
# Soát đề: OK
# Viết code dưới đây:
def ket_qua_thi(diem):
    if diem >= 5:
        return "Đậu"
    else:
        return "Rớt"



# BÀI 4
# Viết hàm  xep_loai(diem)   (diem từ 0 đến 10)
#   từ 9 trở lên        → "Xuất sắc"
#   từ 8 đến dưới 9     → "Giỏi"
#   từ 6.5 đến dưới 8   → "Khá"
#   từ 5 đến dưới 6.5   → "Trung bình"
#   dưới 5              → "Yếu"
# CHÚ Ý thứ tự elif và các điểm ranh giới (8, 6.5, 5).
#   xep_loai(9.5) → "Xuất sắc"    xep_loai(8)   → "Giỏi"
#   xep_loai(6.5) → "Khá"         xep_loai(5)   → "Trung bình"
#   xep_loai(4)   → "Yếu"
# Soát đề: OK
# Viết code dưới đây:
def xep_loai(diem):
    if diem >= 9:
        return "Xuất sắc"
    elif 8<= diem <9:
        return "Giỏi"
    elif 6.5 <= diem < 8:
        return "Khá"
    elif 5 <= diem <6.5:
        return "Trung bình"
    else:
        return "Yếu"



# BÀI 5
# Viết hàm  trong_khoang(x)  trả về True nếu x nằm từ 1 đến 10 (tính cả 1 và 10), ngược lại False.
# Thử viết bằng so sánh nối liền:  1 <= x <= 10
#   trong_khoang(1)   → True
#   trong_khoang(10)  → True
#   trong_khoang(0)   → False
#   trong_khoang(11)  → False
# Soát đề: OK
# Viết code dưới đây:
def trong_khoang(x):
    if 1<= x <=10:
        return True
    else:
        return False



# BÀI 6
# Viết hàm  cuoi_tuan(thu)  trả về True nếu thu là "Thứ Bảy" HOẶC "Chủ nhật", ngược lại False.
# Trước khi so sánh: xóa khoảng trắng 2 đầu và viết thường toàn bộ (để "  CHỦ NHẬT " cũng đúng).
#   cuoi_tuan("Thứ Bảy")       → True
#   cuoi_tuan("  CHỦ NHẬT ")   → True
#   cuoi_tuan("Thứ Hai")       → False
# Soát đề: OK
# Viết code dưới đây:
def cuoi_tuan(thu):
    thu = thu.strip().lower()
    if thu == "thứ bảy" or thu == "chủ nhật":
        return True
    else:
        return False



# BÀI 7
# Viết hàm  gia_ve(tuoi)  trả về SỐ:
#   dưới 6 tuổi       → 0
#   từ 6 đến 17       → 50000
#   từ 18 đến 59      → 90000
#   từ 60 trở lên     → 45000
#   gia_ve(5) → 0      gia_ve(6) → 50000     gia_ve(17) → 50000
#   gia_ve(18) → 90000 gia_ve(60) → 45000
# Soát đề: OK
# Viết code dưới đây:
def gia_ve(tuoi):
    if tuoi < 6:
        return 0
    elif 6 <= tuoi <= 17:
        return 50000
    elif 18 <= tuoi <= 59:
        return 90000
    else:
        return 45000



# BÀI 8
# Viết hàm  phi_ship(tong_tien)  trả về SỐ:
#   tổng tiền từ 300000 trở lên → 0 (miễn phí), dưới 300000 → 30000
#   phi_ship(300000) → 0
#   phi_ship(299999) → 30000
# Soát đề: OK
# Viết code dưới đây:
def phi_ship(tong_tien):
    if tong_tien >= 300000:
        return 0
    else:
        return 30000



# BÀI 9
# Viết hàm  du_dieu_kien(ten, tuoi)  trả về True khi CẢ HAI điều kiện đúng:
#   - tên không rỗng sau khi xóa khoảng trắng 2 đầu
#   - tuổi từ 18 trở lên
#   du_dieu_kien("An", 18)    → True
#   du_dieu_kien("   ", 20)   → False
#   du_dieu_kien("Bình", 17)  → False
# Soát đề: OK
# Viết code dưới đây:
def du_dieu_kien(ten, tuoi):
    if ten.strip() != "" and tuoi >= 18:
        return True
    else:
        return False
    



# BÀI 10 · SỬA LỖI
# Code dưới SAI. Sửa để:
#   c10_muc_do(8) → "Tốt"     c10_muc_do(6) → "Đạt"     c10_muc_do(3) → "Chưa đạt"
# Gợi ý: chạy thử c10_muc_do(8) và tự hỏi Python dừng ở nhánh nào.
# Soát đề: OK
def c10_muc_do(diem):
    if diem >= 8:
        return "Tốt"
    elif diem >= 5:
        return "Đạt"
    else:
        return "Chưa đạt"


# BÀI 11 · CHƯƠNG TRÌNH HOÀN CHỈNH
# Viết hàm  main():
#   - Hỏi bằng input:  "Điểm: "   (điểm có thể lẻ, ví dụ 8.5 → dùng kiểu số nào?)
#   - GỌI xep_loai (bài 4)
#   - In ra ĐÚNG 1 dòng, ví dụ nhập "8.5":
#         Xếp loại: Giỏi
# Comment kế hoạch (① HỎI / ② XỬ LÝ / ③ IN RA) bên trong main.
# Cuối file gọi main() đúng chuẩn.
# Soát đề: OK
# Viết code dưới đây:
def main():
    diem = float(input("Điểm: "))
    da_xep_loai = xep_loai(diem)
    print(f"Xếp loại: {da_xep_loai}")
if __name__ == "__main__":
    main()

