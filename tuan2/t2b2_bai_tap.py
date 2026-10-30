# =================================================================
# TUẦN 2 · BUỔI 2 · BÀI TẬP: %, hàm trả về bool, match
# =================================================================
# Được mở ghi chú. KHÔNG dùng AI gợi ý code.
# Mỗi bài: code → print tạm thử ĐỦ ví dụ → đúng hết → xóa print → # Soát đề: OK
# Tên hàm / chuỗi / số: COPY từ đề.  Chấm:  python cham_t2b2.py  (trong tuan2)
# =================================================================


# BÀI 1
# Viết hàm  la_so_chan(n)  trả về True nếu n chẵn, False nếu lẻ.
# YÊU CẦU: viết kiểu Pythonic — chỉ 1 dòng return, KHÔNG dùng if.
#   la_so_chan(4) → True    la_so_chan(7) → False    la_so_chan(0) → True
# Soát đề: OK
# Viết code dưới đây:
def la_so_chan(n):
    return n % 2 == 0



# BÀI 2
# Viết hàm  chia_het(a, b)  trả về True nếu a chia hết cho b (1 dòng return).
#   chia_het(10, 5) → True    chia_het(10, 3) → False    chia_het(9, 3) → True
# Soát đề: OK
# Viết code dưới đây:
def chia_het(a,b):
    return a % b ==0



# BÀI 3
# Viết hàm  so_du(a, b)  trả về SỐ dư khi chia a cho b.
#   so_du(17, 5) → 2    so_du(10, 2) → 0    so_du(4, 7) → 4
# Soát đề: OK
# Viết code dưới đây:
def so_du(a, b):
    return a % b




# BÀI 4
# Viết hàm  fizz(n):
#   chia hết cho CẢ 3 VÀ 5 → "FizzBuzz"
#   chỉ chia hết cho 3     → "Fizz"
#   chỉ chia hết cho 5     → "Buzz"
#   còn lại                → trả về chính số đó dưới dạng CHUỖI, ví dụ "7"
# CHÚ Ý thứ tự điều kiện!
#   fizz(15) → "FizzBuzz"   fizz(9) → "Fizz"   fizz(10) → "Buzz"   fizz(7) → "7"
# Soát đề: OK
# Viết code dưới đây:
def fizz(n):
    if n % 3 == 0 and n % 5 ==0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return "7"



# BÀI 5
# Viết hàm  nam_nhuan(nam)  trả về True nếu là năm nhuận:
#   chia hết cho 4 VÀ KHÔNG chia hết cho 100,  HOẶC  chia hết cho 400.
#   nam_nhuan(2024) → True    nam_nhuan(2023) → False
#   nam_nhuan(1900) → False   nam_nhuan(2000) → True
# Soát đề: OK
# Viết code dưới đây:
def nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0 



# BÀI 6  (dùng match)
# Viết hàm  ten_thu(so)  dùng match:
#   2 → "Thứ Hai"   3 → "Thứ Ba"   4 → "Thứ Tư"   5 → "Thứ Năm"   6 → "Thứ Sáu"
#   7 → "Thứ Bảy"   8 → "Chủ nhật"   số khác → "Không hợp lệ"
#   ten_thu(2) → "Thứ Hai"   ten_thu(8) → "Chủ nhật"   ten_thu(9) → "Không hợp lệ"
# Soát đề: OK
# Viết code dưới đây:
def ten_thu(so):
    match so:
        case 2:
            return "Thứ Hai"
        case 3:
            return "Thứ Ba"
        case 4:
            return "Thứ Tư"
        case 5:
            return "Thứ Năm"
        case 6:
            return "Thứ Sáu"
        case 7:
            return "Thứ Bảy"
        case 8:
            return "Chủ nhật"
        case _:
            return "Không hợp lệ"



# BÀI 7  (dùng match với |)
# Viết hàm  loai_qua(ten)  dùng match. Trước đó: xóa khoảng trắng 2 đầu + viết thường.
#   "cam" hoặc "chanh" hoặc "bưởi"  → "Họ cam quýt"
#   "táo" hoặc "lê"                 → "Họ hoa hồng"
#   còn lại                         → "Không rõ"
#   loai_qua("  Cam ") → "Họ cam quýt"   loai_qua("lê") → "Họ hoa hồng"   loai_qua("dưa") → "Không rõ"
# Soát đề: OK
# Viết code dưới đây:
def loai_qua(ten):
    ten = ten.strip().lower()
    match ten:
        case "cam" | "chanh" | "bưởi":
            return "Họ cam quýt"
        case "táo" | "lê":
            return "Họ hoa hồng"
        case _:
            return "Không rõ"



# BÀI 8 · SỬA LỖI (nhiều hơn 1 lỗi)
# Đúng phải là:  c8_la_so_le(7) → True   c8_la_so_le(4) → False
# Soát đề: OK
def c8_la_so_le(n):
    if n % 2 == 1:
        return True
    else:
        return False


# BÀI 9 · SỬA LỖI
# Đúng phải là:  c9_mau("đỏ") → "Dừng"   c9_mau("xanh") → "Đi"   c9_mau("vàng") → "Chậm lại"   c9_mau("tím") → "?"
# Soát đề: OK
def c9_mau(den):
    match den:
        case "đỏ":
            return "Dừng"
        case "xanh":
            return "Đi"
        case "vàng":
            return "Chậm lại"
        case "tím":
            return "?"


# BÀI 10 · ĐOÁN (không chạy thử)
# 23 % 4 bằng bao nhiêu?
# Soát đề: OK
cau_10 = "3"


# BÀI 11 · CHƯƠNG TRÌNH HOÀN CHỈNH
# Viết hàm  main():
#   - Hỏi:  "Nhập số: "   (số NGUYÊN)
#   - GỌI la_so_chan (bài 1)
#   - In ĐÚNG 1 dòng:  "8 là số chẵn"  hoặc  "7 là số lẻ"
# Comment kế hoạch ① HỎI / ② XỬ LÝ / ③ IN RA trong main. Cuối file gọi main() đúng chuẩn.
# Soát đề: OK
# Viết code dưới đây:
def main():
    #Hỏi 1 số nguyên
    so = int(input("Nhập số: "))
    #Xử lí gọi là số chẵn (bai1)
    la_chan = la_so_chan(so)
    #In ra 1 dòng bạn nhé
    if la_chan:
        print(f"{so} là số chẵn")
    else:
        print(f"{so} là số lẻ")
    

