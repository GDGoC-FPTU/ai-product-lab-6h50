# Phase 1 — SCAN: AI Opportunity Scan

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | Xanh SM | Lặp lại | So khớp và phân bổ lại cuốc xe khi khách yêu cầu thay đổi điểm đến giữa chừng. |
| 2 | Xanh SM | Tốn thời gian | Điều phối viên xử lý thủ công sự cố sạc pin hoặc xe chết máy thực địa (tìm trạm trống, soạn hướng dẫn). |
| 3 | VinFast | AI-upgrade | Tự động tạo nháp phản hồi cho khách hàng khi giá trúng cước hoặc lộ trình thay đổi trên app quản lý xe. |
| 4 | Vinhomes | AI-upgrade | Phân loại và trả lời tự động các phản hồi 1-star của cư dân trên ứng dụng quản lý toà nhà. |
| 5 | Vinmec | Pain từ người khác | Bác sĩ phải viết tóm tắt xuất viện và khuyến nghị điều trị bằng tay, mất nhiều thời gian mỗi bệnh nhân. |

---

# Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

## QUICK PROBLEM CARD #1

Bài toán (1 câu): Điều phối viên Xanh SM cần xử lý khẩn cấp sự cố sạc pin real-time khi tài xế báo hết pin hoặc giảm mạnh.

Công ty thành viên: [x] Xanh SM

Ai đang đau (Actor)? Điều phối viên điều vận và tài xế đang trong hành trình.

Workflow thủ công hiện tại (3-5 bước):
1. Tài xế báo sự cố về tổng đài.
2. Điều phối viên xác định vị trí xe và trạng thái pin.
3. Điều phối viên tra trạm sạc còn chỗ và soạn tin nhắn hướng dẫn.
4. Gửi nháp cho tài xế và gọi xe cứu hộ nếu cần.

Bước nào tốn thời gian/lỗi nhất? Bước 3-4 (⏱ ~12 phút/lượt).
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4: tự động đề xuất trạm sạc phù hợp và soạn draft thông tin.

Đo thành công bằng gì (Metric có số)? Giảm thời gian xử lý từ 15 phút xuống dưới 3 phút, tỉ lệ hướng dẫn an toàn đạt >98%.

Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent

## QUICK PROBLEM CARD #2

Bài toán (1 câu): Hệ thống CSKH Vinhomes trả lời phàn nàn cư dân theo mẫu, dẫn đến phản hồi chậm và thiếu cá nhân hoá.

Công ty thành viên: [x] Vinhomes

Ai đang đau (Actor)? Nhân viên CSKH và cư dân đang chờ giải quyết.

Workflow thủ công hiện tại (3-5 bước):
1. Nhân viên nhận phản hồi từ app.
2. Đọc nội dung khiếu nại và phân loại loại vụ việc.
3. Soạn thảo phản hồi theo quy trình.
4. Gửi phản hồi cho cư dân.

Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ ~10 phút/lượt).
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3: phân loại nhanh và tạo nháp phản hồi chuẩn.

Đo thành công bằng gì (Metric có số)? Giảm thời gian trả lời từ 10 phút xuống dưới 3 phút, đạt 90% sự hài lòng ban đầu.

Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent

## QUICK PROBLEM CARD #3

Bài toán (1 câu): Phân tích dữ liệu ghi chú hủy chuyến Xanh SM để tìm pattern lỗi và ưu tiên cải thiện điều phối.

Công ty thành viên: [x] Xanh SM

Ai đang đau (Actor)? Nhóm phân tích vận hành và quản lý dịch vụ.

Workflow thủ công hiện tại (3-5 bước):
1. Thu thập báo cáo hủy chuyến từ tài xế và khách.
2. Đọc mô tả và gắn nhãn thủ công.
3. Tổng hợp nguyên nhân và báo cáo cho bộ phận.
4. Xây dựng đề xuất cải tiến.

Bước nào tốn thời gian/lỗi nhất? Bước 2 (⏱ ~15 phút/lượt).
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2: tự động gắn nhãn nguyên nhân và tóm tắt pattern.

Đo thành công bằng gì (Metric có số)? Tiết kiệm 70% thời gian phân tích và đạt độ chính xác gắn nhãn >90%.

Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
