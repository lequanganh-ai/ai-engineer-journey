# CS50P · PROBLEM SET 0 — ĐỀ BÀI TIẾNG VIỆT

Đề gốc (tiếng Anh): cs50.harvard.edu/python → Problem Set 0
Ghi chú này **tóm tắt đề bằng tiếng Việt**. Mỗi bài có thêm bảng **từ vựng tiếng Anh** — mở đề gốc đặt cạnh, đọc song song để quen dần.

- **Buổi 3:** bài 1–3 (Indoor Voice, Playback Speed, Making Faces)
- **Buổi 4:** bài 4–5 (Einstein, Tip Calculator)

---

## Cách làm mỗi bài

1. Tạo file **đúng tên** trong thư mục `ps0/`
2. Dòng đầu file: `# Soát đề: ...` → chỉ đổi thành `# Soát đề: OK` sau khi đã so kết quả với ví dụ
3. Viết **comment kế hoạch** trước, code sau
4. Tự chạy thử với các ví dụ trong ghi chú + **tự nghĩ thêm 1 ví dụ**
5. Chạy máy chấm: `python cham_ps0.py` (đứng trong thư mục `ps0/`)
6. Dán code + kết quả gửi Claude để review

> Đề **không quy định** câu hỏi trong `input()` → bạn được tự đặt, ví dụ `input("Nhập câu: ")`.
> Nhưng phần **in ra** phải đúng y như ví dụ.

---

## BÀI 1 · Indoor Voice — `indoor.py`

**Bối cảnh:** "Indoor voice" = giọng nói nhỏ khi ở trong nhà. Viết HOA giống như đang hét — chương trình này giúp người ta "nói nhỏ lại".

**Yêu cầu:**
- Hỏi người dùng nhập một câu
- In ra **đúng câu đó** nhưng **viết thường toàn bộ**
- Khoảng trắng, dấu câu giữ nguyên

**Ví dụ:**

| Nhập | In ra |
|---|---|
| `HELLO` | `hello` |
| `THIS IS CS50` | `this is cs50` |
| `50` | `50` |

**Gợi ý:** phương thức chuỗi bạn đã học ở buổi 1.

| Từ tiếng Anh | Nghĩa |
|---|---|
| prompt the user for input | hỏi người dùng nhập (dùng `input`) |
| output | in ra |
| lowercase / uppercase | chữ thường / chữ hoa |
| whitespace | khoảng trắng |

---

## BÀI 2 · Playback Speed — `playback.py`

**Bối cảnh:** Một số người xem video ở tốc độ 1.5x, 2x. Bài này "mô phỏng" việc nói **chậm lại** bằng cách chèn dấu chấm giữa các từ.

**Yêu cầu:**
- Hỏi người dùng nhập một câu
- In ra câu đó, nhưng **mỗi dấu cách được thay bằng `...`** (3 dấu chấm, không có dấu cách)

**Ví dụ:**

| Nhập | In ra |
|---|---|
| `This is CS50` | `This...is...CS50` |
| `This is our week on functions` | `This...is...our...week...on...functions` |
| `Let's implement a function called hello` | `Let's...implement...a...function...called...hello` |

**Gợi ý — kiến thức MỚI:** phương thức `.replace(cái_cũ, cái_mới)` — thay mọi chỗ có `cái_cũ` bằng `cái_mới`:

```python
"a-b-c".replace("-", "+")     # "a+b+c"
```

Đây là lần đầu bạn **tự áp dụng một hàm mới** từ ví dụ — đúng kỹ năng "đọc tài liệu gốc".

| Từ tiếng Anh | Nghĩa |
|---|---|
| replace | thay thế |
| space | dấu cách |
| period | dấu chấm |
| sequence of three periods | chuỗi 3 dấu chấm `...` |

---

## BÀI 3 · Making Faces — `faces.py`

**Bối cảnh:** Ngày xưa người ta gõ `:)` và `:(` thay cho mặt cười. Bài này đổi chúng thành emoji thật.

**Yêu cầu — 2 hàm:**

1. **`convert(text)`**
   - Nhận vào một chuỗi
   - **Trả về (return)** chuỗi đó, trong đó:
     - mọi `:)` đổi thành 🙂
     - mọi `:(` đổi thành 🙁
     - phần chữ khác **giữ nguyên**
2. **`main()`**
   - Hỏi người dùng nhập
   - **Gọi `convert`** với dữ liệu vừa nhập
   - **In ra** kết quả
3. Cuối file gọi `main()` (dùng `if __name__ == "__main__":` như bạn đã học)

**Ví dụ:**

| Nhập | In ra |
|---|---|
| `Hello :)` | `Hello 🙂` |
| `Goodbye :(` | `Goodbye 🙁` |
| `Hello :) Goodbye :(` | `Hello 🙂 Goodbye 🙁` |

**Gợi ý:**
- `convert` dùng **return**, `main` dùng **print** — đúng bài học buổi 2
- Có 2 thứ cần đổi → có thể gọi `.replace` **2 lần**
- Copy emoji từ ghi chú này: 🙂 🙁

| Từ tiếng Anh | Nghĩa |
|---|---|
| implement a function | viết (cài đặt) một hàm |
| accepts a str as input | nhận vào một chuỗi (tham số) |
| returns | trả về |
| converted to | được đổi thành |
| all other text unchanged | chữ còn lại giữ nguyên |

---

## BÀI 4 · Einstein — `einstein.py`  *(buổi 4)*

**Bối cảnh:** Công thức nổi tiếng **E = mc²** — năng lượng (E, đơn vị Joule) bằng khối lượng (m, kg) nhân bình phương tốc độ ánh sáng (c).

**Yêu cầu:**
- Hỏi người dùng nhập khối lượng **m** (số **nguyên**, kg)
- In ra năng lượng **E** (số **nguyên**)
- Dùng **c = 300000000** (mét/giây)

**Ví dụ:**

| Nhập | In ra |
|---|---|
| `1` | `90000000000000000` |
| `14` | `1260000000000000000` |
| `50` | `4500000000000000000` |

**Gợi ý:** bình phương là `** 2`. In ra số **không có dấu phẩy**.

| Từ tiếng Anh | Nghĩa |
|---|---|
| mass | khối lượng |
| integer | số nguyên |
| equivalent | tương đương |
| speed of light | tốc độ ánh sáng |
| squared | bình phương |

---

## BÀI 5 · Tip Calculator — `tip.py`  *(buổi 4)*

**Bối cảnh:** Ở Mỹ, ăn nhà hàng xong phải để lại **tiền tip** (tiền boa), thường 15–20% hóa đơn.

**Đề cho sẵn hàm `main` (chép y nguyên vào file):**

```python
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main()
```

**Bạn viết 2 hàm:**
1. **`dollars_to_float(d)`** — nhận chuỗi dạng `"$50.00"`, **bỏ dấu `$` ở đầu**, trả về **số thực** `50.0`
2. **`percent_to_float(p)`** — nhận chuỗi dạng `"15%"`, **bỏ dấu `%` ở cuối**, trả về **số thực dạng thập phân** `0.15` (tức là chia 100)

**Ví dụ:**

| Nhập (hóa đơn, phần trăm) | In ra |
|---|---|
| `$50.00`, `15%` | `Leave $7.50` |
| `$100.00`, `18%` | `Leave $18.00` |
| `$15.00`, `25%` | `Leave $3.75` |

**Gợi ý:** `.replace` (bài 2) hoặc tra thêm `.removeprefix()` / `.removesuffix()`. Rồi `float(...)`.

| Từ tiếng Anh | Nghĩa |
|---|---|
| tip | tiền boa |
| meal | bữa ăn |
| percentage | phần trăm |
| leading `$` | dấu `$` ở đầu |
| trailing `%` | dấu `%` ở cuối |
| TODO | "việc cần làm" — chỗ bạn phải viết code |

---

## Cảnh báo

Trên mạng có rất nhiều repo GitHub chứa sẵn lời giải Problem Set 0. **Không mở.** Chép lời giải = mất phần quan trọng nhất, và CS50 coi đó là vi phạm học thuật.
