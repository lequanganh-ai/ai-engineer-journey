"""
MÁY CHẤM · BÀI KIỂM TRA CUỐI BUỔI 1 + 2 — bạn KHÔNG cần sửa file này.
Chạy:  python cham_kiem_tra_cuoi.py
"""
import builtins
import importlib.util
import io
import os
from contextlib import redirect_stdout

FILE = "kiem_tra_cuoi_buoi1_2.py"

HAM = [
    ("Câu 1", "lam_sach_ma", [(("  ab12x ",), "AB12X"), (("sp-09",), "SP-09")]),
    ("Câu 2", "tien_phong", [((2,), 1000000), ((3, 400000), 1200000)]),
    ("Câu 3", "tong_chuoi", [(("12", "8"), 20), (("0", "35"), 35)]),
    ("Câu 4", "diem_tb", [((7, 8, 8), 7.7), ((9, 9, 9), 9.0), ((5, 6, 6), 5.7)]),
    ("Câu 5", "the_sach", [(("  nha gia kim ", 79000), "Nha Gia Kim: 79,000 đồng"),
                           (("đắc nhân tâm", 1250000), "Đắc Nhân Tâm: 1,250,000 đồng")]),
    ("Câu 6", "ket_qua", [(("An", 7, 8, 8), "An: 7.70"), (("Bình", 9, 9, 9), "Bình: 9.00")]),
    ("Câu 7", "c7_tong_tien", [((3,), 150000), ((0,), 0)]),
]
DOAN = [("Câu 8", "cau_8", "8"), ("Câu 9", "cau_9", "None")]
MAIN_TESTS = [
    (["  nha gia kim ", "2", "79000"],
     "--- PHIẾU MUA SÁCH ---\nSách: Nha Gia Kim\nSố cuốn: 2\nTổng: 158,000 đồng\n----------------------"),
    (["dac nhan tam", "1", "86000"],
     "--- PHIẾU MUA SÁCH ---\nSách: Dac Nhan Tam\nSố cuốn: 1\nTổng: 86,000 đồng\n----------------------"),
]


def bang(kq, mong):
    if isinstance(mong, float) or isinstance(kq, float):
        try:
            return abs(kq - mong) < 1e-6
        except TypeError:
            return False
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
        print("⬜ Câu 10: chưa thấy hàm main")
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
            print(f"❌ Câu 10: lỗi khi chạy (nhập {nhap}) → {type(e).__name__}: {e}")
            return 0
        if chuan(buf.getvalue()) != chuan(mong):
            print(f"❌ Câu 10: kết quả chưa đúng (khi nhập {nhap})")
            print("   --- bạn in ra ---")
            print("   " + chuan(buf.getvalue()).replace("\n", "\n   "))
            print("   --- cần in ra ---")
            print("   " + mong.replace("\n", "\n   "))
            return 0
    print("✅ Câu 10")
    return 1


def main():
    if not os.path.exists(FILE):
        print(f"Không thấy {FILE} — đặt 2 file cùng thư mục rồi chạy lại.")
        return
    print(f"\n===== KIỂM TRA CUỐI BUỔI 1 + 2 · {FILE} =====\n")
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
    print(f"\nĐIỂM: {diem}/10  →  " + ("ĐẠT ✅ (mục tiêu ≥ 8)" if diem >= 8 else "CHƯA ĐẠT (mục tiêu ≥ 8)"))
    print("Chụp màn hình kết quả LẦN ĐẦU gửi Claude — chưa sửa gì thêm.")


if __name__ == "__main__":
    main()
