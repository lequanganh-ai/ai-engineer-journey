# =================================================================
# BUỔI 5 · PHẦN A · KIỂM TRA TỔNG HỢP TUẦN 1
# Mục tiêu: ≥ 8/10 NGAY LẦN ĐẦU  +  Soát đề 10/10
# =================================================================
# Luật:
#   - KHÔNG mở bất kỳ ghi chú nào, KHÔNG hỏi gợi ý, KHÔNG dùng AI gợi ý code.
#   - Soát đề chỉ ghi OK SAU KHI đã chạy thử đủ ví dụ. Viết CHÍNH XÁC (copy):
#         # Soát đề: OK
#   - Làm xong cả PHẦN A (file này) và PHẦN B (tu_viet.py) rồi mới chạy máy chấm 1 LẦN:
#         python cham_tuan1.py
# =================================================================


# CÂU 1
# Viết hàm  chuan_hoa_ten(ten)
# Xóa khoảng trắng hai đầu, viết hoa chữ đầu mỗi từ.
#   chuan_hoa_ten("  nguyễn văn an ")  → "Nguyễn Văn An"
# Soát đề: OK
# Viết code dưới đây:
def chuan_hoa_ten(ten):
    return ten.strip().title()



# CÂU 2
# Viết hàm  tien_dien(so_kwh, gia)  với gia mặc định là 3000.
# Trả về SỐ: số kWh × giá.
#   tien_dien(100)         → 300000
#   tien_dien(50, 2500)    → 125000
# Soát đề: OK
# Viết code dưới đây:
def tien_dien(so_kwh, gia=3000):
    return so_kwh * gia



# CÂU 3
# Viết hàm  tong_ba_chuoi(a, b, c)
# a, b, c là CHUỖI chứa số nguyên. Trả về SỐ là tổng của chúng.
#   tong_ba_chuoi("1", "2", "3")  → 6
# Soát đề: OK
# Viết code dưới đây:
def tong_ba_chuoi(a, b, c):
    return int(a)+int(b)+int(c)



# CÂU 4
# Viết hàm  trung_binh(a, b, c)
# Trả về SỐ: trung bình 3 số, làm tròn 2 chữ số thập phân.
#   trung_binh(8, 7, 9)  → 8.0
#   trung_binh(7, 8, 8)  → 7.67
# Soát đề: OK
# Viết code dưới đây:
def trung_binh(a, b, c):
    return round((a+b+c)/3, 2)



# CÂU 5
# Viết hàm  bang_diem(ten, a, b, c)
# GỌI chuan_hoa_ten (câu 1) và trung_binh (câu 4).
# Điểm hiển thị đúng 1 chữ số thập phân, sau đó là chữ " điểm".
#   bang_diem("  lê an ", 7, 8, 8)  → "Lê An: 7.7 điểm"
# Soát đề: OK
# Viết code dưới đây:
def bang_diem(ten, a, b, c):
    ten_chuan = chuan_hoa_ten(ten)
    tb = trung_binh(a,b,c)
    return f"{ten_chuan}: {tb:.1f} điểm"



# CÂU 6
# Viết hàm  doi_usd(chuoi)
# chuoi có dấu $ ở đầu. Bỏ dấu $ rồi trả về SỐ THỰC.
#   doi_usd("$12.50")  → 12.5
#   doi_usd("$100")    → 100.0
# Soát đề: OK
# Viết code dưới đây:
def doi_usd(chuoi):
    return float(chuoi.replace("$",""))



# CÂU 7 · SỬA LỖI (có NHIỀU HƠN 1 lỗi)
# Đúng phải là:  c7_hoa_don("An", 200000)  → "An: 180,000 đồng"
# Soát đề: OK
def c7_gia_sau_giam(gia, phan_tram=10):
    giam = gia * phan_tram // 100
    return gia - giam


def c7_hoa_don(ten, gia):
    return f"{ten}: {c7_gia_sau_giam(gia):,} đồng"


# CÂU 8 · ĐỌC THÔNG BÁO LỖI
# Chạy một file thì thấy:
#     Traceback (most recent call last):
#       File "bai.py", line 4, in <module>
#         so = int(chuoi)
#     ValueError: invalid literal for int() with base 10: '1,000'
# LOẠI LỖI này tên là gì? (chỉ ghi tên loại lỗi)
# Soát đề: OK
cau_8 = "ValueError"


# CÂU 9 · ĐỌC CODE (đoán, KHÔNG chạy thử)
# Đoạn code sau in ra gì?
#     print(2 + 3 * 2 ** 2)
# Soát đề: OK
cau_9 = "14"


# CÂU 10 · CHƯƠNG TRÌNH HOÀN CHỈNH
# Viết hàm  main():
#   - Hỏi 2 lần bằng input:  "Tên chủ hộ: "   "Số kWh: "
#   - Số kWh là số NGUYÊN
#   - GỌI chuan_hoa_ten (câu 1) và tien_dien (câu 2, dùng giá mặc định)
#   - In ra ĐÚNG 3 dòng, ví dụ nhập "  nguyễn văn an ", "100":
#
#         HÓA ĐƠN TIỀN ĐIỆN
#         Chủ hộ: Nguyễn Văn An
#         Số tiền: 300,000 đồng
#
# Comment kế hoạch (① HỎI / ② XỬ LÝ / ③ IN RA) bên trong main trước khi code.
# Cuối file nhớ có dòng gọi main() đúng chuẩn.
# Soát đề: OK
# Viết code dưới đây:
def main():
    #Hỏi tên chủ hộ, số kwh(số nguyên)
    ten = input("Tên chủ hộ: ")
    so_kwh = int(input("Sô kwh: "))
    #xử lí:Làm sạch tên, tính tiền điện(giá mặc định)
    lam_sach =chuan_hoa_ten(ten)
    tien = tien_dien(so_kwh)
    #In ra: 3 dòng đúng như đề
    print("HÓA ĐƠN TIỀN ĐIỆN")
    print(f"Chủ hộ: {lam_sach}")
    print(f"Số tiền: {tien:,} đồng")
if __name__ == "__main__":
    main()
