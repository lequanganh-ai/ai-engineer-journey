# =================================================================
# BÀI KIỂM TRA LẦN 2 · BUỔI 1 + BUỔI 2   (khoảng 30 phút)
# =================================================================
# Quy tắc: KHÔNG mở ghi chú, KHÔNG xem bài cũ, KHÔNG dùng AI.
# Chấm điểm:   python cham_kiem_tra.py
# Đạt: 8/10 trở lên → vào buổi 3.
#
# 3 điều cần nhớ khi làm:
#   1. Phép tính viết NGOÀI dấu nháy:  return a + b   (không phải "a + b")
#   2. COPY câu ví dụ trong đề, rồi thay phần thay đổi bằng {biến}
#   3. Python phân biệt chữ HOA / thường:  None ≠ NONE
# =================================================================


# ---------------------------------------------------------------
# PHẦN A · VIẾT HÀM
# ---------------------------------------------------------------

def cau_1_chuan_hoa_ma(ma):
    """Mã sản phẩm: xóa khoảng trắng hai đầu và đổi hết thành CHỮ HOA.
    Ví dụ: cau_1_chuan_hoa_ma("  ab12x ")  →  "AB12X"
    """
    return ma.strip().upper()


def cau_2_loi_moi(ten, ngay="thứ Bảy"):
    """Tham số ngay có giá trị mặc định là "thứ Bảy".
    Ví dụ: cau_2_loi_moi("Lan")             →  "Mời Lan dự tiệc vào thứ Bảy."
           cau_2_loi_moi("Minh", "Chủ nhật") →  "Mời Minh dự tiệc vào Chủ nhật."
    """
    return f"Mời {ten} dự tiệc vào {ngay}."


def cau_3_tong_roi_nhan_doi(a, b):
    """a, b là CHUỖI chứa số nguyên. Cộng chúng lại rồi nhân 2.
    Ví dụ: cau_3_tong_roi_nhan_doi("3", "4")  →  14
    """
    return (int(a) + int(b)) * 2


def cau_4_tien_lai(goc, lai_suat=5):
    """Tiền lãi = goc × lai_suat / 100, làm tròn 2 chữ số thập phân.
    Ví dụ: cau_4_tien_lai(1000)      →  50.0
           cau_4_tien_lai(2000, 7.5) →  150.0
           cau_4_tien_lai(999, 3)    →  29.97
    """
    return round(goc * lai_suat / 100, 2)


def cau_5_bang_gia(ten_mon, gia):
    """Làm sạch tên món (bỏ khoảng trắng thừa, viết hoa chữ đầu mỗi từ),
    giá hiển thị ĐÚNG 2 chữ số thập phân.
    Ví dụ: cau_5_bang_gia("  pho bo ", 3.5)  →  "Pho Bo - 3.50 USD"
           cau_5_bang_gia("banh mi", 2)      →  "Banh Mi - 2.00 USD"
    """
    return f"{ten_mon.strip().title()} - {gia:.2f} USD"


# ---------------------------------------------------------------
# PHẦN B · ĐỌC CODE, ĐOÁN KẾT QUẢ (ghi đáp án dạng chuỗi, giữ dấu nháy)
# ---------------------------------------------------------------

# CÂU 6: in ra gì?
#
#     def f(x):
#         return x + 10
#
#     print(f(f(5)) - f(0))
#
cau_6 = "15"


# CÂU 7: in ra gì?
#
#     def chao(ten="ban"):
#         return "Hi " + ten
#
#     print(chao("An") + "!")
#
cau_7 = "Hi An!"


# CÂU 8: in ra gì?
#
#     def m(n):
#         return n + 1
#         return n + 2
#
#     print(m(5))
#
cau_8 = "6"


# ---------------------------------------------------------------
# PHẦN C · SỬA LỖI (sửa trực tiếp vào code bên dưới)
# ---------------------------------------------------------------

# CÂU 9: chạy không báo lỗi nhưng kết quả sai.
# Đúng phải là: cau_9_gio_sang_phut(2) → 120
def cau_9_gio_sang_phut(gio):
    ket_qua = gio * 60
    return ket_qua


# CÂU 10: gọi cau_10_tong_tien(3) bị lỗi NameError.
# Đúng phải là: cau_10_tong_tien(3) → 60
# (Được sửa cả hai hàm, giữ nguyên tên cau_10_tong_tien.)
def cau_10_tong_tien(so_luong):
    gia = 20
    return tinh_tien(so_luong,gia)


def tinh_tien(so_luong,gia):
    return so_luong * gia
