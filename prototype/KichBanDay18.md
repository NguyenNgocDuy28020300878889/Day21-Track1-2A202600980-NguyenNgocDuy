# 📝 Kịch Bản Chi Tiết Toàn Bộ Vòng Đời Trải Nghiệm (HCAI)
**Tính năng:** AI Gợi ý hành trang theo thời tiết và hoạt động (Smart Packing & Prep)
*Bài thực hành Ngày 18 — Human-Centered AI Design (Giai đoạn 0 & Tổng hợp)*

Tài liệu này là kết quả tổng hợp của tất cả các kịch bản trải nghiệm bao gồm: Thiết lập kỳ vọng lúc Onboarding, Luồng tương tác chuẩn (Happy Path & Thay đổi lịch trình) và Các nhánh xử lý sai sót, không chắc chắn (Failure & Recovery).

---

## 📑 MỤC LỤC
1. [Kịch bản 1: Thiết lập kỳ vọng Onboarding & Cấp quyền (Bắt buộc)](#1-kịch-bản-onboarding-thiết-lập-kỳ-vọng-&-cấp-quyền)
2. [Kịch bản 2: Tương tác chính - AI Hỏi thêm để làm rõ & Thiết lập Checklist](#2-kịch-bản-tương-tác-chính---ai-hỏi-thêm-để-làm-rõ-&-thiết-lập-checklist)
3. [Kịch bản 3: Thay đổi lịch trình - AI Tự động cập nhật & Hỏi ý kiến ghi nhớ](#3-kịch-bản-thay-đổi-lịch-trình---ai-tự-động-cập-nhật-&-hỏi-ý-kiến-ghi-nhớ)
4. [Kịch bản 4: Thời tiết thay đổi đột ngột làm lệch đề xuất (Sai sót & Khôi phục)](#4-kịch-bản-sai-sót-1-thời-tiết-thay-đổi-đột-ngột)
5. [Kịch bản 5: Hành lý quá cân & Chứa vật dụng cấm bay (Quy định & Tối ưu)](#5-kịch-bản-sai-sót-2-hành-lý-quá-cân-&-chứa-vật-dụng-cấm-bay)
6. [Kịch bản 6: Khảo sát ngắn khi gặp hoạt động độ khó cao (Cát Tiên)](#6-kịch-bản-sai-sót-3-khảo-sát-ngắn-khi-gặp-hoạt-động-độ-khó-cao)
7. [Ma Trận Feedback 2x2 & Bảng Phân bổ Tự chủ (Act / Ask / Don’t Act)](#7-ma-trận-feedback-2x2-&-bảng-phân-bổ-tự-chủ)

---

## 1. KỊCH BẢN ONBOARDING: Thiết lập kỳ vọng & Cấp quyền

*   **Bối cảnh:** Lần đầu tiên người dùng sử dụng tính năng Smart Packing & Prep.
*   **Chi tiết thiết lập kỳ vọng:**
    *   **AI có thể làm gì:** Kết nối API dự báo thời tiết tại điểm đến, phân tích lịch trình chuyến đi để đề xuất và phân nhóm vật dụng cần thiết.
    *   **AI không thể làm gì (Giới hạn):** AI không tự biết tủ đồ thực tế của bạn có gì và tuyệt đối không tự động thực hiện thanh toán/mua bán ngoài app. Người dùng nắm quyền kiểm soát và quyết định cuối cùng.
*   **Quyền hạn yêu cầu:** Người dùng chủ động bật/tắt (Toggle) quyền truy cập Dự báo thời tiết địa phương và Đọc lịch trình cá nhân.

---

## 2. KỊCH BẢN TƯƠNG TÁC CHÍNH: AI Hỏi thêm để làm rõ & Thiết lập Checklist

### 2.1. Bối cảnh ban đầu
*   Người dùng nhập: *"Tôi đi Đà Lạt từ ngày 10 đến 12/7. Hãy chuẩn bị danh sách hành lý cho tôi."*
*   AI đã biết: Điểm đến (Đà Lạt), Thời gian (3 ngày 2 đêm), Thời tiết (mát mẻ, có khả năng mưa), Hoạt động (sightseeing, đi Langbiang, đi chợ đêm).
*   AI chưa biết: Phương tiện di chuyển là gì, hình thức tham quan Langbiang (Trekking hay xe Jeep), phong cách đóng đồ (Gọn nhẹ hay đầy đủ).

### 2.2. Luồng màn hình (UI States)
1.  **Màn hình 1 (Loading):** Hiện trạng thái AI đang quét thời tiết và lịch trình chuyến đi (`System Explicit Feedback`).
2.  **Màn hình 2 (Hộp thoại hỏi - Ask):** AI hỏi phương thức di chuyển tại Langbiang (Trekking hay Jeep) và phong cách hành trang mong muốn.
3.  **Màn hình 3 (Kết quả Checklist - Act):** AI sinh checklist phân nhóm rõ ràng (Thiết yếu, Theo thời tiết, Theo hoạt động).
4.  **Màn hình 4 (Lớp giải thích - Explainability):** Người dùng bấm `Vì sao AI đề xuất?` tại mục "Giày bám tốt", AI hiện tooltip: *"Đề xuất vì có hoạt động trekking Langbiang và thời tiết có mưa"*.
5.  **Màn hình 5 (Phản hồi & Khôi phục):** Người dùng bỏ tick chọn "Giày trekking" $\rightarrow$ AI hỏi lý do $\rightarrow$ Người dùng chọn "Đi xe Jeep" $\rightarrow$ AI tự động cập nhật bỏ các vật dụng trekking khác và báo xác nhận chỉ áp dụng cho chuyến đi này.

---

## 3. KỊCH BẢN THAY ĐỔI LỊCH TRÌNH: AI Tự động cập nhật & Hỏi ý kiến ghi nhớ

### 3.1. Bối cảnh
Người dùng đã có checklist Nha Trang 4 ngày. Sau đó, họ thêm hoạt động *"Lặn ngắm san hô ngày 2"* vào lịch trình.

### 3.2. Luồng màn hình (UI States)
1.  **Màn hình 1 (Phát hiện):** AI hiện thông báo phát hiện lịch trình thay đổi và đề xuất các vật dụng lặn biển phù hợp.
2.  **Màn hình 2 (So sánh Trước/Sau):** Bảng so sánh trực quan các món đề xuất thêm (Đồ bơi, khăn nhanh khô) và món cắm cờ *"Cần kiểm tra"* (kính lặn, ống thở vì nhà cung cấp có thể đã trang bị sẵn).
3.  **Màn hình 3 (Xử lý thiết bị - Don't Act):** Hỏi người dùng muốn Mang, Thuê hay Mua. Nếu chọn Mua, AI hiện link tham khảo nhưng không tự thêm vào giỏ hay thanh toán (`Don't Act`).
4.  **Màn hình 4 (Ghi nhớ thói quen - Quyền riêng tư):** Người dùng bỏ chọn "Thuốc chống say tàu" và chọn lý do "Tôi không say". AI hỏi: *"Có muốn ghi nhớ lâu dài không?"*. Mặc định chọn là không để bảo vệ quyền riêng tư trừ khi người dùng chủ động cho phép.

---

## 4. KỊCH BẢN SAI SÓT 1: Thời tiết thay đổi đột ngột

*   **Sự cố:** 2 ngày trước khi đi Fansipan, thời tiết đột ngột đổi từ nắng ráo ($22^\circ\text{C}$) sang lạnh sâu ($8^\circ\text{C}$) kèm mưa gió.
*   **Trạng thái AI:** AI phát hiện qua API thời tiết thời gian thực.
*   **Hành động khôi phục (Recovery):**
    *   Hiện biểu ngữ cảnh báo màu đỏ nổi bật trên cùng app: `⚠️ Thời tiết Fansipan đã thay đổi đột ngột!`.
    *   Cung cấp nút: **[Cập nhật hành lý theo thời tiết mới]** và **[Giữ nguyên danh sách cũ]**.
    *   Khi người dùng xác nhận, hiển thị bảng so sánh chuyển đổi nhanh (loại bớt áo thun ngắn, đề xuất thêm áo phao ấm, găng tay len, áo mưa tiện lợi).

---

## 5. KỊCH BẢN SAI SÓT 2: Hành lý quá cân & Chứa vật dụng cấm bay

*   **Sự cố:** Người dùng đặt vé Vietjet Air chỉ có 7kg xách tay, nhưng checklist gợi ý đầy đủ đồ cắm trại (lều, túi ngủ, flycam, gậy leo núi, dao kéo đa năng) nặng tới 12kg.
*   **Hành động khôi phục (Recovery):**
    *   Thanh đo cân nặng chuyển sang màu Đỏ (`12kg / 7kg xách tay`).
    *   Gắn nhãn cảnh báo đỏ sát bên cạnh các vật dụng vi phạm: `🚫 Cấm mang lên cabin (Dao đa năng)` và `⚠️ Bắt buộc xách tay, cấm ký gửi (Pin Lithium)`.
    *   Nút chọn nhanh: **[Tối ưu hóa theo luật bay]** (AI sẽ tự động bỏ lều/túi ngủ và đề xuất dịch vụ thuê ngoài tại Đà Lạt) hoặc **[Tôi sẽ mua thêm ký gửi]** (AI cập nhật lại hạn mức lên 20kg).

---

## 6. KỊCH BẢN SAI SÓT 3: Khảo sát ngắn khi gặp hoạt động độ khó cao

*   **Sự cố:** Người dùng đi trekking rừng quốc gia Cát Tiên vào mùa mưa, AI cần đề xuất đồ chống vắt/côn trùng chuyên dụng nhưng chưa biết thể trạng/kinh nghiệm của người dùng.
*   **Hành động khôi phục (Recovery):**
    *   Hiển thị một bảng câu hỏi ngắn gọn thân thiện: *"Bạn đã sẵn sàng cho chuyến đi rừng Cát Tiên?"*.
    *   Cung cấp tag chọn nhanh về: Kinh nghiệm (Lần đầu, Chuyên nghiệp) và Loại da (Có nhạy cảm hay không).
    *   Cập nhật danh sách cá nhân hóa dựa trên câu trả lời (Ví dụ: Thêm tất chống vắt cao cổ, thuốc DEET >30% cho da nhạy cảm) kèm lý giải vì sao cần thiết.

---

## 7. MA TRẬN FEEDBACK 2X2 & BẢNG PHÂN BỔ TỰ CHỦ

### 7.1. Ma Trận Feedback 2x2
| Tương tác | Tường minh (Explicit) | Ngầm định (Implicit) |
| :--- | :--- | :--- |
| **User $\rightarrow$ System** | Người dùng bấm nút báo thời tiết sai; check/uncheck thêm bớt đồ; chọn lý do xóa vật dụng. | Giữ lại đồ giữ ấm dù trời nắng (AI ghi nhận thói quen mặc ấm cá nhân để cá nhân hóa các đề xuất tiếp theo). |
| **System $\rightarrow$ User** | Hiện banner cảnh báo đỏ thời tiết thay đổi; hiện tag `🚫 Cấm xách tay` sát tên vật dụng. | Thanh cân nặng tự chuyển đỏ khi quá tải; in đậm và đẩy các đồ thiết yếu nhất lên đầu danh sách. |

### 7.2. Phân bổ Tự chủ (Act / Ask / Don't Act)
*   **Act (Tự động thực hiện):** Phân tích thời tiết & lịch trình, tự phân nhóm hành lý, tự động tạo checklist bản nháp, phát hiện lịch trình đổi để đề xuất cập nhật.
*   **Ask (Hỏi trước):** Hỏi bối cảnh khi thiếu thông tin quan trọng, xin phép lưu sở thích lâu dài, hỏi phương án xử lý hành lý quá giới hạn bay.
*   **Don't Act (Tuyệt đối không tự ý):** Không tự đặt hàng, không tự mua sắm hay thanh toán liên kết ngoài, không tự lưu thông tin sức khỏe nhạy cảm khi chưa xin phép.
