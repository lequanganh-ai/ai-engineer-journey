# =================================================================
# TUẦN 2 · BUỔI 1 · LUYỆN LẠI (đúng các lỗi bạn vừa mắc)
# Mục tiêu: 8/8 NGAY LẦN CHẠY ĐẦU  +  Soát đề 8/8 (thật)
# =================================================================
# Luật:
#   - KHÔNG hỏi gợi ý. Được mở ghi chú.
#   - Mỗi bài: viết code → thêm print tạm thử ĐỦ ví dụ (nhất là điểm ranh giới)
#     → đúng hết → xóa print → đổi thành  # Soát đề: OK
#   - Chuỗi và con số: COPY từ đề, không gõ tay.
#   - Kiểm tra dòng đường dẫn trên vùng code phải là  tuan2 > t2b1_luyen_lai.py
#   - Chạy máy chấm 1 LẦN:   python cham_t2b1_luyen_lai.py
# =================================================================


# BÀI 1
# Viết hàm  nhiet_do(t)
#   dưới 0          → "Đóng băng"
#   từ 0 đến dưới 25 → "Mát"
#   từ 25 trở lên   → "Nóng"
#   nhiet_do(-1) → "Đóng băng"   nhiet_do(0) → "Mát"   nhiet_do(25) → "Nóng"
# Soát đề: OK
# Viết code dưới đây:
def nhiet_do(t):
    if t < 0:
        return "Đóng băng"
    elif 0 <= t < 25:
        return "Mát"
    else:
        return "Nóng"



# BÀI 2 · SỬA LỖI  (lỗi giống bài 7 lúc nãy)
# Đúng phải là:  c2_size(155) → "S"   c2_size(160) → "M"   c2_size(170) → "M"   c2_size(171) → "L"
# Soát đề: OK
def c2_size(cm):
    if cm < 160:
        return "S"
    elif 160 <= cm <= 170:
        return "M"
    else:
        return "L"


# BÀI 3  (giống bài 6 lúc nãy)
# Viết hàm  la_quan_tri(ten)  trả về True nếu ten là "admin" HOẶC "root", ngược lại False.
# Trước khi so sánh: xóa khoảng trắng 2 đầu và viết thường toàn bộ.
#   la_quan_tri("  ADMIN ")  → True
#   la_quan_tri("Root")      → True
#   la_quan_tri("an")        → False
# Soát đề: OK
# Viết code dưới đây:
def la_quan_tri(ten):
    ten = ten.strip().lower()
    if ten == "admin" or ten == "root":
        return True
    else:
        return False



# BÀI 4  (cẩn thận số 0)
# Viết hàm  phi_gui_xe(so_gio)  trả về SỐ:
#   từ 2 giờ trở xuống   → 5000
#   từ 3 đến 5 giờ       → 10000
#   trên 5 giờ           → 20000
#   phi_gui_xe(2) → 5000    phi_gui_xe(3) → 10000    phi_gui_xe(5) → 10000    phi_gui_xe(6) → 20000
# Soát đề: OK
# Viết code dưới đây:
def phi_gui_xe(so_gio):
    if so_gio <= 2:
        return 5000
    elif 3 <= so_gio <= 5:
        return 10000
    else:
        return 20000



# BÀI 5 · SỬA LỖI  (lỗi giống bài 10 lúc nãy)
# Đúng phải là:  c5_huy_hieu(95) → "Vàng"   c5_huy_hieu(80) → "Bạc"
#                c5_huy_hieu(50) → "Đồng"   c5_huy_hieu(49) → "Chưa có"
# Soát đề: OK
def c5_huy_hieu(diem):
    if diem >= 95:
        return "Vàng"
    elif diem >= 80:
        return "Bạc"
    elif diem >= 50:
        return "Đồng"
    else:
        return "Chưa có"


# BÀI 6  (mỗi con số có vai trò riêng)
# Viết hàm  tien_giam(tong)  trả về SỐ tiền được giảm:
#   tổng từ 1000000 trở lên     → giảm 100000
#   tổng từ 500000 đến dưới 1000000 → giảm 30000
#   dưới 500000                 → 0
#   tien_giam(1000000) → 100000   tien_giam(999999) → 30000
#   tien_giam(500000)  → 30000    tien_giam(499999) → 0
# Soát đề: OK
# Viết code dưới đây:
def tien_giam(tong):
    if tong >= 1000000:
        return 100000
    elif 500000 <= tong <= 1000000:
        return 30000
    else:
        return 0



# BÀI 7
# Viết hàm  mat_khau_on(mk)  trả về True khi CẢ HAI điều kiện đúng:
#   - mk không rỗng sau khi xóa khoảng trắng 2 đầu
#   - mk KHÁC "123456"
#   mat_khau_on("abc@2026") → True
#   mat_khau_on("123456")   → False
#   mat_khau_on("   ")      → False
# Soát đề: OK
# Viết code dưới đây:
def mat_khau_on(mk):
    if mk.strip() != "" and mk != "123456":
        return True
    else:
        return False 
    


# BÀI 8 · CHƯƠNG TRÌNH HOÀN CHỈNH
# Viết hàm  main():
#   - Hỏi bằng input:  "Chiều cao (cm): "   (số NGUYÊN)
#   - GỌI c2_size (bài 2, sau khi đã sửa)
#   - In ra ĐÚNG 1 dòng, ví dụ nhập "165":
#         Size: M
# Comment kế hoạch (① HỎI / ② XỬ LÝ / ③ IN RA) bên trong main.
# Cuối file gọi main() đúng chuẩn.
# Soát đề: OK
# Viết code dưới đây:
def main():
    hoi = int(input("Chiều cao (cm): "))
    sua = c2_size(hoi)
    print(f"Size: {sua}")

if __name__ == "__main__":
    main()
