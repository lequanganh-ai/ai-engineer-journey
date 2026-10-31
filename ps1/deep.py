# Soát đề: OK
# Đã thử thêm: <100> - <No>
#Hỏi: `What is the Answer to the Great Question of Life, the Universe, and Everything? `
#Xử lí: - Nếu người dùng trả lời 42, hoặc forty-two, hoặc forty two|Mọi câu trả lời khác|
# Xử lí: chuẩn hóa (xóa khoảng trắng 2 đầu + viết thường), rồi so với "42" / "forty-two" / "forty two"
#In ra: Yes/No
tra_loi = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
match tra_loi:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
