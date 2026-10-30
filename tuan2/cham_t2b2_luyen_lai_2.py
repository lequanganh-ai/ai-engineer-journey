"""MÁY CHẤM · LUYỆN LẠI LẦN 2 (tuần 2 buổi 2). Chạy: python cham_t2b2_luyen_lai_2.py"""
import builtins, importlib.util, io, os
from contextlib import redirect_stdout

FILE = "t2b2_luyen_lai_2.py"
HAM = [
    ("Bài 1", "chan_le", [((4,), "Chẵn"), ((0,), "Chẵn"), ((7,), "Lẻ, dư 1"), ((13,), "Lẻ, dư 1"), ((99,), "Lẻ, dư 1")]),
    ("Bài 2", "du_cho_5", [((12,), "2"), ((10,), "0"), ((14,), "4"), ((3,), "3"), ((101,), "1")]),
    ("Bài 3", "muc_do", [(("h",), "Cao"), (("H",), "Cao"), ((" M ",), "Trung bình"), (("m",), "Trung bình"),
                         (("l",), "Thấp"), (("L ",), "Thấp"), (("x",), "Không rõ"), (("",), "Không rõ")]),
    ("Bài 4", "duoc_giam_gia", [((True, 250000), True), ((False, 250000), False), ((True, 100000), False),
                                ((True, 200000), True), ((False, 50000), False)]),
    ("Bài 5", "trang_thai", [((True,), "Đang hoạt động"), ((False,), "Ngoại tuyến")]),
    ("Bài 6a", "la_nam_nhuan", [((2024,), True), ((2023,), False), ((1900,), False), ((2000,), True)]),
]
MAIN = [(["2024"], "2024 là năm nhuận"), (["2023"], "2023 không phải năm nhuận"),
        (["1900"], "1900 không phải năm nhuận"), (["2000"], "2000 là năm nhuận")]


def bang(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return a is b
    return a == b and type(a) == type(b)


def nap():
    spec = importlib.util.spec_from_file_location("bai", FILE)
    mod = importlib.util.module_from_spec(spec)
    goc = builtins.input
    builtins.input = lambda *_: (_ for _ in ()).throw(RuntimeError('thiếu if __name__ == "__main__":'))
    try:
        with redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        builtins.input = goc
    return mod


def main():
    if not os.path.exists(FILE):
        print(f"Không thấy {FILE} — dòng nhắc lệnh có kết thúc bằng \\tuan2> chưa?")
        return
    print(f"\n===== LUYỆN LẠI LẦN 2 · {FILE} =====\n")
    try:
        mod = nap()
    except Exception as e:
        print(f"File có lỗi: {type(e).__name__}: {e}")
        return
    diem = 0
    for nhan, ten, cases in HAM:
        f = getattr(mod, ten, None)
        if f is None:
            print(f"⬜ {nhan}: chưa thấy hàm {ten}")
            continue
        loi = None
        for args, mong in cases:
            try:
                with redirect_stdout(io.StringIO()):
                    kq = f(*args)
            except Exception as e:
                loi = f"lỗi khi gọi {ten}{args} → {type(e).__name__}: {e}"
                break
            if not bang(kq, mong):
                loi = f"gọi {ten}{args}\n      bạn trả về : {kq!r}\n      cần trả về : {mong!r}"
                break
        if loi:
            print(f"❌ {nhan}: {loi}")
        else:
            print(f"✅ {nhan}")
            if nhan != "Bài 6a":
                diem += 1
    m = getattr(mod, "main", None)
    ok6 = m is not None
    if ok6:
        for nhap, mong in MAIN:
            hang = list(nhap)
            mod.input = lambda *_: hang.pop(0)
            buf = io.StringIO()
            try:
                with redirect_stdout(buf):
                    m()
            except Exception as e:
                print(f"❌ Bài 6: lỗi khi nhập {nhap} → {type(e).__name__}: {e}")
                ok6 = False
                break
            if buf.getvalue().strip() != mong:
                print(f"❌ Bài 6: nhập {nhap}\n      bạn in ra : {buf.getvalue().strip()!r}\n      cần in ra : {mong!r}")
                ok6 = False
                break
    else:
        print("⬜ Bài 6: chưa thấy hàm main")
    if ok6:
        print("✅ Bài 6")
        diem += 1
    dong = [d.strip() for d in open(FILE, encoding="utf-8")]
    ok = sum(1 for d in dong if d == "# Soát đề: OK")
    thu = sum(1 for d in dong if d.startswith("# Đã thử thêm:") and d != "# Đã thử thêm: ...")
    print(f"\nĐIỂM: {diem}/6   ·   Soát đề: {ok}/6   ·   Đã thử thêm: {thu}/6")
    print("HOÀN THÀNH 🎉" if diem == 6 and ok == 6 and thu == 6 else "Chưa đạt — chụp toàn bộ kết quả gửi Claude.")


if __name__ == "__main__":
    main()
