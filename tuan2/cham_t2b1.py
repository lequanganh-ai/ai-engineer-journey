"""
MÁY CHẤM · TUẦN 2 · BUỔI 1 — bạn KHÔNG cần sửa file này.
Chạy:  python cham_t2b1.py     (cùng thư mục với t2b1_bai_tap.py)
"""
import builtins
import importlib.util
import io
import os
from contextlib import redirect_stdout

FILE = "t2b1_bai_tap.py"
HAM = [
    ("Bài 1", "so_lon_hon", [((3, 5), 5), ((7, 2), 7), ((4, 4), 4), ((-1, -5), -1)]),
    ("Bài 2", "so_sanh", [((1, 2), "nhỏ hơn"), ((5, 3), "lớn hơn"), ((4, 4), "bằng nhau")]),
    ("Bài 3", "ket_qua_thi", [((5,), "Đậu"), ((4.9,), "Rớt"), ((10,), "Đậu"), ((0,), "Rớt")]),
    ("Bài 4", "xep_loai", [((9.5,), "Xuất sắc"), ((9,), "Xuất sắc"), ((8,), "Giỏi"), ((8.9,), "Giỏi"),
                           ((6.5,), "Khá"), ((7.9,), "Khá"), ((5,), "Trung bình"), ((6.4,), "Trung bình"),
                           ((4,), "Yếu"), ((4.99,), "Yếu")]),
    ("Bài 5", "trong_khoang", [((1,), True), ((10,), True), ((5,), True), ((0,), False), ((11,), False)]),
    ("Bài 6", "cuoi_tuan", [(("Thứ Bảy",), True), (("  CHỦ NHẬT ",), True), (("thứ bảy",), True),
                            (("Thứ Hai",), False), (("",), False)]),
    ("Bài 7", "gia_ve", [((5,), 0), ((6,), 50000), ((17,), 50000), ((18,), 90000), ((59,), 90000), ((60,), 45000)]),
    ("Bài 8", "phi_ship", [((300000,), 0), ((299999,), 30000), ((1000000,), 0)]),
    ("Bài 9", "du_dieu_kien", [(("An", 18), True), (("   ", 20), False), (("Bình", 17), False), (("", 17), False)]),
    ("Bài 10", "c10_muc_do", [((8,), "Tốt"), ((10,), "Tốt"), ((6,), "Đạt"), ((5,), "Đạt"), ((3,), "Chưa đạt")]),
]
MAIN_TESTS = [(["8.5"], "Xếp loại: Giỏi"), (["10"], "Xếp loại: Xuất sắc"), (["4.5"], "Xếp loại: Yếu")]


def bang(kq, mong):
    if isinstance(mong, bool) or isinstance(kq, bool):
        return kq is mong
    if isinstance(mong, float) or isinstance(kq, float):
        try:
            return abs(kq - mong) < 1e-6
        except TypeError:
            return False
    return kq == mong and type(kq) == type(mong)


def nap():
    spec = importlib.util.spec_from_file_location("bai", FILE)
    mod = importlib.util.module_from_spec(spec)
    goc = builtins.input

    def cam(_=""):
        raise RuntimeError('file gọi input()/main() ngay khi import — thiếu  if __name__ == "__main__":')
    builtins.input = cam
    try:
        with redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        builtins.input = goc
    return mod


def cham_ham(mod, nhan, ten, cases):
    ham = getattr(mod, ten, None)
    if ham is None:
        print(f"⬜ {nhan}: chưa thấy hàm {ten}")
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
            print(f"❌ {nhan}: hàm dùng print thay vì return" if buf.getvalue().strip() else f"⬜ {nhan}: hàm trả về None (chưa có return?)")
            return 0
        if not bang(kq, mong):
            print(f"❌ {nhan}: gọi {ten}{args}\n      bạn trả về : {kq!r}\n      cần trả về : {mong!r}")
            return 0
    print(f"✅ {nhan}")
    return 1


def cham_main(mod):
    ham = getattr(mod, "main", None)
    if ham is None:
        print("⬜ Bài 11: chưa thấy hàm main")
        return 0
    for nhap, mong in MAIN_TESTS:
        hang = list(nhap)

        def gia(_=""):
            if not hang:
                raise RuntimeError("gọi input() nhiều hơn 1 lần")
            return hang.pop(0)
        mod.input = gia
        buf = io.StringIO()
        try:
            with redirect_stdout(buf):
                ham()
        except Exception as e:
            print(f"❌ Bài 11: lỗi khi chạy (nhập {nhap}) → {type(e).__name__}: {e}")
            return 0
        ra = buf.getvalue().strip()
        if ra != mong:
            print(f"❌ Bài 11: khi nhập {nhap}\n      bạn in ra : {ra!r}\n      cần in ra : {mong!r}")
            return 0
    print("✅ Bài 11")
    return 1


def main():
    if not os.path.exists(FILE):
        print(f"Không thấy {FILE} — đứng đúng thư mục chưa? (gõ ls để kiểm tra)")
        return
    print(f"\n===== TUẦN 2 · BUỔI 1 · {FILE} =====\n")
    try:
        mod = nap()
    except Exception as e:
        print(f"File có lỗi, chưa chạy được: {type(e).__name__}: {e}")
        return
    diem = sum(cham_ham(mod, n, t, c) for n, t, c in HAM) + cham_main(mod)
    ok = sum(1 for d in open(FILE, encoding="utf-8") if d.strip() == "# Soát đề: OK")
    print(f"\nĐiểm: {diem}/11   ·   Soát đề: {ok}/11" + ("" if ok >= 11 else "  ⚠️"))
    print("HOÀN THÀNH 🎉" if diem == 11 and ok >= 11 else "Làm tiếp bài chưa đạt nhé.")


if __name__ == "__main__":
    main()
