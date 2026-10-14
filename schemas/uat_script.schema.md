# 📐 Master UAT Script Schema (v1.0.0)
> **Trạng thái:** Active Standard | **Áp dụng cho:** `uat_script_generator`, `templates/uat_scripts_report.md`

---

## 1. 🎯 Mục Đích & Triết Lý Thiết Kế
Schema này quy định cấu trúc chuẩn cho các kịch bản nghiệm thu người dùng cuối (User Acceptance Test - UAT).

Khác với Test Case kỹ thuật (Manual Test Case) vốn đi sâu vào từng trường nhập liệu, mã trạng thái và điều kiện biên, **UAT Scripts được thiết kế dành riêng cho Khách hàng (Client), Chủ sở hữu sản phẩm (Product Owner - PO) và Người dùng doanh nghiệp (Business Users)**.

### Triết lý cốt lõi:
1. **Ngôn ngữ kinh doanh (Business Language):** Dễ hiểu, không chứa thuật ngữ kỹ thuật chuyên sâu (như HTTP status code, database table, regex).
2. **Luồng trải nghiệm trọn vẹn (End-to-End User Journeys):** Đánh giá theo hành trình người dùng thực tế từ lúc bắt đầu đến khi đạt được mục tiêu kinh doanh.
3. **Xác thực giá trị (Value Validation):** Trọng tâm kiểm tra hệ thống có mang lại giá trị kỳ vọng không (ví dụ: tiền đã về tài khoản, thông báo xác nhận đã gửi, cuốc xe kết thúc an toàn).

---

## 2. 🆔 Chuẩn Định Dạng UAT Script ID
UAT Script ID bắt buộc tuân theo quy tắc:
$$\text{UAT-[MODULE]-[NNN]}$$
- **`[MODULE]`**: Mã module nghiệp vụ 3-4 chữ cái (Ví dụ: `RID` = Rider, `DRV` = Driver, `FIN` = Financial, `PAY` = Payment).
- **`[NNN]`**: Số thứ tự gồm 3 chữ số bắt đầu từ `001` (Ví dụ: `UAT-RID-001`, `UAT-FIN-005`).

---

## 3. 📋 Bảng Đặc Tả Thuộc Tính (Field Specification)

| Tên trường (Field) | Kiểu dữ liệu | Bắt buộc | Ràng buộc giá trị | Mô tả & Hướng dẫn |
|---|:---:|:---:|---|---|
| **`uat_id`** | String | ✅ Có | Regex: `^UAT-[A-Z0-9]{2,6}-\d{3}$` | Mã định danh duy nhất của kịch bản nghiệm thu. |
| **`title`** | String | ✅ Có | 15 – 120 ký tự | Tên kịch bản nghiệm thu phản ánh mục tiêu người dùng. |
| **`user_role`** | String | ✅ Có | `Rider` \| `Driver` \| `Host` \| `Admin` \| `Fleet Manager` | Vai trò người dùng thực hiện kịch bản. |
| **`user_story`** | String | ✅ Có | Cấu trúc: `Là [ai], tôi muốn [làm gì], để [đạt được gì]` | Khung câu chuyện người dùng mô tả bối cảnh kinh doanh. |
| **`pre_condition`**| String | ✅ Có | Trạng thái ban đầu dễ hiểu | Bối cảnh cần thiết trước khi bắt đầu (ví dụ: "Tài khoản có số dư 500.000 VNĐ"). |
| **`steps`** | String | ✅ Có | Chuỗi các hành động thực tế tuần tự, ngăn cách bằng `<br>` | Các bước người dùng thực hiện (Ví dụ: `Bước 1: Mở app...<br>Bước 2: Chọn đổi điểm đến...`). |
| **`test_data`** | String | ⬜ Tuỳ chọn | Dữ liệu mẫu thực tế | Dữ liệu kiểm thử dễ hiểu (tên đường phố, số tiền cụ thể). |
| **`expected_outcome`**| String | ✅ Có | Kết quả kinh doanh quan sát được | Kết quả nghiệp vụ rõ ràng (giao diện, email xác nhận, trừ tiền chính xác). |
| **`acceptance_criteria`**| String | ✅ Có | Tham chiếu mục tiêu trong PRD/SRS | Tiêu chí nghiệm thu cốt lõi được thoả mãn. |
| **`risk_ref`** | String | ⬜ Tuỳ chọn | `RISK-[MODULE]-[NNN]` | Rủi ro kinh doanh tương ứng được kịch bản này kiểm chứng. |
| **`verdict`** | Enum | ✅ Có | `Pass` \| `Fail` \| `Conditional Pass` \| `Not Executed` | Kết luận nghiệm thu của đại diện kinh doanh/khách hàng. |

---

## 4. 📝 Định Dạng Trình Bày Chuẩn Trong Báo Cáo

### A. Định dạng Khối Chi Tiết Kịch Bản (Detailed Journey Block):
```markdown
### 📌 [UAT-RID-001]: Rider đổi điểm đến trong khi đang di chuyển và hoàn tất thanh toán cước mới
- **Vai trò (User Role)**: Rider (Hành khách)
- **User Story**: Là một hành khách đang ngồi trên xe, tôi muốn đổi điểm trả khách sang một địa chỉ mới để phù hợp với kế hoạch đột xuất của mình.
- **Điều kiện ban đầu (Pre-conditions)**: Cuốc xe đang ở trạng thái di chuyển (In Trip), tài xế đã đón khách, chưa đến gần điểm trả khách ban đầu (>500m).
- **Rủi ro kiểm chứng (Risk Ref)**: `RISK-RID-002` (Không tự ý đổi lộ trình nếu chưa xác thực thanh toán tiền tăng thêm).

**📋 Các bước thực hiện (Business Steps):**
1. Mở màn hình theo dõi lộ trình trực tiếp của cuốc xe đang chạy.
2. Nhấn vào biểu tượng cây bút chì (✏️) bên cạnh ô điểm đến "DROP OFF".
3. Nhập và chọn địa chỉ điểm đến mới (Cách xa hơn điểm ban đầu 3km).
4. Quan sát màn hình xác nhận: kiểm tra giờ đến mới (Absolute ETA), tiền cước cũ, tiền chênh lệch tăng thêm (+25.000đ), tổng cước mới.
5. Nhấn nút "Gửi yêu cầu" (Send Request).

**🎯 Kết quả mong đợi (Expected Business Outcome):**
- Ứng dụng hiển thị thông báo "Điểm đến đã được cập nhật thành công".
- Lộ trình trên bản đồ tự động vẽ lại đường đi mới về phía điểm đến mới.
- Ứng dụng của tài xế nhận thông báo cập nhật lộ trình đồng bộ và tự động điều hướng sang cung đường mới.
- Thẻ tín dụng của hành khách tạm giữ (pre-authorization) đúng số tiền chênh lệch 25.000đ mà không phát sinh thêm bất kỳ phụ phí bất thường nào.

**🏁 Kết luận nghiệm thu (Sign-off):** [ ] Pass  [ ] Fail  [ ] Conditional Pass
- **Người nghiệm thu (Reviewer)**: _______________________   **Ngày**: ____/____/2026
```

### B. Định dạng Bảng Kịch Bản Tóm Tắt (UAT Summary Table):
```markdown
| UAT ID | Kịch bản nghiệm thu | Vai trò | Trọng tâm kiểm thử | Tiêu chí thành công | Kết quả |
|---|---|---|---|---|:---:|
| `UAT-RID-001` | Đổi điểm đến giữa chuyến hợp lệ | Rider | Luồng tăng cước tiêu chuẩn | Lộ trình và cước mới đồng bộ cả khách và tài xế | Pass |
| `UAT-RID-002` | Thẻ hết tiền khi đổi điểm đến | Rider | Xử lý lỗi thẻ từ chối | Giữ nguyên lộ trình cũ, thông báo rõ ràng cho khách | Pass |
| `UAT-RID-003` | Tài xế từ chối vì lý do an toàn | Driver | Van an toàn của tài xế | Chốt cước theo cự ly thực tế, không phạt tài xế | Pass |
```
