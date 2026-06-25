# Phân tích Các Bước Phải Làm - Day 21 Lab: Thiết kế Test Inputs cho AI Evals

Tài liệu này phân tích chi tiết các bước cần thực hiện để hoàn thành bài lab Day 21, được chia thành hai giai đoạn chính: **Cá nhân** và **Nhóm**.

---

## I. GIAI ĐOẠN 1: THỰC HIỆN CÁ NHÂN (Tạo Scenario Dataset v0)

Mục tiêu của pha này là mỗi học viên tự thiết kế một bộ test inputs có coverage rõ ràng cho use case của mình, bao gồm tối thiểu **10 scenarios/combinations** và tối thiểu **20 natural-language user inputs** sau khi lọc.

### Bước 1: Chọn Use Case & Xác định Unit of AI Work
*   **Nhiệm vụ:** Chọn lại use case đã làm từ Day 18/19. Xác định một lát cắt cụ thể đại diện cho **Unit of AI Work** (đơn vị nhỏ nhất cần đánh giá).
*   **Chi tiết:** Chọn một điểm mà AI nhận đầu vào (input) và xử lý ra đầu ra (output/action) cụ thể có thể đánh giá được. Tránh chọn lát cắt quá rộng như "đánh giá toàn bộ chatbot".
*   **Bảng cần điền:**
    *   Use case từ Day 18/19
    *   Persona chính
    *   Unit of AI Work
    *   Input user đưa vào
    *   Output agent cần tạo
    *   Agent được phép làm gì?
    *   Agent không được phép làm gì?

### Bước 2: Viết Quality Question (Câu hỏi chất lượng)
*   **Nhiệm vụ:** Chuyển đổi một câu hỏi chất lượng mơ hồ như *"Agent có tốt không?"* thành một câu hỏi kiểm thử cụ thể về rủi ro hoặc sự hài lòng của người dùng.
*   **Chi tiết:** Xác định rõ hành vi nào của Agent nếu xảy ra lỗi sẽ gây mất lòng tin nghiêm trọng từ người dùng hoặc làm hỏng quy trình.
*   **Bảng cần điền:**
    *   Quality question chính
    *   Vì sao câu hỏi này quan trọng với user?
    *   Nếu agent fail ở đây, hậu quả là gì?
    *   Behavior nào là bắt buộc?
    *   Behavior nào bị cấm?

### Bước 3: Thiết kế User Input Grid (Ít nhất 3 Dimensions chính)
*   **Nhiệm vụ:** Chọn ít nhất 3 chiều kiểm thử (dimensions) để thay đổi expected behavior của Agent.
*   **Chi tiết:** Các dimension có thể là:
    *   `user_intent` (check đơn hàng, đổi trả, bảo hành...)
    *   `context_completeness` (đầy đủ thông tin, thiếu mã đơn, mơ hồ...)
    *   `risk_level` (thấp, trung bình, cao...)
*   **Lưu ý:** Loại bỏ các dimension yếu không thực sự làm thay đổi expected behavior của Agent (ví dụ: độ dài câu hỏi dài/ngắn, user vui/buồn).
*   **Bảng cần điền:**
    *   Dimension | Values | Vì sao làm agent phải đổi behavior?

### Bước 4: Lựa chọn 10 Tổ hợp (Meaningful Combinations) đáng test nhất
*   **Nhiệm vụ:** Chọn ra tối thiểu 10 scenarios đại diện từ lưới Input Grid, không nhân ma trận tổ hợp tất cả các trường hợp một cách máy móc.
*   **Tiêu chí chọn:** Giữ lại các tổ hợp thường gặp, dễ làm Agent sai, có rủi ro/hậu quả cao, hoặc có tính mơ hồ (ambiguity).
*   **Bảng cần điền:**
    *   Bảng 10 combinations cá nhân gồm: *Combination ID (C01 - C10), Dimension values, Expected behavior, Vì sao đáng test, và Phân loại (representative/challenge/high-risk).*

### Bước 5: Dùng AI hỗ trợ sinh câu hỏi tự nhiên (Paraphrase)
*   **Nhiệm vụ:** Sử dụng LLM để viết lại 10 tổ hợp đã chọn thành các câu hỏi tự nhiên như người dùng thật (mỗi tổ hợp sinh 2 câu đầu vào $\rightarrow$ tổng cộng 20+ câu).
*   **Nguyên tắc:** Con người quyết định độ bao phủ (coverage), AI chỉ giúp viết nhiều cách diễn đạt tự nhiên hơn. Không để AI tự ý chọn intent hay context.
*   **Yêu cầu lưu trữ:** Lưu lại Prompt đã dùng và kết quả thô thu được từ AI.

### Bước 6: Lọc thủ công (Human Filter)
*   **Nhiệm vụ:** Kiểm tra từng câu do AI sinh ra dựa trên bộ câu hỏi lọc để giữ lại những câu chất lượng và loại bỏ những câu lỗi.
*   **Tiêu chí loại bỏ:** Loại bỏ nếu AI làm thay đổi intent gốc, làm case quá sạch, tự ý thêm context ngoài tổ hợp, trùng lặp wording hoặc không giúp làm rõ câu hỏi chất lượng (quality question).
*   **Đầu ra:** Danh sách tối thiểu **20 natural-language user inputs** sau khi lọc.

### Bước 7: Hoàn thiện cá nhân (Scenario Dataset v0 & Coverage Note)
*   **Nhiệm vụ:** Lập bảng dữ liệu kiểm thử cá nhân đầu tiên và viết một đoạn đánh giá ngắn (5–7 dòng).
*   **Đầu ra:**
    1.  Bảng **Scenario Dataset v0** theo đúng schema yêu cầu.
    2.  **Coverage note** trả lời các câu hỏi: *Đang cover tốt lát cắt nào? Chưa cover lát cắt nào? Có tổ hợp nào cố tình bỏ qua không? Câu nào rủi ro nhất/boundary case khó nhất?*

---

## II. GIAI ĐOẠN 2: LÀM VIỆC NHÓM (Group Merge & Coverage Review)

Mục tiêu của pha này là thảo luận để thống nhất tiêu chuẩn kiểm thử, loại bỏ trùng lặp và chốt một **Scenario Dataset v1 chung của nhóm với ít nhất 30 rows**.

### Bước 8: Trình bày chéo & Thảo luận (Step 1)
*   **Nhiệm vụ:** Mỗi thành viên trình bày nhanh trong 3 phút về: *Use case, Quality question, Các dimensions đã chọn, 2 combinations tốt nhất, 1 input rủi ro nhất và khoảng trống bao phủ (gaps) còn thiếu.*

### Bước 9: Chuẩn hóa Dimensions & Khử trùng lặp (Step 2 & 3)
*   **Nhiệm vụ:** 
    *   Thảo luận nhóm để gom các dimensions tương đương của các thành viên về các tên biến chuẩn hóa chung (ví dụ: `user_intent`, `context_completeness`, `risk_level`). Chọn ít nhất 3 dimensions chính cho Scenario Dataset v1.
    *   Duyệt qua các inputs của các thành viên để khử trùng lặp (Deduplicate). Với các inputs giống nhau, nhóm quyết định giữ câu tốt nhất, merge wording hoặc chỉ giữ cả hai nếu test các style/persona hoàn toàn khác nhau.

### Bước 10: Kiểm tra độ bao phủ (Coverage Matrix) (Step 4)
*   **Nhiệm vụ:** Lập ma trận bao phủ (Coverage Matrix) để thống kê số lượng dữ liệu kiểm thử hiện có cho từng giá trị kiểm thử đã chuẩn hóa.
*   **Đầu ra:** Bảng **Coverage matrix** ghi nhận số dòng hiện có cho mỗi giá trị và đánh giá xem đã đủ độ phủ chưa.

### Bước 11: Chốt Scenario Dataset v1 của nhóm (Step 5)
*   **Nhiệm vụ:** Lọc và hoàn thiện bộ dữ liệu cuối cùng đạt **ít nhất 30 dòng**.
*   **Yêu cầu bộ dữ liệu v1:** Phải có đủ các loại (representative, challenge, high-risk), có ít nhất 2 câu test nhập nhằng (ambiguous), 2 câu rủi ro cao, 2 câu dễ làm Agent chọn sai action, và đa dạng về văn phong (style).
*   **Đầu ra:** Bảng **Scenario Dataset v1** của nhóm theo đúng schema chung (có thêm cột `risk_if_fail` và `merge_decision`).

### Bước 12: Viết Group Coverage Review & Handoff Note (Bài 7)
*   **Nhiệm vụ:** 
    *   Trả lời ngắn bộ câu hỏi đánh giá độ bao phủ của nhóm (Group coverage review).
    *   Viết ghi chú bàn giao (Handoff note - 5-7 dòng) để chuẩn bị cho giai đoạn chạy Agent và đọc trace sau này. Dự đoán trước các điểm Agent dễ sai (failure prediction) và đề xuất các rows cần ưu tiên chạy trước.
*   **Đầu ra:** Handoff note của nhóm. Gom toàn bộ báo cáo cá nhân và nhóm thành một link báo cáo duy nhất để nộp bài.

---

## III. TIMELINE GỢI Ý (Tổng thời gian: 150 phút)

*   **10 phút:** Đọc đề, chọn use case + Unit of AI Work.
*   **15 phút:** Viết Quality question.
*   **20 phút:** Tạo User Input Grid cá nhân (ít nhất 3 dimensions).
*   **20 phút:** Chọn scenarios/combinations cá nhân (ít nhất 10 scenarios).
*   **25 phút:** Dùng AI sinh câu hỏi + Lọc thủ công (20+ inputs).
*   **15 phút:** Hoàn thiện cá nhân (Scenario Dataset v0 + Coverage Note).
*   **25 phút:** Trình bày nhóm, chuẩn hóa dimensions + khử trùng lặp.
*   **15 phút:** Nhóm làm ma trận coverage + chốt Scenario Dataset v1 (30+ rows).
*   **5 phút:** Viết Handoff note và đóng gói nộp bài.
