# Deep-Dive Report — Xanh SM Charging Incident Response

## 1. Bài toán được chọn
Nhóm chọn bài toán: **Xanh SM Xử lý sự cố sạc pin thực địa**.

## 2. 6-field Problem Statement

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) tại Trung tâm Điều vận Xanh SM. |
| **2. Current Workflow** | Khi tài xế báo hết pin, dispatcher xác định vị trí xe, tra cứu trạm sạc VinFast còn trống, soạn nháp hướng dẫn bằng tay, gửi cho tài xế và gọi cứu hộ nếu pin quá thấp. |
| **3. Bottleneck** | Bước tra cứu trạm sạc và soạn hướng dẫn mất nhiều thời gian nhất, thường phải kiểm tra nhiều nguồn và soạn tin tay, dẫn đến trễ phản hồi. |
| **4. Business Impact** | Mất ~15 phút/lượt xử lý, với khoảng 80 sự cố mỗi ngày tại khu vực Hà Nội, gây lãng phí 20 giờ nhân sự/ngày và tăng rủi ro xe không kịp nạp pin. |
| **5. Success Metric** | Giảm thời gian xử lý từ 15 phút xuống dưới 3 phút; đạt tỉ lệ hướng dẫn trạm sạc an toàn >98%. |
| **6. Operational Boundary** | AI chỉ tạo nháp draft để dispatcher phê duyệt; không tự gửi tin; không đề xuất trạm sạc cách >5km khi pin <5%; nếu không có lựa chọn an toàn thì dispatch mobile charger. |

## 3. Future-State Flow & AI Fit

### AI Fit
* Chọn: **LLM Feature**
* Lý do: Quy trình có cấu trúc rõ ràng, cần tạo nháp hướng dẫn an toàn, và HITL cần giữ để tránh sai sót.

### Future-State Flow

1. Tài xế báo sự cố sạc pin.
2. Hệ thống tự động lấy vị trí xe và trạng thái pin từ API.
3. LLM dựng nháp hướng dẫn trạm sạc phù hợp.
4. Dispatcher review và duyệt nháp trước khi gửi.
5. Nếu pin <5% hoặc không có trạm an toàn, hệ thống yêu cầu dispatch mobile charger.

### Mô tả bước
* 🔵 AI Step: Tạo draft text dựa trên dữ liệu vị trí, pin và trạm sạc.
* 🟢 Human Step: Dispatcher duyệt draft và quyết định gửi hoặc gọi cứu hộ.
* ↩️ Fallback: Nếu draft không thỏa điều kiện an toàn, dispatcher dùng lại quy trình thủ công và gọi cứu hộ.

## 4. Evaluate — AI Readiness Checklist

1. [x] Có dữ liệu mẫu/logs sạch để test (vị trí xe, trạng thái pin, danh sách trạm sạc).
2. [x] Rủi ro AI sai có trong tầm kiểm soát qua HITL + fallback (human review trước khi gửi).
3. [ ] Stakeholders sẵn sàng thay đổi quy trình cũ? Cần thảo luận thêm với bộ phận vận hành Xanh SM.

## 5. Quyết định cuối cùng
[ ] GO  [x] NOT YET  [ ] NO-GO

### Lý giải
Dự án có metric rõ ràng và scope hẹp, nhưng cần xác minh dữ liệu trạm sạc và quy trình phê duyệt dispatcher trước khi triển khai. AI phù hợp để tạo nháp, nhưng chưa đủ điều kiện GO nếu chưa có kiểm soát xác thực nguồn dữ liệu và thực nghiệm với stakeholder.
