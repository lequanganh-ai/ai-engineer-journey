"""
MÁY CHẤM BUỔI 1 — bạn KHÔNG cần sửa file này.
Chạy:  python buoi01_cham_diem.py
       python buoi01_cham_diem.py buoi01_loi_giai.py   (chấm file khác, ví dụ lời giải)
"""
import io
import re
import sys
from contextlib import redirect_stdout

# (số bài, danh sách dữ liệu nhập giả lập, kết quả mong đợi)
TESTS = {
    1: [([], "Xin chào, thế giới!")],
    2: [([], "Tôi đang học Python.\nMục tiêu: trở thành AI Engineer.\nBắt đầu: 06/10/2026")],
    3: [([], "Tôi học Python qua khóa CS50P.")],
    4: [(["Lan"], "Xin chào, Lan!"), (["Quang Anh"], "Xin chào, Quang Anh!")],
    5: [(["Lan", "Bắc Ninh"], "Lan đến từ Bắc Ninh."), (["Minh", "Huế"], "Minh đến từ Huế.")],
    6: [([], "2026-10-06")],
    7: [([], "bún chả\nphở")],
    8: [(["phở"], "Món yêu thích của tôi là phở."), (["bánh mì"], "Món yêu thích của tôi là bánh mì.")],
    9: [(["   lê quang anh  "], "Xin chào, Lê Quang Anh"), (["nguyễn văn an"], "Xin chào, Nguyễn Văn An")],
    10: [(["Lan"], "====================\nHọc viên: Lan\n===================="),
         (["Quang Anh"], "====================\nHọc viên: Quang Anh\n====================")],
}


def tach_bai(ma_nguon):
    """Tách file bài làm thành từng đoạn theo dòng '# ===== BÀI N'."""
    phan = re.split(r"^# ===== BÀI (\d+).*$", ma_nguon, flags=re.M)
    bai = {}
    for i in range(1, len(phan) - 1, 2):
        bai[int(phan[i])] = phan[i + 1]
    return bai


def co_code(doan):
    for dong in doan.splitlines():
        if dong.strip() and not dong.strip().startswith("#"):
            return True
    return False


def chay(doan, du_lieu_nhap):
    hang_doi = list(du_lieu_nhap)

    def input_gia(loi_nhac=""):
        if not hang_doi:
            raise RuntimeError("chương trình gọi input() nhiều hơn đề bài yêu cầu")
        return hang_doi.pop(0)  # lời nhắc không in ra để dễ so sánh kết quả

    bo_dem = io.StringIO()
    with redirect_stdout(bo_dem):
        exec(doan, {"input": input_gia, "__name__": "__bai__"})
    return bo_dem.getvalue()


def chuan_hoa(s):
    return "\n".join(dong.rstrip() for dong in s.strip().splitlines())


def main():
    ten_file = sys.argv[1] if len(sys.argv) > 1 else "buoi01_bai_tap.py"
    try:
        with open(ten_file, encoding="utf-8") as f:
            bai = tach_bai(f.read())
    except FileNotFoundError:
        print(f"Không tìm thấy file {ten_file}. Hãy để 2 file trong cùng một thư mục.")
        return

    dat = 0
    print(f"\n===== CHẤM BUỔI 1 · {ten_file} =====\n")
    for so, cases in TESTS.items():
        doan = bai.get(so)
        if doan is None:
            print(f"⚠️  Bài {so}: không thấy dòng '# ===== BÀI {so}' — đừng xóa dòng đó nhé.")
            continue
        if not co_code(doan):
            print(f"⬜ Bài {so}: chưa làm")
            continue
        loi = None
        for nhap, mong_doi in cases:
            try:
                ra = chay(doan, nhap)
            except Exception as e:
                loi = f"code bị lỗi → {type(e).__name__}: {e}"
                break
            if chuan_hoa(ra) != chuan_hoa(mong_doi):
                nhap_txt = f" (khi nhập {nhap})" if nhap else ""
                loi = (f"kết quả chưa đúng{nhap_txt}\n"
                       f"      bạn in ra : {chuan_hoa(ra)!r}\n"
                       f"      cần in ra : {chuan_hoa(mong_doi)!r}")
                break
        if loi:
            print(f"❌ Bài {so}: {loi}")
        else:
            dat += 1
            print(f"✅ Bài {so}")

    print(f"\nĐiểm: {dat}/{len(TESTS)}")
    if dat == len(TESTS):
        print("Xuất sắc! Commit bài làm lên GitHub nhé.")
    elif dat >= 9:
        print("Rất tốt! Bài 10 là thử thách, thử thêm nhé.")
    else:
        print("Làm tiếp bài chưa đạt. Đọc kỹ dòng 'cần in ra' để so sánh từng ký tự.")


if __name__ == "__main__":
    main()
