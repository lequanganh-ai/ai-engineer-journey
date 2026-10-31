# =================================================================
# BUỔI 3 · KIỂM TRA BUỔI 2 (%, hàm bool, match)
# Mục tiêu: ≥ 8/10 NGAY LẦN ĐẦU · Soát đề 10/10 · Đã thử thêm 8/8
# =================================================================
# KHÔNG mở ghi chú, KHÔNG hỏi gợi ý, KHÔNG dùng AI gợi ý code.
# Câu 1–7 và 10: thêm dòng  # Đã thử thêm: <giá trị ĐỀ KHÔNG CHO> → <kết quả chạy THẬT>
# Viết CHÍNH XÁC:  # Soát đề: OK      Chấm 1 LẦN:  python cham_kiem_tra_t2b2.py  (trong tuan2)
# =================================================================


# CÂU 1
# Viết hàm  la_so_le(n)  — 1 dòng return, KHÔNG dùng if.
#   la_so_le(3) → True    la_so_le(10) → False
# Soát đề: OK
# Đã thử thêm: <3> - <True>
# Viết code dưới đây:
def la_so_le(n):
    return n % 2 != 0




# CÂU 2
# Viết hàm  nhan_xet(n):
#   chia hết cho 4 → "Chia hết cho 4"
#   còn lại        → "Dư " + số dư khi chia cho 4      (n = 10 → "Dư 2")
#   nhan_xet(8) → "Chia hết cho 4"    nhan_xet(10) → "Dư 2"
# Soát đề: OK
# Đã thử thêm: <8> -> <Chia hết cho 4>
# Viết code dưới đây:
def nhan_xet(n):
    if n % 4 == 0:
        return "Chia hết cho 4"
    else:
        return f"Dư {n % 4}"




# CÂU 3
# Viết hàm  huy_chuong(hang)  dùng match. hang là SỐ.
#   1 → "Vàng"   2 → "Bạc"   3 → "Đồng"   khác → "Không có"
#   huy_chuong(1) → "Vàng"    huy_chuong(3) → "Đồng"    huy_chuong(4) → "Không có"
# Soát đề: OK
# Đã thử thêm: <1> - <Vàng>
# Viết code dưới đây:
def huy_chuong(hang):
    match hang:
        case 1:
            return "Vàng"
        case 2:
            return "Bạc"
        case 3:
            return "Đồng"
        case _:
            return "Không có"





# CÂU 4
# Viết hàm  den_giao_thong(mau)  dùng match. Người dùng có thể nhập hoa/thường, dư khoảng trắng.
#   "xanh" → "Đi"    "vàng" hoặc "cam" → "Chậm lại"    "đỏ" → "Dừng"    khác → "Không rõ"
#   den_giao_thong(" XANH ") → "Đi"    den_giao_thong("cam") → "Chậm lại"    den_giao_thong("tím") → "Không rõ"
# Soát đề: OK
# Đã thử thêm: <Xanh> -> <Đi>
# Viết code dưới đây:
def den_giao_thong(mau):
    mau = mau.strip().lower()
    match mau:
        case "xanh":
            return "Đi"
        case "vàng" | "cam":
            return "Chậm lại"
        case "đỏ":
            return "Dừng"
        case _:
            return "Không rõ"




# CÂU 5
# Viết hàm  duoc_muon(la_sinh_vien, dang_muon)  — la_sinh_vien là True/False, dang_muon là số sách đang mượn.
# Trả về True khi: là sinh viên VÀ đang mượn ít hơn 3 cuốn.   1 dòng return.
#   duoc_muon(True, 2) → True    duoc_muon(True, 3) → False    duoc_muon(False, 0) → False
# Soát đề: OK
# Đã thử thêm: <True, 2) -> True
# Viết code dưới đây:
def duoc_muon(la_sinh_vien, dang_muon):
    return la_sinh_vien and dang_muon < 3



# CÂU 6 · SỬA LỖI (nhiều hơn 1 lỗi)
# Quy tắc: được vào khi co_the là True VÀ tuổi từ 18 trở lên.
# Đúng phải là:  c6_duoc_vao(True, 18) → True   c6_duoc_vao(True, 30) → True
#                c6_duoc_vao(False, 30) → False c6_duoc_vao(True, 17) → False
# Soát đề: OK
# Đã thử thêm: <True, 18> -> <True>
def c6_duoc_vao(co_the, tuoi):
    return co_the  and tuoi >= 18


# CÂU 7 · SỬA LỖI
# Đúng phải là:  c7_chu_so_cuoi(127) → "7"   c7_chu_so_cuoi(40) → "0"   (chữ số hàng đơn vị, dạng CHUỖI)
# Gợi ý toán: chữ số cuối = số dư khi chia cho 10.
# Soát đề: OK
# Đã thử thêm: <40> -> <0>
def c7_chu_so_cuoi(n):
    if n % 10 == 0:
        return "0"
    else:
        return f"{n % 10}"



# CÂU 8 · ĐOÁN (không chạy thử)
# 29 % 6 bằng bao nhiêu?
# Soát đề: OK
cau_8 = "5"


# CÂU 9 · ĐOÁN (không chạy thử) — đoạn code in ra gì?
#     x = 10
#     match x:
#         case 5:
#             print("A")
#         case 10 | 20:
#             print("B")
#         case _:
#             print("C")
# Soát đề: OK
cau_9 = "B"


# CÂU 10 · CHƯƠNG TRÌNH HOÀN CHỈNH
# Viết hàm  co_31_ngay(thang)  dùng match: tháng 1, 3, 5, 7, 8, 10, 12 → True, còn lại → False.
# Viết hàm  main():
#   - Hỏi:  "Nhập tháng: "  (số NGUYÊN)
#   - GỌI co_31_ngay
#   - In ĐÚNG 1 dòng:  "Tháng 7 có 31 ngày"   hoặc   "Tháng 4 không có 31 ngày"
# Comment ① HỎI / ② XỬ LÝ / ③ IN RA BÊN TRONG main. Cuối file gọi main() đúng chuẩn.
# Soát đề: OK
# Đã thử thêm: <Tháng 7 có 31 ngày>
# Viết code dưới đây:
def co_31_ngay(thang):
    match thang:
        case 1 | 3 | 5| 7| 8 | 10 | 12:
            return True
        case _:
            return False
def main():
    thang = int(input("Nhập tháng: "))
    ngay = co_31_ngay(thang)
    if ngay:
        print(f"Tháng {thang} có 31 ngày")
    else:
        print(f"Tháng {thang} không có 31 ngày") 
if __name__ == "__main__":
    main()
