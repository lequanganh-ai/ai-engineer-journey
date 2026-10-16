"""
MÁY CHẤM ÔN TẬP BUỔI 1 — bạn KHÔNG cần sửa file này.
Chạy:  python on_tap_cham_diem.py
"""
import io
import re
import sys
from contextlib import redirect_stdout

# Câu 1–6: (dữ liệu nhập giả lập, kết quả mong đợi)
CHAY = {
    1: [([], "Python là ngôn ngữ đầu tiên của tôi.")],
    2: [(["20"], "Bạn 20 tuổi."), (["35"], "Bạn 35 tuổi.")],
    3: [([], "Python-AI")],
    4: [(["   hà nội  "], "Tôi sống ở Hà Nội."), (["hồ chí minh"], "Tôi sống ở Hồ Chí Minh.")],
    5: [(["3", "4"], "Tổng: 7"), (["10", "25"], "Tổng: 35")],
    6: [(["12.5", "3"], "Thành tiền: 37.50"), (["9.99", "2"], "Thành tiền: 19.98")],
}
# Câu 7–9: (tên biến, đáp án)
DOAN = {7: ("cau_7", "53"), 8: ("cau_8", "abc"), 9: ("cau_9", "[AN]")}


def tach(ma):
    phan = re.split(r"^# ===== CÂU (\d+).*$", ma, flags=re.M)
    return {int(phan[i]): phan[i + 1] for i in range(1, len(phan) - 1, 2)}


def co_code(doan):
    return any(d.strip() and not d.strip().startswith("#") for d in doan.splitlines())


def chay(doan, nhap):
    hang = list(nhap)

    def input_gia(_=""):
        if not hang:
            raise RuntimeError("gọi input() nhiều hơn đề bài yêu cầu")
        return hang.pop(0)

    buf = io.StringIO()
    ns = {"input": input_gia, "__name__": "__bai__"}
    with redirect_stdout(buf):
        exec(doan, ns)
    return buf.getvalue(), ns


def chuan(s):
    return "\n".join(d.rstrip() for d in s.strip().splitlines())


def main():
    ten = sys.argv[1] if len(sys.argv) > 1 else "on_tap_buoi01.py"
    try:
        with open(ten, encoding="utf-8") as f:
            bai = tach(f.read())
    except FileNotFoundError:
        print(f"Không tìm thấy {ten}. Để 2 file trong cùng thư mục nhé.")
        return

    dat = 0
    print(f"\n===== ÔN TẬP BUỔI 1 · {ten} =====\n")
    for so in range(1, 10):
        doan = bai.get(so)
        if doan is None:
            print(f"⚠️  Câu {so}: không thấy dòng '# ===== CÂU {so}'")
            continue
        if so in CHAY:
            if not co_code(doan):
                print(f"⬜ Câu {so}: chưa làm")
                continue
            loi = None
            for nhap, mong in CHAY[so]:
                try:
                    ra, _ = chay(doan, nhap)
                except Exception as e:
                    loi = f"code bị lỗi → {type(e).__name__}: {e}"
                    break
                if chuan(ra) != chuan(mong):
                    them = f" (khi nhập {nhap})" if nhap else ""
                    loi = (f"kết quả chưa đúng{them}\n"
                           f"      bạn in ra : {chuan(ra)!r}\n"
                           f"      cần in ra : {mong!r}")
                    break
        else:
            bien, dap_an = DOAN[so]
            try:
                _, ns = chay(doan, [])
            except Exception as e:
                print(f"❌ Câu {so}: lỗi → {type(e).__name__}: {e}")
                continue
            tra_loi = str(ns.get(bien, "")).strip()
            if not tra_loi:
                print(f"⬜ Câu {so}: chưa điền đáp án")
                continue
            # Không in đáp án đúng ở phần đoán, để bạn tự suy nghĩ lại
            loi = None if tra_loi == dap_an else f"bạn đoán {tra_loi!r} — chưa đúng, thử chạy đoạn code đó để xem vì sao"
        if loi:
            print(f"❌ Câu {so}: {loi}")
        else:
            dat += 1
            print(f"✅ Câu {so}")

    print(f"\nĐiểm: {dat}/9")
    if dat >= 7:
        print("Đạt! Bạn đã nắm chắc buổi 1 → vào buổi 2 thôi.")
    else:
        print("Chưa đạt 7/9. Gửi kết quả cho Claude để ôn lại phần còn yếu nhé.")


if __name__ == "__main__":
    main()
