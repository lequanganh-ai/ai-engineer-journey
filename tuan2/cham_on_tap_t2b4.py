"""MÁY CHẤM · ÔN TẬP TUẦN 2 BUỔI 4 — không cần sửa file này.  Chạy: python cham_on_tap_t2b4.py"""
import builtins, importlib.util, io, os, re, subprocess, sys
from contextlib import redirect_stdout

THU_MUC = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(THU_MUC, "on_tap_t2b4.py")

CAU = [
    ("Câu 1 · doi_phut", "doi_phut", [("1:45", 105), ("0:30", 30), ("2:00", 120), ("10:05", 605), ("3:59", 239)], int),
    ("Câu 2 · doi_gio", "doi_gio", [("9:45", 9.75), ("14:30", 14.5), ("6:00", 6.0), ("23:15", 23.25), ("0:06", 0.1)], float),
    ("Câu 3 · tinh", "tinh", [("6 * 7", 42.0), ("9 / 2", 4.5), ("3 - 10", -7.0), ("5 % 2", None),
                             ("12 + 8", 20.0), ("100 / 8", 12.5), ("2 ^ 3", None)], float),
    ("Câu 4 · dinh_dang", "dinh_dang", [(42, "42.0"), (4.567, "4.6"), (0, "0.0"), (-2.25, "-2.2"), (7.05, "7.0")], str),
    ("Câu 5 · ca_hoc", "ca_hoc", [(7.0, "sáng"), (11.5, "sáng"), (12.0, "nghỉ"), (16.75, "chiều"), (13.0, "chiều"),
                                  (6.99, "nghỉ"), (11.51, "nghỉ"), (16.76, "nghỉ"), (9.0, "sáng"), (20.0, "nghỉ")], str),
    ("Câu 6 · sửa lỗi gio_ra_so", "gio_ra_so", [("8:15", 8.25), ("10:30", 10.5), ("0:45", 0.75), ("21:00", 21.0)], float),
]
CHUONG_TRINH = [("9:45", "Ca sáng"), ("12:10", "Ca nghỉ"), ("13:00", "Ca chiều"), ("11:30", "Ca sáng"),
                ("16:46", "Ca nghỉ"), ("7:00", "Ca sáng"), ("15:20", "Ca chiều")]


def nap():
    spec = importlib.util.spec_from_file_location("on_tap", FILE)
    mod = importlib.util.module_from_spec(spec)
    goc = builtins.input
    builtins.input = lambda _="": (_ for _ in ()).throw(RuntimeError("main() chạy ngay khi import — thiếu if __name__"))
    try:
        with redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        return mod, None
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"
    finally:
        builtins.input = goc


def bang(kq, mong):
    if mong is None:
        return kq is None
    if isinstance(mong, str):
        return kq == mong
    return isinstance(kq, (int, float)) and not isinstance(kq, bool) and abs(kq - mong) < 1e-9


def cham_ham(mod, ten_ham, tests, kieu):
    ham = getattr(mod, ten_ham, None)
    if ham is None:
        return f"chưa có hàm {ten_ham}"
    for vao, mong in tests:
        buf = io.StringIO()
        try:
            with redirect_stdout(buf):
                kq = ham(vao)
        except Exception as e:
            return f"{ten_ham}({vao!r}) → {type(e).__name__}: {e}"
        if kq is None and buf.getvalue().strip() and mong is not None:
            return f"{ten_ham} dùng print thay vì return"
        if not bang(kq, mong):
            return f"{ten_ham}({vao!r})\n      bạn trả về : {kq!r}\n      cần trả về : {mong!r}"
        if mong is not None and kieu is int and not isinstance(kq, int):
            return f"{ten_ham}({vao!r}) trả về {kq!r} — đề cần SỐ NGUYÊN"
        if mong is not None and kieu is float and ten_ham == "tinh" and not isinstance(kq, float):
            return f"tinh({vao!r}) trả về {kq!r} (int) — đề cần SỐ THỰC, ví dụ 42.0"
    return None


def chay(nhap):
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    try:
        kq = subprocess.run([sys.executable, FILE], input=nhap + "\n", capture_output=True,
                            text=True, encoding="utf-8", timeout=10, cwd=THU_MUC, env=env)
    except subprocess.TimeoutExpired:
        return None, "chạy quá 10 giây"
    if kq.returncode != 0:
        d = [x for x in kq.stderr.strip().splitlines() if x.strip()]
        return None, d[-1] if d else "lỗi không rõ"
    return kq.stdout, None


def dem_soat(noi_dung):
    """Đếm số câu có # Soát đề: OK và # Đã thử thêm có nội dung, theo từng khối CÂU."""
    khoi = re.split(r"\n# CÂU \d", noi_dung)[1:]
    soat = sum(1 for k in khoi if any(d.strip() == "# Soát đề: OK" for d in k.splitlines()))
    thu = sum(1 for k in khoi if any(d.strip().startswith("# Đã thử thêm:") and d.split(":", 1)[1].strip()
                                     and "<" not in d for d in k.splitlines()))
    return soat, thu, len(khoi)


def main():
    print("\n===== ÔN TẬP · TUẦN 2 BUỔI 4 =====\n")
    if not os.path.exists(FILE):
        print("Chưa có file on_tap_t2b4.py"); return
    mod, loi_nap = nap()
    if loi_nap:
        print(f"❌ Không chạy được file → {loi_nap}\n   (đọc traceback: python on_tap_t2b4.py)"); return
    diem = 0
    for ten, ham, tests, kieu in CAU:
        loi = cham_ham(mod, ham, tests, kieu)
        if loi:
            print(f"❌ {ten}: {loi}")
        else:
            print(f"✅ {ten}"); diem += 1
    # câu 6 phải có dòng "# Lỗi:"
    noi_dung = open(FILE, encoding="utf-8").read()
    # câu 7
    loi7 = None
    if "def main" not in noi_dung:
        loi7 = "chưa có main"
    for nhap, mong in CHUONG_TRINH:
        if loi7:
            break
        out, err = chay(nhap)
        if err:
            loi7 = f"nhập {nhap!r} → {err}"; break
        if "Giờ vào lớp? " not in out:
            loi7 = f"câu hỏi input phải đúng y 'Giờ vào lớp? '  (bạn in: {out.splitlines()[0] if out else ''!r})"; break
        cuoi = out.replace("Giờ vào lớp? ", "").strip()
        if cuoi != mong:
            loi7 = f"nhập {nhap!r}\n      bạn in : {cuoi!r}\n      cần in : {mong!r}"; break
    if not loi7:
        than_main = noi_dung.split("def main", 1)[1]
        if "doi_gio(" not in than_main or "ca_hoc(" not in than_main:
            loi7 = "main phải GỌI doi_gio và ca_hoc (không viết lại)"
    if loi7:
        print(f"❌ Câu 7 · chương trình: {loi7}")
    else:
        print("✅ Câu 7 · chương trình"); diem += 1

    print(f"\nĐiểm: {diem}/7")
    soat, thu, tong = dem_soat(noi_dung)
    print(f"Soát đề: {soat}/{tong} câu   ·   Đã thử thêm: {thu}/{tong} câu")
    if "# Lỗi:" not in noi_dung:
        print("⚠️  Câu 6 chưa có dòng '# Lỗi: ...' giải thích")
    print("\nNhắc: 'Đã thử thêm' phải là giá trị KHÔNG có trong đề, kết quả COPY từ màn hình.")


if __name__ == "__main__":
    main()
