# 📖 Requirement Reading Rule
<RULE[project_requirements]>
Luôn luôn quét và đọc lại nội dung trực tiếp của các file requirements (thông qua các tool như view_file, grep_search...) mỗi khi nhận được yêu cầu phân tích, cập nhật hay viết code liên quan đến requirements.
Tuyệt đối KHÔNG ĐƯỢC dựa vào trí nhớ, thông tin từ các context trước đó, hay các file cache cũ. Điều này giúp đảm bảo bạn luôn tiếp cận với tài liệu mới nhất và ngăn ngừa việc sinh ra các lỗi ảo hoặc sử dụng requirements đã bị xóa bỏ.
</RULE[project_requirements]>

# 📝 Report Naming Rule
<RULE[report_naming]>
Khi tạo báo cáo phân tích requirements (Gap Analysis, Quality Report, v.v.), bắt buộc phải đặt tên file report theo định dạng chứa tên của file requirement được phân tích (ví dụ: `Host_Listing_Management_Req_Gap_Report.md`).
Tuyệt đối không dùng tên chung chung như `requirement_gap_analysis.md`.
</RULE[report_naming]>

# 🗑️ Report Overwrite Rule
<RULE[report_overwrite]>
Khi chạy lại báo cáo phân tích cho cùng một document và cùng một yêu cầu, bắt buộc phải XÓA hoặc GHI ĐÈ (overwrite) hoàn toàn lên file report trước đó thay vì sửa chữa hay chèn thêm (append) nội dung. Điều này đảm bảo file report luôn là một bản build mới nhất, tránh tình trạng chắp vá gây nhầm lẫn.
</RULE[report_overwrite]>
