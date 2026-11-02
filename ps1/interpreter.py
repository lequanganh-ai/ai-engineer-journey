# Soát đề: OK
# Đã thử thêm: 20 * 10 -> 200.0
# Hỏi: Expression: người dùng nhập bieuer thức x, y ,z cách nhau bằng dấu cách
# Xử lí: 1: tách chuỗi thành 3 phần bằng split()
#        2:x,z đang là chuỗi cần đổi sang số int
#        3: Dựa vào y để chọn phép tính dùng match vì đã cho giá trị cụ thể
#        4: Tính ra kết quả 
#In ra:1 phép tính đã được tính toán hoàn tất bạn nhé dạng số thực 1 chữ số thập phân {:.1f}
x , y, z = input("Expression: ").split(" ")
x = int(x)
z = int(z)
match y:
    case "+":
        ket_qua = x + z
    case "-":
        ket_qua = x - z
    case "*":
        ket_qua = x * z
    case "/":
        ket_qua = x / z
    case _:
        print("Không có giá trị")
        exit()

print(f"{ket_qua:.1f}")
    