# 📐 Master Finding Schema (v1.0.0)
> **Trạng thái:** Active Standard | **Áp dụng cho:** `requirement_gap_analyst`, `requirement_logic_analyst`, `advanced_edge_case_analyzer`, `risk_analyst`, `design_auditor`

---

## 1. 🎯 Mục Đích & Phạm Vi
Schema này định nghĩa cấu trúc chuẩn duy nhất cho mọi phát hiện (Finding), lỗ hổng (Gap), bất thường logic (Logic Anomaly), rủi ro (Risk) và sai lệch thiết kế (Design Mismatch) được tạo ra bởi bất kỳ Agent nào trong QA Framework.

Mọi template và báo cáo (`*_Req_Gap_Report.md`, `*_Logic_Anomaly_Report.md`, `*_Risk_Analysis_Report.md`, `*_Edge_Case_Report.md`, `*_Design_Audit_Report.md`) **BẮT BUỘC** tuân thủ schema này để đảm bảo khả năng liên kết, truy vết chéo và kiểm tra tự động (automated validation).

---

## 2. 🆔 Chuẩn Định Dạng Finding ID

Finding ID bắt buộc tuân theo quy tắc:
$$\text{[TYPE]-[MODULE]-[NNN]}$$

### Các tiền tố TYPE chuẩn:
| Tiền tố TYPE | Agent phụ trách | Loại phát hiện | Ví dụ |
|:---:|---|---|---|
| **`GAP`** | `requirement_gap_analyst` | Lỗ hổng yêu cầu, thiếu sót quy tắc, đứt đoạn truy vết PRD vs SRS | `GAP-RID-001` |
| **`LOGIC`** | `requirement_logic_analyst` | Mâu thuẫn nội tại, phi lý nghiệp vụ, chuyển trạng thái bất thường | `LOGIC-RID-001` |
| **`EDGE`** | `advanced_edge_case_analyzer` | Tình huống biên cực hạn, concurrency, race condition, ngắt quãng | `EDGE-RID-001` |
| **`BVA`** | `advanced_edge_case_analyzer` | Giá trị kiểm thử tại biên số liệu hoặc thời gian | `BVA-RID-001` |
| **`RISK`** | `risk_analyst` | Rủi ro kỹ thuật, tài chính, an ninh, hiệu năng, vận hành | `RISK-RID-001` |
| **`DES`** | `design_auditor` | Sai lệch UI/UX giữa Wireframe/Design với SRS | `DES-RID-001` |

- **`[MODULE]`**: Mã viết tắt 3-4 ký tự in hoa đại diện cho module nghiệp vụ (Ví dụ: `RID` = In-Trip Ride, `FIN` = Host Financial, `SCH` = Scheduled Trips, `AUTH` = Authentication, `PAY` = Payment).
- **`[NNN]`**: Số thứ tự gồm 3 chữ số bắt đầu từ `001` (Ví dụ: `001`, `002`, `015`). Không dùng số tự do (ví dụ `1` hay `01`).

---

## 3. 📋 Bảng Đặc Tả Thuộc Tính (Field Specification)

| Tên trường (Field) | Kiểu dữ liệu | Bắt buộc | Ràng buộc giá trị (Constraints) | Mô tả & Hướng dẫn |
|---|:---:|:---:|---|---|
| **`finding_id`** | String | ✅ Có | Regex: `^(GAP\|LOGIC\|EDGE\|BVA\|RISK\|DES)-[A-Z0-9]{2,6}-\d{3}$` | Mã định danh duy nhất của phát hiện trong toàn bộ dự án. |
| **`title`** | String | ✅ Có | Độ dài: 10 – 120 ký tự | Tóm tắt ngắn gọn bản chất của vấn đề. |
| **`type`** | Enum | ✅ Có | `Ambiguity` \| `Contradiction` \| `Missing Rule` \| `Logic Anomaly` \| `Invalid State Transition` \| `Risk` \| `Edge Case` \| `Design Mismatch` | Phân loại bản chất của phát hiện. |
| **`severity`** | Enum | ✅ Có | `Critical` (P0) \| `High` (P1) \| `Medium` (P2) \| `Low` (P3) | Mức độ nghiêm trọng định nghĩa theo `rules/global_rules.md §3`. |
| **`source_doc`** | String | ✅ Có | Tên file chính xác trong `docs/` | Tài liệu nguồn phát hiện vấn đề (Ví dụ: `Rider App FRS.md`). |
| **`location`** | String | ✅ Có | Tên mục, Section ID, hoặc số dòng | Vị trí chính xác trong tài liệu (Ví dụ: `Section 3.5, lines 1771-1800`). |
| **`evidence`** | String | ✅ Có | Trích dẫn trực tiếp trong ngoặc kép hoặc `[NOT FOUND in {doc}]` | Bằng chứng gốc trích từ tài liệu. **CẤM bịa đặt bằng chứng.** |
| **`explanation`** | String | ✅ Có | Giải thích rõ ràng bằng Tiếng Việt | Lý do vì sao đây là lỗ hổng hoặc bất thường logic. |
| **`impact`** | String | ✅ Có | Phân tích tác động nghiệp vụ/kỹ thuật | Hậu quả nếu không xử lý (ảnh hưởng Dev, Tester hoặc End-user). |
| **`recommendation`**| String | ⬜ Tuỳ chọn | Giải pháp khắc phục đề xuất | Đề xuất hướng xử lý. Nếu thiếu thông tin kỹ thuật thì để trống, không đoán mò. |
| **`status`** | Enum | ✅ Có | `Open` \| `Pending Verification` \| `Confirmed` \| `Rejected` | Trạng thái hiện tại của phát hiện. Mặc định là `Pending Verification` nếu là gap cần BA xác nhận. |

---

## 4. 📝 Định Dạng Hiển Thị Chuẩn (Standard Markdown Representation)

Mọi báo cáo khi render danh sách Findings phải tuân thủ định dạng khối (Block) hoặc bảng (Register) sau:

### A. Định dạng Khối Chi Tiết (Detailed Block Format):
```markdown
### 📌 [GAP-RID-001]: Thiếu cơ chế xử lý khi hủy chuyến sau khi tài xế đã bấm đón
- **Loại phát hiện (Type)**: Missing Rule
- **Mức độ (Severity)**: 🔴 Critical (P0)
- **Trạng thái (Status)**: Pending Verification
- **Vị trí (Location)**: `Rider App FRS.md` > Section 3.5 (In-Trip Modifications)

**🔍 Bằng chứng (Evidence):**
> "Rider can request cancellation during active trip by tapping Cancel button."
> Target FRS: [NOT FOUND handling rule for driver payout when cancelled after pickup]

**⚠️ Tác động (Impact):**
Tài xế bị mất công đón và di chuyển một đoạn nhưng hệ thống không có công thức đền bù cước cơ bản, dẫn đến tranh chấp tài chính và lỗi tính tiền tại Stripe.

**💡 Đề xuất (Recommendation):**
Bổ sung Business Rule: Nếu hủy sau pickup, áp dụng Minimum Trip Fare hoặc tính cước theo cự ly thực tế đã di chuyển đến điểm hủy.
```

### B. Định dạng Bảng Tóm Tắt (Register Table Format):
```markdown
| Finding ID | Title | Type | Severity | Status | Location |
|---|---|---|:---:|:---:|---|
| `GAP-RID-001` | Thiếu công thức hủy sau pickup | Missing Rule | 🔴 Critical | Pending Verification | Sec 3.5 |
| `LOGIC-RID-002` | Mâu thuẫn cước Delta âm | Logic Anomaly | 🟠 High | Open | Sec 3.5.2 |
| `RISK-RID-001` | Double charge khi Pre-auth timeout | Risk (Payment) | 🔴 Critical | Open | Stripe Integration |
```

---

## 5. 🛑 Nguyên Tắc Kiểm Soát Chất Lượng (Quality Rules)
1. **Missing Requirement ≠ Confirmed Defect:** Một yêu cầu bị thiếu trong tài liệu chỉ là một nghi vấn (Gap/Open item). Khi chưa có phản hồi chính thức từ BA/PO, bắt buộc để `status = Pending Verification`.
2. **Không Hallucination:** Không được tạo Finding nếu không trích dẫn được câu chữ trong tài liệu hoặc chỉ ra được vị trí section chính xác đã tra cứu mà không thấy.
