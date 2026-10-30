"""
MÁY CHẤM · LUYỆN LẠI TUẦN 2 · BUỔI 2 · ĐỀ LẦN 2 — bạn KHÔNG cần sửa file này.
Chạy:  python cham_t2b2_luyen_lai.py
"""
import builtins
import importlib.util
import io
import os
from contextlib import redirect_stdout

FILE = "t2b2_luyen_lai.py"

HAM = [
    ("Bài 1", "chia_ba", [((9,), "Chia hết"), ((0,), "Chia hết"), ((7,), "1"), ((8,), "2"), ((22,), "1")]),
    ("Bài 2", "ten_thang", [((1,), "Tháng Một"), ((2,), "Tháng Hai"), ((3,), "Tháng Ba"), ((4,), "Chưa hỗ trợ"), (("1",), "Chưa hỗ trợ")]),
    ("Bài 3", "phan_hoi", [(("  Hello ",), "Xin chào!"), (("chào",), "Xin chào!"), (("BYE",), "Hẹn gặp lại!"),
                           (("tạm biệt",), "Hẹn gặp lại!"), (("abc",), "Tôi chưa hiểu."), (("",), "Tôi chưa hiểu.")]),
    ("Bài 4", "la_boi_cua_7", [((14,), True), ((15,), False), ((0,), True)]),
    ("Bài 5", "c5_size", [(("s",), "Nhỏ"), (("M",), "Vừa"), (("l",), "Lớn"), (("XL",), "Không có"), (("xxl",), "Không có")]),
    ("Bài 6", "ve_vao_cong", [((20, True), True), ((20, False), False), ((16, True), False), ((18, True), True)]),
]
DOAN = []
MAIN_TESTS = [(["14"], "14 là bội của 7"), (["15"], "15 không là bội của 7"), (["0"], "0 là bội của 7")]


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
        print("⬜ Bài 7: chưa thấy hàm main")
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
            print(f"❌ Bài 7: lỗi khi chạy (nhập {nhap}) → {type(e).__name__}: {e}")
            return 0
        if chuan(buf.getvalue()) != chuan(mong):
            print(f"❌ Bài 7: kết quả chưa đúng (khi nhập {nhap})")
            print("   --- bạn in ra ---")
            print("   " + chuan(buf.getvalue()).replace("\n", "\n   "))
            print("   --- cần in ra ---")
            print("   " + mong.replace("\n", "\n   "))
            return 0
    print("✅ Bài 7")
    return 1


def main():
    if not os.path.exists(FILE):
        print(f"Không thấy {FILE} — đặt 2 file cùng thư mục rồi chạy lại.")
        return
    print(f"\n===== LUYỆN LẠI TUẦN 2 · BUỔI 2 · {FILE} =====\n")
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
    print(f"\nSoát đề: {so_ok}/7 bài đã đánh dấu OK" + ("" if so_ok >= 7 else "  ⚠️  chưa soát đủ — quy tắc mới chưa được làm"))
    print(f"\nĐIỂM: {diem}/7  →  " + ("HOÀN THÀNH 🎉" if diem == 7 else "Làm tiếp bài chưa đạt"))
    print("Chụp toàn bộ kết quả gửi Claude.")


if __name__ == "__main__":
    main()
