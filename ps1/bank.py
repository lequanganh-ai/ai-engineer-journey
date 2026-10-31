# Soát đề: OK
# Đã thử thêm: hello -> $0
# ① HỎI: câu chào (Greeting: )
# ② XỬ LÝ: chuẩn hóa (strip + lower) → bắt đầu bằng "hello"? → $0
#          → không thì bắt đầu bằng "h"? → $20  → còn lại → $100
# ③ IN RA: $0 / $20 / $100
chao = input("Greeting: ").strip().lower()
if chao.startswith("hello"):
    print("$0")
elif chao.startswith("h"):
    print("$20")
else:
    print("$100")