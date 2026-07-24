# Báo cáo cá nhân - 01 Problem Scan

## 1. Bảng quét cơ hội (SCAN)
| # | Công ty (Subsidiary) | Lăng kính (Lens) | Mô tả ngắn bài toán |
|---|----------------------|------------------|---------------------|
| 1 | **Xanh SM** | Tốn thời gian | Nhân viên điều phối mất nhiều thời gian kiểm tra khoảng cách và điều xe cứu hộ khi tài xế báo pin yếu dưới 5%. |
| 2 | **Vinmec** | Lặp lại | So khớp và trích xuất dữ liệu từ bệnh án giấy/PDF thủ công vào hệ thống HIS. |
| 3 | **Vinhomes** | Lặp lại | Trả lời lặp đi lặp lại các câu hỏi của cư dân về hóa đơn điện nước, phí dịch vụ. |
| 4 | **VinFast** | AI-upgrade | Hỗ trợ phân tích mã lỗi (error codes) từ xe và gợi ý hướng xử lý trực tiếp trên app cho người dùng. |
| 5 | **Vinpearl** | AI-upgrade | Đội ngũ Sale mất thời gian lên lịch trình tour cá nhân hóa thủ công cho từng nhóm khách gia đình. |

## 2. 3 Quick Problem Cards

### 🃏 Quick Card 1: Xanh SM Intelligent Dispatcher
- **Bài toán:** Tự động điều phối trạm sạc hoặc gọi xe sạc lưu động cho tài xế Xanh SM khi xe sắp hết pin.
- **Tác nhân (Actor):** Tổng đài viên (Dispatcher) & Tài xế Xanh SM.
- **Quy trình hiện tại:** Tài xế gọi tổng đài báo pin yếu -> Tổng đài viên tra cứu vị trí -> Tìm trạm sạc gần nhất trên bản đồ -> Nếu xa quá 5km, gọi đội cứu hộ pin di động -> Xác nhận với tài xế.
- **Bottleneck:** Mất 5-10 phút để tra cứu và đưa ra quyết định, dễ sai sót nếu tính nhầm khoảng cách khiến xe chết máy giữa đường.
- **Điểm AI có thể hỗ trợ:** AI tự động bắt tín hiệu GPS và mức pin, suy luận khoảng cách và tự động đề xuất trạm sạc hoặc gọi cứu hộ tức thì.
- **Metric thành công:** Giảm thời gian điều phối từ 5 phút xuống dưới 10 giây; 0% sự cố hết pin dọc đường do chỉ định sai trạm.
- **Kiến trúc đề xuất:** Agent (AI có khả năng gọi tool/API điều xe).

### 🃏 Quick Card 2: Vinmec Medical Record Parser
- **Bài toán:** Số hóa nhanh hồ sơ bệnh án giấy cũ và kết quả xét nghiệm ngoài.
- **Tác nhân (Actor):** Y tá / Nhân viên hành chính.
- **Quy trình hiện tại:** Nhận bệnh án -> Đọc từng tờ -> Gõ lại thông tin tiền sử bệnh, dị ứng thuốc vào máy tính.
- **Bottleneck:** Tốn 10 phút/hồ sơ, dễ gõ sai tên thuốc, sai liều lượng do chữ bác sĩ khó đọc hoặc mệt mỏi.
- **Metric thành công:** Giảm 80% thời gian nhập liệu, độ chính xác nhận diện thuốc đạt 99%.
- **Kiến trúc đề xuất:** LLM (Kết hợp OCR).

### 🃏 Quick Card 3: Vinhomes Resident Assistant
- **Bài toán:** Bot trả lời tự động chuyên sâu về hóa đơn và nội quy tòa nhà.
- **Tác nhân (Actor):** Ban Quản Lý (BQL) Vinhomes.
- **Quy trình hiện tại:** Cư dân nhắn Zalo/App -> BQL tra cứu file Excel -> Soạn tin nhắn giải thích.
- **Bottleneck:** Cuối tháng BQL bị quá tải tin nhắn, phải mất nhiều giờ để rep các câu hỏi giống hệt nhau.
- **Metric thành công:** Tự động hóa 70% các câu hỏi thường gặp, giảm thời gian chờ đợi phản hồi của cư dân từ 30 phút xuống 2 giây.
- **Kiến trúc đề xuất:** LLM (RAG - Truy xuất tài liệu nội bộ).
