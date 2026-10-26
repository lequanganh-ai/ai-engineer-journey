# =================================================================
# BÀI KIỂM TRA CUỐI BUỔI 1 + 2 · ĐỀ LẦN 2   (mục tiêu: ≥ 8/10 NGAY LẦN ĐẦU)
# =================================================================
# Luật:
#   - KHÔNG mở ghi chú, KHÔNG xem bài cũ, KHÔNG hỏi gợi ý.
#   - Chuỗi mẫu → COPY từ đề, không gõ tay.
#   - QUY TẮC MỚI: làm xong mỗi câu, so kết quả với ví dụ của đề TỪNG KÝ TỰ,
#     rồi mới thay  # Soát đề: ...  bằng  # Soát đề: OK
#     (máy chấm đếm số dòng "# Soát đề: OK")
#   - Làm xong TẤT CẢ rồi mới chạy máy chấm, và chỉ chạy 1 LẦN.
#
# Chấm điểm:          python cham_kiem_tra_lan3.py
# Chạy thử câu 10:    python kiem_tra_lan3.py
# =================================================================


# CÂU 1
# Viết hàm  chuan_hoa_email(email)
# Xóa khoảng trắng hai đầu và viết THƯỜNG toàn bộ.
#   chuan_hoa_email("  AnH@Gmail.COM ")  → "anh@gmail.com"
# Soát đề: ...
# Viết code dưới đây:
def chuan_hoa_email(email):
    return email.strip().lower()



# CÂU 2
# Viết hàm  tien_ve(so_ve, gia_ve)  với gia_ve mặc định là 90000.
# Trả về SỐ: số vé × giá mỗi vé.
#   tien_ve(2)           → 180000
#   tien_ve(3, 75000)    → 225000
# Soát đề: ...
# Viết code dưới đây:
def tien_ve(so_ve, gia_ve=90000):
    return so_ve * gia_ve



# CÂU 3
# Viết hàm  nhan_doi_tong(a, b)
# a và b là CHUỖI chứa số nguyên. Cộng hai số, rồi nhân đôi kết quả.
# Trả về SỐ.
#   nhan_doi_tong("3", "4")  → 14
# Soát đề: ...
# Viết code dưới đây:
def nhan_doi_tong(a, b):
    return ((int(a) + int(b)) * 2)



# CÂU 4
# Viết hàm  phan_tram(dat, tong)
# Trả về SỐ: dat chia tong nhân 100, làm tròn 1 chữ số thập phân.
#   phan_tram(7, 9)  → 77.8
#   phan_tram(1, 3)  → 33.3
# Soát đề: ...
# Viết code dưới đây:
def phan_tram(dat, tong):
    return round((dat / tong) * 100, 1)



# CÂU 5
# Viết hàm  nhan_ve(phim, ghe)
# Tên phim: xóa khoảng trắng hai đầu, viết hoa chữ đầu mỗi từ.
# Mã ghế: viết HOA toàn bộ.
#   nhan_ve("  avatar 3 ", "b7")  → "Avatar 3 - Ghế B7"
# Soát đề: ...
# Viết code dưới đây:
def nhan_ve(phim, ghe):
    return f"{phim.strip().title()} - Ghế {ghe.upper()}"



# CÂU 6
# Viết hàm  bao_cao(ten, dat, tong)
# GỌI LẠI phan_tram (câu 4). Hiển thị đúng 1 chữ số thập phân và dấu %.
#   bao_cao("An", 7, 9)    → "An: 77.8%"
#   bao_cao("Bình", 9, 9)  → "Bình: 100.0%"
# Soát đề: ...
# Viết code dưới đây:
def bao_cao(ten ,dat, tong):
    dat_trong = phan_tram(dat, tong)
    return f"{ten}: {dat_trong:.1f}%"



# CÂU 7 · SỬA LỖI
# Code dưới đây SAI (có nhiều hơn 1 lỗi). Sửa trực tiếp để  c7_tien_luong(8) → 200000
# Soát đề: ...
def c7_tien_luong(gio):
    luong = 25000
    return gio* luong


def c7_nhan(gio, luong):
    return (gio*luong) 


# CÂU 8 · ĐỌC CODE (đoán, KHÔNG chạy thử)
# Đoạn code sau in ra gì?
#     def a(x):
#         return x + 1
#     def b(x):
#         return a(a(x)) * 2
#     print(b(1))
# Soát đề: ...
cau_8 = "6"


# CÂU 9 · ĐỌC CODE (đoán, KHÔNG chạy thử)
# Đoạn code sau in ra gì?
#     def chao(ten):
#         return "Hi " + ten
#         print("xong")
#     x = chao("An")
#     print(x)
# Soát đề: ...
cau_9 = "Hi An"


# CÂU 10 · CHƯƠNG TRÌNH HOÀN CHỈNH
# Viết hàm  main():
#   - Hỏi 3 lần bằng input:  "Tên phim: "   "Số vé: "   "Giá mỗi vé: "
#   - Tên phim: xóa khoảng trắng hai đầu, viết hoa chữ đầu mỗi từ
#   - Số vé và giá là số NGUYÊN
#   - In ra ĐÚNG 5 dòng (ví dụ nhập "  avatar 3 ", "3", "90000"):
#
#         === VÉ XEM PHIM ===
#         Phim: Avatar 3
#         Số vé: 3
#         Thành tiền: 270,000 đồng
#         ===================
#
#     (dòng cuối: 19 dấu =, bằng độ dài dòng đầu)
#
# Viết 3 dòng comment kế hoạch (① HỎI / ② XỬ LÝ / ③ IN RA) TRƯỚC khi viết code.
# Cuối file nhớ có dòng gọi main() đúng chuẩn.
# Soát đề: ...
# Viết code dưới đây:
def main():
    ten = input("Tên phim: ").strip().title()
    so_ve = int(input("Số vé: "))
    gia_moi_ve = int(input("Giá mỗi vé: "))

    tong_tien = so_ve * gia_moi_ve

    print("=== VÉ XEM PHIM ===")
    print(f"Phim: {ten}")
    print(f"Số vé: {so_ve}")
    print(f"Thành tiền: {tong_tien:,} đồng")
    print("="*19)
if __name__ =="(__main__)":
    main()