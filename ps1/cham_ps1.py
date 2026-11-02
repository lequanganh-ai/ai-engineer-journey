"""MÁY CHẤM · CS50P PROBLEM SET 1. Đặt trong thư mục ps1/ cùng bài làm. Chạy: python cham_ps1.py"""
import os, subprocess, sys

THU_MUC = os.path.dirname(os.path.abspath(__file__))
BAI = [
    ("Bài 1 · Deep Thought", "deep.py", [
        (["42"], "Yes"), (["Forty-Two"], "Yes"), (["  forty two "], "Yes"), (["FORTY TWO"], "Yes"),
        (["50"], "No"), (["forty-three"], "No"), (["42.0"], "No"), ([""], "No")]),
    ("Bài 2 · Home Federal Savings", "bank.py", [
        (["Hello"], "$0"), (["Hello, Newman"], "$0"), (["  HELLO there"], "$0"),
        (["How you doing?"], "$20"), (["hey"], "$20"), (["H"], "$20"),
        (["What's happening?"], "$100"), (["Ahello"], "$100")]),
    ("Bài 3 · File Extensions", "extensions.py", [
        (["happy.jpg"], "image/jpeg"), (["cat.jpeg"], "image/jpeg"), (["  Document.PDF "], "application/pdf"),
        (["notes.txt"], "text/plain"), (["a.gif"], "image/gif"), (["a.PNG"], "image/png"), (["b.zip"], "application/zip"),
        (["program.exe"], "application/octet-stream"), (["README"], "application/octet-stream"),
        (["jpg"], "application/octet-stream")]),
    ("Bài 4 · Math Interpreter", "interpreter.py", [
        (["1 + 1"], "2.0"), (["2 - 3"], "-1.0"), (["2 * 2"], "4.0"), (["50 / 5"], "10.0"), (["7 / 2"], "3.5"), (["10 - 25"], "-15.0")]),
    ("Bài 5 · Meal Time", "meal.py", [
        (["7:00"], "breakfast time"), (["7:30"], "breakfast time"), (["8:00"], "breakfast time"),
        (["12:42"], "lunch time"), (["13:00"], "lunch time"), (["18:32"], "dinner time"), (["19:00"], "dinner time"),
        (["11:11"], ""), (["8:01"], ""), (["6:59"], "")]),
]


def chay(file, nhap):
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    try:
        r = subprocess.run([sys.executable, file], input="\n".join(nhap) + "\n", capture_output=True,
                           text=True, encoding="utf-8", timeout=10, cwd=THU_MUC, env=env)
    except subprocess.TimeoutExpired:
        return None, "chạy quá 10 giây"
    if r.returncode != 0:
        d = [x for x in r.stderr.strip().splitlines() if x.strip()]
        return None, d[-1] if d else "lỗi"
    return r.stdout, None


def khop(dong, mong):
    if not dong.endswith(mong):
        return False
    truoc = dong[:-len(mong)]
    return truoc == "" or truoc[-1] in " ?:"


def cham_convert(duong):
    import importlib.util, io, builtins
    from contextlib import redirect_stdout
    spec = importlib.util.spec_from_file_location("meal", duong)
    mod = importlib.util.module_from_spec(spec)
    goc = builtins.input
    builtins.input = lambda *_: (_ for _ in ()).throw(RuntimeError('main() chạy khi import — thiếu if __name__ == "__main__":'))
    try:
        with redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    except Exception as e:
        return f"không import được meal.py → {e}"
    finally:
        builtins.input = goc
    f = getattr(mod, "convert", None)
    if f is None:
        return "chưa thấy hàm convert (đề bắt buộc)"
    for vao, mong in [("7:30", 7.5), ("7:00", 7.0), ("18:45", 18.75), ("12:06", 12.1)]:
        try:
            kq = f(vao)
        except Exception as e:
            return f"lỗi khi gọi convert({vao!r}) → {e}"
        if not isinstance(kq, (int, float)) or abs(kq - mong) > 1e-9:
            return f"convert({vao!r})\n      bạn trả về : {kq!r}\n      cần trả về : {mong!r}"
    return None


def main():
    print("\n===== CS50P · PROBLEM SET 1 =====\n")
    dat = 0
    for ten, file, tests in BAI:
        duong = os.path.join(THU_MUC, file)
        if not os.path.exists(duong):
            print(f"⬜ {ten}: chưa có file {file}")
            continue
        loi = None
        for nhap, mong in tests:
            out, err = chay(duong, nhap)
            if err:
                loi = f"khi nhập {nhap} → {err}"
                break
            dong = out.rstrip("\n").splitlines()[-1].rstrip() if out.strip() else ""
            if mong == "":
                if dong.endswith("time"):
                    loi = f"khi nhập {nhap!r}: không được in gì, nhưng bạn in {dong!r}"
                    break
                continue
            if not khop(dong, mong):
                loi = f"khi nhập {nhap!r}\n      bạn in ra : {dong!r}\n      cần in ra : {mong!r}"
                break
        if not loi and file == "meal.py":
            loi = cham_convert(duong)
        if loi:
            print(f"❌ {ten}: {loi}")
            continue
        noi = open(duong, encoding="utf-8").read().splitlines()
        canh = []
        if not any(d.strip() == "# Soát đề: OK" for d in noi):
            canh.append("thiếu # Soát đề: OK")
        if not any(d.strip().startswith("# Đã thử thêm:") and d.strip() != "# Đã thử thêm: ..." for d in noi):
            canh.append("thiếu # Đã thử thêm")
        print(f"✅ {ten}" + (f"   ⚠️  {', '.join(canh)}" if canh else ""))
        dat += 1
    print(f"\nĐạt {dat}/{len(BAI)} bài")


if __name__ == "__main__":
    main()
