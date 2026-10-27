"""
MÁY CHẤM · BUỔI 5 · TỔNG KẾT TUẦN 1 — bạn KHÔNG cần sửa file này.
Chạy:  python cham_tuan1.py     (đặt cùng thư mục với kiem_tra_tuan1.py và tu_viet.py)
"""
import builtins
import importlib.util
import io
import os
from contextlib import redirect_stdout

PHAN_A = ("kiem_tra_tuan1.py", [
    ("Câu 1", "chuan_hoa_ten", [(("  nguyễn văn an ",), "Nguyễn Văn An"), (("lê bình",), "Lê Bình")]),
    ("Câu 2", "tien_dien", [((100,), 300000), ((50, 2500), 125000)]),
    ("Câu 3", "tong_ba_chuoi", [(("1", "2", "3"), 6), (("10", "0", "5"), 15)]),
    ("Câu 4", "trung_binh", [((8, 7, 9), 8.0), ((7, 8, 8), 7.67), ((1, 2, 2), 1.67)]),
    ("Câu 5", "bang_diem", [(("  lê an ", 7, 8, 8), "Lê An: 7.7 điểm"), (("bình", 9, 9, 9), "Bình: 9.0 điểm")]),
    ("Câu 6", "doi_usd", [(("$12.50",), 12.5), (("$100",), 100.0)]),
    ("Câu 7", "c7_hoa_don", [(("An", 200000), "An: 180,000 đồng"), (("Bình", 50000), "Bình: 45,000 đồng")]),
], [("Câu 8", "cau_8", "ValueError"), ("Câu 9", "cau_9", "14")], ("Câu 10", 2, [
    (["  nguyễn văn an ", "100"], "HÓA ĐƠN TIỀN ĐIỆN\nChủ hộ: Nguyễn Văn An\nSố tiền: 300,000 đồng"),
    (["lê bình", "50"], "HÓA ĐƠN TIỀN ĐIỆN\nChủ hộ: Lê Bình\nSố tiền: 150,000 đồng"),
]))

PHAN_B = ("tu_viet.py", [
    ("tao_hashtag", "tao_hashtag", [(("  hoc python moi ngay ",), "#HocPythonMoiNgay"), (("ai",), "#Ai")]),
], [], ("main()", 1, [
    (["  hoc python moi ngay "], "#HocPythonMoiNgay"),
    (["ai engineer"], "#AiEngineer"),
]))


def bang(kq, mong):
    if isinstance(mong, float) or isinstance(kq, float):
        try:
            return abs(kq - mong) < 1e-6
        except TypeError:
            return False
    return kq == mong and type(kq) == type(mong)


def nap(file):
    spec = importlib.util.spec_from_file_location(file[:-3], file)
    mod = importlib.util.module_from_spec(spec)
    goc = builtins.input

    def cam(_=""):
        raise RuntimeError('file gọi input()/main() ngay khi import — thiếu  if __name__ == "__main__":')
    builtins.input = cam
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


def cham_main(mod, nhan, so_input, tests):
    ham = getattr(mod, "main", None)
    if ham is None:
        print(f"⬜ {nhan}: chưa thấy hàm main")
        return 0
    for nhap, mong in tests:
        hang = list(nhap)

        def input_gia(_=""):
            if not hang:
                raise RuntimeError(f"gọi input() nhiều hơn {so_input} lần")
            return hang.pop(0)
        mod.input = input_gia
        buf = io.StringIO()
        try:
            with redirect_stdout(buf):
                ham()
        except Exception as e:
            print(f"❌ {nhan}: lỗi khi chạy (nhập {nhap}) → {type(e).__name__}: {e}")
            return 0
        if chuan(buf.getvalue()) != chuan(mong):
            print(f"❌ {nhan}: kết quả chưa đúng (khi nhập {nhap})")
            print("   --- bạn in ra ---\n   " + chuan(buf.getvalue()).replace("\n", "\n   "))
            print("   --- cần in ra ---\n   " + mong.replace("\n", "\n   "))
            return 0
    print(f"✅ {nhan}")
    return 1


def cham_phan(ten_phan, cau_hinh):
    file, ham_list, doan_list, (nhan_main, so_input, main_tests) = cau_hinh
    print(f"\n===== {ten_phan} · {file} =====\n")
    if not os.path.exists(file):
        print(f"Không thấy {file} — đặt cùng thư mục rồi chạy lại.")
        return 0, len(ham_list) + len(doan_list) + 1, 0
    try:
        mod = nap(file)
    except Exception as e:
        print(f"File có lỗi, chưa chạy được: {type(e).__name__}: {e}")
        return 0, len(ham_list) + len(doan_list) + 1, 0
    diem = sum(cham_ham(mod, n, t, c) for n, t, c in ham_list)
    for n, bien, da in doan_list:
        tl = str(getattr(mod, bien, "")).strip()
        if not tl:
            print(f"⬜ {n}: chưa điền đáp án")
        elif tl == da:
            diem += 1
            print(f"✅ {n}")
        else:
            print(f"❌ {n}: bạn đoán {tl!r} — chưa đúng")
    diem += cham_main(mod, nhan_main, so_input, main_tests)
    so_ok = sum(1 for d in open(file, encoding="utf-8") if d.strip() == "# Soát đề: OK")
    return diem, len(ham_list) + len(doan_list) + 1, so_ok


def main():
    a, tong_a, ok_a = cham_phan("PHẦN A · KIỂM TRA TỔNG HỢP", PHAN_A)
    print(f"\nPhần A: {a}/{tong_a}   ·   Soát đề: {ok_a}/10" + ("" if ok_a >= 10 else "  ⚠️  chưa soát đủ"))
    b, tong_b, ok_b = cham_phan("PHẦN B · TỰ VIẾT TỪ ĐẦU", PHAN_B)
    print(f"\nPhần B: {b}/{tong_b}   ·   Soát đề: " + ("OK" if ok_b >= 1 else "chưa có  ⚠️"))
    dat = a >= 8 and ok_a >= 10 and b == tong_b and ok_b >= 1
    print("\n" + "=" * 45)
    print("BUỔI 5: " + ("ĐẠT ✅ — hoàn thành TUẦN 1" if dat else "CHƯA ĐẠT (cần A ≥ 8/10, soát đề 10/10, B 2/2 có soát đề)"))
    print("Chụp màn hình kết quả LẦN ĐẦU gửi Claude — chưa sửa gì thêm.")


if __name__ == "__main__":
    main()
