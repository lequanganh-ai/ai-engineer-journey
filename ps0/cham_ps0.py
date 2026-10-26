"""
MÁY CHẤM · CS50P PROBLEM SET 0 — bạn KHÔNG cần sửa file này.
Đặt file này trong thư mục ps0/ cùng các bài làm, rồi chạy:
    python cham_ps0.py
Bài nào chưa có file thì máy chấm bỏ qua.
"""
import importlib.util
import io
import os
import subprocess
import sys
from contextlib import redirect_stdout

THU_MUC = os.path.dirname(os.path.abspath(__file__))

BAI = [
    ("Bài 1 · Indoor Voice", "indoor.py", [
        (["HELLO"], "hello"),
        (["THIS IS CS50"], "this is cs50"),
        (["50"], "50"),
    ]),
    ("Bài 2 · Playback Speed", "playback.py", [
        (["This is CS50"], "This...is...CS50"),
        (["This is our week on functions"], "This...is...our...week...on...functions"),
        (["Let's implement a function called hello"], "Let's...implement...a...function...called...hello"),
    ]),
    ("Bài 3 · Making Faces", "faces.py", [
        (["Hello :)"], "Hello 🙂"),
        (["Goodbye :("], "Goodbye 🙁"),
        (["Hello :) Goodbye :("], "Hello 🙂 Goodbye 🙁"),
    ]),
    ("Bài 4 · Einstein", "einstein.py", [
        (["1"], "90000000000000000"),
        (["14"], "1260000000000000000"),
        (["50"], "4500000000000000000"),
    ]),
    ("Bài 5 · Tip Calculator", "tip.py", [
        (["$50.00", "15%"], "Leave $7.50"),
        (["$100.00", "18%"], "Leave $18.00"),
        (["$15.00", "25%"], "Leave $3.75"),
    ]),
]

CONVERT = [("Hello :)", "Hello 🙂"), ("Goodbye :(", "Goodbye 🙁"), ("no faces here", "no faces here")]


def chay(file, nhap):
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    try:
        kq = subprocess.run(
            [sys.executable, file], input="\n".join(nhap) + "\n",
            capture_output=True, text=True, encoding="utf-8", timeout=10, cwd=THU_MUC, env=env,
        )
    except subprocess.TimeoutExpired:
        return None, "chương trình chạy quá 10 giây (chờ input thừa? vòng lặp?)"
    if kq.returncode != 0:
        dong = [d for d in kq.stderr.strip().splitlines() if d.strip()]
        return None, dong[-1] if dong else "lỗi không rõ"
    return kq.stdout, None


def cham_convert():
    spec = importlib.util.spec_from_file_location("faces", os.path.join(THU_MUC, "faces.py"))
    mod = importlib.util.module_from_spec(spec)
    import builtins
    goc = builtins.input
    builtins.input = lambda _="": (_ for _ in ()).throw(RuntimeError("main() chạy ngay khi import — thiếu if __name__ == \"__main__\":"))
    try:
        with redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    except Exception as e:
        return f"không import được faces.py → {type(e).__name__}: {e}"
    finally:
        builtins.input = goc
    ham = getattr(mod, "convert", None)
    if ham is None:
        return "chưa thấy hàm convert (đề yêu cầu đúng tên này)"
    for vao, mong in CONVERT:
        buf = io.StringIO()
        with redirect_stdout(buf):
            try:
                kq = ham(vao)
            except Exception as e:
                return f"lỗi khi gọi convert({vao!r}) → {type(e).__name__}: {e}"
        if kq is None and buf.getvalue().strip():
            return "convert dùng print thay vì return"
        if kq != mong:
            return f"convert({vao!r})\n      bạn trả về : {kq!r}\n      cần trả về : {mong!r}"
    return None


def main():
    print("\n===== CS50P · PROBLEM SET 0 =====\n")
    dat = co = 0
    for ten, file, tests in BAI:
        duong = os.path.join(THU_MUC, file)
        if not os.path.exists(duong):
            print(f"⬜ {ten}: chưa có file {file}")
            continue
        co += 1
        loi = None
        for nhap, mong in tests:
            out, err = chay(duong, nhap)
            if err:
                loi = f"khi nhập {nhap} → {err}"
                break
            dong_cuoi = out.rstrip("\n").splitlines()[-1].rstrip() if out.strip() else ""
            if not dong_cuoi.endswith(mong):
                loi = f"khi nhập {nhap}\n      bạn in ra  : {dong_cuoi!r}\n      cần in ra  : {mong!r}"
                break
        if not loi and file == "faces.py":
            loi = cham_convert()
        if not loi:
            soat = open(duong, encoding="utf-8").read()
            canh_bao = "" if any(d.strip() == "# Soát đề: OK" for d in soat.splitlines()) else "   ⚠️  thiếu dòng # Soát đề: OK"
            print(f"✅ {ten}{canh_bao}")
            dat += 1
        else:
            print(f"❌ {ten}: {loi}")
    print(f"\nĐạt {dat}/{co} bài đã làm  ·  tổng Problem Set 0: {dat}/5")


if __name__ == "__main__":
    main()
