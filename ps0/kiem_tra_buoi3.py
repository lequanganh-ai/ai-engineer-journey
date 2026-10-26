# =================================================================
# KIỂM TRA BUỔI 3 (chuỗi, .replace, gọi hàm, đọc lỗi)
# Mục tiêu: ≥ 8/10 NGAY LẦN ĐẦU  +  Soát đề 10/10
# =================================================================
# Luật:
#   - KHÔNG mở ghi chú, KHÔNG xem bài cũ, KHÔNG hỏi gợi ý, KHÔNG dùng AI gợi ý code.
#   - Mỗi câu: thử ĐỦ các ví dụ trong đề, so TỪNG KÝ TỰ,
#     rồi mới đổi  # Soát đề: ...  thành  # Soát đề: OK
#   - Làm xong TẤT CẢ rồi mới chạy máy chấm, và chỉ chạy 1 LẦN.
#
# Đặt file này và cham_kiem_tra_buoi3.py CÙNG thư mục (ps0), rồi:
#     python cham_kiem_tra_buoi3.py
# Chạy thử câu 10:   python kiem_tra_buoi3.py
# =================================================================


# CÂU 1
# Viết hàm  noi_nho(text)
# Xóa khoảng trắng hai đầu và viết THƯỜNG toàn bộ.
#   noi_nho("  HELLO World ")  → "hello world"
# Soát đề: OK
# Viết code dưới đây:
def noi_nho(text):
    return text.strip().lower()



# CÂU 2
# Viết hàm  noi_gach(text)
# Thay MỖI dấu cách bằng dấu gạch ngang "-".
#   noi_gach("machine learning co ban")  → "machine-learning-co-ban"
# Soát đề: OK
# Viết code dưới đây:
def noi_gach(text):
    return text.replace(" ", "-")



# CÂU 3
# Viết hàm  slug(text)
# Làm 3 việc theo thứ tự: xóa khoảng trắng hai đầu → viết thường → thay dấu cách bằng "-".
#   slug("  AI Engineer Roadmap ")  → "ai-engineer-roadmap"
# Soát đề: Ok
# Viết code dưới đây:
def slug(text):
    return text.strip().lower().replace(" ", "-")



# CÂU 4
# Viết hàm  doi_mat(text)
# Đổi  :D  thành 😄   và   ;)  thành 😉   (copy emoji từ đây). Chữ khác giữ nguyên.
#   doi_mat("Hi :D bye ;)")  → "Hi 😄 bye 😉"
# Soát đề: gọi hàm sau đó thực hiện đổi :D thành 😄 và đổi ;) thành 😉 các chữ khác thì cứ giữ nguyên thôi
# Viết code dưới đây:
def doi_mat(text):
    return text.replace(":D", "😄").replace(";)", "😉")



# CÂU 5
# Viết hàm  bo_dau_phay(so)
# so là CHUỖI có dấu phẩy hàng nghìn. Bỏ hết dấu phẩy rồi trả về SỐ NGUYÊN.
#   bo_dau_phay("1,250,000")  → 1250000
#   bo_dau_phay("999")        → 999
# Soát đề: Ok
# Viết code dưới đây:
def bo_dau_phay(so):
    return int(so.replace(",", ""))


# CÂU 6
# Viết hàm  tong_hai_gia(a, b)
# a, b là CHUỖI dạng "1,000". GỌI bo_dau_phay (câu 5) cho TỪNG chuỗi, rồi trả về TỔNG (số).
#   tong_hai_gia("1,000", "2,500")  → 3500
# Soát đề: Ok
# Viết code dưới đây:
def tong_hai_gia(a, b):
    chuoi_1 = bo_dau_phay(a)
    chuoi_2 = bo_dau_phay(b)
    tong = chuoi_1 + chuoi_2
    return tong
    



# CÂU 7 · SỬA LỖI (có NHIỀU HƠN 1 lỗi)
# Đúng phải là:  c7_hien("hi")  → "Kết quả: HI"
# Soát đề: Ok
def c7_to(text):
    text.upper()
    return text


def c7_hien(text):
    return(f"Kết quả: {text.upper()}")


# CÂU 8 · ĐỌC THÔNG BÁO LỖI
# Chạy một file thì thấy:
#     Traceback (most recent call last):
#       File "bai.py", line 3, in <module>
#         ket_qua = cau.replace("a")
#     TypeError: replace() takes at least 2 positional arguments (1 given)
# Lỗi nằm ở DÒNG SỐ MẤY của file? (chỉ ghi con số)
# Soát đề: Ok
cau_8 = "3"


# CÂU 9 · ĐỌC CODE (đoán, KHÔNG chạy thử)
# Đoạn code sau in ra gì?
#     s = "a b c"
#     print(s.replace(" ", "").upper())
# Soát đề: Ok
cau_9 = "ABC"


# CÂU 10 · CHƯƠNG TRÌNH HOÀN CHỈNH
# Viết hàm  main():
#   - Hỏi bằng input:  "Tiêu đề: "
#   - GỌI hàm slug (câu 3) với dữ liệu vừa nhập
#   - In ra ĐÚNG 1 dòng, ví dụ nhập "  Hoc Python Co Ban ":
#
#         Đường dẫn: /blog/hoc-python-co-ban
#
# Viết comment kế hoạch (① HỎI / ② XỬ LÝ / ③ IN RA) bên trong main trước khi code.
# Cuối file nhớ có dòng gọi main() đúng chuẩn.
# Soát đề: Ok
def main():
    trang_thai = input("Nhập một câu: ")
    ket_qua = slug(trang_thai)
    print(f"Đường dẫn: /blog/{ket_qua}")
if __name__ == "__main__":
    main()


