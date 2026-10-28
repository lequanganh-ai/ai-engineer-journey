"""
MÁY CHẤM · TUẦN 2 · BUỔI 1 · LUYỆN LẠI — bạn KHÔNG cần sửa file này.
Chạy:  python cham_t2b1_luyen_lai.py     (cùng thư mục với t2b1_bai_tap.py)
"""
import builtins
import importlib.util
import io
import os
from contextlib import redirect_stdout

FILE = "t2b1_luyen_lai.py"
HAM = [
    ("Bài 1", "nhiet_do", [((-1,), "Đóng băng"), ((0,), "Mát"), ((24.9,), "Mát"), ((25,), "Nóng")]),
    ("Bài 2", "c2_size", [((155,), "S"), ((159,), "S"), ((160,), "M"), ((170,), "M"), ((171,), "L")]),
    ("Bài 3", "la_quan_tri", [(("  ADMIN ",), True), (("Root",), True), (("an",), False), (("administrator",), False)]),
    ("Bài 4", "phi_gui_xe", [((1,), 5000), ((2,), 5000), ((3,), 10000), ((5,), 10000), ((6,), 20000)]),
    ("Bài 5", "c5_huy_hieu", [((95,), "Vàng"), ((100,), "Vàng"), ((80,), "Bạc"), ((94,), "Bạc"), ((50,), "Đồng"), ((49,), "Chưa có")]),
    ("Bài 6", "tien_giam", [((1000000,), 100000), ((999999,), 30000), ((500000,), 30000), ((499999,), 0)]),
    ("Bài 7", "mat_khau_on", [(("abc@2026",), True), (("123456",), False), (("   ",), False)]),
]
MAIN_TESTS = [(["165"], "Size: M"), (["150"], "Size: S"), (["180"], "Size: L")]


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
        print("⬜ Bài 8: chưa thấy hàm main")
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
            print(f"❌ Bài 8: lỗi khi chạy (nhập {nhap}) → {type(e).__name__}: {e}")
            return 0
        ra = buf.getvalue().strip()
        if ra != mong:
            print(f"❌ Bài 8: khi nhập {nhap}\n      bạn in ra : {ra!r}\n      cần in ra : {mong!r}")
            return 0
    print("✅ Bài 8")
    return 1


def main():
    if not os.path.exists(FILE):
        print(f"Không thấy {FILE} — đứng đúng thư mục chưa? (gõ ls để kiểm tra)")
        return
    print(f"\n===== LUYỆN LẠI · {FILE} =====\n")
    try:
        mod = nap()
    except Exception as e:
        print(f"File có lỗi, chưa chạy được: {type(e).__name__}: {e}")
        return
    diem = sum(cham_ham(mod, n, t, c) for n, t, c in HAM) + cham_main(mod)
    ok = sum(1 for d in open(FILE, encoding="utf-8") if d.strip() == "# Soát đề: OK")
    print(f"\nĐiểm: {diem}/8   ·   Soát đề: {ok}/8" + ("" if ok >= 8 else "  ⚠️"))
    print("HOÀN THÀNH 🎉" if diem == 8 and ok >= 8 else "Làm tiếp bài chưa đạt nhé.")


if __name__ == "__main__":
    main()
