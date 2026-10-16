# =================================================================
# ÔN TẬP BUỔI 1 · KIỂM TRA NHANH (15–20 phút)
# =================================================================
# Không mở ghi chú, không xem lại bài cũ, cố gắng tự làm hết.
#
# Phần A (bài 1–6): viết code dưới mỗi đề bài.
# Phần B (câu 7–9): ĐỌC code, ĐOÁN kết quả, ghi đáp án vào biến.
#   → Đoán trước, KHÔNG chạy thử rồi mới điền nhé!
#
# Chấm điểm:  python on_tap_cham_diem.py
# Đạt 7/9 trở lên → vào buổi 2.
# KHÔNG xóa các dòng "# ===== CÂU ..."
# =================================================================


# ===== CÂU 1 =====
# In ra đúng dòng:
#   Python là ngôn ngữ đầu tiên của tôi.
print("Python là ngôn ngữ đầu tiên của tôi.")


# ===== CÂU 2 =====
# Hỏi tuổi bằng input("Tuổi: ") rồi dùng f-string in ra:
#   Bạn <tuổi> tuổi.
# Ví dụ nhập 20  →  Bạn 20 tuổi.
tuoi = input("Tuổi: ")
print(f"Bạn {tuoi} tuổi.")


# ===== CÂU 3 =====
# Dùng HAI lệnh print, trong đó lệnh thứ nhất có tham số end,
# để in ra trên CÙNG MỘT DÒNG:
#   Python-AI
print("Python", end="-")
print("AI")


# ===== CÂU 4 =====
# Hỏi thành phố bằng input("Thành phố: "). Người dùng hay gõ lộn xộn,
# ví dụ "   hà nội  ". Làm sạch rồi in ra:
#   Tôi sống ở Hà Nội.
thanh_pho = input("Thành phố: ").strip().title()
print(f"Tôi sống ở {thanh_pho}.")


# ===== CÂU 5 =====
# Hỏi 2 số nguyên bằng input("Số thứ nhất: ") và input("Số thứ hai: "),
# rồi in ra tổng:
#   Tổng: <tổng>
# Ví dụ nhập 3 và 4  →  Tổng: 7      (không phải 34!)
a = int(input("Số thứ nhất: "))
b = int(input("Số thứ hai: "))
tong = a+b
print("Tổng: ",tong)


# ===== CÂU 6 =====
# Hỏi giá một món (số thực) bằng input("Giá: ")
# và số lượng (số nguyên) bằng input("Số lượng: ").
# In ra thành tiền với ĐÚNG 2 chữ số thập phân:
#   Thành tiền: <số tiền>
# Ví dụ nhập 12.5 và 3  →  Thành tiền: 37.50
gia = float(input("Giá: "))
so_luong = int(input("Số lượng: "))
thanh_tien = gia * so_luong
print(f"Thành tiền {thanh_tien:.2f}")


# ===== CÂU 7 =====
# ĐỌC đoạn code sau và ĐOÁN nó in ra gì:
#
#     x = "5"
#     y = "3"
#     print(x + y)
#
# Ghi đáp án vào biến dưới đây (giữ trong dấu nháy):
cau_7 = "53"


# ===== CÂU 8 =====
# ĐOÁN kết quả:
#
#     print("a", "b", "c", sep="")
#
cau_8 = "abc"


# ===== CÂU 9 =====
# ĐOÁN kết quả:
#
#     ten = "  an  "
#     print(f"[{ten.strip().upper()}]")
#
cau_9 = "[AN]"
