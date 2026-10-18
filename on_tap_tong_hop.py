# =================================================================
# ÔN TẬP TỔNG HỢP · TẬP TRUNG BUỔI 2   (phần 2 + phần 3)
# =================================================================
# Chấm điểm:   python cham_on_tap_tong_hop.py
# Không mở ghi chú, không xem bài cũ.
# =================================================================


# =================================================================
# PHẦN 2 · TỰ VIẾT HÀM TỪ ĐẦU (KHÔNG có khung sẵn)
# =================================================================
# Mỗi bài: TỰ viết dòng def, tham số, và return.
# Đặt ĐÚNG tên hàm + thứ tự tham số như đề (máy chấm gọi theo tên đó).
# -----------------------------------------------------------------

# BÀI 1
# Viết hàm  doi_usd_sang_vnd(usd, ty_gia)  với ty_gia mặc định là 25000.
# Trả về số tiền VND.
#   doi_usd_sang_vnd(2)          → 50000
#   doi_usd_sang_vnd(2, 26000)   → 52000
# Viết code dưới đây:
def doi_usd_sang_vnd(usd, ty_gia=25000):
    return usd * ty_gia




# BÀI 2
# Viết hàm  tinh_tien_taxi(km, gia_mo_cua, gia_km)
#   với gia_mo_cua mặc định 10000, gia_km mặc định 15000.
# Tiền taxi = giá mở cửa + số km × giá mỗi km.
#   tinh_tien_taxi(3)                 → 55000
#   tinh_tien_taxi(3, 12000)          → 57000
#   tinh_tien_taxi(2, 10000, 20000)   → 50000
# Viết code dưới đây:
def tinh_tien_taxi(km, gia_mo_cua=10000, gia_km=15000):
    return gia_mo_cua + km * gia_km



# BÀI 3
# Viết hàm  tinh_diem_tb(toan, van, anh)
# Trả về SỐ: trung bình 3 môn, làm tròn 2 chữ số thập phân.
#   tinh_diem_tb(8, 7, 9)  → 8.0
#   tinh_diem_tb(7, 8, 8)  → 7.67
# Viết code dưới đây:
def tinh_diem_tb(toan, van, anh):
    return round((toan+van+anh)/3, 2)



# BÀI 4
# Viết hàm  bang_diem(ten, toan, van, anh)
# GỌI LẠI tinh_diem_tb để lấy điểm TB. Làm sạch tên (strip + title).
# Điểm hiển thị đúng 2 chữ số thập phân.
#   bang_diem("  nguyễn an ", 8, 7, 9)  → "Nguyễn An: 8.00"
#   bang_diem("bình", 7, 8, 8)          → "Bình: 7.67"
# Viết code dưới đây:
def bang_diem(ten, toan, van, anh):
    tb = tinh_diem_tb(toan, van, anh)
    ten_sach = ten.strip().title()
    return f"{ten_sach}: {tb:.2f}" 



# BÀI 5
# Viết hàm  tong_hoa_don(so_ly, gia_ly, phi_ship)
#   với gia_ly mặc định 35000, phi_ship mặc định 15000.
# Tổng = số ly × giá mỗi ly + phí ship.
#   tong_hoa_don(2)            → 85000
#   tong_hoa_don(2, 40000)     → 95000
#   tong_hoa_don(1, 30000, 0)  → 30000
# Viết code dưới đây:
def tong_hoa_don(so_ly, gia_ly=35000, phi_ship=15000):
    return so_ly * gia_ly + phi_ship



# BÀI 6
# Viết hàm  in_hoa_don(ten, so_ly)
# GỌI LẠI tong_hoa_don(so_ly) (dùng giá và phí ship mặc định).
#   in_hoa_don("An", 2)  → "Khách An - 2 ly - Tổng: 85,000 đồng"
# Viết code dưới đây:
def in_hoa_don(ten, so_ly):
    tong = tong_hoa_don(so_ly)
    return f"Khách {ten} - {so_ly} ly - Tổng: {tong:,} đồng"



# =================================================================
# PHẦN 3A · SỬA LỖI (code bên dưới đều SAI — sửa trực tiếp)
# =================================================================

# S1: đúng phải là  s1_tien_luong(8) → 240000
def s1_tien_luong(gio, luong_gio=30000):
    return gio * luong_gio


# S2: a, b là CHUỖI chứa số.  Đúng phải là  s2_cong_chuoi("5", "7") → 12
def s2_cong_chuoi(a, b):
    return (int(a)+int(b))


# S3: đúng phải là  s3_chao("An") → "Xin chào, An!"
def s3_chao(ten):
    return f"Xin chào, {ten}!"


# S4: gọi s4_thanh_tien(5) bị NameError.  Đúng phải là → 60000
def s4_thanh_tien(so_luong):
    gia = 12000
    return s4_nhan(so_luong,gia)


def s4_nhan(so_luong,gia):
    return so_luong * gia


# S5: trung bình của a và b.  Đúng phải là  s5_trung_binh(4, 6) → 5.0
def s5_trung_binh(a, b):
    return (int(a) +int(b)) / 2


# S6: đúng phải là  s6_mo_ta("An", 4, 6) → "An: 5.0"
def s6_mo_ta(ten, a, b):
    tb = s5_trung_binh(a, b)
    return f"{ten}: {tb}"


# =================================================================
# PHẦN 3B · ĐỌC CODE, ĐOÁN KẾT QUẢ (đoán TRƯỚC, đừng chạy thử)
# =================================================================

# D1: in ra gì?
#     def a(x):
#         return x * 3
#     def b(x):
#         return a(x) + 1
#     print(b(2))
d1 = "7"

# D2: in ra gì?
#     def c(n=5):
#         return n - 1
#     print(c() + c(10))
d2 = "13"

# D3: sau khi chạy, biến y bằng bao nhiêu?
#     def p(x):
#         print(x)
#         return x * 2
#     y = p(3)
d3 = "6"

# D4: in ra gì?
#     def q(x):
#         return x + 1
#         print("xong")
#     print(q(q(1)))
d4 = "3"
