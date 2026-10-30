# =================================================================
# TUẦN 2 · BUỔI 2 · LUYỆN LẠI (đúng các lỗi vừa mắc)
# Mục tiêu: 7/7 NGAY LẦN ĐẦU  +  Soát đề 7/7 (viết đúng: # Soát đề: OK)
# =================================================================
# KHÔNG hỏi gợi ý. Được mở ghi chú. Tên hàm / chuỗi: COPY từ đề.
# Thử ĐỦ ví dụ (và tự nghĩ thêm 1 số KHÁC ví dụ) trước khi ghi OK.
# Chấm:  python cham_t2b2_luyen_lai.py   (trong tuan2)
# =================================================================


# BÀI 1  (lỗi cũ: chép ví dụ vào code)
# Viết hàm  chia_ba(n):
#   chia hết cho 3 → "Chia hết"
#   còn lại        → trả về số dư dưới dạng CHUỖI   (ví dụ n = 7 → "1", n = 8 → "2")
#   chia_ba(9) → "Chia hết"    chia_ba(7) → "1"    chia_ba(8) → "2"
# Soát đề: OK
# Viết code dưới đây:
def chia_ba(n):
    if n % 3 == 0:
        return "Chia hết"
    else:
        return str(n%3)



# BÀI 2  (lỗi cũ: case sai kiểu dữ liệu)
# Viết hàm  ten_thang(so)  dùng match. so là SỐ.
#   1 → "Tháng Một"   2 → "Tháng Hai"   3 → "Tháng Ba"   số khác → "Chưa hỗ trợ"
#   ten_thang(1) → "Tháng Một"   ten_thang(3) → "Tháng Ba"   ten_thang(4) → "Chưa hỗ trợ"
# Soát đề: OK
# Viết code dưới đây:
def ten_thang(so):
    match so:
        case 1:
            return "Tháng Một"
        case 2:
            return "Tháng Hai"
        case 3:
            return "Tháng Ba"
        case _:
            return "Chưa hỗ trợ"



# BÀI 3  (lỗi cũ: thiếu trường hợp còn lại)
# Viết hàm  phan_hoi(lenh)  dùng match. Trước đó: xóa khoảng trắng 2 đầu + viết thường.
#   "hi" hoặc "hello" hoặc "chào"  → "Xin chào!"
#   "bye" hoặc "tạm biệt"          → "Hẹn gặp lại!"
#   MỌI lệnh khác                  → "Tôi chưa hiểu."
#   phan_hoi("  Hello ") → "Xin chào!"   phan_hoi("tạm biệt") → "Hẹn gặp lại!"   phan_hoi("abc") → "Tôi chưa hiểu."
# Soát đề: OK
# Viết code dưới đây:
def phan_hoi(lenh):
    lenh = lenh.strip().lower()
    match lenh:
        case "hi" | "hello" | "chào":
            return "Xin chào!"
        case "bye" | "tạm biệt":
            return "Hẹn gặp lại!"
        case _:
            return "Tôi chưa hiểu."



# BÀI 4  (Pythonic: 1 dòng return, KHÔNG dùng if)
# Viết hàm  la_boi_cua_7(n)  trả về True nếu n chia hết cho 7.
#   la_boi_cua_7(14) → True    la_boi_cua_7(15) → False
# Soát đề: OK
# Viết code dưới đây:
def la_boi_cua_7(n):
    return n % 7 == 0



# BÀI 5 · SỬA LỖI (nhiều hơn 1 lỗi)
# Người dùng có thể nhập chữ hoa hoặc thường. Size khác S/M/L đều là "Không có".
# Đúng phải là:  c5_size("s") → "Nhỏ"   c5_size("M") → "Vừa"   c5_size("l") → "Lớn"   c5_size("XL") → "Không có"
# Soát đề: OK
def c5_size(ki_hieu):
    match ki_hieu:
        case "s":
            return "Nhỏ"
        case "M":
            return "Vừa"
        case "l":
            return "Lớn"
        case _:
            return "Không có"


# BÀI 6
# Viết hàm  ve_vao_cong(tuoi, co_ve)  trả về True khi: tuổi từ 18 trở lên VÀ co_ve là True.
# (co_ve đã là True/False — KHÔNG viết == True)   1 dòng return.
#   ve_vao_cong(20, True) → True   ve_vao_cong(20, False) → False   ve_vao_cong(16, True) → False
# Soát đề: OK
# Viết code dưới đây:
def ve_vao_cong(tuoi, co_ve):
    return tuoi >= 18 and co_ve 



# BÀI 7 · CHƯƠNG TRÌNH (lỗi cũ: in True/False thay vì câu)
# Viết hàm  main():
#   - Hỏi:  "Nhập số: "   (số NGUYÊN)
#   - GỌI la_boi_cua_7 (bài 4)
#   - In ĐÚNG 1 dòng:  "14 là bội của 7"   hoặc   "15 không là bội của 7"
# Comment ① HỎI / ② XỬ LÝ / ③ IN RA trong main. Cuối file gọi main() đúng chuẩn.
# Soát đề: OK
# Viết code dưới đây:
#Ý 1:Hỏi nhập số
def main():
    hoi = int(input("Nhập số: "))

    la_boi = la_boi_cua_7(hoi)

    if la_boi:
        print(f"{hoi} là bội của 7")
    else:
        print(f"{hoi} không là bội của 7")

if __name__ == "__main__":
    main()

