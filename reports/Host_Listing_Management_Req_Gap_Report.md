# 🧠 Requirement & Traceability Gap Report

---

## 📄 Document Metadata
| Property | Details |
|----------|---------|
| **Date Generated** | 2026-07-01 |
| **Documents Analyzed**| `Host Listing Management.md` |
| **Analyzed By** | Requirement & Gap Analyst (v3.0.0) |
| **Requirement Quality Score** | **75%** |
| **Overall Health** | 🟡 Needs Revision |

---

## 📊 1. Executive Summary

| Severity / Type | Critical 🔴 | High 🟠 | Medium 🟡 | Low 🟢 |
|-----------------|------------|--------|----------|-------|
| **Traceability Gaps (Cross-Doc)** | 0 | 0 | 0 | 0 |
| **Logic Defects (Internal)** | 1 | 3 | 4 | 2 |

*(Note: Cross-Document Traceability was skipped because only 1 document was provided).*

---

## 🚨 2. Traceability Gaps (Cross-Document)
*(N/A - Only 1 requirement document provided for analysis).*

---

## 🚨 3. Requirement Quality Defects (Internal)
*(Ambiguity, Missing Business Rules, Missing Edge Cases)*

### 📌 [REQ-DEF-001]: Missing Content for Confirmation Trigger
- **Category**: Logic (Incomplete)
- **Severity**: 🔴 Critical 
- **Location**: `FR-ACS-LIM-2.6 Confirmation Trigger`

**🔍 Evidence:**
> "FR-ACS-LIM-2.6 Confirmation Trigger" *(Followed by entirely blank space)*

**❌ Defect & Recommendation:**
Phần 2.6 hoàn toàn bị bỏ trống, không có định nghĩa nút Save/Discard cho phần chỉnh sửa thông tin xe. Nếu không có trigger lưu dữ liệu, luồng UI sẽ bị kẹt.
👉 **Fix**: Bổ sung chi tiết hành vi của nút "Lưu thay đổi" và "Hủy", tương tự như mục 3.4.

---

### 📌 [REQ-DEF-002]: Missing Odometer Logic Validation (Go-Backwards Risk)
- **Category**: Edge Case / Business Logic
- **Severity**: 🟠 High
- **Location**: `FR-ACS-LIM-2.2 Odometer Metric Control`

**🔍 Evidence:**
> "It allows the host to input an integer representing the car's current total mileage configuration."

**❌ Defect & Recommendation:**
Không có Business Rule nào ngăn chặn việc Host nhập số Odometer *nhỏ hơn* số Odometer hiện tại trong cơ sở dữ liệu (Tua công tơ mét).
👉 **Fix**: Thêm Validation Rule: `New Odometer Value >= Current Odometer Value`. Nếu nhập nhỏ hơn, hiển thị lỗi.

---

### 📌 [REQ-DEF-003]: Missing Pricing Tier Validation
- **Category**: Business Logic
- **Severity**: 🟠 High
- **Location**: `FR-ACS-LIM-3.3 Duration-Based Tier Percentage Reductions`

**🔍 Evidence:**
> "Validation Constraint Rules: The input fields shall only accept numeric values between 0 and 99."

**❌ Defect & Recommendation:**
Hệ thống chỉ validate số 0-99, nhưng không validate logic quan hệ giữa các tier. Host có thể thiết lập: Giảm giá 3 ngày = 50%, nhưng giảm giá 30 ngày = 10%. Điều này phá vỡ logic khuyến mãi dài ngày.
👉 **Fix**: Bổ sung Rule: `3+ Day % <= 7+ Day % <= 30+ Day %`. 

---

### 📌 [REQ-DEF-004]: Missing Automated Buffer Release Rule
- **Category**: Edge Case
- **Severity**: 🟠 High
- **Location**: `FR-ACS-LIM-4.2.2 Automated Pre & Post-Trip Buffer`

**🔍 Evidence:**
> "...the system shall automatically convert both the specified calendar days immediately preceding (BEFORE) and immediately following (AFTER) the reservation block into the Unavailable (Solid Grey) state."

**❌ Defect & Recommendation:**
Tài liệu định nghĩa rất kỹ việc block 5 ngày trước/sau khi Booking thành công. Tuy nhiên, nếu Renter HỦY (Cancel) booking đó thì sao? 
👉 **Fix**: Cần định nghĩa rõ: Khi một Booking bị Cancelled, hệ thống có tự động nhả (unblock) trạng thái Unavailable của 5 ngày đệm đó về lại Available hay không.

---

### 📌 [REQ-DEF-005]: Unhandled Primary Location Deactivation
- **Category**: Edge Case
- **Severity**: 🟡 Medium
- **Location**: `FR-ACS-LIM-5.3.2 Immutable Location Lock Rules`

**🔍 Evidence:**
> "Hide Location: ...Activating this flag immediately flags the record as inactive, hiding it entirely from future marketplace search..."

**❌ Defect & Recommendation:**
Nếu Host chọn "Hide" chính cái địa điểm đang được gán badge "Primary", hệ thống sẽ xử lý thế nào? Xe không thể không có địa điểm Primary.
👉 **Fix**: Thêm logic: Không cho phép Hide "Primary Location" trừ khi Host chọn một location khác lên làm Primary trước.

---

### 📌 [REQ-DEF-006]: Missing Media Validation Constraints
- **Category**: NFR / Logic
- **Severity**: 🟡 Medium
- **Location**: `FR-ACS-LIM-2.4 Gallery Layout Matrix`

**🔍 Evidence:**
> "...showing active vs capacity metrics (e.g., "7/10 Photos Uploaded")."

**❌ Defect & Recommendation:**
Chưa định nghĩa số lượng ảnh tối thiểu (Minimum required) để xe được phép lên sàn (Listed). Cũng như chưa định nghĩa dung lượng/định dạng ảnh cho phép.
👉 **Fix**: Bổ sung constraint: Phải có ít nhất 1 ảnh (MAIN) để kích hoạt List. Định dạng JPG/PNG, Max 5MB/ảnh.

---

## 🗺️ 4. Missing Requirement Map

| Category | Missing Items |
|----------|---------------|
| **Missing Flows** | - Luồng Hủy Booking (Tác động tới Calendar Buffer)<br>- Luồng chuyển đổi Primary Location |
| **Missing Rules** | - Logic validation giá giảm dần (`3+ <= 7+ <= 30+`)<br>- Logic ngăn chặn tua lùi Odometer |
| **Missing States** | - Nút Save/Discard bị trống ở mục 2.6<br>- Pagination/Lazy load cho danh sách xe ở mục 1.1 |
| **Missing Edge Cases**| - Text truncation cho tên xe quá dài trên Profile Card<br>- Nhập description toàn ký tự trắng |

---

## ✅ 5. Action Items (Prioritized)
| Priority | Action Required |
|----------|-----------------|
| **P0** | Viết bổ sung ngay phần **2.6 Confirmation Trigger** (Lưu / Hủy thông tin). |
| **P1** | Bổ sung các rule validation chặn nhập sai logic cho: **Odometer** và **Pricing Tier**. |
| **P1** | Cụ thể hóa luồng giải phóng Calendar Buffer khi Booking bị hủy (Cancel). |
| **P2** | Định nghĩa rõ điều kiện file Upload (Dung lượng, định dạng, số lượng tối thiểu). |
| **P2** | Xử lý chặn logic ẩn (Hide) địa điểm Primary. |

---
# End of Report
