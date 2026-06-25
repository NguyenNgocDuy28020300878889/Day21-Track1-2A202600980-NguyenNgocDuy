# 🎒 Prototype Thiết Kế Trải Nghiệm AI: Smart Packing & Prep

*Dự án thực hành thuộc Ngày 18 — Human-Centered AI Design (HCAI)*  
* **Track:** AI Travel Planner  
* **Lát cắt:** Gợi ý hành trang theo thời tiết và hoạt động chuyến đi (Smart Packing & Prep)  
* **Mã học viên:** 2A202600980  
* **Học viên thực hiện:** Nguyễn Ngọc Duy  

---

## 📖 Tổng Quan Dự Án
Dự án tập trung vào việc thiết kế một lát cắt trải nghiệm AI giúp người dùng chuẩn bị hành lý tối ưu khi đi du lịch. Thiết kế tuân thủ nghiêm ngặt các nguyên lý **Human-Centered AI (HCAI)** nhằm đảm bảo người dùng:
1. **Hiểu đúng và tin đúng mức (Mental Model & Calibration):** AI chỉ đóng vai trò gợi ý (Co-pilot), quyền quyết định tối cao thuộc về con người.
2. **Giữ quyền kiểm soát (User Control & Autonomy):** Cung cấp các công cụ chỉnh sửa, cấp quyền minh bạch, và tính năng **Hoàn tác (Undo)**.
3. **Khôi phục dễ dàng khi AI sai sót (Failure & Recovery):** Khi thời tiết thay đổi đột ngột hoặc quá cân hành lý, hệ thống đưa ra giải pháp xử lý một chạm.

---

## 🚀 Từng Bước Đã Thực Hiện (Step-by-Step Achievements)

### Bước 1: Xác Định Phạm Vi & Thiết Lập Kịch Bản Trải Nghiệm
*   Chọn lát cắt tập trung: **Gợi ý hành trang** dựa trên thời tiết thực tế tại điểm đến và hoạt động trong lịch trình (tránh làm phạm vi quá rộng như "toàn bộ ứng dụng du lịch").
*   Xây dựng chi tiết 6 kịch bản trải nghiệm trong [kichban.md](file:///c:/Users/PC/Desktop/Assigtment/Day21-Track1-2A202600980-NguyenNgocDuy-1/kichban.md) từ Onboarding (T0), Tương tác chuẩn (T1, T2, T3) đến xử lý sai sót và khôi phục (T6, T7).

### Bước 2: Thiết Kế Sơ Đồ Vòng Đời Trải Nghiệm (Flow Map)
*   Sử dụng **Mermaid.js** để vẽ và hệ thống hóa toàn bộ các điểm chạm, mức độ tự chủ của AI (`Act`, `Ask`, `Don't Act`) và các nhánh xử lý khôi phục lỗi. Chi tiết sơ đồ xem tại [flowmap.md](file:///c:/Users/PC/Desktop/Assigtment/Day21-Track1-2A202600980-NguyenNgocDuy-1/flowmap.md).

### Bước 3: Hiện Thực Hóa Giao Diện Onboarding Thiết Lập Kỳ Vọng
*   Xây dựng giao diện Onboarding tích hợp trong [prototype_day18.html#onboarding](file:///c:/Users/PC/Desktop/Assigtment/Day21-Track1-2A202600980-NguyenNgocDuy-1/prototype_day18.html#onboarding) gồm 3 màn hình tương tác:
    *   **Màn hình Welcome:** Định hình rõ giới hạn hệ thống ("Tôi chỉ gợi ý và không tự thanh toán", "Tôi chưa biết tủ đồ thực tế của bạn").
    *   **Màn hình Cấp quyền (Permissions):** Toggle switch cho phép người dùng chủ động bật/tắt quyền đọc thời tiết & lịch trình.
    *   **Màn hình Nhập liệu (Inputs):** Form trực quan để người dùng khởi tạo chuyến đi.

### Bước 4: Hiện Thực Luồng Chính & Phân Định Mức Tự Chủ (Agency)
*   Xây dựng luồng Happy Path & Agency tích hợp trong [prototype_day18.html#mainpath](file:///c:/Users/PC/Desktop/Assigtment/Day21-Track1-2A202600980-NguyenNgocDuy-1/prototype_day18.html#mainpath) thể hiện rõ:
    *   **Mức Ask (Hỏi trước):** AI đặt câu hỏi làm rõ phương tiện di chuyển (Jeep hay Trekking) tại Langbiang khi bối cảnh còn mơ hồ.
    *   **Mức Act (Tự động):** AI tự động điền và sắp xếp checklist nháp do rủi ro thấp.
    *   **Mức Don't Act (Tuyệt đối không tự ý):** Khi thấy thiếu sạc dự phòng, AI chỉ hiển thị đề xuất và link mua sắm bên ngoài, hoàn toàn không tự động thanh toán.
    *   **Explainability (Giải trình):** Nút `ⓘ` cạnh mỗi món đồ quan trọng mở ra lý do chi tiết ("Đề xuất áo ấm vì dự báo có mưa 80% và lạnh 15°C").

### Bước 5: Hiện Thực Luồng Khôi Phục Sai Sót & Tích Hợp Hoàn Tác (Undo)
*   Xây dựng luồng Khôi phục tích hợp trong [prototype_day18.html#recovery](file:///c:/Users/PC/Desktop/Assigtment/Day21-Track1-2A202600980-NguyenNgocDuy-1/prototype_day18.html#recovery) giải quyết 2 tình huống lỗi/thay đổi:
    *   **Fansipan đổi thời tiết đột ngột:** Hiển thị banner đỏ cảnh báo. Nút *[Cập nhật đồ ấm]* cho phép 1 chạm đổi sang trang phục giữ nhiệt.
    *   **Vietjet Air quá tải cân nặng xách tay (>7kg):** Thanh đo tải trọng chuyển sang màu đỏ. Nút *[Tối ưu theo luật bay]* tự động loại đồ cấm bay (dao kéo, gậy kim loại) và gợi ý thuê lều tại điểm đến để đưa hành lý về mức 4.5kg an toàn (thanh xanh).
    *   **Tích hợp Hoàn tác (Undo):** Trên Toast thông báo của mọi hành động khôi phục đều có liên kết **`[Hoàn tác]`** giúp người dùng đảo ngược quyết định và quay lại trạng thái cũ ngay lập tức nếu lỡ tay.

### Bước 6: Thiết Thiết Kế Opt-In Bảo Vệ Quyền Riêng Tư
*   Trong luồng [prototype_day18.html#mainpath](file:///c:/Users/PC/Desktop/Assigtment/Day21-Track1-2A202600980-NguyenNgocDuy-1/prototype_day18.html#mainpath), khi người dùng bỏ tick chọn "Giày leo núi", AI sẽ hiển thị một Modal hỏi có muốn ghi nhớ thói quen này cho các chuyến đi trekking sau không.
*   Hộp chọn "Đồng ý ghi nhớ" **để trống theo mặc định (Opt-in)**. Nếu người dùng không chọn mà nhấn xác nhận, AI tôn trọng quyền riêng tư và sẽ không ghi nhớ lâu dài sở thích này.

### Bước 7: Trực Quan Hóa Vòng Phản Hồi Hai Chiều 2x2
*   Xây dựng giao diện phản hồi 2x2 tích hợp trong [prototype_day18.html#feedback](file:///c:/Users/PC/Desktop/Assigtment/Day21-Track1-2A202600980-NguyenNgocDuy-1/prototype_day18.html#feedback) dưới dạng một Dashboard tương tác. Giảng viên có thể nhấp vào các thẻ màu đại diện cho 4 ô phản hồi:
    *   *User Explicit:* Xóa đồ bơi và chọn lý do "Đi công tác".
    *   *User Implicit:* Thời gian người dùng dừng lại đọc tooltip / bỏ qua link mua sạc.
    *   *System Explicit:* Toast xác nhận đã hiểu bối cảnh và xóa đồ.
    *   *System Implicit:* Đẩy các món đồ thiết yếu lên đầu danh sách và in đậm.

---

## 🛠️ Cấu Trúc Thư Mục Nộp Bài

```text
Day21-Track1-2A202600980-NguyenNgocDuy-1/
├── README.md               # Tài liệu tổng quan dự án (tệp này)
├── flowmap.md              # Sơ đồ Mermaid.js vòng đời trải nghiệm
├── kichban.md              # Kịch bản chi tiết 6 tình huống HCAI
├── onboarding-ui.md        # Wireframe và giải trình giao diện onboarding
├── index.html              # Hub thuyết trình chính (Presentation Slide Deck)
├── prototype_day18.html    # Giao diện Prototype Ngày 18 hợp nhất (Onboarding, Happy Path, Recovery, Feedback)
├── prototype_day20.html    # Giao diện Prototype Ngày 20 cải tiến
├── day18_report.md         # Báo cáo thiết kế HCAI Ngày 18 (đã đổi tên)
├── day20_report.md         # Báo cáo phân tích chuyên sâu Ngày 20 (đã đổi tên)
└── evaluation_evidence.md  # Dẫn chứng đánh giá (Checklist & Evidence)
```

---

## 💻 Hướng Dẫn Chạy Thử Prototype
Bạn không cần kết nối API hay cơ sở dữ liệu thật. Toàn bộ trải nghiệm đã được mô phỏng mượt mà trên nền tảng HTML/CSS/JavaScript thuần:

1.  Mở tệp [index.html](file:///c:/Users/PC/Desktop/Assigtment/Day21-Track1-2A202600980-NguyenNgocDuy-1/index.html) bằng bất kỳ trình duyệt web nào (Chrome, Edge, Safari...).
2.  Trang chủ `Presentation Slide Deck` sẽ đóng vai trò thuyết trình chính. Tại đây bạn có thể:
    *   Bấm vào các link tương tác trên Slide 1 để chuyển sang các luồng của **Prototype Ngày 18 hợp nhất** (`prototype_day18.html`).
    *   Bấm vào các menu slide để xem các phân tích chuyên sâu về Retention, Hook Loop, Measurement Ladder, Tracking.
3.  Khi mở các trang prototype con (được thiết kế dạng mockup khung điện thoại di động thông minh), hãy click vào các nút bấm, toggle switches và checkbox để tương tác và cảm nhận phản hồi thời gian thực của hệ thống.