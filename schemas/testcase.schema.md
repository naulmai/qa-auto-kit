# 📐 Master Test Case Schema (14-Column Specification)
> **Trạng thái:** Active Standard | **Áp dụng cho:** `testcase_generator`, `coverage_analyst`, `scripts/md_to_csv.py`, `templates/testcases.md`

---

## 1. 🎯 Mục Đích & Tiêu Chuẩn Cốt Lõi
Schema này định nghĩa cấu trúc dữ liệu chuẩn cho bảng Test Case 14-cột của toàn bộ repository. Bảng Test Case phải đáp ứng đồng thời 3 mục tiêu:
1. **Human-Readable:** QA/QC, Dev và PO dễ dàng đọc, rà soát và thực thi manual.
2. **Import-Ready:** Có thể chuyển đổi tự động sang file CSV bằng `scripts/md_to_csv.py` và import trực tiếp vào Jira / Xray / Zephyr / TestRail mà không phát sinh lỗi parse.
3. **Traceable:** Mọi test case truy vết trực tiếp về FR ID, Risk ID và Edge Case ID.

---

## 2. 📋 Danh Mục 14 Cột Bắt Buộc (Exact 14-Column Specification)

> ⚠️ **Quy tắc bất biến:** Thứ tự và tên tiêu đề của 14 cột bằng tiếng Anh **TUYỆT ĐỐI KHÔNG ĐƯỢC THAY ĐỔI HOẶC DỊCH SANG TIẾNG VIỆT**.

| # | Tên cột (Header) | Kiểu dữ liệu | Bắt buộc | Ràng buộc & Giá trị hợp lệ | Quy chuẩn viết nội dung |
|:---:|---|:---:|:---:|---|---|
| **1** | **`Test Case ID`** | String | ✅ Có | Regex: `^[A-Z0-9]{2,8}-(TC\|[A-Z0-9]{2,6})-\d{3}$`<br>Ví dụ: `RID-TC-001`, `MOD-DEST-001` | Mã định danh duy nhất trong file. Không được trùng lặp. |
| **2** | **`Module`** | String | ✅ Có | Tên Module cấp cao (Ví dụ: `Ride In Progress`, `Authentication`, `Host Financial`) | Phản ánh đúng phân hệ trong tài liệu FRS/SRS. |
| **3** | **`Function`** | String | ✅ Có | Tên tính năng cụ thể (Ví dụ: `In-Trip Modifications`, `Driver Payout`) | Tên tính năng con đang được kiểm thử. |
| **4** | **`FR ID`** | String | ✅ Có | Mã yêu cầu (Ví dụ: `FR-RID-7.1`, `FR-ACS-FIN-2.3`) | Truy vết trực tiếp về mục trong tài liệu requirement. |
| **5** | **`Test Case Description`** | String | ✅ Có | Viết bằng tiếng Anh, bắt đầu bằng `Verify that...` hoặc `Verify [component/behavior]...` | Mô tả súc tích mục tiêu kiểm thử của test case. |
| **6** | **`Pre-Requisite`** | String | ✅ Có | Điều kiện tiên quyết. Nếu có nhiều điều kiện, ngăn cách bằng thẻ `<br>`. | Trạng thái ban đầu của hệ thống, tài khoản, dữ liệu trước khi test. |
| **7** | **`Steps Description`** | String | ✅ Có | Viết bằng tiếng Anh. Mỗi bước bắt đầu bằng **Action Verb** (`Navigate`, `Click`, `Enter`, `Select`, `Upload`, `Verify`). Ngăn cách bằng `<br>`. | Định dạng: `Step 1: ...<br>Step 2: ...<br>Step 3: ...`. Cấm xuống dòng thực tế `\n` trong ô bảng. |
| **8** | **`Test Data`** | String | ⬜ Tuỳ chọn | Dữ liệu đầu vào cụ thể (chuỗi, số, biên BVA, trạng thái). Ngăn cách các trường bằng `<br>`. | Dữ liệu tham số hóa có giá trị rõ ràng. Nếu không có dữ liệu riêng thì để trống hoặc `N/A`. |
| **9** | **`Expected Result`** | String | ✅ Có | Viết bằng tiếng Anh. **Bắt buộc là Observable Outcome** (kết quả quan sát được từ phía người dùng/hệ thống). | Không viết hành động thao tác vào đây. Bảo tồn nguyên vẹn các thông báo lỗi, nhãn UI gốc trong ngoặc kép. |
| **10**| **`Priority`** | Enum | ✅ Có | `Critical` \| `High` \| `Medium` \| `Low` | Mức độ ưu tiên thực thi trong chu kỳ test. |
| **11**| **`Severity`** | Enum | ✅ Có | `Blocker` \| `Critical` \| `Major` \| `Minor` \| `Trivial` | Mức độ ảnh hưởng nếu test case này phát hiện lỗi. |
| **12**| **`Type`** | Enum | ✅ Có | `Functional` \| `Negative` \| `Boundary` \| `UI` \| `Security` \| `Performance` \| `Integration` \| `Regression` | Phân loại kỹ thuật kiểm thử của ca test. |
| **13**| **`Automation Candidate`**| Enum | ✅ Có | `Yes` \| `No` | Đánh giá tính khả thi để chuyển thành automated script (nhị phân chuẩn phục vụ đo lường tỷ lệ tự động hóa). |
| **14**| **`Remarks`** | String | ⬜ Tuỳ chọn | Ghi chú thêm, mapping rủi ro (`RISK-RID-001`), hoặc giả định bắt buộc `[Assumption]: ...`. | Bắt buộc ghi `[Assumption]: ...` nếu expected result chưa có tài liệu xác nhận 100%. |

---

## 3. 🛡️ Quy Tắc Viết Nội Dung Bảng (Markdown Table Formatting Rules)

### 1. Quy tắc Xuống Dòng (HTML Line Break `<br>`):
- Tuyệt đối **KHÔNG dùng ký tự xuống dòng thực tế** (`\n` hoặc Enter) bên trong bất kỳ ô nào của bảng markdown, vì sẽ làm gãy cấu trúc dòng bảng khi chuyển sang CSV.
- Mọi điểm ngắt dòng trong ô bảng BẮT BUỘC sử dụng thẻ `<br>`.

### 2. Quy tắc Thoát Ký Tự Pipe (`\|`):
- Nếu nội dung trong ô có chứa ký tự dấu gạch đứng `|` (pipe), bắt buộc phải escape thành `\|` để parser bảng của `md_to_csv.py` không nhận nhầm thành cột mới.

### 3. Chuẩn Ngôn Ngữ Kép (Language Governance):
- Tiêu đề cột và toàn bộ nội dung trong ô (Description, Steps, Expected Result, Pre-requisite) viết bằng **English**.
- Nhãn UI, mã lỗi, tên trạng thái, câu thông báo được quy định trong tài liệu nguồn FRS: **BẢO TỒN NGUYÊN VẸN** (ví dụ: `Click the "Hủy chuyến" button`, hiển thị thông báo `"Bạn có chắc chắn muốn hủy chuyến?"`).

### 4. Quy tắc Định Dạng Toán Học & Tiền Tệ (Plain-Text Math & Currency Rule — Anti-LaTeX):
- **CẤM TUYỆT ĐỐI** sử dụng cú pháp toán học LaTeX (`$...$`, `$$...$$`, `\Delta`, `\$`, `\times`, `\le`, `\ge`, `\text{...}`) trong bất kỳ ô nào của bảng Test Case. Cú pháp này gây lỗi hiển thị nghiêm trọng khi xuất sang CSV hoặc copy/paste sang Google Sheets / Microsoft Excel.
- **Quy chuẩn chuyển đổi bắt buộc:**
  - **Ký hiệu toán Hy Lạp:** Chuyển sang từ ngữ thông thường trong ngoặc đơn, ví dụ: dùng `(Delta)` hoặc `Delta` thay vì `$\Delta$`.
  - **Ký hiệu tiền tệ:** Viết trực tiếp ký hiệu tiền tệ `$38.50` (hoặc `VND 50,000`), TUYỆT ĐỐI KHÔNG escape gạch chéo `\$38.50`.
  - **Toán tử số học:** Dùng ký tự bàn phím chuẩn: `=`, `+`, `-`, `*`, `<=`, `>=`, `!=`, `~`.
  - **Công thức & Biểu thức:** Viết dưới dạng văn bản rõ ràng, tự nhiên:
    - ❌ CẤM: `Fare Delta $\Delta$ calculates exactly as: $\$38.50 - \$30.00 = +\$8.50$.`
    - ✅ CHUẨN: `Fare Delta (Delta) = $38.50 - $30.00 = +$8.50`
    - ❌ CẤM: `Fare Delta $\Delta \le \$0$`
    - ✅ CHUẨN: `Fare Delta (Delta) <= $0`
    - ❌ CẤM: `$\text{New Total} = \text{Base} + \text{Distance}$`
    - ✅ CHUẨN: `New Total = Base + Distance`
    - ❌ CẤM: `Extreme fare increase ($\Delta > \$40$ or $\Delta > 100\%$)`
    - ✅ CHUẨN: `Extreme fare increase (Delta > $40 or Delta > 100%)`

---

## 4. 📝 Ví Dụ Bảng Chuẩn Thực Tế

```markdown
| Test Case ID | Module | Function | FR ID | Test Case Description | Pre-Requisite | Steps Description | Test Data | Expected Result | Priority | Severity | Type | Automation Candidate | Remarks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RID-TC-001 | Ride In Progress | In-Trip Modifications | FR-RID-7.1 | Verify edit pencil icon is displayed adjacent to DROP OFF destination when trip is In Trip | Trip is in active `In Trip` status after driver confirmed pickup.<br>Modification count = 0. | Step 1: Open live tracking view for active trip.<br>Step 2: Inspect Route Detail card DROP OFF destination row. | Status: `In Trip`<br>Mod Count: 0 | An active edit pencil icon (✏️) is displayed adjacent to the final DROP OFF destination row.<br>The pencil icon is tappable. | High | Major | UI | Yes | |
| RID-TC-002 | Ride In Progress | In-Trip Modifications | FR-RID-7.4 | Verify destination change is rejected when payment pre-authorization fails | Rider requested destination change with fare increase Delta > $0.<br>Card on file is expired or declined. | Step 1: Select new destination with Delta = +$5.00.<br>Step 2: Tap "Send Request" button.<br>Step 3: Observe system handling during Stripe pre-auth failure. | Delta: `+$5.00`<br>Card: `Declined` | System keeps the original destination intact without rerouting.<br>The system displays error message: "We couldn't validate your payment method. Your trip will continue to the original destination." | Critical | Blocker | Negative | Yes | [Assumption]: Retry limit is 1 before auto-rollback |
```
