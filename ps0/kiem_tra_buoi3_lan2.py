# =================================================================
# KIỂM TRA BUỔI 3 · ĐỀ LẦN 2
# Mục tiêu: ≥ 8/10 NGAY LẦN ĐẦU  +  Soát đề 10/10  +  ảnh tự chạy thử câu 10
# =================================================================
# Luật:
#   - KHÔNG mở ghi chú (trừ loi-thuong-gap.md), KHÔNG hỏi gợi ý, KHÔNG dùng AI gợi ý code.
#   - Mỗi câu: thử ĐỦ các ví dụ, so TỪNG KÝ TỰ, rồi mới đổi dòng soát đề.
#     Viết CHÍNH XÁC:   # Soát đề: OK     (copy dòng này, đừng gõ tay)
#   - Câu 10: tự chạy  python kiem_tra_buoi3_lan2.py  → CHỤP ẢNH → rồi mới chạy máy chấm.
#   - Trước khi chạy máy chấm: đi hết CHECKLIST trong loi-thuong-gap.md
#   - Chỉ chạy máy chấm 1 LẦN.
#
# Chấm điểm:   python cham_kiem_tra_buoi3_lan2.py
# =================================================================


# CÂU 1
# Viết hàm  het_len(text)
# Xóa khoảng trắng hai đầu và viết HOA toàn bộ.
#   het_len("  xin chao ")  → "XIN CHAO"
# Soát đề: OK
# Viết code dưới đây:
def het_len(text):
    return text.strip().upper()



# CÂU 2
# Viết hàm  noi_gach_duoi(text)
# Thay MỖI dấu cách bằng dấu gạch dưới "_".
#   noi_gach_duoi("hoc may co ban")  → "hoc_may_co_ban"
# Soát đề: OK
# Viết code dưới đây:
def noi_gach_duoi(text):
    return text.replace(" ", "_")



# CÂU 3
# Viết hàm  ten_bien(text)
# Làm 3 việc theo thứ tự: xóa khoảng trắng hai đầu → viết thường → thay dấu cách bằng "_".
#   ten_bien("  Tong Tien ")  → "tong_tien"
# Soát đề: OK
# Viết code dưới đây:
def ten_bien(text):
    return text.strip().lower().replace(" ", "_")



# CÂU 4
# Viết hàm  doi_ky_hieu(text)
# Đổi  <3  thành ♥   và   :P  thành 😛   (copy ký hiệu từ đây). Chữ khác giữ nguyên.
#   doi_ky_hieu("I <3 Python :P")  → "I ♥ Python 😛"
# Soát đề: OK
# Viết code dưới đây:
def doi_ky_hieu(text):
    return text.replace("<3", "♥").replace(":P","😛")



# CÂU 5
# Viết hàm  bo_cham(so)
# so là CHUỖI viết kiểu Việt Nam, dùng DẤU CHẤM ngăn hàng nghìn.
# Bỏ hết dấu chấm rồi trả về SỐ NGUYÊN.
#   bo_cham("1.500.000")  → 1500000
#   bo_cham("750")        → 750
# Soát đề: OK
# Viết code dưới đây:
def bo_cham(so):
    return int(so.strip().title().replace(".", ""))



# CÂU 6
# Viết hàm  hieu_hai_gia(a, b)
# a, b là CHUỖI dạng "5.000". GỌI bo_cham (câu 5) cho TỪNG chuỗi,
# rồi trả về a TRỪ b (số).
#   hieu_hai_gia("5.000", "1.500")  → 3500
# Soát đề: OK
# Viết code dưới đây:
def hieu_hai_gia(a, b):
    chuoi_1 = bo_cham(a)
    chuoi_2 = bo_cham(b)
    return chuoi_1 - chuoi_2



# CÂU 7 · SỬA LỖI (có NHIỀU HƠN 1 lỗi)
# Đúng phải là:  c7_the("  Python ")  → "#python"
# Soát đề: OK
def c7_lam_sach(text):
    return text.strip().lower()


def c7_the(text):
    ket_qua = c7_lam_sach(text)
    return f"#{ket_qua}"


# CÂU 8 · ĐỌC THÔNG BÁO LỖI
# Chạy một file thì thấy:
#     Traceback (most recent call last):
#       File "bai.py", line 7, in <module>
#         tong = so_luong * gia
#     NameError: name 'gia' is not defined
# Biến nào CHƯA được tạo ra? (chỉ ghi tên biến)
# Soát đề: OK
cau_8 = "gia"


# CÂU 9 · ĐỌC CODE (đoán, KHÔNG chạy thử)
# Đoạn code sau in ra gì?
#     print(int("1,000".replace(",", "")) + 1)
# Soát đề: OK
cau_9 = "1001"


# CÂU 10 · CHƯƠNG TRÌNH HOÀN CHỈNH
# Viết hàm  main():
#   - Hỏi bằng input:  "Tên biến: "
#   - GỌI hàm ten_bien (câu 3) với dữ liệu vừa nhập
#   - In ra ĐÚNG 1 dòng, ví dụ nhập "  Tong Tien ":
#
#         Gợi ý: tong_tien = 0
#
# Viết comment kế hoạch (① HỎI / ② XỬ LÝ / ③ IN RA) bên trong main trước khi code.
# Cuối file nhớ có dòng gọi main() đúng chuẩn.
# Soát đề: OK
# Viết code dưới đây:
def main():
    can_goi =input("Tên biến: ")
    ket_qua =ten_bien(can_goi)
    print(f"Gợi ý: {ket_qua} = 0")
if __name__ == "__main__":
    main()


