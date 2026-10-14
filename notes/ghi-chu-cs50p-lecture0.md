# Ghi chú CS50P – Lecture 0: Hàm và Biến (Functions, Variables)

> Ghi chú tiếng Việt theo bài giảng CS50P Lecture 0 (David J. Malan, Harvard).
> Bản gốc tiếng Anh: https://cs50.harvard.edu/python/notes/0/
> Phần 1–16: học ở **buổi 1**. Phần 17–18 (`def`, `return`): học ở **buổi 2**.

---

## 1. Viết và chạy chương trình Python

- **VS Code** là trình soạn thảo, nơi bạn viết code.
- **Terminal** là nơi bạn gõ lệnh để chạy chương trình.
- File Python có đuôi `.py`. Chạy bằng lệnh:

```bash
python hello.py
```

```python
print("hello, world")
```

Python đọc file của bạn và chuyển code thành lệnh mà máy tính thực hiện được.

---

## 2. Hàm (function) và đối số (argument)

- **Hàm** là một hành động có sẵn mà Python biết làm. Ví dụ `print` là hàm "in ra màn hình".
- **Đối số** là giá trị bạn đưa vào trong dấu ngoặc `( )` để hàm xử lý.

```python
print("hello, world")
#  ↑ hàm     ↑ đối số
```

---

## 3. Lỗi (bug)

Lỗi là chuyện bình thường, lập trình viên giỏi cũng gặp mỗi ngày.

```python
print("hello, world"     # thiếu dấu ) → SyntaxError
```

Khi gặp lỗi: **đọc thông báo lỗi** trong terminal. Nó thường chỉ ra dòng nào sai và sai gì.

---

## 4. Hàm `input` – hỏi người dùng

`input` hiện một câu hỏi, chờ người dùng gõ, rồi **trả về** (return) chữ người dùng đã gõ.

```python
input("What's your name? ")
```

⚠️ Nếu không lưu kết quả lại thì câu trả lời sẽ mất. Vì vậy cần **biến**.

💡 Nhớ để **một dấu cách sau dấu `?`** để chữ người dùng gõ không dính vào câu hỏi.

---

## 5. Biến (variable)

**Biến** là một "chiếc hộp" có tên, dùng để chứa giá trị.

```python
name = input("What's your name? ")
print("hello,", name)
```

- Dấu `=` **không phải** "bằng" như trong toán. Nó nghĩa là **gán**: lấy giá trị **bên phải** bỏ vào biến **bên trái**.
- Đọc dòng trên là: "hỏi tên người dùng, rồi cất câu trả lời vào biến `name`".

---

## 6. Chú thích (comment)

Dòng bắt đầu bằng `#` là **chú thích**. Python bỏ qua nó, nó chỉ dành cho người đọc code.

```python
# Hỏi tên người dùng
name = input("What's your name? ")

# Chào người dùng
print("hello,", name)
```

Chú thích giúp bạn (và người khác) hiểu code **làm gì và tại sao**.

---

## 7. Mã giả (pseudocode)

Trước khi code, viết **kế hoạch bằng lời** dưới dạng chú thích, rồi điền code vào từng bước:

```python
# Hỏi tên người dùng
# Chào người dùng bằng tên của họ
```

Rất hữu ích khi bạn chưa biết bắt đầu từ đâu.

---

## 8. Hàm nhận nhiều đối số

Các đối số cách nhau bằng dấu phẩy. `print` sẽ tự **thêm một dấu cách** giữa chúng.

```python
print("hello,", name)     # → hello, Lan
```

---

## 9. Chuỗi (string) và tham số (parameter)

- **Chuỗi** (`str`) là kiểu dữ liệu chứa văn bản, viết trong dấu nháy `"..."` hoặc `'...'`.
- **Tham số** là các "nút điều chỉnh" của hàm. Hàm `print` có hai tham số hay dùng:

| Tham số | Mặc định | Ý nghĩa |
|---|---|---|
| `sep` | `" "` (dấu cách) | Ký tự **ngăn cách** giữa các đối số |
| `end` | `"\n"` (xuống dòng) | Ký tự in ra **ở cuối** |

```python
print("hello,", end="")    # không xuống dòng
print(name)                # in tiếp trên cùng dòng

print("2026", "10", "14", sep="-")   # → 2026-10-14
```

`\n` là ký tự **xuống dòng**.

---

## 10. Dấu nháy lồng nhau

Muốn in dấu nháy kép bên trong chuỗi:

```python
print("hello, "friend"")       # ❌ lỗi: Python tưởng chuỗi kết thúc sớm
print('hello, "friend"')       # ✅ cách 1: dùng nháy đơn bên ngoài
print("hello, \"friend\"")     # ✅ cách 2: thêm dấu \ trước dấu nháy (escape)
```

---

## 11. f-string – chèn biến vào chuỗi

Thêm chữ `f` trước dấu nháy, rồi đặt biến trong `{ }`:

```python
print(f"hello, {name}")
```

Đây là cách **gọn và dễ đọc nhất**. Khóa học (và thực tế đi làm) dùng cách này rất nhiều.

---

## 12. Các phương thức (method) của chuỗi

Chuỗi có sẵn nhiều "phương thức", gọi bằng dấu chấm `.`:

| Phương thức | Tác dụng | Ví dụ |
|---|---|---|
| `.strip()` | Xóa khoảng trắng thừa ở **đầu và cuối** | `"  lan  "` → `"lan"` |
| `.title()` | Viết hoa **chữ cái đầu mỗi từ** | `"le quang anh"` → `"Le Quang Anh"` |
| `.capitalize()` | Viết hoa chữ cái đầu **của cả câu** | `"le quang anh"` → `"Le quang anh"` |
| `.lower()` / `.upper()` | Chuyển thành chữ thường / chữ hoa | `"AI"` → `"ai"` |

Có thể **nối nhiều phương thức** liên tiếp:

```python
name = input("What's your name? ").strip().title()
```

💡 Bài học quan trọng: **người dùng hay gõ "lộn xộn"**, nên luôn làm sạch dữ liệu họ nhập. Đây cũng là việc đầu tiên khi làm dữ liệu cho AI!

---

## 13. Số nguyên (`int`)

⚠️ **Bẫy quan trọng:** `input` luôn trả về **chuỗi**, kể cả khi người dùng gõ số.

```python
x = input("What's x? ")    # gõ 1
y = input("What's y? ")    # gõ 2
print(x + y)               # → 12  (nối chuỗi "1" + "2", không phải cộng số!)
```

Giải pháp: **ép kiểu** sang số nguyên bằng `int()`:

```python
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)               # → 3 ✅
```

Hàm lồng nhau chạy **từ trong ra ngoài**: `input(...)` chạy trước, rồi `int(...)` đổi kết quả thành số.

Các phép toán: `+` cộng, `-` trừ, `*` nhân, `/` chia, `%` chia lấy dư.

---

## 14. Dễ đọc là ưu tiên số 1

Một bài có nhiều cách giải. Hãy chọn cách **dễ đọc nhất**, đừng cố viết thật ngắn mà khó hiểu.

```python
# Dễ đọc hơn
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)

# Ngắn hơn nhưng khó đọc
print(int(input("What's x? ")) + int(input("What's y? ")))
```

---

## 15. Số thực (`float`)

`float` là số **có phần thập phân**, ví dụ `1.5`, `3.14`.

```python
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)          # làm tròn đến số nguyên gần nhất
print(f"{z:,}")           # dấu phẩy ngăn cách hàng nghìn: 1000 → 1,000
```

---

## 16. Làm tròn số thực

```python
z = x / y
print(round(z, 2))        # cách 1: làm tròn 2 chữ số thập phân
print(f"{z:.2f}")         # cách 2: định dạng trong f-string, hiển thị 2 chữ số
```

Ví dụ `2 / 3` → `0.67`.

---

## 17. `def` – tự tạo hàm *(học ở buổi 2)*

```python
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):     # "world" là giá trị mặc định
    print("hello,", to)

main()                     # phải gọi main() thì chương trình mới chạy
```

- **Thụt lề** (4 dấu cách) cho biết dòng nào nằm **bên trong** hàm.
- Tham số có thể có **giá trị mặc định**.

---

## 18. `return` – trả giá trị về *(học ở buổi 2)*

```python
def square(n):
    return n * n

x = int(input("What's x? "))
print("x squared is", square(x))
```

- `print` chỉ **hiện ra màn hình**.
- `return` **gửi giá trị về** cho nơi gọi hàm, để lưu vào biến hoặc dùng tiếp.

---

## Tóm tắt nhanh

| Khái niệm | Nhớ trong 1 câu |
|---|---|
| Hàm | Hành động có sẵn, ví dụ `print`, `input` |
| Đối số | Giá trị đưa vào trong `( )` |
| Biến | Hộp có tên chứa giá trị; `=` là **gán** |
| Chú thích | Dòng bắt đầu bằng `#`, Python bỏ qua |
| `str` | Văn bản, trong dấu nháy |
| `sep`, `end` | Điều chỉnh cách `print` ngăn cách và kết thúc |
| f-string | `f"... {bien} ..."` để chèn biến |
| `.strip()`, `.title()` | Làm sạch, chuẩn hóa chữ |
| `int`, `float` | Số nguyên, số thực; `input` luôn trả về chuỗi |
| `round(x, 2)` / `:.2f` | Làm tròn 2 chữ số thập phân |

## Tự kiểm tra (trả lời không cần nhìn ghi chú)

1. Vì sao `print(x + y)` ra `12` thay vì `3` khi người dùng gõ 1 và 2?
2. Dấu `=` trong `name = "Lan"` nghĩa là gì?
3. Viết một dòng in ra `2026/10/14` từ 3 giá trị `"2026"`, `"10"`, `"14"`.
4. Khác nhau giữa `.title()` và `.capitalize()`?
5. Hai cách in số `0.6666...` thành `0.67`?

## Từ vựng tiếng Anh nên nhớ

function (hàm) · argument (đối số) · parameter (tham số) · variable (biến) · assign (gán) · string (chuỗi) · integer (số nguyên) · float (số thực) · comment (chú thích) · bug (lỗi) · return value (giá trị trả về) · method (phương thức) · cast (ép kiểu)
