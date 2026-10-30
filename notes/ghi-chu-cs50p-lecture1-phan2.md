# CS50P · LECTURE 1 · CONDITIONALS — PHẦN 2 (từ 34:44 đến hết)

**Tuần 2 · Buổi 2.** Nội dung: dấu `%`, số chẵn/lẻ, hàm trả về `True/False`, viết kiểu "Pythonic", lệnh `match`.

---

## 1. Dấu `%` — chia lấy dư (modulo)

| Phép | Kết quả | Vì sao |
|---|---|---|
| `7 % 2` | `1` | 7 = 2×3 + **1** |
| `8 % 2` | `0` | 8 = 2×4 + **0** |
| `17 % 5` | `2` | 17 = 5×3 + **2** |
| `10 % 3` | `1` | 10 = 3×3 + **1** |
| `4 % 7` | `4` | 4 = 7×0 + **4** (số nhỏ hơn số chia → dư chính nó) |

**Ứng dụng quan trọng nhất:** `a % b == 0` ⇔ **a chia hết cho b**.
- Chẵn: `n % 2 == 0` · Lẻ: `n % 2 == 1` (hoặc `!= 0`)
- Chia hết cho 3: `n % 3 == 0`

---

## 2. Chương trình parity.py — 3 cách viết, từ dài đến gọn

```python
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
```

**Cách 1 — đầy đủ:**
```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

**Cách 2 — một dòng (biểu thức điều kiện):**
```python
def is_even(n):
    return True if n % 2 == 0 else False
```

**Cách 3 — Pythonic (gọn nhất, nên dùng):**
```python
def is_even(n):
    return n % 2 == 0
```
Vì sao được? `n % 2 == 0` **bản thân nó đã là `True` hoặc `False`** → trả về luôn, không cần `if`.

> Quy tắc: thấy `if <điều kiện>: return True else: return False` → rút gọn thành `return <điều kiện>`.

**Đặt tên hàm trả về bool:** bắt đầu bằng `is_` / `la_` / `co_` để đọc như câu hỏi: `is_even(x)` → "x có chẵn không?"

**Gọi hàm bool trong `if`:** viết `if is_even(x):` — **không** cần `== True`.

---

## 3. Lệnh `match` (house.py)

Dùng `if/elif`:
```python
name = input("What's your name? ")
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
```

Dùng `match` (gọn hơn khi so **một biến** với **nhiều giá trị cụ thể**):
```python
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```
- `match <biến>:` rồi các `case <giá trị>:` thụt vào
- `|` nghĩa là **hoặc** (chỉ dùng trong `case`)
- `case _:` = **trường hợp còn lại** (giống `else`) — đặt **cuối cùng**
- Chạy `case` khớp **đầu tiên**, rồi dừng (không chạy tiếp)

**Khi nào dùng gì?**
| Tình huống | Dùng |
|---|---|
| So 1 biến với **giá trị cụ thể** ("Harry", 1, 2, 3) | `match` gọn hơn |
| So sánh **khoảng** (`>= 90`, `< 18.5`) | `if / elif` (`match` không hợp) |

---

## 4. Lỗi hay gặp

| Lỗi | Sai | Đúng |
|---|---|---|
| Dùng `=` thay `==` | `return n % 2 = 0` | `return n % 2 == 0` |
| So sánh thừa | `if is_even(x) == True:` | `if is_even(x):` |
| Trả về chuỗi thay vì bool | `return "True"` | `return True` |
| `case _` đặt đầu | bắt hết mọi thứ | đặt **cuối cùng** |
| Dùng `or` trong case | `case "A" or "B":` | `case "A" \| "B":` |
| Quên `:` | `case "Harry"` | `case "Harry":` |

---

## 5. Tự kiểm tra (gửi Claude trước khi làm bài tập)

1. `23 % 4` = ? `4 % 23` = ?
2. Viết gọn nhất hàm `is_odd(n)` (số lẻ) chỉ bằng 1 dòng `return`.
3. `if is_even(x) == True:` và `if is_even(x):` khác nhau không? Nên viết cách nào?
4. Trong `match`, `case _:` có tác dụng gì? Đặt ở đầu thì chuyện gì xảy ra?
5. Bài xếp loại điểm (`>= 9 → Xuất sắc`…) nên dùng `match` hay `if/elif`? Vì sao?
