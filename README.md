# AI Quality Assurance & Requirement Analysis Framework (v3.1.0)

An ultra-lean, **Agent-Based AI Framework** designed to perform Requirement Analysis, Risk Assessment, Test Engineering, and Business Validation on software requirements.

> **Note**: This system focuses purely on logic analysis, risk assessment, and manual/UAT test generation. It does NOT include CI/CD, automation testing, API testing, or database testing.

---

## 🏗 Architecture

This framework uses a deterministic, multi-agent architecture where agents share inputs and outputs with each other.

```text
Input Documents → Rules & Governance → Workflow → Agents → Output Reports & Exports
```

### Folder Structure

| Folder | Purpose |
|--------|---------|
| `docs/requirements/` | **Input**: PRD, BRD, SRS. |
| `docs/designs/` | **Input**: UI Flow, Wireframes, Figma exports. |
| `reports/` | **Output**: Where all generated Markdown reports, CSVs, and DOCX files are saved. |
| `.agents/` | **AI Governance**: Framework kiểm soát hành vi AI Agent (`AGENTS.md`) — Anti-hallucination protocols, Level -1 đến Level 4 test engineering rules, source-of-truth governance cho AI Coding Assistants. |
| `agents/` | **Analytical QA Agents**: Chứa 10 prompt định nghĩa vai trò phân tích chuyên biệt (Gap, Logic Anomaly, Risk, Testcase, Coverage...). |
| `workflows/` | **Orchestration**: Defines the execution pipelines for different SDLC phases (01 to 05). |
| `rules/` | **Standards**: Global standards, requirement quality metrics, test generation rules, and reporting formats. |
| `schemas/` | **Master Contracts**: Schemas chuẩn cho Findings (`finding.schema.md`), Test Cases 14 cột (`testcase.schema.md`), UAT (`uat_script.schema.md`), và Coverage (`coverage.schema.md`). |
| `templates/` | **Formatting**: Reusable Markdown templates for consistent report output. |
| `scripts/` | **Export Utilities**: Python scripts for artifact conversions (`md_to_csv.py`, `md_to_docx.py`). |

> 💡 **Phân biệt quan trọng giữa `.agents/` và `agents/`:**
> - `.agents/` (ẩn): Chứa quy tắc quản trị cấp hệ thống (`AGENTS.md`) quy định AI coding assistant (Antigravity, Cursor, Copilot) phải tuân thủ nghiêm ngặt: không được bịa đặt (Anti-hallucination), chuẩn ngôn ngữ (Báo cáo tiếng Việt, Testcase tiếng Anh), xử lý fail-fast, phân loại Testability.
> - `agents/`: Chứa các role/agent nghiệp vụ cụ thể tham gia vào từng bước phân tích và sinh test trong pipeline.

---

## 🤖 The Agents

1. **`requirement_gap_analyst`**: Audits internal logic (ambiguity, edge cases) AND detects cross-document traceability gaps (e.g. PRD vs SRS).
2. **`requirement_logic_analyst`**: Challenges business plausibility, detects logical anomalies, internal contradictions, invalid state transitions, missing rules, and hidden assumptions.
3. **`design_auditor`**: Audits Design/UI flow against SRS to find missing components, error states, and flow mismatches.
4. **`advanced_edge_case_analyzer`**: Deep dives into extreme data boundaries, concurrency, race conditions, and state interruptions.
5. **`risk_analyst`**: Identifies business, technical, security, performance, and operational risks. Prioritizes them for testing.
6. **`scenario_generator`**: Generates comprehensive Test Scenarios covering positive, negative, and edge cases.
7. **`testcase_generator`**: Generates step-by-step Manual Test Cases from Scenarios.
8. **`uat_script_generator`**: Generates User Acceptance Test scripts written in business language for clients/stakeholders.
9. **`coverage_analyst`**: Maps the generated test cases back to the requirements to calculate coverage.
10. **`master_orchestrator`**: The central controller that runs the workflows.

---

## 🔄 Workflows & Use Cases (Khi nào dùng cái nào?)

Hệ thống có 5 Workflow chính, phục vụ cho các thời điểm (Phases) khác nhau trong vòng đời phát triển phần mềm (SDLC):

### 1. `01_Requirement_Review_Workflow.md` (Requirement & Design Review)
- **Giai đoạn**: Khởi tạo dự án (Project Kick-off) / Design Phase.
- **Khi nào dùng**: Khi BA vừa viết xong Draft Requirement và team Design vừa làm xong giao diện.
- **Thứ tự thực thi**: `requirement_gap_analyst` → `requirement_logic_analyst` → `design_auditor` (tuỳ chọn) → `Executive Summary`.
- **Mục đích**: Phát hiện lỗ hổng logic, bất thường nghiệp vụ (`requirement_logic_analyst`), mâu thuẫn trong yêu cầu và kiểm tra tính nhất quán giữa Design với Requirement. Đưa ra đánh giá Go/No-Go trước khi Dev bắt đầu code.

### 2. `02_Shift_Left_Risk_Assessment.md` (Shift-Left Risk Assessment)
- **Giai đoạn**: Sprint Planning / Backlog Grooming.
- **Khi nào dùng**: Khi cần ước lượng rủi ro của một tính năng mới trước khi quyết định đưa vào Sprint phát triển.
- **Thứ tự thực thi**: `requirement_gap_analyst` → `requirement_logic_analyst` → `advanced_edge_case_analyzer` → `risk_analyst` → `Development Readiness Report`.
- **Mục đích**: Tập trung rà soát tính hợp lý nghiệp vụ, dò tìm rủi ro tiềm ẩn (bảo mật, hiệu năng, nghiệp vụ) và các lỗi hóc búa (Edge Cases). Giúp PM/EM cân nhắc mức độ rủi ro và độ sẵn sàng trước khi sprint bắt đầu.

### 3. `03_QA_Test_Engineering.md` (Full QA Test Engineering)
- **Giai đoạn**: Development Phase / QA Planning.
- **Khi nào dùng**: Khi Dev đang code và team QA/Tester cần chuẩn bị sẵn Kịch bản kiểm thử (Test Scenarios & Test Cases).
- **Thứ tự thực thi**: `requirement_gap_analyst` → `requirement_logic_analyst` → `advanced_edge_case_analyzer` → `risk_analyst` → `scenario_generator` → `testcase_generator` → `coverage_analyst` → `CSV Export`.
- **Mục đích**: Sinh ra bộ test đầy đủ (Positive, Negative, Boundary, 14 cột chuẩn) và đo lường độ bao phủ (Coverage) 100% trước khi xuất file CSV sẵn sàng import vào Test Management Tools (Jira/Xray/TestRail).

### 4. `04_Business_UAT_Validation.md` (Business UAT Validation - UAT Readiness)
- **Giai đoạn**: Staging / Pre-Release.
- **Khi nào dùng**: Khi chuẩn bị bàn giao phần mềm cho Khách hàng (Client) hoặc người dùng cuối (Business User) nghiệm thu.
- **Thứ tự thực thi**: `requirement_gap_analyst` (baseline check) → `risk_analyst` → `scenario_generator` → `uat_script_generator` → `UAT Readiness Report`.
- **Mục đích**: Kiểm tra nền tảng yêu cầu, tự động viết ra các kịch bản UAT bằng ngôn ngữ kinh doanh (User Stories & Acceptance Journeys), có tính đến các rủi ro cốt lõi để khách hàng dễ thao tác nghiệm thu.

### 5. `05_Ultimate_QA_Pipeline.md` (Comprehensive QA Pipeline)
- **Giai đoạn**: Major Release / Regression Testing.
- **Khi nào dùng**: Trước một đợt ra mắt phiên bản lớn cực kỳ quan trọng, hoặc cần kiểm thử hồi quy toàn bộ hệ thống cũ.
- **Thứ tự thực thi**: Chạy toàn diện 10 Agents từ Step 1 đến Step 9, sau đó tại Step 10 tự động hóa việc xuất cả file CSV và tài liệu Word (.docx).
- **Mục đích**: Dòng chảy tự động và toàn diện nhất: phân tích khoảng trống tài liệu, thử thách tính hợp lý nghiệp vụ, tìm edge cases, ma trận rủi ro, test scenarios, test cases chi tiết, kịch bản UAT, chốt sổ coverage 100%, và tổng hợp báo cáo Executive Summary kèm export đa định dạng.

---

## 🛠 Export Utilities & Scripts

Thư mục `scripts/` cung cấp 2 tiện ích chuyển đổi tài liệu chuẩn:

1. **`scripts/md_to_csv.py`**:
   - Tự động trích xuất bảng Test Case 14-cột từ file `*_Testcases.md` sang định dạng `.csv` UTF-8 BOM.
   - Xử lý mượt mà thẻ `<br>`, escaped pipe (`\|`), và các ký tự đặc biệt, sẵn sàng import trực tiếp vào Jira / Xray / Zephyr / TestRail.
   - Sử dụng: `python scripts/md_to_csv.py reports/[Requirement_Name]_Testcases.md reports/[Requirement_Name]_Testcases.csv`

2. **`scripts/md_to_docx.py`**:
   - Chuyển đổi báo cáo Markdown sang tài liệu Microsoft Word (`.docx`) chuyên nghiệp.
   - Tự động định dạng bảng, tiêu đề, blockquote, bullet points và làm sạch các biểu thức toán học LaTeX.
   - Sử dụng: `python scripts/md_to_docx.py reports/[Requirement_Name]_Executive_Summary.md reports/[Requirement_Name]_Executive_Summary.docx`

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
4. **Language Standard**: QA reports in Vietnamese, Test Case tables in English, preserving exact UI labels and business codes.

