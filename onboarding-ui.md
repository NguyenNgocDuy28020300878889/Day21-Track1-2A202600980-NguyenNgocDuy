# 📱 Thiết Kế Chi Tiết Giao Diện Onboarding (Giai đoạn 2)
**Tính năng:** AI Gợi ý hành trang theo thời tiết và hoạt động (Smart Packing & Prep)
*Bài thực hành Ngày 18 — Human-Centered AI Design (Giai đoạn 2)*

Tài liệu này chi tiết hóa 3 màn hình Onboarding đầu tiên theo chuẩn HCAI, giúp thiết lập kỳ vọng rõ ràng cho người dùng về khả năng/giới hạn của AI và thu thập quyền truy cập dữ liệu một cách minh bạch.

---

## 🖥️ Màn Hình 1: Welcome (Thiết Lập Kỳ Vọng)

### 1. Phác thảo giao diện (Wireframe)
```text
+------------------------------------------+
|                                          |
|                [ Logo App ]              |
|                                          |
|       Trợ Lý Hành Trang Thông Minh       |
|                                          |
|  Tôi sẽ phân tích dự báo thời tiết và    |
|  lịch trình để giúp bạn chuẩn bị hành    |
|  lý tối ưu nhất cho mỗi chuyến đi.       |
|                                          |
|  +-------------------------------------+ |
|  | 💡 Tuyên bố giới hạn (Mental Model)  | |
|  | - AI gợi ý dựa trên dữ liệu thời tiết | |
|  |   và lịch trình do bạn cung cấp.    | |
|  | - Tôi chưa biết tủ đồ thực tế của bạn | |
|  |   có những gì.                       | |
|  | - Bạn luôn là người quyết định cuối  | |
|  |   cùng đối với checklist.            | |
|  +-------------------------------------+ |
|                                          |
|            [ Nút: Tiếp tục ]             |
|                                          |
+------------------------------------------+
```

### 2. Copywriting Chi Tiết
*   **Tiêu đề:** Trợ Lý Hành Trang Thông Minh (AI Smart Packing)
*   **Mô tả:** *"Tôi sẽ phân tích dự báo thời tiết tại điểm đến và các hoạt động trong lịch trình để đề xuất danh sách hành lý cá nhân hóa, giúp bạn không quên đồ quan trọng và tránh mang thừa."*
*   **Giới hạn hệ thống (System Boundaries):** 
    *   *"Tôi chỉ đưa ra đề xuất và không tự ý thực hiện giao dịch mua sắm hay đặt dịch vụ."*
    *   *"Gợi ý được tối ưu theo thời tiết thực tế, tuy nhiên tôi chưa biết tủ đồ cá nhân của bạn hiện có gì. Bạn hoàn toàn có thể tùy chỉnh danh sách này."*

### 3. Giải trình HCAI (Design Rationale)
*   **Tiêu chuẩn áp dụng:** Microsoft HAX **G1** (Làm rõ hệ thống có thể làm gì) và **G2** (Làm rõ mức độ hiệu quả của hệ thống).
*   **Lý do thiết kế:** Ngăn ngừa việc người dùng quá tin tưởng (Overtrust) dẫn đến việc đổ lỗi cho AI nếu gợi ý bị thiếu món đồ họ thích, đồng thời định hình rõ AI chỉ đóng vai trò hỗ trợ gợi ý (Co-pilot), quyền quyết định thuộc về con người.

---

## 🔐 Màn Hình 2: Quyền Hạn (Permissions & Data Control)

### 1. Phác thảo giao diện (Wireframe)
```text
+------------------------------------------+
|  < Quay lại                              |
|                                          |
|          Cấp Quyền Để AI Tối Ưu          |
|                                          |
|  Để tự động tạo checklist chính xác,     |
|  vui lòng cho phép truy cập:             |
|                                          |
|  [🔌] Truy cập Thời tiết            (o)  |
|      Giúp đề xuất đồ giữ ấm/che mưa      |
|      theo dự báo thời gian thực.         |
|                                          |
|  [📅] Đọc Lịch trình chuyến đi       (o)  |
|      Phân tích các hoạt động (ví dụ:     |
|      trekking, bơi) để chọn đồ phù hợp.  |
|                                          |
|  +-------------------------------------+ |
|  | 🔒 Cam kết bảo mật quyền riêng tư    | |
|  | Dữ liệu này chỉ xử lý tức thời cho  | |
|  | chuyến đi này và không lưu trữ lâu   | |
|  | dài nếu chưa được bạn cho phép.     | |
|  +-------------------------------------+ |
|                                          |
|         [ Nút: Bắt đầu chuyến đi ]       |
|                                          |
+------------------------------------------+
```

### 2. Copywriting Chi Tiết
*   **Tiêu đề:** Cấp Quyền Để AI Tối Ưu
*   **Quyền 1:** Truy cập Dự báo thời tiết (Mặc định: BẬT). *Mô tả ích lợi:* "Đề xuất quần áo, ô/dù, kem chống nắng phù hợp với nhiệt độ và khả năng mưa thực tế tại điểm đến."
*   **Quyền 2:** Đọc Lịch trình chuyến đi (Mặc định: BẬT). *Mô tả ích lợi:* "Tự động phát hiện các hoạt động đặc thù (leo núi, lặn biển, tiệc tối) để thêm trang bị phù hợp."
*   **Cam kết riêng tư:** *"Chúng tôi tôn trọng quyền riêng tư của bạn. Dữ liệu thời tiết và lịch trình chỉ được dùng để tạo checklist và sẽ không chia sẻ cho bên thứ ba."*

### 3. Giải trình HCAI (Design Rationale)
*   **Tiêu chuẩn áp dụng:** Google PAIR Guidebook - **Data Collection & Consent**.
*   **Lý do thiết kế:** Cung cấp lý do (Rationale) cụ thể tại sao ứng dụng cần quyền này ngay cạnh toggle switch. Người dùng được toàn quyền bật/tắt (User Control). Nếu tắt quyền, AI vẫn sẽ chạy nhưng chuyển sang chế độ dự phòng là hỏi người dùng nhập tay ở màn hình tiếp theo.

---

## ✍️ Màn Hình 3: Nhập Liệu Đầu Vào (User Inputs)

### 1. Phác thảo giao diện (Wireframe)
```text
+------------------------------------------+
|  < Quay lại                              |
|                                          |
|         Thông Tin Chuyến Đi Của Bạn       |
|                                          |
|  Điểm đến:                               |
|  [ Đà Lạt, Lâm Đồng                 ]    |
|                                          |
|  Thời gian:                              |
|  [ Từ 10/07/2026   ] -> [ Đến 12/07/2026 ]|
|                                          |
|  Số lượng người đi:                      |
|  [-]  1 người lớn  [+]                   |
|                                          |
|  * AI sẽ quét lịch trình đã liên kết     |
|    và dự báo thời tiết Đà Lạt vào ngày   |
|    10-12/7 sắp tới.                      |
|                                          |
|                                          |
|           [ Nút: Tạo Checklist ]         |
|                                          |
+------------------------------------------+
```

### 2. Copywriting Chi Tiết
*   **Nhãn ô nhập:**
    *   *"Điểm đến của bạn (Ví dụ: Nha Trang, Đà Lạt...)"*
    *   *"Thời gian đi và về"*
*   **Nút hành động:** "Tạo Checklist" (AI sẽ bắt đầu trạng thái Loading phân tích như mô tả ở Giai đoạn 1).

### 3. Giải trình HCAI (Design Rationale)
*   **Tiêu chuẩn áp dụng:** Microsoft HAX **G10** (Cung cấp các thiết lập đầu vào trực quan và dễ sửa lỗi).
*   **Lý do thiết kế:** Giới hạn phạm vi nhập liệu rõ ràng để AI có đủ dữ kiện truy vấn API thời tiết và tính toán số lượng trang phục phù hợp dựa trên số ngày đi và số người đi thực tế.
