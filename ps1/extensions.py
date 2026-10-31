# Soát đề: OK
# Đã thử thêm: note.txt -> text/plain
# ① HỎI: tên file (File name: )
# ② XỬ LÝ: chuẩn hóa (strip + lower) → endswith từng đuôi: gif, jpg/jpeg, png, pdf, txt, zip
#          → không khớp đuôi nào → application/octet-stream
# ③ IN RA: media type tương ứng (image/gif, image/jpeg, ...)
ten_file = input("File name: ").strip().lower()

if ten_file.endswith(".gif"):
    print("image/gif")
elif ten_file.endswith(".jpg") or ten_file.endswith(".jpeg"):
    print("image/jpeg")
elif ten_file.endswith("png"):
    print("image/png")
elif ten_file.endswith("pdf"):
    print("application/pdf")
elif ten_file.endswith("txt"):
    print("text/plain")
elif ten_file.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")