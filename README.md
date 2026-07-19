# AI Quality Assurance & Requirement Analysis Framework (v3.0.0)

An ultra-lean, **Agent-Based AI Framework** designed to perform Requirement Analysis, Risk Assessment, Test Engineering, and Business Validation on software requirements.

> **Note**: This system focuses purely on logic analysis, risk assessment, and manual/UAT test generation. It does NOT include CI/CD, automation testing, API testing, or database testing.

---

## 🏗 Architecture

This framework uses a deterministic, multi-agent architecture where agents share inputs and outputs with each other.

```text
Input Documents → Rules → Workflow → Agents → Output Reports
```

### Folder Structure

| Folder | Purpose |
|--------|---------|
| `docs/requirements/` | **Input**: PRD, BRD, SRS. |
| `docs/designs/` | **Input**: UI Flow, Wireframes, Figma exports. |
| `reports/` | **Output**: Where all generated Markdown reports are saved. |
| `agents/` | **Core Logic**: Contains the definitions for the 9 analytical agents. |
| `workflows/` | **Orchestration**: Defines the execution pipelines for different phases. |
| `rules/` | **Standards**: Global standards, requirement quality metrics, and reporting formats. |
| `templates/` | **Formatting**: Reusable Markdown templates for consistent report output. |

---

## 🤖 The Agents (v3.0.0)

1. **`requirement_gap_analyst`**: Audits internal logic (ambiguity, edge cases) AND detects cross-document traceability gaps (e.g. PRD vs SRS).
2. **`design_auditor`**: Audits Design/UI flow against SRS to find missing components, error states, and flow mismatches.
3. **`advanced_edge_case_analyzer`**: Deep dives into extreme data boundaries, concurrency, race conditions, and state interruptions.
4. **`risk_analyst`**: Identifies business, technical, security, performance, and operational risks. Prioritizes them for testing.
5. **`scenario_generator`**: Generates comprehensive Test Scenarios covering positive, negative, and edge cases.
6. **`testcase_generator`**: Generates step-by-step Manual Test Cases from Scenarios.
7. **`uat_script_generator`**: Generates User Acceptance Test scripts written in business language for clients/stakeholders.
8. **`coverage_analyst`**: Maps the generated test cases back to the requirements to calculate coverage.
9. **`master_orchestrator`**: The controller that runs the workflows.

---

## 🔄 Workflows & Use Cases (Khi nào dùng cái nào?)

Hệ thống có 5 Workflow chính, phục vụ cho các thời điểm (Phases) khác nhau trong vòng đời phát triển phần mềm (SDLC):

### 1. `01_Requirement_Review_Workflow.md` (Requirement & Design Review)
- **Giai đoạn**: Khởi tạo dự án (Project Kick-off) / Design Phase.
- **Khi nào dùng**: Khi BA vừa viết xong Draft Requirement và team Design vừa làm xong giao diện.
- **Mục đích**: Phát hiện lỗ hổng logic, mâu thuẫn trong yêu cầu và kiểm tra tính nhất quán giữa Design với Requirement. Đưa ra đánh giá Go/No-Go trước khi Dev bắt đầu code.
- **Ví dụ thực tế**: BA bàn giao tài liệu PRD cho tính năng "Đăng ký tài khoản tài xế" và Designer bàn giao wireframe giao diện. Chạy workflow này để check xem trên thiết kế UI có thiếu các trường bắt buộc không (ví dụ: PRD bắt buộc upload Bằng lái xe nhưng UI thiếu nút Upload), hoặc thiết kế UI có phát sinh các trạng thái chưa được định nghĩa trong PRD không.

### 2. `02_Shift_Left_Risk_Assessment.md` (Shift-Left Risk Assessment)
- **Giai đoạn**: Sprint Planning / Backlog Grooming.
- **Khi nào dùng**: Khi cần ước lượng rủi ro của một tính năng mới trước khi quyết định đưa vào Sprint phát triển.
- **Mục đích**: Tập trung dò tìm rủi ro tiềm ẩn (bảo mật, hiệu năng, nghiệp vụ) và các lỗi hóc búa (Edge Cases). Giúp Project Manager (PM) cân nhắc mức độ rủi ro của tính năng.
- **Ví dụ thực tế**: Team chuẩn bị làm tính năng "Thanh toán qua ví điện tử". Trước khi dev code, chạy workflow này để dò tìm các Edge Case và rủi ro bảo mật tiềm ẩn như: mất kết nối khi đang trừ tiền ví (race condition), tài khoản bị trừ tiền 2 lần do người dùng nhấn nút Submit liên tục (double submission), hoặc lỗi rò rỉ token thanh toán.

### 3. `03_QA_Test_Engineering.md` (Full QA Test Engineering)
- **Giai đoạn**: Development Phase / QA Planning.
- **Khi nào dùng**: Khi Dev đang code và team QA/Tester cần chuẩn bị sẵn Kịch bản kiểm thử (Test Scenarios & Test Cases).
- **Mục đích**: Sinh ra bộ test đầy đủ (Positive, Negative, Boundary) và đo lường độ bao phủ (Coverage) để đảm bảo không lọt lỗi.
- **Ví dụ thực tế**: Dev đang code tính năng "Đặt xe (Booking Trip)". QA cần viết bộ test cases chi tiết. Chạy workflow này để tự động sinh ra Test Scenarios và Test Cases chi tiết (các bước nhập điểm đón/đến, tính giá tiền, áp mã giảm giá, trường hợp lỗi mạng). Cuối cùng đo lường xem bộ testcase đã bao phủ toàn bộ điều kiện nghiệp vụ trong tài liệu PRD chưa.

### 4. `04_Business_UAT_Validation.md` (Business UAT Validation - UAT Readiness)
- **Giai đoạn**: Staging / Pre-Release.
- **Khi nào dùng**: Khi chuẩn bị bàn giao phần mềm cho Khách hàng (Client) hoặc người dùng cuối (Business User) nghiệm thu.
- **Mục đích**: Tự động viết ra các kịch bản UAT bằng ngôn ngữ phi kỹ thuật (kinh doanh), có tính đến các rủi ro cốt lõi để khách hàng dễ thao tác theo.
- **Ví dụ thực tế**: Tính năng "Rút tiền cho tài xế (Driver Payout)" đã code xong và đang ở môi trường Staging. Trước khi bàn giao cho PO (Product Owner) nghiệm thu, chạy workflow này để sinh bộ kịch bản UAT dễ hiểu bằng ngôn ngữ nghiệp vụ (ví dụ: "Là tài xế, tôi muốn rút 500k về ngân hàng..." -> các bước thực hiện -> kết quả mong đợi hiển thị số dư mới hợp lệ) giúp người dùng cuối dễ dàng test theo đúng luồng nghiệp vụ.

### 5. `05_Ultimate_QA_Pipeline.md` (Comprehensive QA Pipeline)
- **Giai đoạn**: Major Release / Regression Testing.
- **Khi nào dùng**: Trước một đợt ra mắt phiên bản lớn cực kỳ quan trọng, hoặc cần kiểm thử hồi quy toàn bộ hệ thống cũ.
- **Mục đích**: Chạy một lèo tất cả các Agents từ khâu đọc hiểu, dò lỗi, phân tích rủi ro, viết test case đến UAT script. Dòng chảy tự động và toàn diện nhất.
- **Ví dụ thực tế**: Chuẩn bị release phiên bản lớn v3.0.0 của ứng dụng RideArc (gồm cả Đặt xe, Thanh toán, Đăng ký). Đây là đợt Regression lớn trước khi Go-live. Chạy workflow này để quét toàn bộ hệ thống từ đầu đến cuối: phân tích lại lỗ hổng tài liệu, tìm edge cases, đánh giá rủi ro tổng thể, sinh scenario/testcase chi tiết, viết UAT, và đo lường độ bao phủ tổng quan.

---

## 🚀 Cách chạy (Execution Flow)

1. **Chuẩn bị đầu vào**: Bỏ file tài liệu requirement (PRD.md, BRD.md, SRS.md, v.v.) vào thư mục `docs/requirements/`. Nếu có design, bỏ vào `docs/designs/`.
2. **Kích hoạt Orchestrator**:
   ```bash
   Run agents/master_orchestrator.md
   ```
3. **Chọn Workflow**: Yêu cầu Master Orchestrator chạy một trong 5 workflow tương ứng với nhu cầu hiện tại của bạn.

---

## 🛡 Core Principles

1. **No Hallucination**: Agents are strictly forbidden from inventing requirements.
2. **Evidence-Based**: Every finding (except 'Missing' features) must cite direct quotes from the input documents.
3. **Deterministic Output**: Reports always follow predefined templates.
