"""
MÁY CHẤM · BÀI TẬP TUẦN 2 · BUỔI 2 · ĐỀ LẦN 2 — bạn KHÔNG cần sửa file này.
Chạy:  python cham_t2b2.py
"""
import builtins
import importlib.util
import io
import os
from contextlib import redirect_stdout

FILE = "t2b2_bai_tap.py"

HAM = [
    ("Bài 1", "la_so_chan", [((4,), True), ((7,), False), ((0,), True), ((-3,), False)]),
    ("Bài 2", "chia_het", [((10, 5), True), ((10, 3), False), ((9, 3), True)]),
    ("Bài 3", "so_du", [((17, 5), 2), ((10, 2), 0), ((4, 7), 4)]),
    ("Bài 4", "fizz", [((15,), "FizzBuzz"), ((30,), "FizzBuzz"), ((9,), "Fizz"), ((10,), "Buzz"), ((7,), "7")]),
    ("Bài 5", "nam_nhuan", [((2024,), True), ((2023,), False), ((1900,), False), ((2000,), True)]),
    ("Bài 6", "ten_thu", [((2,), "Thứ Hai"), ((4,), "Thứ Tư"), ((7,), "Thứ Bảy"), ((8,), "Chủ nhật"), ((9,), "Không hợp lệ"), ((1,), "Không hợp lệ")]),
    ("Bài 7", "loai_qua", [(("  Cam ",), "Họ cam quýt"), (("bưởi",), "Họ cam quýt"), (("lê",), "Họ hoa hồng"), (("TÁO",), "Họ hoa hồng"), (("dưa",), "Không rõ")]),
    ("Bài 8", "c8_la_so_le", [((7,), True), ((4,), False)]),
    ("Bài 9", "c9_mau", [(("đỏ",), "Dừng"), (("xanh",), "Đi"), (("vàng",), "Chậm lại"), (("tím",), "?")]),
]
DOAN = [("Bài 10", "cau_10", "3")]
MAIN_TESTS = [(["8"], "8 là số chẵn"), (["7"], "7 là số lẻ"), (["0"], "0 là số chẵn")]


def bang(kq, mong):
    if isinstance(mong, float) or isinstance(kq, float):
        try:
            return abs(kq - mong) < 1e-6
        except TypeError:
            return False
    if isinstance(mong, bool) or isinstance(kq, bool):
        return kq is mong
    return kq == mong and type(kq) == type(mong)


def input_cam(_=""):
    raise RuntimeError("file gọi input()/main() ngay khi import — thiếu  if __name__ == \"__main__\":")


def nap():
    spec = importlib.util.spec_from_file_location("bai_lam", FILE)
    mod = importlib.util.module_from_spec(spec)
    goc = builtins.input
    builtins.input = input_cam
    try:
        with redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        builtins.input = goc
    return mod


def cham_ham(mod, nhan, ten, cases):
    ham = getattr(mod, ten, None)
    if ham is None:
        print(f"⬜ {nhan}: chưa thấy hàm {ten} (đặt đúng tên chưa?)")
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
        print("⬜ Bài 11: chưa thấy hàm main")
        return 0
    for nhap, mong in MAIN_TESTS:
        hang = list(nhap)

        def input_gia(_=""):
            if not hang:
                raise RuntimeError("gọi input() nhiều hơn số lần đề yêu cầu")
            return hang.pop(0)

        mod.input = input_gia
        buf = io.StringIO()
        try:
            with redirect_stdout(buf):
                ham()
        except Exception as e:
            print(f"❌ Bài 11: lỗi khi chạy (nhập {nhap}) → {type(e).__name__}: {e}")
            return 0
        if chuan(buf.getvalue()) != chuan(mong):
            print(f"❌ Bài 11: kết quả chưa đúng (khi nhập {nhap})")
            print("   --- bạn in ra ---")
            print("   " + chuan(buf.getvalue()).replace("\n", "\n   "))
            print("   --- cần in ra ---")
            print("   " + mong.replace("\n", "\n   "))
            return 0
    print("✅ Bài 11")
    return 1


def main():
    if not os.path.exists(FILE):
        print(f"Không thấy {FILE} — đặt 2 file cùng thư mục rồi chạy lại.")
        return
    print(f"\n===== BÀI TẬP TUẦN 2 · BUỔI 2 · {FILE} =====\n")
    try:
        mod = nap()
    except Exception as e:
        print(f"File có lỗi, chưa chạy được: {type(e).__name__}: {e}")
        print("Đọc số dòng (line) trong thông báo để tìm chỗ sai.")
        return
    diem = sum(cham_ham(mod, n, t, c) for n, t, c in HAM)
    for n, bien, da in DOAN:
        tl = str(getattr(mod, bien, "")).strip()
        if not tl:
            print(f"⬜ {n}: chưa điền đáp án")
        elif tl == da:
            diem += 1
            print(f"✅ {n}")
        else:
            print(f"❌ {n}: bạn đoán {tl!r} — chưa đúng")
    diem += cham_main(mod)
    so_ok = sum(1 for d in open(FILE, encoding="utf-8") if d.strip() == "# Soát đề: OK")
    print(f"\nSoát đề: {so_ok}/11 bài đã đánh dấu OK" + ("" if so_ok >= 11 else "  ⚠️  chưa soát đủ — quy tắc mới chưa được làm"))
    print(f"\nĐIỂM: {diem}/11  →  " + ("HOÀN THÀNH 🎉" if diem == 11 else "Làm tiếp bài chưa đạt"))
    print("Chụp toàn bộ kết quả gửi Claude.")


if __name__ == "__main__":
    main()
