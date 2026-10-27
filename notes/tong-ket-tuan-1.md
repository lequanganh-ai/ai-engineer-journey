# TỔNG KẾT TUẦN 1 · NHỮNG ĐIỀU QUAN TRỌNG NHẤT (buổi 1–4)

Đọc kỹ file này **trước buổi 5**. Bài kiểm tra tổng hợp sẽ hỏi đúng những thứ ở đây.
Chi tiết hơn: `tong-hop-buoi01-02.md` (kiến thức), `loi-thuong-gap.md` (lỗi + checklist).

---

## PHẦN 1 · KIẾN THỨC CỐT LÕI

### 1. `input()` LUÔN trả về CHUỖI
```python
so = int(input("Số: "))        # muốn tính toán → bọc int() hoặc float()
```
- `"3" + "4"` → `"34"` (ghép) · `3 + 4` → `7` (cộng)
- Tiền VND, số lượng → `int` · có số lẻ ($50.00, điểm) → `float`

### 2. Phương thức chuỗi (luôn trả về chuỗi MỚI)
| Viết | Tác dụng |
|---|---|
| `.strip()` | xóa khoảng trắng 2 đầu |
| `.lower()` / `.upper()` | thường hết / hoa hết |
| `.title()` | hoa chữ đầu mỗi từ |
| `.replace(cũ, mới)` | thay mọi chỗ `cũ` bằng `mới` — cần **2 đối số**; `mới = ""` để xóa |

Nối liền, chạy **từ trái sang phải**: `text.strip().lower().replace(" ", "-")`

### 3. Thứ tự khi bọc hàm
```python
int(so.replace(",", ""))       # ✅ xử lý chuỗi TRƯỚC, đổi số bọc NGOÀI CÙNG
int(so).replace(",", "")       # ❌ đổi số trước → lỗi
```
Python chạy **phần trong ngoặc trước**.

### 4. f-string và định dạng
```python
f"Khách: {ten}"                # chèn biến — phải có chữ f
f"{tien:,} đồng"               # 158,000 đồng  (dấu phẩy hàng nghìn)
f"{diem:.2f}"                  # 7.70          (đúng 2 chữ số thập phân)
```
- `round(x, 1)` → trả về **SỐ** · `f"{x:.1f}"` → trả về **CHUỖI**
- `{ }` chỉ dùng **bên trong** f-string

### 5. Phép toán
`+ - * /` · `//` chia lấy nguyên · `%` chia lấy dư · `**` lũy thừa · `"=" * 19` lặp chuỗi
Thứ tự: `**` → `* / // %` → `+ -`. Muốn khác → **ngoặc**: `(a + b + c) / 3`

### 6. Hàm: `def` và `return`
```python
def ten_ham(tham_so, mac_dinh=10):
    return ket_qua
```
- **Viết** hàm (`def`) ≠ **gọi** hàm (`ten_ham(...)`). Chỉ gọi mới chạy
- Tham số có mặc định đứng **sau**
- `return` xong là hàm **dừng**; không có `return` → trả về `None`
- Trong `return` viết được phép tính: `return float(p.replace("%", "")) / 100`

### 7. `return` khác `print`
| | `return` | `print` |
|---|---|---|
| Làm gì | gửi kết quả về chỗ gọi | hiện lên màn hình |
| Dùng ở | **hàm nhỏ** | **chỉ trong `main()`** |
| `input()` | ❌ không dùng trong hàm nhỏ | ✅ dùng trong `main()` |

### 8. Gọi hàm
```python
ket_qua = ten_ham(du_lieu)     # giá trị trong ngoặc → đưa vào tham số của hàm
```
Đề ghi "GỌI hàm X" → gọi đúng X, **không viết lại**.

### 9. Phạm vi biến
Biến tạo trong hàm nào **chỉ sống trong hàm đó**. Cần ở hàm khác → **truyền qua tham số**.

### 10. Khung chương trình chuẩn
```python
def ham_nho(...):
    return ...


def main():
    # ① HỎI    → input (+ int/float)
    # ② XỬ LÝ  → gọi hàm nhỏ
    # ③ IN RA  → print
    ...


if __name__ == "__main__":
    main()
```

---

## PHẦN 2 · KỸ NĂNG LÀM VIỆC

### Terminal
- `cd ps0` vào thư mục · `cd ..` ra ngoài · `ls` xem file · **Tab** tự điền tên file
- Terminal mới mở → luôn ở thư mục gốc → `cd` lại
- `No such file or directory` → (1) dòng nhắc lệnh đúng thư mục chưa? (2) tên file đúng từng chữ chưa?

### Đọc thông báo lỗi (traceback)
Đọc **từ dưới lên**: dòng cuối = **loại lỗi**, `line X` = **dòng sai**
| Lỗi | Nghĩa thường gặp |
|---|---|
| `NameError: name 'x' is not defined` | chưa có dòng nào tạo biến `x` (sai tên / khác hàm) |
| `TypeError: ... takes 2 arguments (1 given)` | gọi hàm thiếu đối số |
| `ValueError: invalid literal for int()` | đổi chuỗi còn ký tự lạ (`,` `$`) sang số |

### Đọc kết quả máy chấm
- `'1250000'` có dấu nháy → **chuỗi** · `1250000` không nháy → **số**
- Sai dây chuyền: hàm A sai → mọi hàm gọi A cũng sai. **Sửa ở gốc.**

### Git — sau mỗi buổi
```
git add .
git commit -m "nói rõ đã làm gì"
git push
```

---

## PHẦN 3 · QUY TRÌNH LÀM 1 BÀI (bắt buộc)

1. `# Soát đề: ...` ở đầu
2. Đọc đề → comment kế hoạch **① HỎI / ② XỬ LÝ / ③ IN RA**, viết cho **mọi trường hợp**, không gắn vào ví dụ
3. Code — chuỗi in ra & câu hỏi `input` **copy từ đề**
4. **Ctrl + S**
5. Chạy thử **ĐỦ mọi ví dụ của đề, nhập ĐÚNG Y NHƯ ĐỀ** + 1 ví dụ tự nghĩ
6. So **từng ký tự** → đúng hết mới đổi thành `# Soát đề: OK` (copy-dán)
7. Chạy máy chấm

> **Ví dụ trong đề dùng để THỬ, không phải để chép vào code.**
> **`# Soát đề: OK` = "tôi ĐÃ kiểm tra", không phải thủ tục cho xong.**

---

## PHẦN 4 · 5 LỖI NGUY HIỂM NHẤT CỦA BẠN (theo số lần mắc)

| # | Lỗi | Số lần | Bằng chứng gần nhất |
|---|---|---|---|
| 1 | **Báo xong khi chưa kiểm tra đủ** | rất nhiều | PS0 bài 1–3 thử 1 ví dụ; tip ghi OK khi còn ra $750 |
| 2 | **Phải nhắc nhiều lần mới sửa** | ≥ 6 | `input("Hỏi người dùng nhập")`, "chèn", `#Soát đề` — mỗi thứ 2–3 lần |
| 3 | **Số hay chuỗi** | 5 | câu 5–6 buổi 3: `'1250000'`, `'10002500'` |
| 4 | **Chép khung cũ không đối chiếu đề** | 2 | câu 10 của cả 2 bài kiểm tra |
| 5 | **"Gần đúng" 1 ký tự** | ≥ 5 | `ok`/`OK`, `playblack.py`, thiếu " đồng", `3000000` vs `300000000` |

---

## PHẦN 5 · TIẾN BỘ CÓ BẰNG CHỨNG

| | Lần đầu | Gần nhất |
|---|---|---|
| Kiểm tra buổi 1+2 | 5/10 | 10/10 (đề lần 2) |
| Kiểm tra buổi 3 | 6/10 | 10/10, soát đề 10/10 |
| Tự thử đủ ví dụ không cần nhắc | 0/3 bài (PS0 1–3) | ✅ Einstein |
| Problem Set 0 (Harvard) | — | **5/5** |
