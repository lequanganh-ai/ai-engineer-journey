"""
MÁY CHẤM BUỔI 2 — bạn KHÔNG cần sửa file này.
Chạy:  python buoi02_cham_diem.py
       python buoi02_cham_diem.py buoi02_loi_giai.py   (chấm file khác)
"""
import importlib.util
import io
import sys
from contextlib import redirect_stdout

# (tên hàm, [(đối số, kết quả mong đợi), ...])
TESTS = [
    ("bai_01_chao", [(("Lan",), "Xin chào, Lan!"), (("Quang Anh",), "Xin chào, Quang Anh!")]),
    ("bai_02_binh_phuong", [((4,), 16), ((0,), 0), ((-3,), 9)]),
    ("bai_03_tong", [((3, 5), 8), ((-1, 1), 0), ((2.5, 0.5), 3.0)]),
    ("bai_04_cong_hai_chuoi_so", [(("1", "2"), 3), (("10", "25"), 35)]),
    ("bai_05_trung_binh", [((1, 2, 2), 1.67), ((3, 3, 3), 3.0), ((1, 2, 3), 2.0)]),
    ("bai_06_tien_tip", [((50, 15), 7.5), ((100, 10), 10.0), ((33.33, 18), 6.0)]),
    ("bai_07_dinh_dang_tien", [((1500000,), "1,500,000 đồng"), ((999,), "999 đồng")]),
    ("bai_08_lam_sach_ten", [(("   lê quang anh ",), "Lê Quang Anh"), (("NGUYỄN văn an",), "Nguyễn Văn An")]),
    ("bai_09_chao_mac_dinh", [((), "Xin chào, bạn!"), (("Minh",), "Xin chào, Minh!")]),
    ("bai_10_doi_nhiet_do", [((37,), "37°C = 98.6°F"), ((0,), "0°C = 32.0°F"), ((100,), "100°C = 212.0°F")]),
    ("bai_11_tinh_dien_tich", [((5, 3), 15), ((10, 2), 20), ((2.5, 4), 10.0)]),
    ("bai_12_tinh_chu_vi", [((5, 3), 16), ((10, 2), 24), ((1, 1), 4)]),
]


def bang_nhau(kq, mong_doi):
    if isinstance(mong_doi, float) or isinstance(kq, float):
        try:
            return abs(kq - mong_doi) < 1e-6
        except TypeError:
            return False
    return kq == mong_doi and type(kq) == type(mong_doi)


def nap_file(ten_file):
    spec = importlib.util.spec_from_file_location("bai_lam", ten_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ten_file = sys.argv[1] if len(sys.argv) > 1 else "buoi02_bai_tap.py"
    try:
        mod = nap_file(ten_file)
    except FileNotFoundError:
        print(f"Không tìm thấy file {ten_file}. Hãy để các file trong cùng một thư mục.")
        return
    except Exception as e:
        print(f"File {ten_file} có lỗi, chưa chạy được: {type(e).__name__}: {e}")
        print("Đọc số dòng (line) trong thông báo lỗi để tìm chỗ sai nhé.")
        return

    dat = 0
    print(f"\n===== CHẤM BUỔI 2 · {ten_file} =====\n")
    for ten_ham, cases in TESTS:
        so = int(ten_ham.split("_")[1])
        ham = getattr(mod, ten_ham, None)
        if ham is None:
            print(f"⚠️  Bài {so}: không thấy hàm {ten_ham} — đừng đổi tên hàm nhé.")
            continue
        loi = None
        chua_lam = False
        for args, mong_doi in cases:
            bo_dem = io.StringIO()
            try:
                with redirect_stdout(bo_dem):
                    kq = ham(*args)
            except Exception as e:
                loi = f"code bị lỗi khi gọi {ten_ham}{args} → {type(e).__name__}: {e}"
                break
            if kq is None:
                if bo_dem.getvalue().strip():
                    loi = ("hàm đang dùng print() để in ra, nhưng cần dùng return để TRẢ kết quả về.\n"
                           f"      bạn in ra: {bo_dem.getvalue().strip()!r}")
                else:
                    chua_lam = True
                break
            if not bang_nhau(kq, mong_doi):
                loi = (f"gọi {ten_ham}{args}\n"
                       f"      bạn trả về : {kq!r}\n"
                       f"      cần trả về : {mong_doi!r}")
                break
        if chua_lam:
            print(f"⬜ Bài {so}: chưa làm")
        elif loi:
            print(f"❌ Bài {so}: {loi}")
        else:
            dat += 1
            print(f"✅ Bài {so}")

    print(f"\nĐiểm: {dat}/{len(TESTS)}")
    if dat == len(TESTS):
        print("Xuất sắc! Đừng quên làm Phần E (hàm main) rồi commit lên GitHub nhé.")
    elif dat >= 10:
        print("Rất tốt! Còn chút nữa thôi.")
    else:
        print("Làm tiếp bài chưa đạt. So sánh kỹ 'bạn trả về' và 'cần trả về'.")


if __name__ == "__main__":
    main()
