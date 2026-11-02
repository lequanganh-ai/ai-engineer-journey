"""MÁY CHẤM · KIỂM TRA BUỔI 3 (tuần 2). Chạy: python cham_kiem_tra_t2b3.py  (trong tuan2)"""
import builtins, importlib.util, io, os
from contextlib import redirect_stdout

FILE = "kiem_tra_t2b3.py"
HAM = [
    ("Câu 1", "link_an_toan", [(("https://ptit.edu.vn",), True), (("  HTTPS://A.COM ",), True), (("http://abc.com",), False), (("ftp://x",), False)]),
    ("Câu 2", "so_viet_nam", [(("0912345678",), True), (("+84912345678",), True), ((" 0123 ",), True), (("+1555123",), False), (("84912",), False)]),
    ("Câu 3", "la_anh", [(("a.png",), True), (("B.JPEG",), True), (("x.Jpg",), True), (("c.pdf",), False), (("png",), False)]),
    ("Câu 4", "loai_loi_chao", [(("Chào buổi sáng em",), "Buổi sáng"), (("  CHÀO BUỔI SÁNG",), "Buổi sáng"),
                                (("chào bạn",), "Chào thường"), (("Chào",), "Chào thường"), (("hi",), "Không chào"), (("xin chào",), "Không chào")]),
    ("Câu 5", "ngon_ngu", [(("main.py",), "Python"), (("README.MD",), "Markdown"), (("INDEX.HTML",), "Web"),
                           ((" a.htm ",), "Web"), (("data.csv",), "Khác"), (("py",), "Khác")]),
    ("Câu 6", "c6_loai", [(("/help",), "Trợ giúp"), (("/START",), "Trợ giúp"), (("/abc",), "Lệnh"), (("hi",), "Tin thường"), (("help",), "Tin thường")]),
    ("Câu 7", "c7_la_pdf", [(("bao_cao.pdf",), True), (("  A.PDF ",), True), (("a.txt",), False)]),
]
DOAN = [("Câu 8", "cau_8", "False"), ("Câu 9", "cau_9", "True")]
HAM10 = [(("sv@ptit.edu.vn",), True), (("  AN@PTIT.EDU.VN ",), True), (("an@gmail.com",), False), (("ptit.edu.vn@x.com",), False)]
MAIN = [(["sv@ptit.edu.vn"], "Email sinh viên PTIT"), (["an@gmail.com"], "Email ngoài"), (["  B@PTIT.EDU.VN"], "Email sinh viên PTIT")]


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
    print(f"\n===== KIỂM TRA BUỔI 3 · {FILE} =====\n")
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
    loi10 = kiem_ham(mod, "email_ptit", HAM10)
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
