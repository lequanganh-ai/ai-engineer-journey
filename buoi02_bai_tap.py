# =================================================================
# BUỔI 2 · BÀI TẬP: TỰ VIẾT HÀM (def), return, int, float
# =================================================================
# Học trước: CS50P Lecture 0, phần "Def" và "Returning Values"
#            (xem ghi chú phần 17–18 trong ghi-chu-cs50p-lecture0.md)
#
# Cách làm:
#   1. Mỗi bài là một hàm có sẵn tên. Xóa dòng `pass` và viết code thay vào.
#   2. Hàm phải dùng `return` để TRẢ KẾT QUẢ VỀ, KHÔNG dùng print.
#   3. Lưu file (Ctrl + S) rồi chấm:   python buoi02_cham_diem.py
#
# Ghi nhớ:  print  = hiện ra màn hình cho NGƯỜI xem
#           return = gửi giá trị về cho CODE dùng tiếp
# =================================================================


# ---------------------------------------------------------------
# PHẦN A · HÀM ĐẦU TIÊN
# ---------------------------------------------------------------

def bai_01_chao(ten):
    """Trả về chuỗi lời chào.
    Ví dụ: bai_01_chao("Lan")  →  "Xin chào, Lan!"
    """
    return(f"Xin chào, {ten}!")


def bai_02_binh_phuong(n):
    """Trả về bình phương của n (n nhân n).
    Ví dụ: bai_02_binh_phuong(4)  →  16
    """
    return pow(n, 2)


def bai_03_tong(a, b):
    """Trả về tổng của hai số a và b.
    Ví dụ: bai_03_tong(3, 5)  →  8
    """
    return a+b


# ---------------------------------------------------------------
# PHẦN B · int VÀ float
# ---------------------------------------------------------------

def bai_04_cong_hai_chuoi_so(x, y):
    """x và y là CHUỖI chứa số (giống kết quả của input()).
    Trả về TỔNG của chúng dưới dạng số nguyên.
    Ví dụ: bai_04_cong_hai_chuoi_so("1", "2")  →  3      (không phải "12"!)
    Gợi ý: int()
    """
    return int(x) + int(y)


def bai_05_trung_binh(a, b, c):
    """Trả về trung bình cộng của 3 số, làm tròn 2 chữ số thập phân.
    Ví dụ: bai_05_trung_binh(1, 2, 2)  →  1.67
    Gợi ý: round(..., 2)
    """
    return round((a+b+c)/3,2)


def bai_06_tien_tip(tien, phan_tram):
    """Tính tiền tip: tien nhân phan_tram chia 100, làm tròn 2 chữ số.
    Ví dụ: bai_06_tien_tip(50, 15)  →  7.5
    (Giống bài "Tip Calculator" trong Problem Set 0 của CS50P.)
    """
    return round((tien*phan_tram)/100,2)


def bai_07_dinh_dang_tien(so):
    """Trả về chuỗi số tiền có dấu phẩy ngăn cách hàng nghìn, kèm chữ "đồng".
    Ví dụ: bai_07_dinh_dang_tien(1500000)  →  "1,500,000 đồng"
    Gợi ý: f-string với {so:,}
    """
    return(f"{so:,} đồng")


# ---------------------------------------------------------------
# PHẦN C · CHUỖI VÀ THAM SỐ MẶC ĐỊNH
# ---------------------------------------------------------------

def bai_08_lam_sach_ten(ten):
    """Xóa khoảng trắng thừa ở đầu/cuối và viết hoa chữ cái đầu mỗi từ.
    Ví dụ: bai_08_lam_sach_ten("   lê quang anh ")  →  "Lê Quang Anh"
    """
    return ten.strip().title()


def bai_09_chao_mac_dinh(ten="bạn"):
    """Tham số ten có giá trị MẶC ĐỊNH là "bạn".
    Ví dụ: bai_09_chao_mac_dinh()        →  "Xin chào, bạn!"
           bai_09_chao_mac_dinh("Minh")  →  "Xin chào, Minh!"
    """
    return f"Xin chào, {ten}!"


# ---------------------------------------------------------------
# PHẦN D · THỬ THÁCH
# ---------------------------------------------------------------

def bai_10_doi_nhiet_do(do_c):
    """Đổi độ C sang độ F theo công thức F = C * 9 / 5 + 32,
    rồi trả về chuỗi có 1 chữ số thập phân:
    Ví dụ: bai_10_doi_nhiet_do(37)   →  "37°C = 98.6°F"
           bai_10_doi_nhiet_do(0)    →  "0°C = 32.0°F"
    Gợi ý: f"{gia_tri:.1f}"
    Thử thêm: có thể gọi lại một hàm khác bên trong hàm này không?
    """
    do_f =do_c * 9/5 +32
    return f"{do_c}°C = {do_f:.1f}°F"


# ---------------------------------------------------------------
# PHẦN D2 · HÌNH CHỮ NHẬT (thêm từ bài tự kiểm tra)
# ---------------------------------------------------------------

def bai_11_tinh_dien_tich(dai, rong):
    """Trả về diện tích hình chữ nhật = dài × rộng.
    Ví dụ: bai_11_tinh_dien_tich(5, 3)  →  15
    Khung hàm có return:
        def ten_ham(a, b):
            return <công thức>
    """
    return dai*rong


def bai_12_tinh_chu_vi(dai, rong):
    """Trả về chu vi hình chữ nhật = (dài + rộng) × 2.
    Ví dụ: bai_12_tinh_chu_vi(5, 3)  →  16
    Nhớ dấu ngoặc ( ) trong công thức!
    """
    return(dai+rong)*2


# ---------------------------------------------------------------
# PHẦN E · TỰ CHẠY THỬ (không chấm điểm)
# ---------------------------------------------------------------
# Viết hàm main() hỏi tên người dùng bằng input(), làm sạch bằng
# bai_08_lam_sach_ten, rồi in lời chào bằng bai_01_chao.
# Chạy:  python buoi02_bai_tap.py

def main():
    ten = bai_08_lam_sach_ten(input("Tên bạn là gì? "))
    print(bai_01_chao(ten))


if __name__ == "__main__":
    main()
