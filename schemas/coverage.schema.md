# 📐 Master Coverage Schema (v1.0.0)
> **Trạng thái:** Active Standard | **Áp dụng cho:** `coverage_analyst`, `templates/coverage_report.md`, `master_orchestrator`

---

## 1. 🎯 Mục Đích & Tiêu Chuẩn Đo Lường
Schema này định nghĩa cấu trúc đo lường độ bao phủ (Coverage) đa chiều của framework. 

Nguyên tắc cốt lõi: **Không đo độ bao phủ một cách hời hợt theo tên tính năng lớn.** Toàn bộ việc tính toán phải dựa trên việc phân rã yêu cầu thành các **điều kiện nguyên tử (Atomic Conditions)** và đối chiếu đa chiều với Scenarios, Edge Cases và Risk items.

---

## 2. 🚦 4 Trạng Thái Testability & Công Thức Tính Toán

Theo quy định `<RULE[requirement_testability_and_coverage_status]>` trong `.agents/AGENTS.md`:

| Trạng thái Testability | Định nghĩa kỹ thuật | Cách tính vào Mẫu số Coverage | Hành động xử lý |
|---|---|:---:|---|
| 🟢 **`TESTABLE`** | Có Acceptance Criteria, Logic rẽ nhánh và Oracle xác định Pass/Fail rõ ràng. | **Tính vào Functional Coverage** (100% khi toàn bộ Atomic Conditions có test case). | Sinh test cases đầy đủ các chiều (Positive, Negative, Boundary). |
| 🟡 **`PARTIALLY TESTABLE`** | Một phần yêu cầu rõ ràng, một phần thiếu công thức hoặc còn định tính. | **Coverage = X/Y Conditions** (Ví dụ: 2/4 conditions = 50% Coverage). | Gắn cờ `PARTIAL / Pending Clarification`. Không được tính là Fully Covered. |
| 🔵 **`NEEDS VERIFICATION`** | Kiểm thử được về mặt lý thuyết nhưng thiếu System Design / API Contract / Technical Evidence. | **Chưa tính vào Functional Coverage** cho đến khi có bằng chứng kỹ thuật chính thức. | Ghi nhận vào Gap Report: `[Verification Request — Pending response from: System Design / BA / Dev]`. |
| 🔴 **`NOT TESTABLE`** | Không có tiêu chí khách quan để xác định Pass/Fail (yêu cầu hoàn toàn cảm tính). | **Loại khỏi mẫu số** (`Coverage = N/A`). | Không sinh test case giả định. Đưa 100% sang Requirement Gap Report. |

---

## 3. 📊 Ma Trận Bao Phủ Đa Chiều (Multi-Dimensional Coverage Matrix)

Một bộ báo cáo Coverage hợp lệ bắt buộc phải có đầy đủ 4 chiều đo lường:

### 1. Chiều 1: Functional Requirement Coverage (Atomic Level)
$$\text{Functional Coverage (\%)} = \frac{\sum \text{Testable Atomic Conditions Covered}}{\sum \text{Total Testable Atomic Conditions}} \times 100\%$$
- **Ngưỡng bắt buộc (Quality Gate):** Phải đạt **100% tuyệt đối** thì pipeline mới được kích hoạt bước export CSV. Nếu $< 100\%$, pipeline tự động quay lại `testcase_generator` để bổ sung.

### 2. Chiều 2: Scenario Coverage
- Tỷ lệ kịch bản trong `*_Test_Scenarios_Report.md` đã được chuyển hóa thành ít nhất một Manual Test Case cụ thể.
- **Mục tiêu:** $\ge 95\%$.

### 3. Chiều 3: Edge Case Coverage
- Tỷ lệ các ca kiểm thử biên cực hạn trong `*_Edge_Case_Report.md` đã có Test Case tương ứng.
- **Mục tiêu:** $100\%$ các ca P0 và P1.

### 4. Chiều 4: Risk Mitigation Coverage
- Tỷ lệ rủi ro trong `*_Risk_Analysis_Report.md` đã có kịch bản kiểm thử phòng ngừa.
- **Mục tiêu:** $100\%$ các rủi ro Critical (P0) và High (P1).

---

## 4. 📋 Bảng Đặc Tả Dữ Liệu Báo Cáo Coverage (Table Specification)

### A. Bảng Phân Rã Yêu Cầu & Trạng Thái Bao Phủ (Requirement Coverage Table):
```markdown
| Atomic ID | Tên Yêu Cầu Con | Trạng Thái Testability | Test Case Mappings | Coverage Status | Ghi Chú |
|---|---|:---:|---|:---:|---|
| `FR-RID-7.1` | Điều kiện kích hoạt đổi điểm đến | 🟢 TESTABLE | `RID-TC-001`, `RID-TC-002` | 100% | Đã bao phủ In Trip vs En Route |
| `FR-RID-7.5` | Khóa cự ly Proximity Lock | 🟢 TESTABLE | `RID-TC-039`, `RID-TC-040` | 100% | BVA 499m vs 500m, 59s vs 60s |
| `FR-RID-7.8` | Tính cước Delta từ Original Pickup | 🟢 TESTABLE | `RID-TC-016`, `RID-TC-017` | 100% | Kiểm thử công thức tính từ điểm đón gốc |
| `FR-RID-7.X` | Hiệu năng phản hồi của Routing Engine | 🔵 NEEDS VERIFICATION | N/A | 0% | [SLA: TBD] — Chưa có API Contract |
```

### B. Bảng Ma Trận Đối Soát Chéo Artifact (Cross-Artifact Traceability Matrix):
```markdown
| Nguồn phát hiện | Item ID | Mức độ nghiêm trọng | Mapped Test Case(s) | Trạng thái phòng ngừa |
|---|---|:---:|---|:---:|
| Risk Report | `RISK-RID-001` | 🔴 Critical | `RID-TC-016`, `RID-TC-017` | ✅ Mitigated |
| Risk Report | `RISK-RID-002` | 🔴 Critical | `RID-TC-026`, `RID-TC-027` | ✅ Mitigated |
| Edge Case Report | `EDGE-RID-001` | 🟠 High | `RID-TC-056` | ✅ Mitigated |
| Edge Case Report | `BVA-RID-005` | 🟠 High | `RID-TC-034` | ✅ Mitigated |
```

---

## 5. 🛑 Nguyên Tắc Phòng Ngừa Báo Cáo Khống (Anti-Coverage-Shortcut Rules)
1. **Cấm gộp đại diện:** Không được sinh 1 test case đại diện rồi ghi *"Các trường hợp khác tương tự"*. Mỗi Atomic Condition phải có ít nhất 1 test case rõ ràng.
2. **Cấm tính khống:** Trạng thái `NEEDS VERIFICATION` hoặc `PARTIALLY TESTABLE` tuyệt đối không được làm tròn thành 100% trong báo cáo tổng hợp gửi cho PM/PO.
