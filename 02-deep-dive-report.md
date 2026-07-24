# Phase 3 & 5: Deep-Dive Report & Evaluation (Vin Smart Future)

## 👥 Thông tin Nhóm
* **Tên nhóm:** Group Smart AI
* **Danh sách thành viên:**
  1. Nguyễn Văn A - MSSV: 20210001
  2. Trần Văn B - MSSV: 20210002

---

## 🎯 1. Quyết định lựa chọn bài toán
* **Bài toán chọn thực hiện Deep-Dive:** Phân loại & trích xuất tự động sự cố phản hồi của khách hàng VinFast.
* **Lý do chọn:** Lượng phản hồi lớn (>1.000 bài/ngày), thời gian xử lý thủ công kéo dài gây ảnh hưởng trực tiếp đến uy tín thương hiệu và trải nghiệm người dùng xe điện.

---

## 🏗️ 2. Problem Statement (6-Field Framework)

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Chuyên viên Chăm sóc Khách hàng (CSKH) & Đội ngũ Kỹ thuật VinFast. |
| **2. Current Workflow** | Khách hàng gửi bài phản ánh/email -> CSKH đọc thủ công từng bài -> Phân loại nhóm lỗi -> Nhập thông tin vào file Excel/CRM -> Chuyển thông tin cho bộ phận kỹ thuật. |
| **3. Bottleneck** | Bước đọc, phân loại cảm xúc và gắn tag lỗi kỹ thuật (Pin, Động cơ, Phần mềm) tốn quá nhiều thời gian (~15 phút/bài), dễ bị quá tải vào giờ cao điểm. |
| **4. Business Impact** | Tốn trung bình 25 giờ làm việc/ngày của nhóm CSKH, thời gian phản hồi sự cố khẩn cấp bị trễ (lên tới 24h), ảnh hưởng đến chỉ số hài lòng khách hàng (NPS). |
| **5. Success Metric** | 1. Giảm thời gian phân loại và tóm tắt từ 15 phút xuống dưới 30 giây/bài.<br>2. Tỉ lệ phân loại đúng nhóm sự cố đạt từ 92% trở lên. |
| **6. Operational Boundary** | AI được phép đọc, phân loại cảm xúc, tóm tắt nội dung và gán tag sự cố ở dạng bản nháp (Draft). **CẤM:** AI tuyệt đối không được tự động gửi email/tin nhắn phản hồi cho khách hàng mà không có sự kiểm duyệt của nhân viên CSKH (Human-In-The-Loop). |

---

## 🔄 3. Future-State Flow & AI Fit

* **Đánh giá AI Fit:** Chọn **LLM Feature** (Gọi API Gemini Flash). Không cần Agent tự trị vì quy trình có cấu trúc rõ ràng và cần con người duyệt kết quả.
* **Quy trình tương lai (Future-State):**
  1. **Khách hàng gửi phản hồi** -> Hệ thống tự động đẩy dữ liệu vào pipeline.
  2. **🔵 AI Step (LLM):** Đọc phản hồi, phân tích cảm xúc (Positive/Negative/Neutral), tóm tắt 2 dòng và gán tag lỗi.
  3. **🟢 Human Step (HITL):** Chuyên viên CSKH kiểm tra kết quả AI phân loại, nhấn nút phê duyệt hoặc chỉnh sửa.
  4. **↩️ Fallback:** Nếu mức độ tin cậy (Confidence Score) của AI < 0.70, hệ thống tự động chuyển bài toán về quy trình xử lý thủ công ban đầu.

---

## 🏁 4. Evaluation & AI Readiness Checklist

### AI Readiness Checklist:
* [x] Có sẵn dữ liệu văn bản phản hồi của khách hàng để làm test cases.
* [x] Rủi ro khi AI sai được kiểm soát hoàn toàn nhờ bước duyệt của con người (HITL) và cơ chế Fallback.
* [x] Đội ngũ CSKH sẵn sàng sử dụng giao diện mới để tăng tốc độ làm việc.

### Quyết định cuối cùng:
**[X] GO (Bắt đầu xây dựng Prototype)**

**Justification (Lý giải quyết định):**
Dự án đạt mức độ khả thi cao. Việc ứng dụng **Gemini 2.5 Flash API** có chi phí rất rẻ (~0.0001$/lượt gọi) nhưng giúp giảm hơn 90% thời gian phân loại của nhân sự, giải quyết triệt để nút thắt cổ chai vận hành.