# =================================================================
# BÀI KIỂM TRA CUỐI BUỔI 1 + 2   (mục tiêu: ≥ 8/10 NGAY LẦN ĐẦU)
# =================================================================
# Luật:
#   - KHÔNG mở ghi chú, KHÔNG xem bài cũ, KHÔNG hỏi gợi ý.
#   - Trước mỗi câu: đọc đề TỪNG DÒNG. Chuỗi mẫu → copy từ đề.
#   - Làm xong TẤT CẢ rồi mới chạy máy chấm, và chỉ chạy 1 LẦN.
#     Điểm lần chạy đầu tiên là điểm thật — chụp màn hình gửi Claude.
#
# Chấm điểm:   python cham_kiem_tra_cuoi.py
# Chạy thử câu 10:   python kiem_tra_cuoi_buoi1_2.py
# =================================================================


# CÂU 1
# Viết hàm  lam_sach_ma(ma)
# Xóa khoảng trắng hai đầu và VIẾT HOA TOÀN BỘ.
#   lam_sach_ma("  ab12x ")  → "AB12X"
# Viết code dưới đây:
def lam_sach_ma(ma):
    return ma.strip().upper()



# CÂU 2
# Viết hàm  tien_phong(so_dem, gia_dem)  với gia_dem mặc định là 500000.
# Trả về SỐ: số đêm × giá mỗi đêm.
#   tien_phong(2)            → 1000000
#   tien_phong(3, 400000)    → 1200000
# Viết code dưới đây:
def tien_phong(so_dem,gia_dem=500000):
    return so_dem * gia_dem



# CÂU 3
# Viết hàm  tong_chuoi(a, b)
# a và b là CHUỖI chứa số nguyên. Trả về SỐ là tổng của chúng.
#   tong_chuoi("12", "8")  → 20
# Viết code dưới đây:
def tong_chuoi(a ,b):
    return (int(a) + int(b))



# CÂU 4
# Viết hàm  diem_tb(a, b, c)
# Trả về SỐ: trung bình 3 điểm, làm tròn 1 chữ số thập phân.
#   diem_tb(7, 8, 8)  → 7.7
#   diem_tb(9, 9, 9)  → 9.0
# Viết code dưới đây:
def diem_tb(a,b,c):
    return round((a+b+c)/3, 1)



# CÂU 5
# Viết hàm  the_sach(ten_sach, gia)
# Làm sạch tên sách (xóa khoảng trắng hai đầu, viết hoa chữ đầu mỗi từ).
# Giá hiển thị có dấu phẩy hàng nghìn.
#   the_sach("  nha gia kim ", 79000)  → "Nha Gia Kim: 79,000 đồng"
# Viết code dưới đây:
def the_sach(ten_sach, gia):
    return f"{ten_sach.strip().title()}: {gia:,} đồng"



# CÂU 6
# Viết hàm  ket_qua(ten, a, b, c)
# GỌI LẠI diem_tb (câu 4) để lấy điểm trung bình.
# Điểm hiển thị đúng 2 chữ số thập phân.
#   ket_qua("An", 7, 8, 8)  → "An: 7.70"
# Viết code dưới đây:
def ket_qua(ten, a, b, c):
    tb = diem_tb(a,b,c)
    return f"{ten}: {tb:.2f}"



# CÂU 7 · SỬA LỖI
# Code dưới đây SAI. Sửa trực tiếp để  c7_tong_tien(3) → 150000
def c7_tong_tien(so_sach):
    gia = 50000
    return c7_nhan(so_sach,gia)


def c7_nhan(so_sach,gia):
    return(so_sach * gia)


# CÂU 8 · ĐỌC CODE (đoán, KHÔNG chạy thử)
# Đoạn code sau in ra gì?
#     def f(x):
#         return x * 2
#     def g(x):
#         return f(x) + f(1)
#     print(g(3))
cau_8 = "8"


# CÂU 9 · ĐỌC CODE (đoán, KHÔNG chạy thử)
# Đoạn code sau in ra 2 dòng. DÒNG THỨ 2 là gì?
#     def h(ten="bạn"):
#         print("Chào", ten)
#     kq = h("An")
#     print(kq)
cau_9 = "None"


# CÂU 10 · CHƯƠNG TRÌNH HOÀN CHỈNH
# Viết hàm  main()  (được phép viết thêm hàm phụ nếu muốn):
#   - Hỏi 3 lần bằng input:  "Tên sách: "   "Số cuốn: "   "Giá mỗi cuốn: "
#   - Tên sách: làm sạch (xóa khoảng trắng hai đầu, viết hoa chữ đầu mỗi từ)
#   - Số cuốn và giá là số NGUYÊN
#   - In ra ĐÚNG 5 dòng (ví dụ nhập "  nha gia kim ", "2", "79000"):
#
#         --- PHIẾU MUA SÁCH ---
#         Sách: Nha Gia Kim
#         Số cuốn: 2
#         Tổng: 158,000 đồng
#         ----------------------
#
#     (dòng cuối: 22 dấu -, bằng độ dài dòng đầu)
#
# Cuối file nhớ có dòng gọi main() đúng chuẩn.
# Viết code dưới đây:
#Hỏi tên sach,số cuốn, giá mỗi cuốn(số nguyên)
# ② XỬ LÝ: làm sạch tên, tính tổng = số cuốn × giá, định dạng tiền
# ③ IN RA: 5 dòng đúng như đề
def main():
    ten = input("Tên sách: ").strip().title()
    so_cuon = int(input("Số cuốn: "))
    gia_moi_cuon = int(input("Giá mỗi cuốn: "))

    tong_tien = so_cuon * gia_moi_cuon

    print("--- PHIẾU MUA SÁCH ---")
    print(f"Sách: {ten}")
    print(f"Số cuốn: {so_cuon}")
    print(f"Tổng: {tong_tien:,} đồng")
    print("-"*22)
if __name__ == "__main__":
    main()
    