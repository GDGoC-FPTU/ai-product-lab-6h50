# AI Log & Reflection

## AI đã giúp gì
Tôi đã dùng AI để tạo prompt prototype cho bài toán Xanh SM xử lý sự cố sạc pin. Cụ thể, tôi định nghĩa ranh giới an toàn trong system prompt, kiểm tra 2 trường hợp tấn công để đảm bảo model không bỏ qua tag [DRAFT_ONLY] và không đề xuất trạm xa khi pin dưới 5%.

## AI sai gì
AI có thể sai trong việc hiểu ranh giới an toàn nếu prompt không đủ nghiêm ngặt. Nếu không có kiểm tra, model có thể trả về gợi ý trạm sạc xa hoặc quên tag [DRAFT_ONLY], dẫn đến hậu quả nghiêm trọng trong quy trình vận hành.

## Sửa đổi ra sao
Tôi đã bổ sung hệ thống output JSON rõ ràng và bắt buộc model tạo draft message với [DRAFT_ONLY]. Tôi cũng sửa phần code để gọi Gemini SDK đúng cách và xử lý lỗi khi API key chưa được cấu hình.
