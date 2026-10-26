# Soát đề: OK

# convert(text):
#   NHẬN: một chuỗi
#   XỬ LÝ: thay :) bằng 🙂, rồi thay :( bằng 🙁
#   TRẢ VỀ: chuỗi đã thay

# main():
#   ① HỎI: Hỏi người dùng nhập
#   ② XỬ LÝ: gọi convert với dữ liệu vừa nhập
#   ③ IN RA: Kết quả
def convert(text):
    return text.replace(":)","🙂").replace(":(", "🙁")
def main():
    trang_thai = input("Nhập một câu: ")
    ket_qua = convert(trang_thai)
    print(ket_qua)
if __name__ == "__main__":
    main()