# CS50P · PROBLEM SET 1 — BÀI 4–5 (tiếng Việt)

Kiến thức MỚI của cả 2 bài: **`.split()` — tách chuỗi thành nhiều phần**.

---

## Kiến thức mới: `.split()` và "unpacking" (gán nhiều biến cùng lúc)

```python
"1 + 1".split(" ")      # ["1", "+", "1"]      ← tách tại mỗi dấu cách → 3 phần
"7:30".split(":")       # ["7", "30"]          ← tách tại dấu ":" → 2 phần
```
Kết quả là một **danh sách** các chuỗi (list — học kỹ ở tuần 3).

**Gán thẳng vào nhiều biến** (David dùng trong bài giảng):
```python
x, y, z = "1 + 1".split(" ")     # x = "1", y = "+", z = "1"
gio, phut = "7:30".split(":")    # gio = "7", phut = "30"
```
- Số biến bên trái **phải bằng** số phần sau khi tách, không thì báo lỗi
- Mỗi phần vẫn là **CHUỖI** → muốn tính toán phải `int()` / `float()`

Tài liệu gốc: docs.python.org → `str.split(sep=None, maxsplit=-1)`: *"Return a list of the words in the string, using sep as the delimiter string."* — trả về danh sách các phần, cắt tại chuỗi `sep`.

---

## BÀI 4 · Math Interpreter — `interpreter.py`

**Yêu cầu:**
- Hỏi: `Expression: ` — người dùng nhập biểu thức dạng `x y z`, cách nhau bằng **dấu cách**
  - `x`, `z` là **số nguyên**; `y` là một trong `+`  `-`  `*`  `/`
- In ra kết quả dạng **số thực, 1 chữ số thập phân**

| Nhập | In ra |
|---|---|
| `1 + 1` | `2.0` |
| `2 - 3` | `-1.0` |
| `2 * 2` | `4.0` |
| `50 / 5` | `10.0` |

(Đề đảm bảo không chia cho 0, luôn đúng dạng `x y z`.)

**Gợi ý:** tách → đổi x, z sang số → `match y` (giá trị cụ thể!) → in với `:.1f`.

| Từ tiếng Anh | Nghĩa |
|---|---|
| arithmetic expression | biểu thức số học |
| operator | toán tử (+ - * /) |
| formatted to one decimal place | định dạng 1 chữ số thập phân |

---

## BÀI 5 · Meal Time — `meal.py`

**Yêu cầu:**
- Hỏi: `What time is it? ` — giờ dạng 24h, ví dụ `7:30`, `12:00`, `18:45`
- In:
  - `breakfast time` nếu từ **7:00 đến 8:00** (tính cả 2 đầu)
  - `lunch time` nếu từ **12:00 đến 13:00**
  - `dinner time` nếu từ **18:00 đến 19:00**
  - Giờ khác → **không in gì cả**
- **BẮT BUỘC cấu trúc** (đề gốc yêu cầu đúng như vậy):
```python
def main():
    ...


def convert(time):
    ...


if __name__ == "__main__":
    main()
```
- `convert(time)` nhận chuỗi `"7:30"` → **trả về số thực** số giờ: `7.5`
  - `"7:00"` → `7.0`, `"7:30"` → `7.5`, `"18:45"` → `18.75`
  - Công thức: giờ + phút / 60

| Nhập | In ra |
|---|---|
| `7:00` | `breakfast time` |
| `7:30` | `breakfast time` |
| `8:00` | `breakfast time` |
| `12:42` | `lunch time` |
| `18:32` | `dinner time` |
| `11:11` | *(không in gì)* |

| Từ tiếng Anh | Nghĩa |
|---|---|
| 24-hour time | giờ 24h |
| convert | chuyển đổi |
| inclusive | tính cả 2 đầu mút |
