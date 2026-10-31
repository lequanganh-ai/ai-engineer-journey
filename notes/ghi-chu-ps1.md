# CS50P · PROBLEM SET 1 — ĐỀ BÀI TIẾNG VIỆT (bài 1–3)

Đề gốc: cs50.harvard.edu/python → Week 1 → Problem Set 1. Đọc bản tiếng Việt, rồi mở đề gốc đặt cạnh và dò bảng từ vựng.

- **Buổi 3 (hôm nay):** bài 1–3 — Deep Thought, Home Federal Savings, File Extensions
- **Buổi 4:** bài 4–5 — Math Interpreter, Meal Time

## Quy trình mỗi bài (như PS0 + thói quen mới)
1. Tạo file **đúng tên** trong thư mục `ps1/`
2. `# Soát đề: ...` và `# Đã thử thêm: ...` ở đầu file
3. Comment kế hoạch ① HỎI / ② XỬ LÝ / ③ IN RA → code
4. Chạy thử **đủ ví dụ** + **giá trị đề không cho**, đúng hết mới ghi OK
5. Chấm:  `python cham_ps1.py`  (đứng trong `ps1`)

> Câu hỏi trong `input()`: đề không bắt buộc, nhưng nên copy câu tiếng Anh của đề. Phần **in ra** phải đúng y như bảng.

---

## BÀI 1 · Deep Thought — `deep.py`

**Bối cảnh:** Trong truyện *The Hitchhiker's Guide to the Galaxy*, siêu máy tính Deep Thought trả lời "câu hỏi lớn về sự sống, vũ trụ và mọi thứ" là **42**.

**Yêu cầu:**
- Hỏi: `What is the Answer to the Great Question of Life, the Universe, and Everything? `
- Nếu người dùng trả lời **42**, hoặc **forty-two**, hoặc **forty two** → in `Yes`
- Mọi câu trả lời khác → in `No`
- **Không phân biệt hoa thường**, **bỏ qua khoảng trắng 2 đầu**

| Nhập | In ra |
|---|---|
| `42` | `Yes` |
| `Forty-Two` | `Yes` |
| `  forty two ` | `Yes` |
| `50` | `No` |
| `forty-three` | `No` |

**Gợi ý:** chuẩn hóa trước, rồi so với 3 đáp án. `match` với `|` rất hợp.

| Từ tiếng Anh | Nghĩa |
|---|---|
| case-insensitively | không phân biệt hoa thường |
| leading/trailing whitespace | khoảng trắng ở đầu/cuối |
| otherwise | ngược lại |

---

## BÀI 2 · Home Federal Savings — `bank.py`

**Bối cảnh:** Trong phim *Seinfeld*, ngân hàng hứa tặng **100 đô** cho khách nếu nhân viên không chào "hello".

**Yêu cầu:**
- Hỏi: `Greeting: ` (người dùng nhập câu chào của nhân viên)
- Câu chào **bắt đầu bằng** `hello` → in `$0`
- Câu chào **bắt đầu bằng chữ `h`** nhưng không phải `hello` (ví dụ `hey`, `how you doing?`) → in `$20`
- Còn lại → in `$100`
- Không phân biệt hoa thường, bỏ qua khoảng trắng ở đầu

| Nhập | In ra |
|---|---|
| `Hello` | `$0` |
| `Hello, Newman` | `$0` |
| `  HELLO there` | `$0` |
| `How you doing?` | `$20` |
| `hey` | `$20` |
| `What's happening?` | `$100` |

**Kiến thức MỚI — tự tra tài liệu:** phương thức `.startswith(...)` — trả về `True` nếu chuỗi **bắt đầu bằng** chuỗi trong ngoặc.
```python
"python".startswith("py")    # True
"python".startswith("on")    # False
```
**Chú ý thứ tự điều kiện!** Câu bắt đầu bằng `hello` thì cũng bắt đầu bằng `h`. Kiểm tra cái nào trước?

| Từ tiếng Anh | Nghĩa |
|---|---|
| greeting | lời chào |
| starts with | bắt đầu bằng |
| output $0 | in ra `$0` |

---

## BÀI 3 · File Extensions — `extensions.py`

**Bối cảnh:** Máy tính nhận biết loại file nhờ **đuôi file** (extension), ví dụ `.jpg` là ảnh. Trên web, mỗi loại có một **"media type"** chuẩn.

**Yêu cầu:**
- Hỏi: `File name: `
- In ra **media type** theo đuôi file:

| Đuôi | In ra |
|---|---|
| `.gif` | `image/gif` |
| `.jpg` hoặc `.jpeg` | `image/jpeg` |
| `.png` | `image/png` |
| `.pdf` | `application/pdf` |
| `.txt` | `text/plain` |
| `.zip` | `application/zip` |
| đuôi khác hoặc không có đuôi | `application/octet-stream` |

- Không phân biệt hoa thường (`CAT.JPG` cũng là `image/jpeg`), bỏ qua khoảng trắng 2 đầu

| Nhập | In ra |
|---|---|
| `happy.jpg` | `image/jpeg` |
| `  Document.PDF ` | `application/pdf` |
| `notes.txt` | `text/plain` |
| `cat.jpeg` | `image/jpeg` |
| `program.exe` | `application/octet-stream` |
| `README` | `application/octet-stream` |

**Kiến thức MỚI — tự tra:** `.endswith(...)` — giống `startswith` nhưng kiểm tra **phần cuối** chuỗi.
```python
"photo.png".endswith(".png")   # True
```
Bài này dùng `if / elif` với `.endswith` là hợp lý (vì kiểm tra đuôi, không phải so cả chuỗi).

| Từ tiếng Anh | Nghĩa |
|---|---|
| file extension / suffix | đuôi file |
| media type | kiểu dữ liệu chuẩn trên web |
| default | mặc định |
