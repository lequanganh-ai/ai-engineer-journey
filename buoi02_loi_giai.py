# BUỔI 2 · LỜI GIẢI THAM KHẢO — chỉ xem SAU KHI đã tự làm.
# Chấm thử:  python buoi02_cham_diem.py buoi02_loi_giai.py


def bai_01_chao(ten):
    return f"Xin chào, {ten}!"


def bai_02_binh_phuong(n):
    return n * n


def bai_03_tong(a, b):
    return a + b


def bai_04_cong_hai_chuoi_so(x, y):
    return int(x) + int(y)


def bai_05_trung_binh(a, b, c):
    return round((a + b + c) / 3, 2)


def bai_06_tien_tip(tien, phan_tram):
    return round(tien * phan_tram / 100, 2)


def bai_07_dinh_dang_tien(so):
    return f"{so:,} đồng"


def bai_08_lam_sach_ten(ten):
    return ten.strip().title()


def bai_09_chao_mac_dinh(ten="bạn"):
    return f"Xin chào, {ten}!"


def bai_10_doi_nhiet_do(do_c):
    do_f = do_c * 9 / 5 + 32
    return f"{do_c}°C = {do_f:.1f}°F"


def bai_11_tinh_dien_tich(dai, rong):
    return dai * rong


def bai_12_tinh_chu_vi(dai, rong):
    return (dai + rong) * 2


def main():
    ten = bai_08_lam_sach_ten(input("Tên bạn là gì? "))
    print(bai_01_chao(ten))


if __name__ == "__main__":
    main()
