"""
MÁY CHẤM · ÔN TẬP TỔNG HỢP + MINI PROJECT — bạn KHÔNG cần sửa file này.
Chạy:  python cham_on_tap_tong_hop.py
"""
import importlib.util
import io
import os
from contextlib import redirect_stdout

PHAN_2 = [
    ("Bài 1", "doi_usd_sang_vnd", [((2,), 50000), ((2, 26000), 52000)]),
    ("Bài 2", "tinh_tien_taxi", [((3,), 55000), ((3, 12000), 57000), ((2, 10000, 20000), 50000)]),
    ("Bài 3", "tinh_diem_tb", [((8, 7, 9), 8.0), ((7, 8, 8), 7.67)]),
    ("Bài 4", "bang_diem", [(("  nguyễn an ", 8, 7, 9), "Nguyễn An: 8.00"), (("bình", 7, 8, 8), "Bình: 7.67")]),
    ("Bài 5", "tong_hoa_don", [((2,), 85000), ((2, 40000), 95000), ((1, 30000, 0), 30000)]),
    ("Bài 6", "in_hoa_don", [(("An", 2), "Khách An - 2 ly - Tổng: 85,000 đồng")]),
]
PHAN_3A = [
    ("S1", "s1_tien_luong", [((8,), 240000)]),
    ("S2", "s2_cong_chuoi", [(("5", "7"), 12)]),
    ("S3", "s3_chao", [(("An",), "Xin chào, An!")]),
    ("S4", "s4_thanh_tien", [((5,), 60000)]),
    ("S5", "s5_trung_binh", [((4, 6), 5.0), ((3, 3), 3.0)]),
    ("S6", "s6_mo_ta", [(("An", 4, 6), "An: 5.0")]),
]
PHAN_3B = [("D1", "d1", "7"), ("D2", "d2", "13"), ("D3", "d3", "6"), ("D4", "d4", "3")]
MINI = [
    ("lam_sach_ten", "lam_sach_ten", [(("  lê an ",), "Lê An")]),
    ("thanh_tien", "thanh_tien", [((3, 35000), 105000)]),
    ("dinh_dang_tien", "dinh_dang_tien", [((105000,), "105,000 đồng"), ((999,), "999 đồng")]),
]
MAIN_TESTS = [
    (["  lê an ", "3", "35000"],
     "===== HÓA ĐƠN =====\nKhách: Lê An\nSố ly: 3\nThành tiền: 105,000 đồng\n==================="),
    (["minh", "1", "29000"],
     "===== HÓA ĐƠN =====\nKhách: Minh\nSố ly: 1\nThành tiền: 29,000 đồng\n==================="),
]


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


def cham_ham(mod, nhan, ten, cases):
    ham = getattr(mod, ten, None)
    if ham is None:
        print(f"⬜ {nhan}: chưa thấy hàm {ten} (đã đặt đúng tên chưa?)")
        return 0
    for args, mong in cases:
        buf = io.StringIO()
        try:
            with redirect_stdout(buf):
                kq = ham(*args)
        except Exception as e:
            print(f"❌ {nhan}: lỗi khi gọi {ten}{args} → {type(e).__name__}: {e}")
            return 0
        if kq is None:
            if buf.getvalue().strip():
                print(f"❌ {nhan}: hàm dùng print thay vì return (in ra {buf.getvalue().strip()!r})")
            else:
                print(f"⬜ {nhan}: hàm trả về None (chưa có return?)")
            return 0
        if not bang(kq, mong):
            print(f"❌ {nhan}: gọi {ten}{args}\n      bạn trả về : {kq!r}\n      cần trả về : {mong!r}")
            return 0
    print(f"✅ {nhan}")
    return 1


def chuan(s):
    return "\n".join(d.rstrip() for d in s.strip().splitlines())


def cham_main(mod):
    ham = getattr(mod, "main", None)
    if ham is None:
        print("⬜ main(): chưa thấy hàm main")
        return 0
    for nhap, mong in MAIN_TESTS:
        hang = list(nhap)

        def input_gia(_=""):
            if not hang:
                raise RuntimeError("gọi input() nhiều hơn 3 lần")
            return hang.pop(0)

        mod.input = input_gia
        buf = io.StringIO()
        try:
            with redirect_stdout(buf):
                ham()
        except Exception as e:
            print(f"❌ main(): lỗi khi chạy (nhập {nhap}) → {type(e).__name__}: {e}")
            return 0
        if chuan(buf.getvalue()) != chuan(mong):
            print(f"❌ main(): kết quả chưa đúng (khi nhập {nhap})")
            print("   --- bạn in ra ---")
            print("   " + chuan(buf.getvalue()).replace("\n", "\n   "))
            print("   --- cần in ra ---")
            print("   " + mong.replace("\n", "\n   "))
            return 0
    print("✅ main()")
    return 1


def main():
    if os.path.exists("on_tap_tong_hop.py"):
        print("\n===== ÔN TẬP TỔNG HỢP · on_tap_tong_hop.py =====")
        try:
            mod = nap("on_tap_tong_hop.py")
        except Exception as e:
            print(f"File có lỗi, chưa chạy được: {type(e).__name__}: {e}")
            mod = None
        if mod:
            print("\n-- Phần 2: tự viết hàm --")
            p2 = sum(cham_ham(mod, n, t, c) for n, t, c in PHAN_2)
            print("\n-- Phần 3A: sửa lỗi --")
            p3a = sum(cham_ham(mod, n, t, c) for n, t, c in PHAN_3A)
            print("\n-- Phần 3B: đọc code --")
            p3b = 0
            for n, bien, da in PHAN_3B:
                tl = str(getattr(mod, bien, "")).strip()
                if not tl:
                    print(f"⬜ {n}: chưa điền")
                elif tl == da:
                    p3b += 1
                    print(f"✅ {n}")
                else:
                    print(f"❌ {n}: bạn đoán {tl!r} — chưa đúng")
            print(f"\nPhần 2: {p2}/6   ·   Phần 3A: {p3a}/6   ·   Phần 3B: {p3b}/4")
            tong = p2 + p3a + p3b
            print(f"TỔNG: {tong}/16  →  " + ("ĐẠT ✅" if tong >= 13 else "Cần ôn thêm (mục tiêu 13/16)"))

    if os.path.exists("mini_project_cafe.py"):
        print("\n===== MINI PROJECT · mini_project_cafe.py =====")
        try:
            mod = nap("mini_project_cafe.py")
        except Exception as e:
            print(f"File có lỗi, chưa chạy được: {type(e).__name__}: {e}")
            return
        diem = sum(cham_ham(mod, n, t, c) for n, t, c in MINI) + cham_main(mod)
        print(f"\nMini project: {diem}/4  →  " + ("HOÀN THÀNH 🎉" if diem == 4 else "Làm tiếp nhé"))


if __name__ == "__main__":
    main()
