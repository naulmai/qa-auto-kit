# Workflow: Full QA Test Engineering

> **Controller**: `agents/master_orchestrator.md`

---

## Purpose
Tự động hóa quá trình sinh kịch bản test từ mức high-level đến chi tiết, và cuối cùng là đo lường độ bao phủ (coverage) để đảm bảo không bỏ sót case nào.

## Execution Order

```mermaid
graph TD
    A[Start Pipeline] --> A1(requirement_gap_analyst)
    A1 --> B(risk_analyst)
    B --> C(advanced_edge_case_analyzer)
    C --> D(scenario_generator)
    D --> E(testcase_generator)
    E --> F(coverage_analyst)
    F --> G[End Pipeline]
```

## Step 1: Requirement & Gap Analysis
- **Agent**: `agents/requirement_gap_analyst.md`
- **Output**: `reports/[Requirement_Name]_Req_Gap_Report.md` (dynamic naming)
- **Objective**: Kiểm tra chất lượng requirement, phát hiện lỗ hổng logic và mâu thuẫn trước khi bắt đầu sinh test.

## Step 2: Risk Analysis (Optional but Recommended)
- **Agent**: `agents/risk_analyst.md`
- **Output**: `reports/[Requirement_Name]_Risk_Analysis_Report.md` (dynamic naming)
- **Objective**: Xác định các rủi ro để hỗ trợ sinh Test Scenarios toàn diện hơn.

## Step 3: Edge Case Analysis (Mandatory for strict rules)
- **Agent**: `agents/advanced_edge_case_analyzer.md`
- **Output**: `reports/[Requirement_Name]_Edge_Case_Report.md` (dynamic naming)
- **Objective**: Phân tích sâu vào các điều kiện biên (Boundary), giới hạn dữ liệu (Data constraints), và luồng rẽ nhánh ngầm định để chuẩn bị kịch bản cho Scenario Generator.

## Step 4: Scenario Generation
- **Agent**: `agents/scenario_generator.md`
- **Output**: `reports/[Requirement_Name]_Test_Scenarios_Report.md` (dynamic naming)
- **Objective**: Phân tích Requirement (kèm Risk Analysis và Edge Cases) để sinh ra các Kịch bản kiểm thử (Test Scenarios) cấp cao.

## Step 5: Test Case Generation
- **Agent**: `agents/testcase_generator.md`
- **Output**: `reports/[Requirement_Name]_Testcases.md`, `reports/[Requirement_Name]_Testcases.csv` (dynamic naming)
- **Objective**: Dựa trên các Scenarios ở trên, sinh ra các Test Cases chi tiết (gồm step-by-step, test data).
- **Execution Rules**:
  - Khi tham chiếu hoặc validate về mặt giao diện/hình ảnh (UI/UX), bắt buộc **phải tham chiếu đến các file ảnh trong thư mục `docs/design/`**.
  - **TUYỆT ĐỐI KHÔNG** sử dụng/tham chiếu các ảnh minh hoạ được nhúng trực tiếp bên trong file FRS (`docs/requirements/*`).

## Step 6: Coverage Analysis
- **Agent**: `agents/coverage_analyst.md`
- **Output**: `reports/[Requirement_Name]_Coverage_Report.md` (dynamic naming)
- **Objective**: Đối chiếu ngược các Test Cases vừa tạo với file Requirement gốc để đảm bảo độ bao phủ 100%.
