# LỖI THƯỜNG GẶP · cập nhật sau buổi 3–4 (26/10/2026)

Đọc file này **trước mỗi bài kiểm tra**. Mỗi lỗi có: **bằng chứng** (đã sai ở đâu), cách nhận ra, cách sửa.
Dùng **checklist cuối file** trước khi chạy máy chấm.

---

## NHÓM A · KHÔNG KIỂM TRA TRƯỚC KHI NỘP  (gây mất điểm nhiều nhất)

### A1. Chạy được 1 lần là báo xong
- **Bằng chứng:** cả 3 bài PS0 (indoor, playback, faces) đều chỉ thử 1 ví dụ rồi báo xong. Kiểm tra buổi 3 câu 10: không chạy thử lần nào trước khi nộp
- **Sửa:** thử **ĐỦ mọi ví dụ trong đề** + 1 ví dụ tự nghĩ. Đặt kết quả **cạnh** dòng trong đề, so từng ký tự

### A2. Đọc đề không kỹ
- **Bằng chứng:** làm tròn 2 chữ số khi đề ghi 1 (đề lần 1 câu 4); thiếu chữ " đồng" (câu 5); `"=====Hóa đơn======="` thay vì `"===== HÓA ĐƠN ====="` (mini project); `"Tổng: "` thay vì `"Giá mỗi cuốn: "`
- **Sửa:** chuỗi in ra / câu hỏi input → **COPY từ đề**, không gõ tay

### A3. "Gần đúng" — sai 1 ký tự
- **Bằng chứng:** `ok` thay vì `OK` (soát đề 0/10 → 2/10); `# Soát đề:OK` thiếu dấu cách; gõ `playblack.py`; `môt` thay vì `một`
- **Sửa:** máy tính so **từng ký tự**. Viết đúng 1 lần rồi **copy-dán**

### A4. Quên lưu file
- **Bằng chứng:** `playback.py` có dấu ● sau khi sửa
- **Sửa:** **Ctrl + S** trước MỖI lần chạy. Nhìn tab: có ● là chưa lưu

---

## NHÓM B · SỐ HAY CHUỖI

### B1. Quên đổi chuỗi sang số → "3" + "4" = "34"
- **Bằng chứng:** buổi 1 (`input` không có `int`); kiểm tra buổi 3 câu 5 trả `'1250000'`, câu 6 ra `'10002500'`
- **Nhận ra:** máy chấm in kết quả **có dấu nháy `' '`** → đó là CHUỖI
- **Sửa:** đề ghi "trả về SỐ" → kết quả cuối phải qua `int()` / `float()`

### B2. Sai thứ tự khi bọc hàm
- **Bằng chứng:** `int(so).replace(",", "")` — đổi số TRƯỚC khi bỏ dấu phẩy → lỗi
- **Sửa:** việc trên **chuỗi** làm trước (`.replace`, `.strip`), `int()` **bọc ngoài cùng**: `int(so.replace(",", ""))`

### B3. `int` hay `float`
- **Bằng chứng:** dùng `float` cho tiền VND → in `158,000.0 đồng`
- **Sửa:** đếm số lượng, tiền VND → `int`. Có số lẻ (điểm, USD) → `float`

### B4. `round()` khác `:.2f`
- `round(x, 1)` → **số** (dùng khi `return` số). `f"{x:.2f}"` → **chuỗi** để hiển thị

---

## NHÓM C · HÀM

### C1. `print` thay cho `return`
- **Bằng chứng:** S1 (ôn tập), câu 7 đề lần 1
- **Sửa:** hàm nhỏ → `return`. Chỉ `main()` mới `print`

### C2. Không tự gọi hàm khi gặp đề mới
- **Bằng chứng:** `faces.py` phải hỏi "gọi convert là như thế nào"; câu 10 buổi 3 tự viết hàm `convert` mới thay vì **gọi `slug`**
- **Sửa:** cú pháp luôn là `ket_qua = ten_ham(du_lieu)`. Đề ghi "GỌI hàm X" → dùng đúng tên X, không viết lại

### C3. Tên biến lệch nhau → NameError
- **Bằng chứng:** câu 10 đề lần 1: lưu giá vào `thanh_tien`, tính bằng `gia` → `NameError: name 'gia'`
- **Sửa:** trước khi chạy, với mỗi biến được **dùng**, chỉ ra dòng nào **tạo** nó (có dấu `=`)

### C4. Tên biến sai nghĩa
- **Bằng chứng:** `trang_thai` chứa câu người dùng nhập (faces, câu 10); `chuoi_1` chứa số
- **Sửa:** tên biến nói đúng **thứ nó chứa**: `cau`, `tieu_de`, `gia_1`

### C5. Thêm xử lý thừa vào hàm đã đúng
- **Bằng chứng:** câu 6 buổi 3: thêm `int(a)` trước `bo_dau_phay` → làm hỏng cái đang đúng
- **Sửa:** mỗi hàm lo đúng việc của nó. Sửa ở **gốc lỗi** (câu 5), không vá ở chỗ khác

### C6. Biến chỉ sống trong hàm tạo ra nó
- **Bằng chứng:** S4 (ôn tập), câu 7 đề lần 1
- **Sửa:** truyền qua **tham số**

---

## NHÓM D · CHÉP KHUNG CŨ KHÔNG ĐỐI CHIẾU ĐỀ MỚI

- **Bằng chứng:** câu 10 đề lần 1 chép mini project → còn `"PHIẾU MUA HÀNG"`, phép `+`, biến lệch; câu 10 buổi 3 chép nguyên `faces.py` → sai câu hỏi input, sai hàm, thiếu phần in
- **Sửa:** được dùng khung cũ, nhưng **đọc lại từng dòng** và hỏi: "dòng này đề MỚI có yêu cầu không?"

---

## NHÓM E · TERMINAL

- `No such file or directory` → kiểm tra **(1)** dòng nhắc lệnh có `\ps0>` không, **(2)** `ls` để so tên file
- Terminal mới mở luôn ở thư mục gốc → phải `cd ps0` lại
- Gõ vài chữ đầu tên file rồi bấm **Tab** để tự điền
- Đọc traceback **từ dưới lên**: dòng cuối = loại lỗi, `line X` = chỗ sai

---

## NHÓM F · LÀM THEO NHẮC NHỞ

- **Bằng chứng:** câu hỏi input, chữ "chèn", soát đề — mỗi thứ phải nhắc **3 lần** mới sửa
- **Sửa:** sau khi đọc nhận xét, **gạch đầu dòng từng điểm** được nhắc, sửa xong điểm nào đánh dấu điểm đó

---

## ✅ CHECKLIST TRƯỚC KHI CHẠY MÁY CHẤM

1. [ ] Mọi chuỗi in ra & câu hỏi `input` đã **copy từ đề**
2. [ ] Đề ghi "trả về SỐ" → có `int`/`float` ở ngoài cùng; ghi "chuỗi" → f-string
3. [ ] Hàm nhỏ dùng `return`, chỉ `main` dùng `print` và `input`
4. [ ] Đề ghi "GỌI hàm X" → đã gọi đúng X
5. [ ] Mọi biến được dùng đều có dòng tạo ra nó, cùng tên, trong cùng hàm
6. [ ] Đã chạy thử **đủ ví dụ trong đề**, so từng ký tự
7. [ ] Dòng soát đề viết **chính xác** `# Soát đề: OK` (copy-dán)
8. [ ] Có `if __name__ == "__main__":` ở cuối (nếu có `main`)
9. [ ] **Ctrl + S**
10. [ ] Terminal đứng đúng thư mục

---

## NHÓM G · ĐIỀU KIỆN (thêm 30/10/2026 — kiểm tra tuần 2 buổi 1: 9/10)

### G1. Kiểm tra "X có phải Y không" nhưng lại so X với chính nó
- **Bằng chứng:** câu 4 `dang_nhap`: viết `ten == ten.strip().lower()` → hỏi "ten đã sạch chưa?", KHÔNG hỏi "ten có phải admin không" → `"an"` cũng lọt qua
- **Sửa:** làm sạch rồi so với **giá trị cụ thể trong đề**: `ten.strip().lower() == "admin"`

### G2. Tham số nào chuẩn hóa, tham số nào không
- **Bằng chứng:** câu 4: tên thì chuẩn hóa, mật khẩu thì so **nguyên văn** (phân biệt hoa thường): `mat_khau == "Py@2026"`
- **Sửa:** đọc đề xem từng tham số có được `.strip()` / `.lower()` không

### G3. Khoảng viết ngược · thứ tự elif · `or` viết tắt (sai ở buổi 1, ĐÃ sửa được ở bài kiểm tra)
- `6 <= tuoi <= 17` (số nhỏ bên trái) · với `>=` xếp từ lớn đến nhỏ · `x == 6 or x == 7` (mỗi vế so sánh đầy đủ)

### Soát đề
- Lần thứ 4 ghi `# Soát đề: OK` cho câu chưa thử đúng (câu 4). Chỉ ghi OK sau khi **mọi ví dụ của đề** đã chạy ra đúng.

---

## NHÓM H · %, BOOL, MATCH (thêm 30/10/2026 — bài tập tuần 2 buổi 2: lần đầu 6/11)

### H1. Chép ví dụ vào code (lặp lại lỗi tuần 1)
- **Bằng chứng:** bài 4 FizzBuzz: `else: return "7"` → `fizz(11)` cũng ra `"7"`
- **Sửa:** "trả về chính số đó dạng chuỗi" = `str(n)`. Luôn tự thử 1 số KHÁC ví dụ của đề

### H2. `case` sai kiểu dữ liệu
- **Bằng chứng:** bài 6 `case "2":` trong khi `ten_thu(2)` truyền SỐ → không khớp → "Không hợp lệ"
- **Sửa:** biến là số → `case 2:` (không nháy). Biến là chuỗi → `case "cam":`. Nhớ `2 == "2"` là False

### H3. Quên `case _` (trường hợp còn lại)
- **Bằng chứng:** bài 9 chỉ thêm `case "tím":` → `c9_mau("hồng")` trả về None
- **Sửa:** "mọi trường hợp khác" = `case _:` đặt CUỐI CÙNG

### H4. In True/False thay vì câu
- **Bằng chứng:** bài 11 `print(f"{goi}")` → in `True`
- **Sửa:** hàm bool trả lời đúng/sai → `main` dùng `if la_chan:` để CHỌN câu in ra; trong câu dùng `{so}` chứ không dùng `{la_chan}`

### H5. Chữ hoa sai
- **Bằng chứng:** `"Chủ Nhật"` thay vì `"Chủ nhật"` → copy chuỗi từ đề

### H6. Chọn `match` hay `if/elif`
- Giá trị CỤ THỂ (2, "đỏ") → `match`. KHOẢNG (`>= 9`) → `if/elif`

### Soát đề
- Lần thứ 5: bài 4, 6, 11 sai vẫn ghi OK. Bài 8, 9 ghi `Ok` (k thường) → máy chấm không nhận

### H7. So tham số bool với chuỗi "True"
- **Bằng chứng:** luyện lại bài 6: `co_ve == "True"` → `True == "True"` là False
- **Sửa:** tham số đã là True/False → dùng thẳng: `return tuoi >= 18 and co_ve`

### H8. Quên `!= 0` → hàm trả về SỐ thay vì True/False
- **Bằng chứng:** `(nam % 4 == 0 and nam % 100) or ...` → `la_nam_nhuan(2024)` trả về `24`. `main` vẫn "tình cờ" chạy đúng vì 24 được coi là đúng
- **Sửa:** mỗi vế phải là một phép so sánh đầy đủ. Luôn thử RIÊNG từng hàm, không chỉ chạy main

### H9. Chép ký tự của ví dụ vào case
- **Bằng chứng:** `case "s"`, `case "M"`, `case "l"` → nhập "S" hay "m" đều ra "Không có"
- **Sửa:** chuẩn hóa trước (`.strip().upper()`) rồi `case` theo MỘT kiểu chữ

### "Đã thử thêm" phải thật
- Ghi giá trị ĐỀ KHÔNG CHO (7, 12 là ví dụ của đề → không tính) và kết quả THẬT sự chạy ra (đã ghi `12 → "1"` trong khi thật là "2")
