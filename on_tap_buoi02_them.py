# =================================================================
# ÔN TẬP THÊM · BUỔI 2 (def, return, tham số, giá trị mặc định)
# =================================================================
# Làm SAU bài kiểm tra. Bài luyện tập, không tính điểm qua môn.
# Mỗi hàm: xóa `pass`, viết code dùng `return` (không dùng print).
# Chấm điểm:   python cham_kiem_tra.py
# =================================================================


# --- Mức 1: một phép tính ---

def on_01_gap_ba(n):
    """Ví dụ: on_01_gap_ba(4) → 12"""
    return n*3


def on_02_hieu(a, b):
    """Trả về a trừ b.  Ví dụ: on_02_hieu(10, 3) → 7"""
    return int(a)-int(b)


def on_03_phut_sang_giay(phut):
    """Đổi phút sang giây.  Ví dụ: on_03_phut_sang_giay(2) → 120"""
    return phut * 60


def on_04_lap_phuong(n):
    """n × n × n.  Ví dụ: on_04_lap_phuong(3) → 27"""
    return n*n*n


# --- Mức 2: chuỗi và f-string ---

def on_05_gioi_thieu(ten, tuoi):
    """Ví dụ: on_05_gioi_thieu("An", 20) → "An, 20 tuổi" """
    return f"{ten}, {tuoi} tuổi"


def on_06_chao_lich_su(ten, xung_ho="bạn"):
    """Ví dụ: on_06_chao_lich_su("Lan")         → "Chào bạn Lan!"
              on_06_chao_lich_su("Hùng", "anh") → "Chào anh Hùng!"
    """
    return f"Chào {xung_ho} {ten}!"


# --- Mức 3: giá trị mặc định và làm tròn ---

def on_07_tien_dien(so_kwh, gia=3000):
    """Tiền điện = số kWh × giá.
    Ví dụ: on_07_tien_dien(100)        → 300000
           on_07_tien_dien(100, 2500)  → 250000
    """
    return so_kwh * gia


def on_08_tinh_bmi(can_nang, chieu_cao):
    """BMI = cân nặng (kg) chia (chiều cao (m) × chiều cao), làm tròn 1 chữ số.
    Ví dụ: on_08_tinh_bmi(60, 1.7) → 20.8
    """
    return round(can_nang/(chieu_cao * chieu_cao), 1)


# --- Mức 4: hàm gọi hàm ---

def on_09_mo_ta_bmi(ten, can_nang, chieu_cao):
    """GỌI LẠI on_08_tinh_bmi bên trong hàm này (đừng viết lại công thức).
    Ví dụ: on_09_mo_ta_bmi("An", 60, 1.7) → "An có BMI 20.8"
    """
    bmi = on_08_tinh_bmi(can_nang,chieu_cao)
    return f"{ten} có BMI {bmi}"


def on_10_tong_lap_phuong(a, b):
    """GỌI LẠI on_04_lap_phuong: trả về a³ + b³.
    Ví dụ: on_10_tong_lap_phuong(1, 2) → 9
    """
    return on_04_lap_phuong(a)+on_04_lap_phuong(b)
