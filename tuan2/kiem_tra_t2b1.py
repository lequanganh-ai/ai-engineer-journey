# =================================================================
# KIỂM TRA TUẦN 2 · BUỔI 1 (điều kiện: if / elif / else / and / or)
# Mục tiêu: ≥ 8/10 NGAY LẦN ĐẦU  +  Soát đề 10/10 (thật)
# =================================================================
# Luật:
#   - KHÔNG mở ghi chú, KHÔNG hỏi gợi ý, KHÔNG dùng AI gợi ý code.
#   - Tên hàm, chuỗi, con số: COPY từ đề.
#   - Mỗi câu: thử ĐỦ ví dụ (print tạm), đúng hết → xóa print → # Soát đề: OK
#   - Kiểm tra đường dẫn trên vùng code:  tuan2 > kiem_tra_t2b1.py
#   - Chạy máy chấm 1 LẦN:   python cham_kiem_tra_t2b1.py
# =================================================================


# CÂU 1
# Viết hàm  dau_so(x)  trả về "dương" nếu x > 0, "âm" nếu x < 0, "không" nếu x bằng 0.
#   dau_so(5) → "dương"    dau_so(-2) → "âm"    dau_so(0) → "không"
# Soát đề: OK
# Viết code dưới đây:
def dau_so(x):
    if x > 0:
        return "dương"
    elif x < 0:
        return "âm"
    else:
        return "không"



# CÂU 2
# Viết hàm  tuoi_teen(t)  trả về True nếu t từ 13 đến 19 (tính cả 13 và 19), ngược lại False.
#   tuoi_teen(13) → True    tuoi_teen(19) → True    tuoi_teen(12) → False    tuoi_teen(20) → False
# Soát đề: OK
# Viết code dưới đây:
def tuoi_teen(t):
    if 13 <= t <= 19:
        return True
    else:
        return False
    


# CÂU 3
# Viết hàm  phan_loai_bmi(bmi)
#   dưới 18.5            → "Gầy"
#   từ 18.5 đến dưới 25  → "Bình thường"
#   từ 25 đến dưới 30    → "Thừa cân"
#   từ 30 trở lên        → "Béo phì"
#   phan_loai_bmi(18.4) → "Gầy"         phan_loai_bmi(18.5) → "Bình thường"
#   phan_loai_bmi(25)   → "Thừa cân"    phan_loai_bmi(30)   → "Béo phì"
# Soát đề: OK
# Viết code dưới đây:
def phan_loai_bmi(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif 18.5 <= bmi < 25:
        return "Bình thường"
    elif 25 <= bmi < 30:
        return "Thừa cân"
    else:
        return "Béo phì"



# CÂU 4
# Viết hàm  dang_nhap(ten, mat_khau)  trả về True khi CẢ HAI đúng:
#   - ten sau khi xóa khoảng trắng 2 đầu và viết thường là "admin"
#   - mat_khau đúng CHÍNH XÁC là "Py@2026" (phân biệt hoa thường, KHÔNG chuẩn hóa)
#   dang_nhap("  Admin ", "Py@2026")  → True
#   dang_nhap("admin", "py@2026")     → False
#   dang_nhap("an", "Py@2026")        → False
# Soát đề: OK
# Viết code dưới đây:
def dang_nhap(ten, mat_khau):
    if ten == ten.strip().lower() =="admin" and mat_khau == "Py@2026":
        return True
    else:
        return False




# CÂU 5
# Viết hàm  phi_tre_han(so_ngay)  trả về SỐ:
#   0 ngày           → 0
#   từ 1 đến 3 ngày  → 10000
#   từ 4 đến 7 ngày  → 30000
#   trên 7 ngày      → 50000
#   phi_tre_han(0) → 0      phi_tre_han(1) → 10000   phi_tre_han(3) → 10000
#   phi_tre_han(4) → 30000  phi_tre_han(7) → 30000   phi_tre_han(8) → 50000
# Soát đề: OK
# Viết code dưới đây:
def phi_tre_han(so_ngay):
    if so_ngay == 0:
        return 0
    elif 1<= so_ngay <=3:
        return 10000
    elif 4 <= so_ngay <= 7:
        return 30000
    else:
        return 50000



# CÂU 6 · SỬA LỖI (có NHIỀU HƠN 1 lỗi)
# Quy tắc: từ 60 tuổi → "Cao tuổi"; từ 18 đến 59 → "Người lớn"; từ 6 đến 17 → "Trẻ em"; dưới 6 → "Miễn phí"
# Đúng phải là:  c6_loai_ve(70) → "Cao tuổi"   c6_loai_ve(30) → "Người lớn"
#                c6_loai_ve(10) → "Trẻ em"     c6_loai_ve(3)  → "Miễn phí"
# Soát đề: OK
def c6_loai_ve(tuoi):
    if tuoi >= 60:
        return "Cao tuổi"
    elif 18 <= tuoi <= 59:
        return "Người lớn"
    elif 6 <= tuoi <= 17:
        return "Trẻ em"
    else:
        return "Miễn phí"


# CÂU 7 · SỬA LỖI
# Tháng 6, 7, 8 là mùa hè. Đúng phải là:  c7_mua_he(7) → True   c7_mua_he(1) → False
# Soát đề: OK
def c7_mua_he(thang):
    if thang == 6 or thang == 7 or thang == 8:
        return True
    else:
        return False


# CÂU 8 · ĐỌC CODE (đoán, KHÔNG chạy thử)
# Đoạn code sau in ra gì?
#     x = 7
#     if x > 5:
#         print("A")
#     elif x > 3:
#         print("B")
#     else:
#         print("C")
# Soát đề: OK
cau_8 = "A"


# CÂU 9 · ĐỌC CODE (đoán, KHÔNG chạy thử)
# Đoạn code sau in ra gì?
#     print(5 > 3 and 2 > 4 or 1 == 1)
# Soát đề: OK
cau_9 = "True"


# CÂU 10 · CHƯƠNG TRÌNH HOÀN CHỈNH
# Viết hàm  main():
#   - Hỏi bằng input:  "Số ngày trễ: "   (số NGUYÊN)
#   - GỌI phi_tre_han (câu 5)
#   - In ra ĐÚNG 1 dòng, có dấu phẩy hàng nghìn, ví dụ nhập "5":
#         Phí trễ hạn: 30,000 đồng
#   - Nhập "0" thì in:   Phí trễ hạn: 0 đồng
# Comment kế hoạch (① HỎI / ② XỬ LÝ / ③ IN RA) bên trong main.
# Cuối file gọi main() đúng chuẩn.
# Soát đề: OK
# Viết code dưới đây:
def main():
    ngay = int(input("Số ngày trễ: "))
    goi = phi_tre_han(ngay)
    print(f"Phí trễ hạn: {goi:,} đồng")
if __name__ == "__main__":
    main()

