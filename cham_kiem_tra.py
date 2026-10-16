"""
MÁY CHẤM · BÀI KIỂM TRA + ÔN TẬP THÊM BUỔI 2 — bạn KHÔNG cần sửa file này.
Chạy:  python cham_kiem_tra.py              (chấm cả 2 file nếu có)
"""
import importlib.util
import io
import os
from contextlib import redirect_stdout

KIEM_TRA = ("kiem_tra_buoi1_2.py", "BÀI KIỂM TRA BUỔI 1 + 2", 8, [
    ("cau_1_lam_sach_email", "ham", [(("  AnH@Gmail.COM ",), "anh@gmail.com"), (("LAN@PTIT.EDU.VN",), "lan@ptit.edu.vn")]),
    ("cau_2_hen_gio", "ham", [(("Lan",), "Chào Lan, hẹn gặp lúc 8 giờ."), (("Minh", 14), "Chào Minh, hẹn gặp lúc 14 giờ.")]),
    ("cau_3_tong_ba_chuoi", "ham", [(("1", "2", "3"), 6), (("10", "20", "5"), 35)]),
    ("cau_4_tien_sau_giam", "ham", [((50, 3), 150.0), ((50, 3, 10), 135.0), ((9.99, 2, 15), 16.98)]),
    ("cau_5_the_diem", "ham", [(("  lê quang anh ", 8.5), "Lê Quang Anh: 8.5 điểm"), (("nguyễn an", 9), "Nguyễn An: 9.0 điểm")]),
    ("cau_6", "doan", "10"),
    ("cau_7", "doan", "ANBINH"),
    ("cau_8", "doan", "None"),
    ("cau_9_tinh_tuoi", "ham", [((2000,), 26), ((2006,), 20)]),
    ("cau_10_gia_sau_thue", "ham", [((100,), 110.0), ((50,), 55.0)]),
])

KIEM_TRA_2 = ("kiem_tra_lan2.py", "BÀI KIỂM TRA LẦN 2", 8, [
    ("cau_1_chuan_hoa_ma", "ham", [(("  ab12x ",), "AB12X"), (("sp-09",), "SP-09")]),
    ("cau_2_loi_moi", "ham", [(("Lan",), "Mời Lan dự tiệc vào thứ Bảy."), (("Minh", "Chủ nhật"), "Mời Minh dự tiệc vào Chủ nhật.")]),
    ("cau_3_tong_roi_nhan_doi", "ham", [(("3", "4"), 14), (("10", "0"), 20)]),
    ("cau_4_tien_lai", "ham", [((1000,), 50.0), ((2000, 7.5), 150.0), ((999, 3), 29.97)]),
    ("cau_5_bang_gia", "ham", [(("  pho bo ", 3.5), "Pho Bo - 3.50 USD"), (("banh mi", 2), "Banh Mi - 2.00 USD")]),
    ("cau_6", "doan", "15"),
    ("cau_7", "doan", "Hi An!"),
    ("cau_8", "doan", "6"),
    ("cau_9_gio_sang_phut", "ham", [((2,), 120), ((0.5,), 30.0)]),
    ("cau_10_tong_tien", "ham", [((3,), 60), ((0,), 0)]),
])

ON_TAP_2 = ("on_tap_lan2.py", "ÔN TẬP LẦN 2", 0, [
    ("on2_01_tien_ve", "ham", [((3,), 150000), ((2, 30000), 60000)]),
    ("on2_02_dien_tich_tam_giac", "ham", [((6, 4), 12.0), ((5, 3), 7.5)]),
    ("on2_03_lam_tron", "ham", [((8.567,), 8.6), ((7.04,), 7.0)]),
    ("on2_04_ho_ten", "ham", [(("Lê", "Anh"), "Lê Anh")]),
    ("on2_05_hien_diem", "ham", [(("An", 8), "An: 8.0"), (("Bình", 7.5), "Bình: 7.5")]),
    ("on2_06_trung_binh", "ham", [((7, 8), 7.5), ((9, 9), 9.0)]),
    ("on2_07_mo_ta_trung_binh", "ham", [(("An", 7, 8), "Điểm TB của An: 7.5")]),
    ("on2_08_tong_tien_ve", "ham", [((2, 1), 130000), ((0, 3), 90000)]),
    ("on2_09_hoa_don", "ham", [(("An", 2, 1), "An trả 130,000 đồng")]),
    ("on2_10_the_tich_hop", "ham", [((2, 3, 4), 24), ((1, 1, 1), 1)]),
])

ON_TAP = ("on_tap_buoi02_them.py", "ÔN TẬP THÊM BUỔI 2", 0, [
    ("on_01_gap_ba", "ham", [((4,), 12), ((0,), 0)]),
    ("on_02_hieu", "ham", [((10, 3), 7), ((3, 10), -7)]),
    ("on_03_phut_sang_giay", "ham", [((2,), 120), ((0.5,), 30.0)]),
    ("on_04_lap_phuong", "ham", [((3,), 27), ((-2,), -8)]),
    ("on_05_gioi_thieu", "ham", [(("An", 20), "An, 20 tuổi")]),
    ("on_06_chao_lich_su", "ham", [(("Lan",), "Chào bạn Lan!"), (("Hùng", "anh"), "Chào anh Hùng!")]),
    ("on_07_tien_dien", "ham", [((100,), 300000), ((100, 2500), 250000)]),
    ("on_08_tinh_bmi", "ham", [((60, 1.7), 20.8), ((80, 1.8), 24.7)]),
    ("on_09_mo_ta_bmi", "ham", [(("An", 60, 1.7), "An có BMI 20.8")]),
    ("on_10_tong_lap_phuong", "ham", [((1, 2), 9), ((2, 3), 35)]),
])


def bang(kq, mong):
    if isinstance(mong, float) or isinstance(kq, float):
        try:
            return abs(kq - mong) < 1e-6
        except TypeError:
            return False
    return kq == mong and type(kq) == type(mong)


def nap(ten_file):
    spec = importlib.util.spec_from_file_location(ten_file[:-3], ten_file)
    mod = importlib.util.module_from_spec(spec)
    with redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def cham(cau_hinh):
    ten_file, tieu_de, nguong, cac_cau = cau_hinh
    if not os.path.exists(ten_file):
        return
    print(f"\n===== {tieu_de} · {ten_file} =====\n")
    try:
        mod = nap(ten_file)
    except Exception as e:
        print(f"File có lỗi, chưa chạy được: {type(e).__name__}: {e}")
        print("Đọc số dòng (line) trong thông báo để tìm chỗ sai.")
        return
    dat = 0
    for ten, loai, du_lieu in cac_cau:
        nhan = ten.split("_")[0] + " " + ten.split("_")[1]
        if loai == "doan":
            tl = str(getattr(mod, ten, "")).strip()
            if not tl:
                print(f"⬜ {nhan}: chưa điền đáp án")
            elif tl == du_lieu:
                dat += 1
                print(f"✅ {nhan}")
            else:
                print(f"❌ {nhan}: bạn đoán {tl!r} — chưa đúng (đáp án không hiện, hãy suy nghĩ lại)")
            continue
        ham = getattr(mod, ten, None)
        if ham is None:
            print(f"⚠️  {nhan}: không thấy hàm {ten} — đừng đổi tên hàm")
            continue
        loi, chua_lam = None, False
        for args, mong in du_lieu:
            buf = io.StringIO()
            try:
                with redirect_stdout(buf):
                    kq = ham(*args)
            except Exception as e:
                loi = f"lỗi khi gọi {ten}{args} → {type(e).__name__}: {e}"
                break
            if kq is None:
                if buf.getvalue().strip():
                    loi = f"hàm dùng print thay vì return (in ra {buf.getvalue().strip()!r})"
                else:
                    chua_lam = True
                break
            if not bang(kq, mong):
                loi = f"gọi {ten}{args}\n      bạn trả về : {kq!r}\n      cần trả về : {mong!r}"
                break
        if chua_lam:
            print(f"⬜ {nhan}: chưa làm (hàm trả về None)")
        elif loi:
            print(f"❌ {nhan}: {loi}")
        else:
            dat += 1
            print(f"✅ {nhan}")
    tong = len(cac_cau)
    print(f"\nĐiểm: {dat}/{tong}")
    if nguong:
        print("ĐẠT ✅ → sẵn sàng vào buổi 3!" if dat >= nguong else f"Chưa đạt {nguong}/{tong}. Gửi kết quả cho Claude để ôn lại nhé.")
    else:
        print("Hoàn thành ôn tập! 🎉" if dat == tong else "Làm tiếp các bài chưa đạt nhé.")


if __name__ == "__main__":
    cham(KIEM_TRA)
    cham(KIEM_TRA_2)
    cham(ON_TAP)
    cham(ON_TAP_2)
