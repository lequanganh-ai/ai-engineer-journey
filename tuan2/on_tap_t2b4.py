# ÔN TẬP · TUẦN 2 BUỔI 4  (split · match · :.1f · convert giờ · khoảng giờ)
# Chạy máy chấm:  python cham_on_tap_t2b4.py
#
# LUẬT (như mọi bài):
#   - KHÔNG xem ghi chú, KHÔNG xin code mẫu khi chưa gửi bản thử
#   - Mỗi câu: thử ĐỦ ví dụ + 1 giá trị tự nghĩ KHÔNG có trong đề
#   - Ghi dưới mỗi câu:
#       # Soát đề: OK
#       # Đã thử thêm: <giá trị> → <kết quả COPY từ màn hình>
#   - Hàm nhỏ chỉ RETURN, không print, không input
#   - Thử 1 hàm: thêm print(ten_ham(...)) TẠM ở cuối file, chạy, rồi XÓA


# CÂU 1 · doi_phut(s)
# Nhận chuỗi "giờ:phút", TRẢ VỀ tổng số phút (SỐ NGUYÊN).
#   doi_phut("1:45")  → 105
#   doi_phut("0:30")  → 30
#   doi_phut("2:00")  → 120
# Soát đề: OK
# Đã thử thêm: 1:20 -> 80
def doi_phut(s):
    gio, phut = s.split(":")
    gio = int(gio)
    phut = int(phut)
    return gio * 60 + phut

    


# CÂU 2 · doi_gio(s)
# Nhận "giờ:phút", TRẢ VỀ số giờ dạng số thực.
#   doi_gio("9:45")  → 9.75
#   doi_gio("14:30") → 14.5
#   doi_gio("6:00")  → 6.0
# Soát đề: OK
# Đã thử thêm: 10:2 -> 10.033333333333333
def doi_gio(s):
    gio , phut = s.split(":")
    gio = float(gio)
    phut = float(phut)
    return phut / 60 + gio


# CÂU 3 · tinh(bieu_thuc)
# Nhận chuỗi "x y z" (cách nhau 1 dấu cách), x và z là số nguyên.
# Dùng match theo phép tính. TRẢ VỀ kết quả là SỐ THỰC (float).
# Phép tính không phải + - * /  → TRẢ VỀ None
#   tinh("6 * 7")  → 42.0
#   tinh("9 / 2")  → 4.5
#   tinh("3 - 10") → -7.0
#   tinh("5 % 2")  → None
# Soát đề: OK
# Đã thử thêm: 10 % 2 ->None
def tinh(bieu_thuc):
    x , y, z = bieu_thuc.split(" ")
    x = int(x)
    z = int(z)
    match y:
        case "+":
            return float(x + z)
        case "-":
            return float(x - z)
        case "*":
            return  float(x * z)
        case "/":
            return  float(x / z)
        case _:
            return None
            


# CÂU 4 · dinh_dang(so)
# TRẢ VỀ CHUỖI của số, đúng 1 chữ số thập phân.
#   dinh_dang(42)    → "42.0"
#   dinh_dang(4.567) → "4.6"
# Soát đề: OK
# Đã thử thêm: 34 -> 34.0
def dinh_dang(so):
    return f"{so:.1f}"

# CÂU 5 · ca_hoc(gio)
# gio là SỐ (ví dụ 9.75). Tính cả hai đầu:
#   7 giờ   đến 11 giờ 30  → "sáng"
#   13 giờ  đến 16 giờ 45  → "chiều"
#   giờ khác               → "nghỉ"
#   ca_hoc(7.0) → "sáng"     ca_hoc(11.5) → "sáng"
#   ca_hoc(12.0) → "nghỉ"    ca_hoc(16.75) → "chiều"
# Soát đề: OK
# Đã thử thêm: 11.0 -> sáng
def ca_hoc(gio):
    gio = float(gio)
    if 7 <= gio <= 11 + 30 / 60:
        return "sáng"
    elif 13<= gio <= 16 + 45 /60:
        return "chiều"
    else:
        return "nghỉ"


# CÂU 6 · SỬA LỖI
# Hàm dưới đây CHẠY BÁO LỖI hoặc ra SAI. Sửa để:
#   gio_ra_so("8:15") → 8.25      gio_ra_so("10:30") → 10.5
# Ghi thêm 1 dòng comment: "# Lỗi: ..." nói rõ đã sai ở đâu (bao nhiêu chỗ).
# Soát đề: OK
# Đã thử thêm: 8:10 -> 8.166666666666666
#Lỗi: split không phải dấu cách định dạng int cho gio, phut, phut chưa được khai báo 
def gio_ra_so(time):
    gio, phut = time.split(":")
    gio = int(gio)
    phut = int(phut)
    return gio + phut / 60


# CÂU 7 · CHƯƠNG TRÌNH ĐẦY ĐỦ (dùng lại câu 2 và câu 5)
# main():
#   - hỏi đúng y:  "Giờ vào lớp? "
#   - GỌI doi_gio rồi GỌI ca_hoc (không viết lại)
#   - in ra:  Ca sáng   /   Ca chiều   /   Ca nghỉ
#   Ví dụ:  nhập 9:45  → in  Ca sáng
#           nhập 12:10 → in  Ca nghỉ
# Soát đề: OK
# Đã thử thêm: 9:44 -> Ca sáng
def main():
    gio_dung = input("Giờ vào lớp? ")
    gio = doi_gio(gio_dung)
    ket_qua = ca_hoc(gio)
    print(f"Ca {ket_qua}")
if __name__ == "__main__":
    main()