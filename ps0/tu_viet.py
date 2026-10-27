# =================================================================
# BUỔI 5 · PHẦN B · TỰ VIẾT TỪ ĐẦU (không khung, không nhìn mẫu)
# =================================================================
# Viết chương trình TẠO HASHTAG.
#
# Yêu cầu:
#   1. Hàm  tao_hashtag(chu_de)
#        - xóa khoảng trắng hai đầu
#        - viết hoa chữ đầu mỗi từ
#        - bỏ HẾT dấu cách
#        - thêm dấu # ở đầu
#        - TRẢ VỀ chuỗi kết quả
#        tao_hashtag("  hoc python moi ngay ")  → "#HocPythonMoiNgay"
#
#   2. Hàm  main()
#        - hỏi bằng input:  "Chủ đề: "
#        - gọi tao_hashtag
#        - in ra kết quả (chỉ 1 dòng, ví dụ:  #HocPythonMoiNgay )
#
#   3. Cuối file gọi main() đúng chuẩn.
#
# Tự viết: dòng soát đề, comment kế hoạch, toàn bộ code.
# Chạy thử:  python tu_viet.py
# =================================================================
# Soát đề: OK
#Hỏi gì: tạo 1 hàm hashtag
def tao_hashtag(chu_de):
    #Xử lí:xóa khoảng trắng hai đầu,viết hoa chữ đầu, bỏ hết dấu cách, thêm dấu # ở đầu
    #in ra chuỗi kết quả như dòng dưới
    return f"#{chu_de.strip().title().replace(" ", "")}"
def main():
    #Hỏi bằng input
    cau_hoi = input("Chủ đề: ")
    goi = tao_hashtag(cau_hoi)
    print(f"{goi}")
if __name__ =="__main__":
    main()
