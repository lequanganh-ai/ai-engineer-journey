# TỔNG HỢP CẦN NHỚ · BUỔI 1 + 2

Đọc lại file này **trước mỗi bài kiểm tra**. Mỗi mục đều có: quy tắc, ví dụ đúng, lỗi bạn từng mắc.

---

## PHẦN A · BUỔI 1: print, input, biến, chuỗi, số

### 1. print và input

```python
print("Xin chào")              # in ra màn hình
ten = input("Tên bạn? ")       # hỏi người dùng, kết quả LUÔN là CHUỖI
```

`print` có 2 tùy chọn hay dùng:

```python
print("A", "B", sep="-")       # A-B      (sep = ký tự ngăn cách, mặc định là dấu cách)
print("A", end="")             # không xuống dòng (end mặc định là "\n")
```

### 2. input() LUÔN trả về CHUỖI ⚠️

```python
x = input("Số: ")              # gõ 3  →  x là "3" (chuỗi)
print(x + x)                   # "33"   ❌ ghép chuỗi, không cộng số

x = int(input("Số: "))         # đổi sang số nguyên
print(x + x)                   # 6      ✅
```

| Hàm | Đổi thành | Ví dụ |
|---|---|---|
| `int("3")` | số nguyên | `3` |
| `float("3.5")` | số thực | `3.5` |
| `str(3)` | chuỗi | `"3"` |

**Dùng `int` hay `float`?** Số lượng, tiền VND thì dùng `int`. Điểm số, giá có lẻ thì dùng `float`.
`float` sẽ sinh ra `.0`: `2 * 50000.0 = 100000.0`. Đây là lỗi bạn gặp ở mini project.

### 3. Các phương thức chuỗi

| Viết | Tác dụng | `"  lê an  "` thành |
|---|---|---|
| `.strip()` | xóa khoảng trắng 2 đầu | `"lê an"` |
| `.title()` | viết hoa chữ đầu mỗi từ | `"  Lê An  "` |
| `.upper()` | VIẾT HOA HẾT | `"  LÊ AN  "` |
| `.lower()` | viết thường hết | `"  lê an  "` |
| `.strip().title()` | nối liền, chạy từ trái sang phải | `"Lê An"` |

Chỉ dùng `.upper()` khi đề yêu cầu. Bạn từng tự thêm vào khi đề không yêu cầu nên bị sai.

### 4. f-string: chèn biến vào chuỗi

```python
ten = "An"
print(f"Xin chào, {ten}!")     # Xin chào, An!
```

- Phải có chữ **`f`** trước dấu nháy, nếu không `{ten}` sẽ in ra nguyên văn.
- `{ }` **chỉ dùng bên trong f-string**.

### 5. Định dạng số trong f-string

| Viết | Ý nghĩa | `x = 105000` | `x = 7.666` |
|---|---|---|---|
| `{x:,}` | dấu phẩy hàng nghìn | `105,000` | |
| `{x:.2f}` | đúng 2 chữ số thập phân | | `7.67` |
| `{x:.1f}` | đúng 1 chữ số thập phân | | `7.7` |
| `{x:,.2f}` | cả hai | `105,000.00` | |

**`:,` và `:.2f` là hai thứ khác nhau.** Tiền VND thì dùng `:,`. Điểm số thì dùng `:.2f`.

### 6. round() và :.2f khác nhau thế nào

| | `round(x, 2)` | `f"{x:.2f}"` |
|---|---|---|
| Trả về | **SỐ** | **CHUỖI** |
| `8.0` cho ra | `8.0` | `"8.00"` |
| Dùng khi | cần tính tiếp, `return` số | cần hiển thị đẹp |

### 7. Phép toán

| Phép | Ví dụ | Kết quả |
|---|---|---|
| `+ - *` | `3 * 4` | `12` |
| `/` | `7 / 2` | `3.5` (luôn ra float) |
| `//` | `7 // 2` | `3` (chia lấy nguyên) |
| `%` | `7 % 2` | `1` (chia lấy dư) |
| `**` | `2 ** 3` | `8` (lũy thừa) |
| chuỗi `*` số | `"=" * 5` | `"====="` |

**Thứ tự ưu tiên:** `**`, rồi `* / // %`, rồi `+ -`. Muốn khác thứ tự thì phải dùng **ngoặc**.

```python
(a + b + c) / 3        # ✅ trung bình
a + b + c / 3          # ❌ chỉ chia c cho 3
```

---

## PHẦN B · BUỔI 2: HÀM (def / return)

### 8. Cấu trúc một hàm

```python
def ten_ham(tham_so_1, tham_so_2=gia_tri_mac_dinh):
    ...xử lý...
    return ket_qua
```

- **Tham số** (parameter) là tên biến trong dòng `def`.
- **Đối số** (argument) là giá trị bạn truyền vào khi gọi: `ten_ham(3, 5)`.
- Tham số **có mặc định** phải đứng **sau** tham số không có mặc định.

```python
def tien_taxi(km, gia_mo_cua=10000, gia_km=15000):
    return gia_mo_cua + km * gia_km

tien_taxi(3)                   # 55000  (dùng cả 2 mặc định)
tien_taxi(3, 12000)            # 57000  (thay gia_mo_cua)
tien_taxi(2, 10000, 20000)     # 50000  (thay cả hai)
```

### 9. return và print khác nhau thế nào ⚠️⚠️

| | `return` | `print` |
|---|---|---|
| Làm gì | **gửi kết quả về** chỗ gọi hàm | **hiện lên màn hình** |
| Dùng tiếp được không | ✅ được | ❌ không, hàm trả về `None` |
| Dùng ở đâu | **hàm nhỏ** (tính toán, ghép chuỗi) | **main()** |

```python
def sai(a, b):
    print(a + b)        # ❌ hàm trả về None
def dung(a, b):
    return a + b        # ✅
```

- `return` xong là hàm **dừng ngay**. Code bên dưới `return` sẽ không chạy.
- Hàm không có `return` thì trả về `None`.

### 10. Hai loại kết quả: SỐ hay CHUỖI

| Đề nói | Viết | Ví dụ |
|---|---|---|
| "trả về SỐ" | **không** có `{ }`, **không** có nháy | `return so_ly * gia` |
| "trả về chuỗi" / có chữ trong kết quả | **f-string** có `{ }` | `return f"{ten}: {diem:.2f}"` |

```python
return {so_ly} * {gia}         # ❌ { } ngoài f-string
return "so_ly * gia"           # ❌ trong nháy thì là chữ, không tính được
return so_ly * gia             # ✅
```

### 11. Dữ liệu vào hàm qua THAM SỐ, không dùng input()

```python
def chao(ten):
    ten = input("Tên? ")       # ❌ máy chấm truyền ten vào rồi, không cần hỏi lại
    return f"Xin chào, {ten}!"
```

`input()` **chỉ đặt trong `main()`**.

### 12. Phạm vi biến (scope)

Biến tạo ra **bên trong** hàm nào thì **chỉ sống trong hàm đó**.

```python
def s4_thanh_tien(so_luong):
    gia = 12000
    return s4_nhan(so_luong)
def s4_nhan(so_luong):
    return so_luong * gia      # ❌ NameError, s4_nhan không thấy biến gia
```

Cách sửa là **truyền qua tham số**. Thêm tham số cho **hàm cần dùng biến** (`s4_nhan`), không phải hàm kia:

```python
def s4_thanh_tien(so_luong):
    gia = 12000
    return s4_nhan(so_luong, gia)
def s4_nhan(so_luong, gia):
    return so_luong * gia      # ✅
```

### 13. Hàm gọi hàm

```python
def tinh_diem_tb(toan, van, anh):
    return round((toan + van + anh) / 3, 2)

def bang_diem(ten, toan, van, anh):
    tb = tinh_diem_tb(toan, van, anh)          # gọi hàm KHÁC, truyền ĐỦ đối số
    return f"{ten.strip().title()}: {tb:.2f}"
```

Hai lỗi bạn từng mắc:
- Hàm **tự gọi chính nó** thay vì gọi hàm khác: `s6_mo_ta` gọi `s6_mo_ta`. ❌
- Truyền **thiếu hoặc sai** đối số.

### 14. Lồng hàm: chạy từ TRONG ra NGOÀI

```python
def q(x):
    return x + 1
print(q(q(1)))
```

Trong cùng: `q(1)` cho ra `2`. Tiếp theo: `q(2)` cho ra `3`. Kết quả in ra: **3**.

### 15. Khung chương trình chuẩn

```python
def ham_nho_1(...):
    return ...

def ham_nho_2(...):
    return ...

def main():
    # ① HỎI    bằng input (nhớ int/float)
    # ② XỬ LÝ  bằng cách gọi các hàm nhỏ
    # ③ IN RA  bằng print
    ...

if __name__ == "__main__":
    main()
```

- `def main():` mới chỉ là **định nghĩa**. Phải có 2 dòng cuối thì chương trình mới **chạy**.
- Dòng `if` phải **sát lề trái**, không thụt vào trong `main`.
- `pass` là "chỗ trống tạm", giúp hàm chưa viết vẫn không lỗi. Nhớ **xóa `pass`** khi viết code thật.

---

## PHẦN C · 10 LỖI BẠN TỪNG MẮC (ĐỌC KỸ!)

| # | Lỗi | Sai | Đúng |
|---|---|---|---|
| 1 | Tính toán trong nháy | `return "a * b"` | `return a * b` |
| 2 | `{ }` ngoài f-string | `return {a} * {b}` | `return a * b` |
| 3 | Quên `int()` | `input("Số: ")` rồi đem cộng | `int(input("Số: "))` |
| 4 | `print` thay `return` | `print(a + b)` | `return a + b` |
| 5 | `input()` trong hàm nhỏ | `ten = input()` trong hàm | dùng tham số `ten` |
| 6 | Hàm tự gọi chính nó | `s6_mo_ta` gọi `s6_mo_ta` | gọi `s5_trung_binh` |
| 7 | Thêm tham số sai hàm | thêm `gia` vào hàm gọi | thêm vào hàm **dùng** `gia` |
| 8 | Thiếu ngoặc | `a + b + c / 3` | `(a + b + c) / 3` |
| 9 | Nhầm định dạng | `{tien:.2f}` cho VND | `{tien:,}` |
| 10 | Không khớp từng ký tự | `"=====Hóa đơn======="` | copy nguyên chuỗi từ đề |

---

## PHẦN D · QUY TRÌNH LÀM MỘT BÀI

1. **Đọc đề**: tên hàm, tham số, giá trị mặc định là gì?
2. **Xác định kết quả**: SỐ thì `return` phép tính. CHUỖI thì `return f"..."`.
3. **Copy chuỗi mẫu** từ đề, chỉ thay phần thay đổi bằng `{bien}`.
4. **Có gọi hàm khác không?** Nếu có, truyền đủ đối số.
5. **Chạy máy chấm**, đọc kỹ dòng "bạn trả về" và "cần trả về".
6. **Ctrl + S** trước khi chạy!

---

## PHẦN E · LỆNH TERMINAL HAY DÙNG

| Lệnh | Tác dụng |
|---|---|
| `cd đường_dẫn` | đi vào thư mục |
| `ls` | xem có những file gì |
| `python ten_file.py` | chạy file |
| `git add .` | chọn tất cả thay đổi |
| `git commit -m "lời nhắn"` | lưu một mốc |
| `git push` | đẩy lên GitHub |
