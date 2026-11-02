# BÀI LUYỆN · CA LÀM VIỆC  (giống bài meal, nhưng KHÔNG chép code meal — tự viết)
#
# Một quán cà phê chia ca như sau (tính cả hai đầu):
#   6:00  đến 11:30  → in "ca sáng"
#   13:00 đến 17:30  → in "ca chiều"
#   18:00 đến 22:00  → in "ca tối"
#   giờ khác         → in "ngoài giờ làm"      ← KHÁC bài meal: lần này CÓ in
#
# Yêu cầu bắt buộc:
#   - Câu hỏi input đúng y:  "Mấy giờ rồi? "
#   - Có hàm convert(time): nhận "13:45" → TRẢ VỀ số 13.75 (return, không print)
#   - main() hỏi, gọi convert, if/elif/else, print
#   - Có if __name__ == "__main__":
#
# Ví dụ:
#   6:00  → ca sáng        11:30 → ca sáng       11:31 → ngoài giờ làm
#   13:45 → ca chiều       22:00 → ca tối        23:15 → ngoài giờ làm
#
# Chạy máy chấm:  python cham_ca_lam.py
#
# Soát đề: OK
# Đã thử thêm: 11:32 -> Ngoài giờ làm
# Kế hoạch (Hỏi / Xử lý / In ra):
def main():
    cau_hoi_dung = input("Mấy giờ rồi? ")
    gio = convert(cau_hoi_dung)
    if 6 <= gio <=11 + 30 / 60:
        print("ca sáng")
    elif 13<= gio <=17 + 30 / 60:
        print("ca chiều")
    elif 18 <= gio <= 22:
        print("ca tối")
    else:
        print("ngoài giờ làm")
def convert(time):
    gio, phut = time.split(":")
    gio = int(gio)
    phut = int(phut)
    return gio + phut / 60
if __name__ =="__main__":
    main()

