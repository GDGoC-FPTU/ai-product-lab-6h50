# Phase 1 & 2: Problem Scan & Quick-Assess (Vin Smart Future)

## 1. Opportunity Scan Matrix (Phase 1)
| # | Công ty thành viên | Lens | Mô tả ngắn bài toán / Bottleneck |
|---|-------------------|------|-----------------------------------|
| 1 | **VinFast** | Repetitive / Time-consuming | Tự động đọc, phân loại và gắn tag lỗi kỹ thuật (Pin, Động cơ, Phần mềm) từ phản hồi của khách hàng. |
| 2 | **Vinmec** | Stakeholder Pain | Tự động phân loại sơ bộ triệu chứng bệnh nhân khi đăng ký khám để xếp đúng chuyên khoa. |
| 3 | **Vinhomes** | Time-consuming | Trích xuất dữ liệu tự động từ tài liệu/hợp đồng cọc mua bán căn hộ sang định dạng JSON. |
| 4 | **Vinpearl** | AI-upgrade | Trợ lý ảo gợi ý lịch trình du lịch cá nhân hóa theo thời gian thực cho du khách. |
| 5 | **Xanh SM** | Repetitive | Tự động tổng hợp và xử lý phản ánh của tài xế về lỗi tính tiền chuyến đi hoặc sai lệch định vị. |

---

## 2. 3 Quick Problem Cards (Phase 2)

### 💳 QUICK PROBLEM CARD #1
* **Bài toán:** Phân loại & trích xuất phản hồi khách hàng VinFast tự động.
* **Công ty thành viên:** VinFast
* **Actor (Ai đang đau):** Chuyên viên CSKH VinFast.
* **Workflow thủ công hiện tại:** 
  1. Nhận email/bài đăng -> 2. Đọc thủ công -> 3. Phân loại loại lỗi -> 4. Nhập Excel/CRM -> 5. Báo phòng kỹ thuật.
* **Bước tốn thời gian/lỗi nhất:** Bước 2 & 3 (Đọc và phân loại thủ công, tốn ~15 phút/lượt).
* **AI hỗ trợ ở bước nào:** Bước 2 & 3 (Trích xuất Sentiment + Tag nhóm lỗi).
* **Metric đo thành công:** Giảm thời gian xử lý từ 15 phút xuống dưới 30 giây/lượt.
* **Quick Architecture:** `[X] LLM Feature`

---

### 💳 QUICK PROBLEM CARD #2
* **Bài toán:** Trích xuất dữ liệu hợp đồng cọc nhà tự động.
* **Công ty thành viên:** Vinhomes
* **Actor (Ai đang đau):** Chuyên viên Pháp lý & Thủ tục.
* **Workflow thủ công hiện tại:** 
  1. Nhận hợp đồng scan -> 2. Đọc dò thông tin cá nhân & mã căn hộ -> 3. Kiểm tra số tiền -> 4. Nhập tay vào ERP.
* **Bước tốn thời gian/lỗi nhất:** Bước 2 & 4 (Đọc dò và nhập tay, tốn ~25 phút/hợp đồng, dễ sai sót CCCD/Mã căn).
* **AI hỗ trợ ở bước nào:** Bước 2 & 3 (Dùng LLM trích xuất các trường thông tin chuẩn JSON).
* **Metric đo thành công:** Giảm thời gian xử lý từ 25 phút xuống dưới 2 phút/hợp đồng.
* **Quick Architecture:** `[X] LLM Feature`

---

### 💳 QUICK PROBLEM CARD #3
* **Bài toán:** Tự động tổng hợp và xử lý phản ánh của tài xế về lỗi tính tiền chuyến đi hoặc sai lệch định vị GPS.
* **Công ty thành viên:** Xanh SM
* **Actor (Ai đang đau):** Chuyên viên Hỗ trợ Đối tác / Trợ lý Vận hành Tổng đài (Ops Supporter).
* **Workflow thủ công hiện tại:** 
  1. Nhận yêu cầu/khiếu nại của tài xế qua ứng dụng đối tác -> 2. Đọc nội dung & tra cứu lịch sử log GPS/chuyến đi -> 3. Kiểm tra công thức tính cước/phụ phí -> 4. Phản hồi tài xế & gửi yêu cầu điều chỉnh số dư (nếu có sai lệch).
* **Bước tốn thời gian/lỗi nhất:** Bước 2 & 3 (Tốn ~12–15 phút/yêu cầu, dễ nhầm lẫn do log GPS phức tạp và nhiều loại phụ phí/khung giờ).
* **AI hỗ trợ ở bước nào:** Bước 2 & 3 (Đọc hiểu phản ánh, trích xuất dữ liệu chuyến đi, tự động đối soát log định vị/cước phí và đề xuất phương án xử lý).
* **Metric đo thành công:** Rút ngắn thời gian xử lý khiếu nại từ 15 phút xuống dưới 2 phút/yêu cầu; Đạt tỷ lệ tự động đối soát chính xác > 95%.
* **Quick Architecture:** `[X] LLM Feature` (Kết hợp Structured Output JSON để xuất báo cáo đối soát cho tư vấn viên xác nhận).