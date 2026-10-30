# =================================================================
# TUẦN 2 · BUỔI 2 · LUYỆN LẠI LẦN 2 — chỉ 3 lỗi: chép ví dụ · so bool với chuỗi · in sai biến
# Mục tiêu: 6/6 NGAY LẦN ĐẦU  +  Soát đề 6/6
# =================================================================
# QUY TẮC MỚI: mỗi bài phải có thêm 1 dòng:
#     # Đã thử thêm: <một giá trị KHÁC ví dụ> → <kết quả bạn thấy>
# Máy chấm sẽ thử RẤT NHIỀU giá trị KHÔNG có trong ví dụ.
# KHÔNG hỏi gợi ý. Chấm:  python cham_t2b2_luyen_lai_2.py   (trong tuan2)
# =================================================================


# BÀI 1  (chữ cố định hay giá trị tính toán?)
# Viết hàm  chan_le(n):
#   n chẵn → "Chẵn"
#   n lẻ   → chuỗi dạng "Lẻ, dư " + số dư khi chia cho 2   (n = 7 → "Lẻ, dư 1")
#   chan_le(4) → "Chẵn"    chan_le(7) → "Lẻ, dư 1"
# Soát đề: OK
# Đã thử thêm: <7>- <Lẻ, dư 1>
# Viết code dưới đây:
def chan_le(n):
    if n % 2 == 0:
        return "Chẵn"
    else:
        return f"Lẻ, dư {n % 2}"




# BÀI 2  (giá trị tính toán dạng chuỗi)
# Viết hàm  du_cho_5(n)  trả về số dư khi chia n cho 5, dưới dạng CHUỖI.
#   du_cho_5(12) → "2"    du_cho_5(10) → "0"
# Soát đề: OK
# Đã thử thêm: <12> -> <"1">
# Viết code dưới đây:
def du_cho_5(n):
    return str(n % 5)




# BÀI 3  (chuẩn hóa trước khi match — KHÔNG chép ký tự trong ví dụ)
# Viết hàm  muc_do(ki_hieu)  dùng match. Người dùng có thể nhập hoa hoặc thường, có thể dư khoảng trắng.
#   "H" → "Cao"    "M" → "Trung bình"    "L" → "Thấp"    khác → "Không rõ"
#   muc_do("h") → "Cao"    muc_do(" M ") → "Trung bình"    muc_do("x") → "Không rõ"
# Soát đề: OK
# Đã thử thêm: <"H"> - <Cao>
# Viết code dưới đây:
def muc_do(ki_hieu):
    ki_hieu = ki_hieu.strip().upper()
    match ki_hieu:
        case "H":
            return "Cao"
        case "M":
            return "Trung bình"
        case "L":
            return "Thấp"
        case _:
            return "Không rõ"




# BÀI 4  (tham số bool — KHÔNG so với "True", KHÔNG viết == True)
# Viết hàm  duoc_giam_gia(la_thanh_vien, tong)  trả về True khi la_thanh_vien là True VÀ tong từ 200000 trở lên.
#   duoc_giam_gia(True, 250000) → True    duoc_giam_gia(False, 250000) → False    duoc_giam_gia(True, 100000) → False
# Soát đề: OK
# Đã thử thêm: <True, 250000) -> True
# Viết code dưới đây:
def duoc_giam_gia(la_thanh_vien, tong):
    return la_thanh_vien and tong >= 200000



# BÀI 5  (tham số bool → chọn chữ)
# Viết hàm  trang_thai(dang_online)  — dang_online là True/False.
#   True → "Đang hoạt động"     False → "Ngoại tuyến"
# Soát đề: OK
# Đã thử thêm: <True> -> <Ngoại tuyến>
# Viết code dưới đây:
def trang_thai(dang_online):
    if dang_online == True:
        return "Đang hoạt động"
    else:
        return "Ngoại tuyến"





# BÀI 6 · CHƯƠNG TRÌNH  (in đúng biến)
# Viết hàm  main():
#   - Hỏi: "Nhập năm: "  (số NGUYÊN)
#   - Năm nhuận khi: chia hết cho 4 VÀ không chia hết cho 100, HOẶC chia hết cho 400.
#     Viết thêm hàm  la_nam_nhuan(nam)  (1 dòng return) rồi GỌI nó trong main.
#   - In ĐÚNG 1 dòng:  "2024 là năm nhuận"   hoặc   "2023 không phải năm nhuận"
# Comment ① HỎI / ② XỬ LÝ / ③ IN RA BÊN TRONG main. Cuối file gọi main() đúng chuẩn.
# Soát đề: OK
# Đã thử thêm: <2023> -> <2023 không phải năm nhuận>
# Viết code dưới đây:
def la_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0
def main():
    nam = int(input("Nhập năm: "))

    nhuan = la_nam_nhuan(nam)
    if nhuan:
        print(f"{nam} là năm nhuận")
    else:
        print(f"{nam} không phải năm nhuận")
if __name__ == "__main__":
    main()
