# CS50P · LECTURE 1 · CONDITIONALS (ĐIỀU KIỆN) — PHẦN 1

**Tuần 2 · Buổi 1.** Video: cs50.harvard.edu/python → Lecture 1 (Conditionals)
Hôm nay xem **từ đầu đến hết phần chấm điểm (grade.py)** — dừng **trước** phần "parity" (số chẵn/lẻ, dấu `%`). Ghi lại phút bạn dừng.

Đến giờ chương trình của bạn **chạy thẳng từ trên xuống**. Hôm nay chương trình biết **rẽ nhánh**: *nếu* điều kiện đúng thì làm việc này, *không thì* làm việc khác.

---

## 1. Toán tử so sánh — kết quả luôn là `True` hoặc `False`

| Viết | Nghĩa | Ví dụ | Kết quả |
|---|---|---|---|
| `==` | bằng | `5 == 5` | `True` |
| `!=` | khác | `5 != 3` | `True` |
| `<` | nhỏ hơn | `2 < 1` | `False` |
| `>` | lớn hơn | `2 > 1` | `True` |
| `<=` | nhỏ hơn hoặc bằng | `5 <= 5` | `True` |
| `>=` | lớn hơn hoặc bằng | `4 >= 5` | `False` |

`True` / `False` là kiểu dữ liệu mới: **bool** (giá trị đúng/sai). Viết hoa chữ đầu, **không** có dấu nháy.

### ⚠️ `=` khác `==`
```python
x = 5        # GÁN: bỏ 5 vào x
x == 5       # SO SÁNH: x có bằng 5 không? → True
```
Viết `if x = 5:` → **SyntaxError**.

---

## 2. `if` — nếu

```python
x = int(input("x: "))
y = int(input("y: "))

if x < y:
    print("x nhỏ hơn y")
```
- Dòng `if` **kết thúc bằng dấu `:`**
- Code chạy khi điều kiện đúng phải **thụt vào 4 dấu cách** (giống thân hàm)
- Điều kiện sai → bỏ qua cả khối thụt vào

---

## 3. Ba `if` riêng lẻ vs `if / elif / else`

**Cách 1 — ba `if` riêng (David viết đầu tiên):**
```python
if x < y:
    print("x nhỏ hơn y")
if x > y:
    print("x lớn hơn y")
if x == y:
    print("x bằng y")
```
Chạy **đúng**, nhưng Python **kiểm tra cả 3 câu** kể cả khi câu đầu đã đúng → lãng phí.

**Cách 2 — `elif` (else if = "không thì nếu"):**
```python
if x < y:
    print("x nhỏ hơn y")
elif x > y:
    print("x lớn hơn y")
elif x == y:
    print("x bằng y")
```
Gặp câu **đúng đầu tiên** → chạy khối đó rồi **bỏ qua toàn bộ phần còn lại**.

**Cách 3 — `else` (không thì):**
```python
if x < y:
    print("x nhỏ hơn y")
elif x > y:
    print("x lớn hơn y")
else:
    print("x bằng y")
```
Không nhỏ hơn, không lớn hơn → chắc chắn bằng. `else` **không có điều kiện**, bắt mọi trường hợp còn lại.

> **Quy tắc:** một chuỗi `if → elif → elif → else` thì **chỉ đúng MỘT khối được chạy**.

---

## 4. `or` và `and`

**`or` (hoặc)** — đúng khi **ít nhất 1** vế đúng:
```python
if x < y or x > y:
    print("x khác y")
else:
    print("x bằng y")
```
(Gọn hơn nữa: `if x != y:`)

**`and` (và)** — đúng khi **cả 2** vế đều đúng:
```python
if score >= 90 and score <= 100:
    print("Grade: A")
```

| `A` | `B` | `A or B` | `A and B` |
|---|---|---|---|
| True | True | True | True |
| True | False | True | False |
| False | True | True | False |
| False | False | False | False |

---

## 5. So sánh nối liền (chained comparison) — kiểu Python

```python
if 90 <= score <= 100:      # giống hệt: score >= 90 and score <= 100
```
Đọc như toán học: "score nằm từ 90 đến 100".

---

## 6. Chấm điểm (grade.py) — THỨ TỰ elif rất quan trọng

**Cách gọn (David viết cuối):**
```python
score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```
Vì sao `elif score >= 80` không cần thêm `and score < 90`? → Nếu score ≥ 90 thì đã vào nhánh A rồi, **không bao giờ xuống tới đây**. Tới được dòng này nghĩa là score **chắc chắn < 90**.

### ⚠️ Đảo thứ tự là SAI
```python
if score >= 60:          # 95 ≥ 60 → đúng NGAY → in "D" ❌
    print("Grade: D")
elif score >= 90:        # không bao giờ tới
    print("Grade: A")
```
> **Quy tắc:** với `>=`, xếp **từ lớn đến nhỏ**. Điều kiện **chặt nhất** đứng **đầu**.

---

## 7. Điều kiện trong hàm (nối với buổi 2 tuần 1)

```python
def ket_qua(diem):
    if diem >= 5:
        return "Đậu"
    else:
        return "Rớt"
```
- Mỗi nhánh có `return` riêng
- `return` chạy là **thoát hàm ngay**, các dòng sau không chạy
- Hàm cũng có thể **trả về bool**:
```python
def trong_khoang(x):
    return 1 <= x <= 10        # trả về True hoặc False trực tiếp
```

---

## 8. Lỗi hay gặp

| Lỗi | Sai | Đúng |
|---|---|---|
| Dùng `=` để so sánh | `if x = 5:` | `if x == 5:` |
| Quên dấu `:` | `if x > 5` | `if x > 5:` |
| Quên thụt lề | `print` sát lề dưới `if` | thụt 4 dấu cách |
| So chuỗi với số | `input("x: ") > 5` → TypeError | `int(input("x: ")) > 5` |
| Thứ tự `elif` sai | `>= 60` đứng trước `>= 90` | lớn → nhỏ |
| `or` viết tắt sai | `if thu == "T7" or "CN":` (luôn True!) | `if thu == "T7" or thu == "CN":` |
| So chuỗi khác hoa/thường | `"An" == "an"` → `False` | chuẩn hóa trước: `.lower()` |

---

## 9. Tự kiểm tra (trả lời trước khi làm bài tập)

1. `5 == 5.0` cho ra gì? `"5" == 5` cho ra gì?
2. Một chuỗi `if / elif / elif / else` có thể chạy **hai** khối cùng lúc không? Vì sao?
3. `if score >= 80` ở dòng `elif` của grade.py: tại sao không cần viết `score < 90`?
4. `True and False or True` cho ra gì? (gợi ý: `and` được tính trước `or`)
5. Vì sao `if thu == "Thứ Bảy" or "Chủ nhật":` luôn đúng?

---

## Buổi sau (buổi 2)
Phần còn lại của Lecture 1: dấu `%` và số chẵn/lẻ, hàm trả về `True/False` kiểu "Pythonic", lệnh `match`.
