# Deep-Dive Report — Vin Smart Future

**Tên nhóm:** Nhóm 6H50
**Họ và tên:
- Đặng Trung Kiên MSV: 2A202601887
- Lê Văn Huy MSV: 2A202601235
- Đỗ Thế Việt MSV: 2A202601897
- Lương Ngọc Quang MSV: 2A202601563
- Phạm Trung Kiên MSV: 2A202601525

**Mảng chọn:** Xanh SM (GSM) — Vận hành xe taxi điện thông minh

---

## 1. Quyết định lựa chọn bài toán

Nhóm chọn bài toán: **Xử lý sự cố sạc pin / hết pin giữa đường cho tài xế Xanh SM**.

Lý do chọn bài toán này:
- Đây là một vấn đề vận hành có tính lặp lại và xảy ra thường xuyên trong giờ cao điểm.
- Có bottleneck rõ ràng ở bước tra cứu trạm sạc và soạn tin nhắn hướng dẫn cho tài xế.
- Hiệu quả của giải pháp có thể đo bằng thời gian xử lý và độ chính xác.
- Bài toán phù hợp để triển khai prototype đầu tiên vì phạm vi vừa đủ, rủi ro kiểm soát được và có thể dùng HITL.

---

## 2. Problem Statement (6-field)

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) tại Trung tâm Điều vận Xanh SM và tài xế xe điện. |
| **2. Current Workflow** | Khi tài xế báo sự cố hết pin hoặc pin thấp giữa đường, điều phối viên phải tra cứu vị trí xe, tìm trạm sạc VinFast còn trụ trống gần nhất, soạn tin nhắn chỉ dẫn cho tài xế, và liên hệ đội cứu hộ khi cần. Toàn bộ quy trình đang thực hiện thủ công qua nhiều hệ thống riêng lẻ. |
| **3. Bottleneck** | Bước tra cứu trạm sạc phù hợp và soạn nội dung hướng dẫn mất nhiều thời gian nhất, thường kéo dài 10–12 phút mỗi lượt, đồng thời dễ sai sót khi chọn trạm không phù hợp hoặc nội dung chưa rõ ràng. |
| **4. Business Impact** | Mỗi ngày có nhiều sự cố pin thực địa, làm tăng thời gian chờ đợi của tài xế, làm giảm hiệu suất điều xe, tăng nguy cơ khách hàng hủy chuyến và gây tổn thất doanh thu. |
| **5. Success Metric** | Giảm thời gian xử lý mỗi sự cố từ 12 phút xuống còn dưới 3 phút; đạt tỷ lệ gợi ý trạm sạc đúng và phù hợp trên 95%. |
| **6. Operational Boundary** | AI được phép tự động thu thập dữ liệu vị trí và đề xuất trạm sạc, đồng thời soạn bản nháp tin nhắn hướng dẫn. Tuyệt đối không được tự động gửi tin mà không có phê duyệt của điều phối viên; không được đề xuất trạm sạc quá xa khi pin dưới mức an toàn. |

---

## 3. Future-State Flow & AI Fit

### AI Fit

**Loại giải pháp đề xuất:** **LLM Feature**  
Không chọn Agentic Loop vì quy trình hiện tại có cấu trúc khá rõ ràng, và việc tự động hóa hoàn toàn có thể gây rủi ro nếu sai trong chọn trạm sạc hoặc gửi chỉ dẫn không chính xác.

### Future-State Flow

```text
1. Tài xế báo sự cố hết pin
   ↓
2. Hệ thống tự động lấy vị trí xe và tình trạng pin
   ↓
3. AI đề xuất trạm sạc phù hợp + nội dung chỉ dẫn ngắn gọn
   ↓
4. Điều phối viên xem lại và phê duyệt (HITL)
   ↓
5. Gửi tin nhắn cho tài xế hoặc gọi cứu hộ nếu cần
   ↓
6. Fallback: Nếu AI không tự tin hoặc dữ liệu thiếu, điều phối viên quay về quy trình thủ công cũ
```

### Vai trò của AI và con người

- **AI làm:** thu thập dữ liệu, gợi ý trạm sạc, soạn bản nháp tin nhắn, tóm tắt tình huống.
- **Con người làm:** phê duyệt, xác nhận mức độ an toàn, quyết định có cần gọi cứu hộ hay không.
- **Human-in-the-loop:** bắt buộc ở bước phê duyệt trước khi gửi tin cho tài xế.
- **Fallback:** nếu AI không có đủ thông tin hoặc kết quả thấp độ tin cậy, hệ thống chuyển sang quy trình thủ công truyền thống.

---

## 4. Evaluate

### Checklist độ sẵn sàng

| Câu hỏi | Trả lời | Ghi chú |
|---|---|---|
| Có sẵn dữ liệu mẫu/logs sạch để test? | Có | Có thể dùng dữ liệu tình huống sự cố, vị trí xe, trạm sạc và mẫu tin nhắn. |
| Rủi ro khi AI sai có nằm trong tầm kiểm soát? | Có | Đã có HITL và fallback. |
| Stakeholder sẵn sàng thay đổi quy trình cũ? | Có | Điều phối viên có thể tiếp nhận workflow mới nếu giảm tải công việc đáng kể. |

### Quyết định cuối cùng

**GO — Bắt đầu xây dựng prototype với phạm vi hẹp.**

### Lý do quyết định

- Bài toán có phạm vi rõ ràng và cụ thể, không đòi hỏi AI xử lý toàn bộ quy trình.
- Có thể xây dựng giải pháp bằng một mô hình nhẹ, kết hợp rule + LLM để giảm rủi ro.
- Metric thành công dễ đo: thời gian xử lý và tỷ lệ đề xuất đúng.
- Nếu prototype thành công, có thể mở rộng sang các tình huống xử lý sự cố khác trong vận hành Xanh SM.

### Ước lượng chi phí sơ bộ

| Hạng mục | Ước lượng |
|---|---:|
| Thiết kế prompt + logic điều kiện | 2–3 ngày |
| Xây dựng prototype backend/API | 3–5 ngày |
| Tích hợp với dữ liệu vị trí và trạm sạc | 2–3 ngày |
| Test và điều chỉnh | 2 ngày |
| Tổng ước lượng | **9–13 ngày công** |

### Chi phí gần đúng (nếu triển khai nội bộ)

- Nhân sự: 1 AI Engineer + 1 Backend Engineer + 1 Product/Operations reviewer.
- Ước tính chi phí: **khoảng 20–35 triệu đồng** cho giai đoạn prototype, tùy vào thời gian và mức độ tích hợp hệ thống.

---

## 5. Kết luận

Bài toán xử lý sự cố sạc pin cho Xanh SM là một lựa chọn phù hợp cho giai đoạn đầu của dự án AI vì vừa có giá trị vận hành rõ ràng, vừa có thể kiểm soát rủi ro bằng cơ chế con người phê duyệt và fallback. Đây là một bài toán đủ nhỏ để prototype nhanh, nhưng đủ lớn để chứng minh hiệu quả của AI trong môi trường vận hành Vingroup.
