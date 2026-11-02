# =================================================================
# BUỔI 4 · KIỂM TRA BUỔI 3 (startswith / endswith, chuẩn hóa, thứ tự điều kiện, or)
# Mục tiêu: ≥ 8/10 NGAY LẦN ĐẦU · Soát đề 10/10 · Đã thử thêm 8/8
# =================================================================
# KHÔNG mở ghi chú, KHÔNG hỏi gợi ý, KHÔNG dùng AI gợi ý code.
# QUY TẮC: MỖI NHÁNH if/elif/else phải có ít nhất 1 lần chạy thử đi vào nó.
# Câu 1–7 và 10: # Đã thử thêm: <giá trị ĐỀ KHÔNG CHO> → <kết quả chạy THẬT>
# Viết CHÍNH XÁC:  # Soát đề: OK      Chấm 1 LẦN:  python cham_kiem_tra_t2b3.py  (trong tuan2)
# =================================================================


# CÂU 1
# Viết hàm  link_an_toan(url)  trả về True nếu url (sau khi xóa khoảng trắng 2 đầu, viết thường)
# bắt đầu bằng "https://". 1 dòng return.
#   link_an_toan("https://ptit.edu.vn") → True    link_an_toan("http://abc.com") → False
# Soát đề: OK
# Đã thử thêm: <"https://ptit.edu.vn"> -> True
# Viết code dưới đây:
def link_an_toan(url):
    return url.strip().lower().startswith("https://")



# CÂU 2
# Viết hàm  so_viet_nam(sdt)  trả về True nếu sdt (xóa khoảng trắng 2 đầu) bắt đầu bằng "+84" HOẶC "0".
#   so_viet_nam("0912345678") → True    so_viet_nam("+84912345678") → True    so_viet_nam("+1555123") → False
# Soát đề: OK
# Đã thử thêm: <"0912345678"> ->True
# Viết code dưới đây:
def so_viet_nam(sdt):
    sdt = sdt.strip()
    return sdt.startswith("+84") or sdt.startswith("0")



# CÂU 3
# Viết hàm  la_anh(ten_file)  trả về True nếu đuôi là .png hoặc .jpg hoặc .jpeg (không phân biệt hoa thường).
#   la_anh("a.png") → True    la_anh("B.JPEG") → True    la_anh("c.pdf") → False
# Soát đề: OK
# Đã thử thêm: <"a.png"> - True
# Viết code dưới đây:
def la_anh(ten_file):
    ten = ten_file.strip().lower()
    return ten.endswith(".png") or ten.endswith(".jpg") or ten.endswith(".jpeg")



# CÂU 4  (chú ý thứ tự!)
# Viết hàm  loai_loi_chao(cau)  — chuẩn hóa (strip + lower) trước:
#   bắt đầu bằng "chào buổi sáng" → "Buổi sáng"
#   bắt đầu bằng "chào"           → "Chào thường"
#   còn lại                       → "Không chào"
#   loai_loi_chao("Chào buổi sáng em") → "Buổi sáng"   loai_loi_chao("chào bạn") → "Chào thường"   loai_loi_chao("hi") → "Không chào"
# Soát đề: OK
# Đã thử thêm: <"Chào buổi sáng em"> -> "Buổi sáng"
# Viết code dưới đây:
def loai_loi_chao(cau):
    cau = cau.strip().lower()
    if cau.startswith("chào buổi sáng"):
        return "Buổi sáng"
    elif cau.startswith("chào"):
        return "Chào thường"
    else:
        return "Không chào"




# CÂU 5
# Viết hàm  ngon_ngu(ten_file)  — không phân biệt hoa thường, bỏ khoảng trắng 2 đầu:
#   đuôi .py → "Python"    đuôi .md → "Markdown"    đuôi .html hoặc .htm → "Web"    khác → "Khác"
#   ngon_ngu("main.py") → "Python"   ngon_ngu("INDEX.HTML") → "Web"   ngon_ngu("data.csv") → "Khác"
# Soát đề: OK
# Đã thử thêm: <"main.py"> -> "Python"
# Viết code dưới đây:
def ngon_ngu(ten_file):
    ten = ten_file.strip().lower()
    if ten.endswith(".py"):
        return "Python"
    elif ten.endswith(".md"):
        return "Markdown"
    elif ten.endswith(".html") or ten.endswith(".htm"):
        return "Web"
    else:
        return "Khác"



# CÂU 6 · SỬA LỖI (nhiều hơn 1 lỗi)
# Quy tắc: "/help" hoặc "/start" → "Trợ giúp";  lệnh khác bắt đầu bằng "/" → "Lệnh";  còn lại → "Tin thường"
# Đúng phải là:  c6_loai("/help") → "Trợ giúp"   c6_loai("/start") → "Trợ giúp"
#                c6_loai("/abc") → "Lệnh"        c6_loai("hi") → "Tin thường"
# Soát đề: OK
# Đã thử thêm: <"/help"> -> "Trợ giúp"
def c6_loai(tin):
    t = tin.strip().lower()
    if t.startswith("/help") or t.startswith("/start"):
        return "Trợ giúp"
    elif t.startswith("/"):
            return "Lệnh"
    else:
        return "Tin thường"


# CÂU 7 · SỬA LỖI
# Đúng phải là:  c7_la_pdf("bao_cao.pdf") → True   c7_la_pdf("  A.PDF ") → True   c7_la_pdf("a.txt") → False
# Soát đề: OK
# Đã thử thêm: <"bao_cao.pdf"> -> True
def c7_la_pdf(ten):
    return ten.strip().lower().endswith(".pdf") or ten.endswith(".PDF")


# CÂU 8 · ĐOÁN (không chạy thử): đoạn code in ra gì?
#     print("Hello".startswith("h"))
# Soát đề: OK
cau_8 = "False"


# CÂU 9 · ĐOÁN (không chạy thử): đoạn code in ra gì?
#     print("a.JPG".lower().endswith(".jpg"))
# Soát đề: OK
cau_9 = "True"


# CÂU 10 · CHƯƠNG TRÌNH HOÀN CHỈNH
# Viết hàm  email_ptit(email)  trả về True nếu email (strip + lower) kết thúc bằng "@ptit.edu.vn".
# Viết hàm  main():
#   - Hỏi:  "Email: "
#   - GỌI email_ptit
#   - In ĐÚNG 1 dòng:  "Email sinh viên PTIT"   hoặc   "Email ngoài"
# Comment ① HỎI / ② XỬ LÝ / ③ IN RA BÊN TRONG main. Cuối file gọi main() đúng chuẩn.
# Soát đề: OK
# Đã thử thêm:  "Email sinh viên PTIT"   "Email ngoài" -> "Email ngoài"
# Viết code dưới đây:
def email_ptit(email):
    return email.strip().lower().endswith("@ptit.edu.vn")

def main():
    email = input("Email: ")
    if email_ptit(email):
        print("Email sinh viên PTIT")
    else:
        print("Email ngoài")
if __name__ == "__main__":
    main()
