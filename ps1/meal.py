# Soát đề: OK
# Đã thử thêm: 12:30 -> lunch time
# Hỏi:What time is it?
# Xử lí:1: 7 <= gio <= 8  → breakfast time
#từ 12 <=gio<= 13 là lunch time
#từ 18 <=gio<= 19 đó là dinner time
# Giờ khác - còn lại :Không in gì cả
#        2: Làm theo cấu trúc bắt buộc của đề def main()->def convert(time)->if....
#        3:convert(time) nhận chuỗi -> trả về số thực 7.5  dổi bằng đấu hai chấm chuỗi đổi thành int
#        4:công thức:gio + phut /60
#Bài này dùng if/elif vi nó cho khoảng thời gian 
#In ra:theo những mốc thời gian xử lí
def main():
    cau_tra_loi = input("What time is it? ")
    gio = convert(cau_tra_loi)
    if 7<= gio <= 8:
        print("breakfast time")
    elif 12 <= gio <= 13:
        print("lunch time")
    elif 18<= gio <= 19:
        print("dinner time")
def convert(time):
    gio ,phut = time.split(":")
    gio = int(gio)
    phut = int(phut)
    return gio + phut /60
if __name__ == "__main__":
    main()