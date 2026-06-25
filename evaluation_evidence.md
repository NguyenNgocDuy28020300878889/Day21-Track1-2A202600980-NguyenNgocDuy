# Dẫn Chứng Đánh Giá (Evaluation Evidence)

Dưới đây là các dẫn chứng cụ thể (trích xuất từ `day20_report.md` và `index.html`) chứng minh bài làm đã đáp ứng đầy đủ các tiêu chí trong Checklist:

### 1. Use case và natural behavior
*   **[x] Chỉ tập trung vào một use case chính:**
    *   *Dẫn chứng:* Tập trung hoàn toàn vào "Smart Packing & Prep" (Gợi ý hành trang theo thời tiết và hoạt động chuyến đi). (Xem *Mở đầu tài liệu phân tích*).
*   **[x] Có The Problem, Persona, Anti-persona, Why và Alternative:**
    *   *Dẫn chứng:* Section `1. Bài 1: Customer Retention Canvas` phân tích rõ 6 khối: The Problem (Mất quá nhiều thời gian đóng gói...), The Persona (Nhân viên văn phòng trẻ...), Anti-Persona (Khách đi tour trọn gói), The Alternative (Dùng Note, tra Google thời tiết thủ công), The Promise.
*   **[x] Frequency được suy ra từ hành vi thật và alternative:**
    *   *Dẫn chứng:* "Hành vi chuẩn bị hành lý du lịch thường diễn ra theo Tháng (Monthly) hoặc theo Quý (Quarterly)." - Phù hợp với thói quen du lịch tự túc của Persona. (Xem *Khối The Frequency ở Bài 1*).

### 2. Core action và metric
*   **[x] Core action cho thấy user nhận được value:**
    *   *Dẫn chứng:* "Nhấn **Xác nhận checklist cuối cùng**. Đây là khoảnh khắc người dùng cam kết chuyển đổi từ việc xem gợi ý của AI sang hành động đóng gói thực tế..." (Xem *Section 2.1*).
*   **[x] Active user có định nghĩa và ngưỡng rõ:**
    *   *Dẫn chứng:* "Một người dùng được tính là 'Active' khi họ hoàn thành việc xác nhận ít nhất 1 checklist hành lý trong khoảng thời gian 30 ngày." (Xem *Section 2.2*).
*   **[x] Retention metric phù hợp natural frequency:**
    *   *Dẫn chứng:* "Dựa trên Tần suất tự nhiên (Monthly), chỉ số giữ chân phù hợp nhất là **Monthly Cohort Retention**." (Xem *Section 2.3*).
*   **[x] Không copy DAU, WAU, MAU hoặc D7 từ sản phẩm khác:**
    *   *Dẫn chứng:* Lập luận chặt chẽ: "Việc ép người dùng quay lại hàng ngày (Daily Retention / DAU) cho một ứng dụng chuẩn bị hành lý du lịch là phi logic và dẫn đến trải nghiệm tồi tệ." (Xem *Section 2.3*).

### 3. Onboarding &rarr; First Core Action
*   **[x] Có current-state journey & Có redesigned journey:**
    *   *Dẫn chứng:* Phân tích rõ ràng 2 luồng: "Hành trình cũ (Day 18)" (Welcome &rarr; Bắt ép cấp quyền GPS &rarr; Form 5 trường...) và "Hành trình Redesign" (Welcome &rarr; Form 2 trường &rarr; Loading &rarr; First Core Action). (Xem *Section 3.1* và *Slide 04, 05*).
*   **[x] Mỗi bước được audit theo Keep, Remove, Delay hoặc Simplify:**
    *   *Dẫn chứng:* Quyền GPS (DELAY), Form nhập liệu 5 trường (SIMPLIFY), Màn hình báo lỗi thời tiết (REMOVE). (Xem *Section 3.1* và *Slide 04*).
*   **[x] Có activation, Time to First Core Action, TTV và aha moment:**
    *   *Dẫn chứng:* "Time to First Core Action giảm từ ~2 phút xuống chỉ còn dưới 30 giây. Aha Moment xảy ra khi người dùng nhìn thấy bản draft checklist đầu tiên..." (Xem *Section 3.2*).
*   **[x] Đã chỉ ra bước thừa hoặc friction trước core action:**
    *   *Dẫn chứng:* Chỉ rõ "Permission cấp quá sớm" và "Form nhập liệu quá rườm rà (5 trường)" là rào cản ngăn bước user. (Xem *Section 3.1*).
*   **[x] Có Before/After comparison:**
    *   *Dẫn chứng:* Thể hiện trực quan, so sánh đối chiếu tại Slide 06 (Before/After & Recovery Path).
*   **[x] Giữ hoặc cải thiện recovery flow Ngày 18:**
    *   *Dẫn chứng:* Cải thiện Recovery Flow "Xử lý thời tiết thay đổi đột biến": Gửi Smart Notification đưa thẳng user về Checklist đang soạn dở, tự động đề xuất thêm đồ phù hợp thay vì văng lỗi đứt gãy trải nghiệm. (Xem *Section 3.3*).

### 4. Measurement
*   **[x] Có Measurement Ladder & North Star & Input Metrics:**
    *   *Dẫn chứng:* Thiết kế cấu trúc hình thang (Ladder) rõ ràng. Có 1 North Star Metric (Tổng số Checklist được xác nhận) và 3 Input Metrics (Activation Rate, Time to Value, Tỷ lệ Edit gợi ý). (Xem *Section 4*).
*   **[x] Phân biệt leading và lagging indicator:**
    *   *Dẫn chứng:* Input Metrics được đánh dấu rõ ràng là (Leading Indicators). Mid/Long-term Business Results được đánh dấu rõ ràng là (Lagging Indicators). (Xem *Section 4*).
*   **[x] Có một trade-off cần theo dõi:**
    *   *Dẫn chứng:* "Nếu tìm cách tăng Số lượng đồ đạc được gợi ý (Volume) ... có thể làm tăng AI Suggestion Edit Rate theo chiều hướng tiêu cực ... làm giảm Tỷ lệ hoàn thành Checklist (North Star Metric)." (Xem *Phân tích Trade-off ở Section 4*).

### 5. Nature, Nurture và Hook
*   **[x] Phân biệt natural frequency với nurture:**
    *   *Dẫn chứng:* Nature là Monthly/Quarterly (Tần suất thấp). Nurture là chiến lược chủ động duy trì tương tác chờ chuyến đi tiếp theo qua Smart Notifications. (Xem *Bảng Section 5.1*).
*   **[x] Nurture không quá dày hoặc quá thưa:**
    *   *Dẫn chứng:* "Gửi hàng ngày (quá dày) sẽ biến thành spam... Thời điểm sát chuyến đi (3-7 ngày trước) là lúc Internal Trigger cao nhất." (Xem *Bảng Nurture ở Section 5.1*).
*   **[x] Hook Review có Trigger, Action, Variable Reward và Investment:**
    *   *Dẫn chứng:* Áp dụng Hook Loop vào "Prep Window" với cấu trúc 4 bước rõ ràng: Trigger (Lo lắng/Thông báo), Action (Mở app tinh chỉnh Checklist), Reward (Cảm giác yên tâm), Investment (Lưu đồ cá nhân vào thư viện). (Xem *Section 5.2*).
*   **[x] Đã xác định rào cản làm action khó thực hiện:**
    *   *Dẫn chứng:* Rào cản là "tốn não và mất quá nhiều thời gian" nghĩ xem mang gì (High Brain Cycles). Tính năng tự động tạo bản nháp của AI giúp dỡ bỏ hoàn toàn rào cản này. (Xem *Alternative ở Bài 1*).
*   **[x] Đã kiểm tra habit có thực sự có lợi cho user:**
    *   *Dẫn chứng:* Khẳng định việc chỉ áp dụng Habit trong "Prep Window" (tuần chuẩn bị hành lý) sẽ giúp user giải quyết bài toán cốt lõi. (Xem *Section 5.2*).
*   **[x] Không ép habit nếu frequency và utility không phù hợp:**
    *   *Dẫn chứng:* Lập luận mạnh mẽ: "Vì tần suất tự nhiên không đạt mức Weekly/Daily, việc áp dụng nguyên mẫu Hook Model để cố nhồi nhét tạo thói quen hàng ngày là khiên cưỡng." (Xem *Section 5.2*).

### 6. Tracking
*   **[x] Metric có định nghĩa, công thức, window và segment:**
    *   *Dẫn chứng:* Active User có định nghĩa "Hoàn thành xác nhận ít nhất 1 checklist" với Window rõ ràng là "trong khoảng thời gian 30 ngày". Các properties event (ví dụ `ai_accuracy_score`) hỗ trợ cực tốt cho phân loại Segment. (Xem *Section 2.2 và Bảng Section 6*).
*   **[x] Event map trực tiếp tới metric:**
    *   *Dẫn chứng:* Trong bảng Tracking (Bài 6), cột "Phục vụ Metric nào?" chỉ đích danh event `checklist_finalized` map trực tiếp tới North Star Metric. (Xem *Section 6*).
*   **[x] Event được gắn lên onboarding/core action flow:**
    *   *Dẫn chứng:* Các event được gán logic dọc theo hành trình từ Onboarding đến Core Action: `trip_creation_started` &rarr; `trip_draft_generated` &rarr; `checklist_item_edited` &rarr; `checklist_finalized`. (Xem *Bảng Section 6*).
*   **[x] Có ít nhất bốn tiêu chí nghiệm thu:**
    *   *Dẫn chứng:* Có đúng 4 Acceptance Criteria chặt chẽ ở cuối bài: (1) Chống trùng lặp event do F5, (2) Bắt buộc đính kèm user_id và timestamp ISO 8601 UTC, (3) Không track PII, (4) Validate Payload theo Schema để đảm bảo tính toàn vẹn. (Xem *Section 6*).
