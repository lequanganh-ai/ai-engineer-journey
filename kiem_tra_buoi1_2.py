# =================================================================
# BÀI KIỂM TRA TỔNG HỢP · BUỔI 1 + BUỔI 2   (khoảng 30 phút)
# =================================================================
# Quy tắc: KHÔNG mở ghi chú, KHÔNG xem bài cũ, KHÔNG dùng AI.
# Chấm điểm:   python cham_kiem_tra.py
# Đạt: 8/10 trở lên → vào buổi 3.
#
# Phần A (câu 1–5): xóa `pass`, viết code dùng `return`.
# Phần B (câu 6–8): ĐỌC code, ĐOÁN kết quả, điền vào biến (đoán trước, đừng chạy thử!)
# Phần C (câu 9–10): code có LỖI, hãy sửa cho đúng.
# =================================================================


# ---------------------------------------------------------------
# PHẦN A · VIẾT HÀM
# ---------------------------------------------------------------

def cau_1_lam_sach_email(email):
    """Người dùng gõ email lộn xộn. Xóa khoảng trắng hai đầu và đổi hết thành chữ thường.
    Ví dụ: cau_1_lam_sach_email("  AnH@Gmail.COM ")  →  "anh@gmail.com"
    """
    return email.strip().lower() #lower là đổi sang chữ thường


def cau_2_hen_gio(ten, gio=8):
    """Tham số gio có giá trị mặc định là 8.
    Ví dụ: cau_2_hen_gio("Lan")      →  "Chào Lan, hẹn gặp lúc 8 giờ."
           cau_2_hen_gio("Minh", 14) →  "Chào Minh, hẹn gặp lúc 14 giờ."
    """
    return f"Chào {ten}, hẹn gặp lúc {gio} giờ."




def cau_3_tong_ba_chuoi(a, b, c):
    """a, b, c là CHUỖI chứa số nguyên (giống kết quả của input()).
    Trả về TỔNG của chúng (kiểu số).
    Ví dụ: cau_3_tong_ba_chuoi("1", "2", "3")  →  6
    """
    return int(a)+int(b)+int(c)


def cau_4_tien_sau_giam(gia, so_luong, giam=0):
    """Tính tiền phải trả = gia × so_luong, rồi giảm đi `giam` phần trăm.
    Công thức: gia * so_luong * (100 - giam) / 100
    Trả về số đã làm tròn 2 chữ số thập phân.
    Ví dụ: cau_4_tien_sau_giam(50, 3)       →  150.0
           cau_4_tien_sau_giam(50, 3, 10)   →  135.0
           cau_4_tien_sau_giam(9.99, 2, 15) →  16.98
    """
    return round(gia*so_luong* (100-giam)/100, 2)


def cau_5_the_diem(ten, diem):
    """Làm sạch tên (bỏ khoảng trắng thừa, viết hoa chữ đầu mỗi từ),
    hiển thị điểm với ĐÚNG 1 chữ số thập phân.
    Ví dụ: cau_5_the_diem("  lê quang anh ", 8.5)  →  "Lê Quang Anh: 8.5 điểm"
           cau_5_the_diem("nguyễn an", 9)          →  "Nguyễn An: 9.0 điểm"
    """
    return f"{ten.strip().title()}: {diem:.1f} điểm"


# ---------------------------------------------------------------
# PHẦN B · ĐỌC CODE, ĐOÁN KẾT QUẢ (ghi đáp án dạng chuỗi, giữ dấu nháy)
# ---------------------------------------------------------------

# CÂU 6: đoạn code sau in ra gì?
#
#     def f(x):
#         return x * 2
#
#     print(f(3) + f(f(1)))
#
cau_6 = "10"


# CÂU 7: đoạn code sau in ra gì?
#
#     def g(ten="an"):
#         return ten.upper()
#
#     print(g() + g("binh"))
#
cau_7 = "ANBINH"


# CÂU 8: sau khi chạy đoạn code sau, biến x có giá trị gì?
#
#     def h(n):
#         print(n + 1)
#
#     x = h(4)
#
cau_8 = "None"


# ---------------------------------------------------------------
# PHẦN C · SỬA LỖI (sửa trực tiếp vào code bên dưới)
# ---------------------------------------------------------------

# CÂU 9: hàm này chạy không báo lỗi nhưng kết quả luôn sai.
# Đúng phải là: cau_9_tinh_tuoi(2000) → 26
def cau_9_tinh_tuoi(nam_sinh):
    tuoi = 2026 -nam_sinh
    return tuoi


# CÂU 10: gọi cau_10_gia_sau_thue(100) bị lỗi NameError.
# Đúng phải là: cau_10_gia_sau_thue(100) → 110.0
# (Được phép sửa cả hai hàm, nhưng giữ nguyên tên cau_10_gia_sau_thue.)
def cau_10_gia_sau_thue(gia):
    thue = 10
    return tinh_thue(gia,thue)


def tinh_thue(gia,thue):
    return gia + gia * thue / 100
