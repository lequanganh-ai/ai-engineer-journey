# =================================================================
# PHẦN 4 · MINI PROJECT: MÁY IN HÓA ĐƠN QUÁN CÀ PHÊ
# =================================================================
# Viết một chương trình HOÀN CHỈNH, tự viết mọi thứ từ đầu.
# Chấm điểm:   python cham_on_tap_tong_hop.py
# Chạy thử:    python mini_project_cafe.py
#
# YÊU CẦU — viết 4 hàm sau:
#
# 1. lam_sach_ten(ten)
#      Xóa khoảng trắng hai đầu, viết hoa chữ đầu mỗi từ.
#      lam_sach_ten("  lê an ")  → "Lê An"
#
# 2. thanh_tien(so_ly, gia_ly)
#      Trả về SỐ: số ly × giá mỗi ly.
#      thanh_tien(3, 35000)  → 105000
#
# 3. dinh_dang_tien(so_tien)
#      Trả về CHUỖI có dấu phẩy hàng nghìn + chữ "đồng".
#      dinh_dang_tien(105000)  → "105,000 đồng"
#
# 4. main()
#      - Hỏi 3 lần bằng input:  "Tên khách: "   "Số ly: "   "Giá mỗi ly: "
#      - Số ly và giá là CHUỖI từ input → nhớ đổi sang số
#      - GỌI 3 hàm trên để xử lý
#      - In ra ĐÚNG 5 dòng (ví dụ nhập "  lê an ", "3", "35000"):
#
#            ===== HÓA ĐƠN =====
#            Khách: Lê An
#            Số ly: 3
#            Thành tiền: 105,000 đồng
#            ===================
#
#        (dòng đầu: 5 dấu =, dấu cách, HÓA ĐƠN, dấu cách, 5 dấu =
#         dòng cuối: 19 dấu =)
#
# Cuối file nhớ có:
#     if __name__ == "__main__":
#         main()
# =================================================================

# Viết code dưới đây:
def lam_sach_ten(ten):
    return ten.strip().title()

def thanh_tien(gia_ly, so_ly):
    return so_ly*gia_ly

def dinh_dang_tien(so_tien):
    return f"{so_tien:,} đồng"

def main():
    ten =input("Tên khách: ")
    so_ly = int(input("Số ly: "))
    gia_ly = int(input("Giá mỗi ly: "))

    ten_sach = lam_sach_ten(ten)
    tien = thanh_tien(so_ly, gia_ly)
    tien_chu = dinh_dang_tien(tien)

    print("===== HÓA ĐƠN =====")
    print(f"Khách: {ten_sach}")
    print(f"Số ly: {so_ly}")
    print(f"Thành tiền: {tien_chu}")
    print("="*19)
if __name__ == "__main__":
    main()