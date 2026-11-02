"""MÁY CHẤM · BÀI LUYỆN CA LÀM — không cần sửa file này.  Chạy: python cham_ca_lam.py"""
import builtins, importlib.util, io, os, subprocess, sys
from contextlib import redirect_stdout

THU_MUC = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(THU_MUC, "ca_lam.py")
TESTS = [("6:00", "ca sáng"), ("11:30", "ca sáng"), ("9:15", "ca sáng"), ("11:31", "ngoài giờ làm"),
         ("12:59", "ngoài giờ làm"), ("13:00", "ca chiều"), ("17:30", "ca chiều"), ("17:45", "ngoài giờ làm"),
         ("18:00", "ca tối"), ("22:00", "ca tối"), ("22:01", "ngoài giờ làm"), ("5:59", "ngoài giờ làm")]
CONVERT = [("13:45", 13.75), ("6:00", 6.0), ("22:30", 22.5), ("9:15", 9.25)]


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


def main():
    print("\n===== BÀI LUYỆN · CA LÀM =====\n")
    if not os.path.exists(FILE):
        print("Chưa có file ca_lam.py"); return
    diem = 0
    # 1. hàm convert
    spec = importlib.util.spec_from_file_location("ca_lam", FILE)
    mod = importlib.util.module_from_spec(spec)
    goc = builtins.input
    builtins.input = lambda _="": (_ for _ in ()).throw(RuntimeError("main() chạy ngay khi import — thiếu if __name__"))
    try:
        with redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        ham = getattr(mod, "convert", None)
    except Exception as e:
        ham = None; print(f"❌ không import được: {type(e).__name__}: {e}")
    finally:
        builtins.input = goc
    loi = None
    if ham is None:
        loi = "chưa có hàm convert"
    else:
        for vao, mong in CONVERT:
            buf = io.StringIO()
            try:
                with redirect_stdout(buf):
                    kq = ham(vao)
            except Exception as e:
                loi = f"convert({vao!r}) → {type(e).__name__}: {e}"; break
            if kq is None and buf.getvalue().strip():
                loi = "convert dùng print thay vì return"; break
            if not isinstance(kq, (int, float)) or abs(kq - mong) > 1e-9:
                loi = f"convert({vao!r}) trả về {kq!r}, cần {mong!r}"; break
    tong = 1 + len(TESTS)
    if loi:
        print(f"❌ convert: {loi}")
    else:
        print("✅ convert"); diem += 1
    # 2. chương trình
    for nhap, mong in TESTS:
        out, err = chay(nhap)
        if err:
            print(f"❌ nhập {nhap!r} → {err}"); continue
        if "Mấy giờ rồi? " not in out:
            print(f"❌ nhập {nhap!r} → câu hỏi input không đúng 'Mấy giờ rồi? '"); continue
        cuoi = out.replace("Mấy giờ rồi? ", "").strip()
        if cuoi == mong:
            print(f"✅ {nhap:>5} → {mong}"); diem += 1
        else:
            print(f"❌ {nhap:>5} → bạn in {cuoi!r}, cần {mong!r}")
    noi_dung = open(FILE, encoding="utf-8").read().splitlines()
    soat = any(d.strip() == "# Soát đề: OK" for d in noi_dung)
    thu = [d for d in noi_dung if d.strip().startswith("# Đã thử thêm:") and d.split(":", 1)[1].strip()]
    print(f"\nĐiểm: {diem}/{tong}")
    print("Soát đề: " + ("OK" if soat else "⚠️ chưa có dòng # Soát đề: OK"))
    print("Đã thử thêm: " + (thu[0].split(":", 1)[1].strip() if thu else "⚠️ chưa ghi"))


if __name__ == "__main__":
    main()
