"""MÁY CHẤM · KIỂM TRA BUỔI 2 (tuần 2). Chạy: python cham_kiem_tra_t2b2.py  (trong tuan2)"""
import builtins, importlib.util, io, os
from contextlib import redirect_stdout

FILE = "kiem_tra_t2b2.py"
HAM = [
    ("Câu 1", "la_so_le", [((3,), True), ((10,), False), ((0,), False), ((101,), True)]),
    ("Câu 2", "nhan_xet", [((8,), "Chia hết cho 4"), ((0,), "Chia hết cho 4"), ((10,), "Dư 2"), ((13,), "Dư 1"), ((7,), "Dư 3")]),
    ("Câu 3", "huy_chuong", [((1,), "Vàng"), ((2,), "Bạc"), ((3,), "Đồng"), ((4,), "Không có"), (("1",), "Không có")]),
    ("Câu 4", "den_giao_thong", [((" XANH ",), "Đi"), (("vàng",), "Chậm lại"), (("Cam",), "Chậm lại"),
                                 (("ĐỎ",), "Dừng"), (("tím",), "Không rõ")]),
    ("Câu 5", "duoc_muon", [((True, 2), True), ((True, 0), True), ((True, 3), False), ((False, 0), False)]),
    ("Câu 6", "c6_duoc_vao", [((True, 18), True), ((True, 30), True), ((False, 30), False), ((True, 17), False)]),
    ("Câu 7", "c7_chu_so_cuoi", [((127,), "7"), ((40,), "0"), ((53,), "3"), ((9,), "9")]),
]
DOAN = [("Câu 8", "cau_8", "5"), ("Câu 9", "cau_9", "B")]
HAM10 = [((1,), True), ((7,), True), ((8,), True), ((12,), True), ((4,), False), ((2,), False), ((11,), False)]
MAIN = [(["7"], "Tháng 7 có 31 ngày"), (["4"], "Tháng 4 không có 31 ngày"), (["12"], "Tháng 12 có 31 ngày"), (["2"], "Tháng 2 không có 31 ngày")]


def bang(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return a is b
    return a == b and type(a) == type(b)


def goi(f, args):
    with redirect_stdout(io.StringIO()):
        return f(*args)


def kiem_ham(mod, ten, cases):
    f = getattr(mod, ten, None)
    if f is None:
        return f"chưa thấy hàm {ten}"
    for args, mong in cases:
        try:
            kq = goi(f, args)
        except Exception as e:
            return f"lỗi khi gọi {ten}{args} → {type(e).__name__}: {e}"
        if not bang(kq, mong):
            return f"gọi {ten}{args}\n      bạn trả về : {kq!r}\n      cần trả về : {mong!r}"
    return None


def main():
    if not os.path.exists(FILE):
        print(f"Không thấy {FILE} — dòng nhắc lệnh có kết thúc bằng \\tuan2> chưa?")
        return
    print(f"\n===== KIỂM TRA BUỔI 2 · {FILE} =====\n")
    spec = importlib.util.spec_from_file_location("bai", FILE)
    mod = importlib.util.module_from_spec(spec)
    goc = builtins.input
    builtins.input = lambda *_: (_ for _ in ()).throw(RuntimeError('thiếu if __name__ == "__main__":'))
    try:
        with redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    except Exception as e:
        print(f"File có lỗi: {type(e).__name__}: {e}")
        return
    finally:
        builtins.input = goc
    diem = 0
    for nhan, ten, cases in HAM:
        loi = kiem_ham(mod, ten, cases)
        print(f"❌ {nhan}: {loi}" if loi else f"✅ {nhan}")
        diem += 0 if loi else 1
    for nhan, bien, da in DOAN:
        tl = str(getattr(mod, bien, "")).strip().strip('"')
        if tl == da:
            diem += 1
            print(f"✅ {nhan}")
        else:
            print(f"❌ {nhan}: bạn đoán {tl!r}" if tl else f"⬜ {nhan}: chưa điền")
    loi10 = kiem_ham(mod, "co_31_ngay", HAM10)
    m = getattr(mod, "main", None)
    if loi10:
        print(f"❌ Câu 10: {loi10}")
    elif m is None:
        print("⬜ Câu 10: chưa thấy hàm main")
    else:
        ok = True
        for nhap, mong in MAIN:
            hang = list(nhap)
            mod.input = lambda *_: hang.pop(0)
            buf = io.StringIO()
            try:
                with redirect_stdout(buf):
                    m()
            except Exception as e:
                print(f"❌ Câu 10: nhập {nhap} → {type(e).__name__}: {e}")
                ok = False
                break
            if buf.getvalue().strip() != mong:
                print(f"❌ Câu 10: nhập {nhap}\n      bạn in ra : {buf.getvalue().strip()!r}\n      cần in ra : {mong!r}")
                ok = False
                break
        if ok:
            diem += 1
            print("✅ Câu 10")
    dong = [d.strip() for d in open(FILE, encoding="utf-8")]
    ok_sd = sum(1 for d in dong if d == "# Soát đề: OK")
    thu = sum(1 for d in dong if d.startswith("# Đã thử thêm:") and d != "# Đã thử thêm: ...")
    print(f"\nĐIỂM: {diem}/10   ·   Soát đề: {ok_sd}/10   ·   Đã thử thêm: {thu}/8")
    print("ĐẠT ✅" if diem >= 8 and ok_sd == 10 and thu == 8 else "CHƯA ĐẠT (cần ≥ 8/10, soát đề 10/10, đã thử thêm 8/8)")
    print("Chụp kết quả LẦN ĐẦU gửi Claude.")


if __name__ == "__main__":
    main()
