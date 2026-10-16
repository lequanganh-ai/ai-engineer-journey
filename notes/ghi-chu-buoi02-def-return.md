# Ghi chú Buổi 2 – Tự viết hàm: `def` và `return`

> Theo CS50P Lecture 0, đoạn từ 1:26:19 đến hết video ("Def" và "Returning Values").
> Bản gốc tiếng Anh: https://cs50.harvard.edu/python/notes/0/ (mục *Def* và *Returning Values*)

---

## 1. Vì sao cần tự viết hàm?

Ở buổi 1 bạn đã **dùng** hàm có sẵn của Python: `print`, `input`, `int`, `round`…
Buổi 2 bạn học cách **tự tạo hàm của riêng mình**.

Lợi ích:
- **Không lặp code.** Viết một lần, gọi bao nhiêu lần cũng được.
- **Đặt tên cho một việc.** Gặp `chao(ten)` là hiểu ngay đoạn code đó làm gì.
- **Chia nhỏ bài toán.** Một chương trình lớn là nhiều hàm nhỏ ghép lại. Code AI sau này cũng viết theo cách này.

---

## 2. Cấu trúc một hàm

```python
def hello(to):
    print("hello,", to)
```

| Phần | Ý nghĩa |
|---|---|
| `def` | Từ khóa báo "tôi đang **định nghĩa** (define) một hàm" |
| `hello` | **Tên hàm**, do bạn tự đặt |
| `(to)` | **Tham số**: "chỗ trống" để nhận dữ liệu khi hàm được gọi |
| `:` | Dấu hai chấm **bắt buộc** ở cuối dòng `def` |
| Dòng thụt vào | **Thân hàm**: những việc hàm sẽ làm |

### Thụt lề (indentation) – cực kỳ quan trọng

Python dùng **thụt lề 4 dấu cách** (hoặc phím Tab) để biết dòng nào **nằm trong hàm**.

```python
def hello(to):
    print("hello,", to)    # ← thụt vào: nằm TRONG hàm

print("xong")              # ← không thụt: nằm NGOÀI hàm
```

⚠️ Sai thụt lề sẽ gặp lỗi `IndentationError`.

💡 Bạn làm web nên sẽ thấy quen: JavaScript dùng `{ }` để đánh dấu khối code, còn Python dùng **thụt lề**.

---

## 3. Định nghĩa hàm và gọi hàm

**Định nghĩa** (`def`) mới chỉ là *dạy* Python cách làm một việc. **Gọi** hàm mới thực sự *làm* việc đó.

```python
def hello(to):          # 1. Định nghĩa: chưa chạy gì cả
    print("hello,", to)

hello("Lan")            # 2. Gọi hàm: lúc này mới in ra "hello, Lan"
hello("Minh")           #    Gọi lại lần nữa: in ra "hello, Minh"
```

⚠️ Phải **định nghĩa trước rồi mới gọi**. Gọi hàm trước khi nó được định nghĩa sẽ báo lỗi `NameError: name 'hello' is not defined`.

---

## 4. Tham số và đối số

Hai từ này hay bị nhầm:

| | Tham số (parameter) | Đối số (argument) |
|---|---|---|
| Là gì | **Tên biến** trong dòng `def` | **Giá trị thật** truyền vào khi gọi |
| Ví dụ | `to` trong `def hello(to):` | `"Lan"` trong `hello("Lan")` |
| Hình dung | Cái **hộp rỗng** có dán nhãn | **Đồ vật** bỏ vào hộp |

Hàm có thể có **nhiều tham số**, cách nhau bằng dấu phẩy:

```python
def gioi_thieu(ten, que):
    print(f"{ten} đến từ {que}.")

gioi_thieu("Lan", "Bắc Ninh")    # ten = "Lan", que = "Bắc Ninh"
```

---

## 5. Giá trị mặc định (default value)

Gán sẵn giá trị cho tham số. Nếu khi gọi **không truyền** đối số, hàm sẽ dùng giá trị mặc định.

```python
def hello(to="world"):
    print("hello,", to)

hello()          # → hello, world   (dùng mặc định)
hello("Lan")     # → hello, Lan     (dùng giá trị truyền vào)
```

Bạn đã gặp điều này ở buổi 1 mà không để ý: `print` có tham số `sep=" "` và `end="\n"` với giá trị mặc định!

---

## 6. Hàm `main()` – cách tổ chức chương trình

Thầy Malan giới thiệu cách viết **chuẩn**: đặt phần chính của chương trình vào hàm `main()`, các hàm phụ viết bên dưới, và **gọi `main()` ở cuối file**.

```python
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()
```

**Vì sao phải gọi `main()` ở cuối?**
Python đọc file **từ trên xuống dưới**:
1. Gặp `def main():` → ghi nhớ hàm `main` (chưa chạy).
2. Gặp `def hello(...):` → ghi nhớ hàm `hello` (chưa chạy).
3. Gặp `main()` → **bây giờ mới chạy**. Lúc này cả hai hàm đều đã được định nghĩa, nên `main` gọi được `hello`.

⚠️ Quên dòng `main()` ở cuối thì chương trình chạy xong **không làm gì cả**, không báo lỗi gì.

💡 Trong các file bài tập bạn sẽ thấy cách viết đầy đủ hơn:
```python
if __name__ == "__main__":
    main()
```
Nghĩa là: "chỉ chạy `main()` khi file này được chạy trực tiếp". Máy chấm điểm cần dòng này để đọc hàm của bạn mà không tự chạy `input()`. Hiện bạn chỉ cần biết nó có tác dụng giống `main()`. Phần này CS50P sẽ giải thích kỹ ở các tuần sau.

---

## 7. Phạm vi biến (scope)

Biến tạo **bên trong** một hàm chỉ tồn tại **trong hàm đó**.

```python
def main():
    name = input("What's your name? ")
    hello()


def hello():
    print("hello,", name)    # ❌ NameError: hàm hello không "nhìn thấy" name của main


main()
```

Cách đúng là **truyền giá trị qua tham số**:

```python
def main():
    name = input("What's your name? ")
    hello(name)              # ✅ đưa name vào hàm hello


def hello(to):
    print("hello,", to)
```

💡 Hình dung mỗi hàm là **một căn phòng kín**. Muốn đưa đồ vào phòng thì phải đưa qua "cửa", tức là qua tham số.

---

## 8. `return` – trả giá trị về

Đây là phần **quan trọng nhất** của buổi 2.

```python
def square(n):
    return n * n


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


main()
```

Khi gặp `return`, hàm:
1. **Dừng lại** ngay (các dòng sau `return` trong hàm sẽ không chạy).
2. **Gửi giá trị về** đúng chỗ đã gọi hàm.

Hình dung `square(x)` như một chiếc máy: bỏ `3` vào, máy **trả ra** `9`. Sau đó bạn muốn làm gì với số 9 cũng được.

```python
ket_qua = square(3)          # lưu vào biến
print(square(3) + 1)         # dùng trong phép tính → 10
print(square(square(2)))     # lồng nhau: square(4) → 16
```

---

## 9. `print` khác `return` thế nào? ⭐

Người mới học hay nhầm điều này nhất:

| | `print` | `return` |
|---|---|---|
| Làm gì | **Hiện** ra màn hình cho **người** xem | **Gửi** giá trị về cho **code** dùng tiếp |
| Sau đó dùng tiếp được không? | ❌ Không | ✅ Có (lưu biến, tính toán…) |
| Hàm dừng lại? | Không | **Có**, dừng ngay |

Ví dụ thấy rõ sự khác nhau:

```python
def binh_phuong_print(n):
    print(n * n)

def binh_phuong_return(n):
    return n * n

a = binh_phuong_print(3)     # màn hình hiện 9, nhưng a = None ❗
b = binh_phuong_return(3)    # màn hình không hiện gì, nhưng b = 9 ✅

print(b + 1)                 # → 10
print(a + 1)                 # ❌ TypeError: không cộng được None với 1
```

`None` là giá trị Python tự trả về khi hàm **không có `return`**, nghĩa là "không có gì".

💡 **Quy tắc vàng:** hàm *tính toán* thì dùng `return`. Chỉ `print` ở nơi cần hiện kết quả cho người dùng, thường là trong `main()`.

---

## 10. Hàm gọi hàm khác

Hàm có thể dùng kết quả của hàm khác:

```python
def doi_sang_f(c):
    return c * 9 / 5 + 32


def mo_ta_nhiet_do(c):
    f = doi_sang_f(c)                  # gọi hàm khác
    return f"{c}°C = {f:.1f}°F"


print(mo_ta_nhiet_do(37))              # → 37°C = 98.6°F
```

Chia việc thành **nhiều hàm nhỏ, mỗi hàm làm một việc** giúp code dễ đọc và dễ sửa.

---

## Lỗi hay gặp

| Lỗi | Nguyên nhân | Cách sửa |
|---|---|---|
| `IndentationError` | Thụt lề sai hoặc không đều | Thụt đúng 4 dấu cách cho thân hàm |
| `SyntaxError` ở dòng `def` | Quên dấu `:` cuối dòng | `def ten(n):` |
| `NameError: name '...' is not defined` | Gọi hàm trước khi định nghĩa, hoặc dùng biến của hàm khác | Định nghĩa trước; truyền qua tham số |
| Chạy file mà không có gì xảy ra | Quên gọi `main()` ở cuối | Thêm `main()` |
| Kết quả là `None` | Hàm dùng `print` thay vì `return` | Đổi thành `return` |
| `TypeError: missing 1 required positional argument` | Gọi hàm thiếu đối số | Truyền đủ đối số, hoặc đặt giá trị mặc định |

---

## Tóm tắt nhanh

| Khái niệm | Nhớ trong 1 câu |
|---|---|
| `def` | Tạo hàm mới |
| Thụt lề | 4 dấu cách đánh dấu thân hàm |
| Tham số / đối số | Hộp rỗng trong `def` / đồ vật truyền vào khi gọi |
| Giá trị mặc định | `def f(x="world")`: không truyền thì dùng mặc định |
| `main()` | Hàm chính, nhớ gọi ở cuối file |
| Phạm vi | Biến trong hàm nào chỉ sống trong hàm đó |
| `return` | Dừng hàm và gửi giá trị về |
| `None` | Giá trị khi hàm không có `return` |

## Tự kiểm tra (trả lời không cần nhìn ghi chú)

1. Đoạn code sau in ra gì? Vì sao?
   ```python
   def f(x):
       print(x * 2)
   y = f(5)
   print(y)
   ```
2. Sửa hàm trên để `print(y)` in ra `10`.
3. Vì sao chương trình có `def main():` mà thiếu dòng `main()` ở cuối thì không chạy gì?
4. Viết hàm `chao(ten="bạn")` trả về `"Xin chào, <ten>!"`. Gọi `chao()` thì được gì?
5. Đoạn code sau lỗi gì? Sửa thế nào?
   ```python
   def main():
       tuoi = 20
       in_tuoi()

   def in_tuoi():
       print(tuoi)

   main()
   ```

## Từ vựng tiếng Anh nên nhớ

define (định nghĩa) · call (gọi) · parameter (tham số) · argument (đối số) · default value (giá trị mặc định) · indentation (thụt lề) · scope (phạm vi) · return value (giá trị trả về) · side effect (tác dụng phụ, ví dụ in ra màn hình) · `None`
