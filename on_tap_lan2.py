# =================================================================
# ÔN TẬP LẦN 2 · LUYỆN ĐÚNG 3 LỖI HAY GẶP
# =================================================================
# Chấm điểm:   python cham_kiem_tra.py   (xem phần "ÔN TẬP LẦN 2")
#
# 3 QUY TẮC VÀNG — đọc kỹ trước khi làm:
#
#   1. TÍNH RA SỐ   → viết tên biến trực tiếp, KHÔNG có { }
#        return so_ve * gia                 ✅
#        return {so_ve} * {gia}             ❌
#
#   2. GHÉP THÀNH CHỮ → f"..." có { } bên trong
#        return f"{ten}: {diem:.1f}"        ✅
#        :.1f CHỈ dùng trong f-string. Làm tròn SỐ thì dùng round(x, 1)
#
#   3. DỮ LIỆU vào hàm qua THAM SỐ — KHÔNG dùng input() trong hàm.
#      GỌI hàm khác → truyền ĐỦ đối số nó cần, rồi return kết quả.
# =================================================================


# ---------------------------------------------------------------
# NHÓM 1 · TÍNH RA SỐ (không dùng { })
# ---------------------------------------------------------------

def on2_01_tien_ve(so_ve, gia=50000):
    """Tiền vé = số vé × giá.
    Ví dụ: on2_01_tien_ve(3)          → 150000
           on2_01_tien_ve(2, 30000)   → 60000
    """
    return so_ve * gia


def on2_02_dien_tich_tam_giac(day, cao):
    """Diện tích tam giác = đáy × cao / 2.
    Ví dụ: on2_02_dien_tich_tam_giac(6, 4) → 12.0
    """
    return day * cao /2


def on2_03_lam_tron(diem):
    """Trả về SỐ đã làm tròn 1 chữ số thập phân (dùng round, không dùng f-string).
    Ví dụ: on2_03_lam_tron(8.567) → 8.6
    """
    return round(diem, 1)


# ---------------------------------------------------------------
# NHÓM 2 · GHÉP THÀNH CHỮ (f-string có { })
# ---------------------------------------------------------------

def on2_04_ho_ten(ho, ten):
    """Ví dụ: on2_04_ho_ten("Lê", "Anh") → "Lê Anh" """
    return f"{ho} {ten}"


def on2_05_hien_diem(ten, diem):
    """Điểm hiển thị đúng 1 chữ số thập phân.
    Ví dụ: on2_05_hien_diem("An", 8)    → "An: 8.0"
           on2_05_hien_diem("Bình", 7.5) → "Bình: 7.5"
    """
    return f"{ten}: {diem:.1f}"


# ---------------------------------------------------------------
# NHÓM 3 · TÍNH SỐ RỒI GHÉP CHỮ (hàm gọi hàm)
# ---------------------------------------------------------------

def on2_06_trung_binh(a, b):
    """Trả về SỐ: trung bình của a và b, làm tròn 1 chữ số.
    Ví dụ: on2_06_trung_binh(7, 8) → 7.5
    """
    return round((a+b)/2, 1)


def on2_07_mo_ta_trung_binh(ten, a, b):
    """GỌI on2_06_trung_binh(a, b) để lấy điểm TB, rồi ghép câu.
    Ví dụ: on2_07_mo_ta_trung_binh("An", 7, 8) → "Điểm TB của An: 7.5"
    """
    tb =on2_06_trung_binh(a, b)
    return f"Điểm TB của {ten}: {tb}"


# ---------------------------------------------------------------
# NHÓM 4 · GỌI HÀM KHÁC VỚI ĐÚNG ĐỐI SỐ
# ---------------------------------------------------------------

def on2_08_tong_tien_ve(nguoi_lon, tre_em):
    """Vé người lớn giá mặc định 50000, vé trẻ em giá 30000.
    GỌI on2_01_tien_ve HAI LẦN rồi cộng lại.
    Ví dụ: on2_08_tong_tien_ve(2, 1) → 130000
    Gợi ý: on2_01_tien_ve(nguoi_lon) + on2_01_tien_ve(tre_em, ...)
    """
    tien_nguoi_lon = on2_01_tien_ve(nguoi_lon)
    tien_tre_em = on2_01_tien_ve(tre_em, 30000)
    return tien_nguoi_lon + tien_tre_em


def on2_09_hoa_don(ten, nguoi_lon, tre_em):
    """GỌI on2_08_tong_tien_ve, rồi ghép câu có dấu phẩy hàng nghìn.
    Ví dụ: on2_09_hoa_don("An", 2, 1) → "An trả 130,000 đồng"
    Gợi ý: {tong:,}
    """
    tong_tien_ve = on2_08_tong_tien_ve(nguoi_lon,tre_em)
    return f"{ten} trả {tong_tien_ve:,} đồng"


def dien_tich_day(dai, rong):
    """Hàm có sẵn — KHÔNG cần sửa."""
    return dai * rong


def on2_10_the_tich_hop(dai, rong, cao):
    """Thể tích hộp = diện tích đáy × chiều cao.
    GỌI hàm có sẵn dien_tich_day(dai, rong), rồi nhân với cao.
    Ví dụ: on2_10_the_tich_hop(2, 3, 4) → 24
    """
    dien_tich = dien_tich_day(dai,rong)
    return dien_tich * cao 
