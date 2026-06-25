# 🗺️ Sơ Đồ Vòng Đời Trải Nghiệm & Nhánh Rẽ AI (Flow Map)
**Tính năng:** AI Gợi ý hành trang theo thời tiết và hoạt động (Smart Packing & Prep)
*Bài thực hành Ngày 18 — Human-Centered AI Design (Giai đoạn 1)*

Tài liệu này hệ thống hóa toàn bộ các kịch bản trải nghiệm (Onboarding, Tương tác thông thường, Thay đổi lịch trình, Sai sót và Khôi phục) từ Giai đoạn 0 thành một sơ đồ Flow Map liền mạch bằng **Mermaid.js**, giúp hiển thị rõ các điểm chạm, mức độ tự chủ của AI (Act, Ask, Don't Act), và cơ chế phản hồi hai chiều (Feedback).

---

## 🎨 Sơ Đồ Mermaid.js Tổng Thể

```mermaid
graph TD
    %% Định nghĩa các lớp màu sắc để phân biệt trạng thái/mức độ tự chủ
    classDef startEnd fill:#f5f5f5,stroke:#9e9e9e,stroke-width:2px,stroke-dasharray: 5 5;
    classDef happyPath fill:#e8f5e9,stroke:#4caf50,stroke-width:2px;
    classDef aiSystem fill:#efebe9,stroke:#795548,stroke-width:2px;
    classDef aiAsk fill:#fffde7,stroke:#fbc02d,stroke-width:2px;
    classDef recovery fill:#ffebee,stroke:#ef5350,stroke-width:2px;
    classDef feedback fill:#f3e5f5,stroke:#ab47bc,stroke-width:2px;

    %% Định nghĩa hình dáng các node trước
    Start([Bắt đầu sử dụng app])
    OnboardingWelcome[Welcome Screen<br/><b>Thiết lập kỳ vọng</b><br/>AI nói rõ khả năng/giới hạn]
    OnboardingPerms[Màn hình xin quyền<br/>Thời tiết & Lịch trình<br/><i>User Control</i>]
    OnboardingInput[Màn hình Input<br/>Nhập điểm đến & Ngày đi]
    
    AIProcessing[AI Đang Phân tích<br/><i>System Explicit Feedback</i>]
    CheckContext{Đầy đủ dữ kiện?}
    
    AskLangbiang[Hộp thoại hỏi bối cảnh<br/>Cách đi Langbiang & Phong cách gói đồ<br/><b>[Mức độ: Ask]</b>]
    UserSelectsLangbiang[Người dùng phản hồi nhanh<br/><i>User Explicit Feedback</i>]
    
    DraftChecklist[Hiện Checklist Đề xuất<br/>Phân nhóm & Lớp giải thích<br/><b>[Mức độ: Act]</b> + Explainability]
    
    UserEditChecklist[Người dùng tích chọn/bỏ đồ]
    RemoveTrekking{Người dùng bỏ giày trekking?}
    AskReasonRemove[AI hỏi lý do xóa<br/><i>User Explicit Feedback</i>]
    ChooseJeep[Chọn: Đi xe Jeep]
    AdjustTrekkingChecklist[AI tự động bỏ đồ trekking<br/>Toast xác nhận chỉ áp dụng chuyến này<br/><i>System Explicit Feedback</i>]
    ConfirmMainChecklist[Xác nhận Checklist Đà Lạt]

    TripActive[Chuyến đi bắt đầu hoạt động]
    EditItinerary[Người dùng thêm hoạt động: Lặn ngắm san hô]
    AIDetectChange[AI tự động phát hiện thay đổi<br/>Đề xuất so sánh Trước/Sau<br/><b>[Mức độ: Act]</b>]
    
    AskRentBuy[Hỏi cách xử lý dụng cụ lặn<br/>Mang / Thuê / Mua<br/><b>[Mức độ: Ask]</b>]
    ShowShopping[Đưa link mua sắm tham khảo<br/><b>[Mức độ: Don't Act tự mua]</b>]
    UpdateRentList[Bỏ kính lặn, giữ đồ bơi]
    
    RemoveMotionSickness{Bỏ thuốc say tàu?}
    AskSavePrefs[Hỏi để ghi nhớ lâu dài<br/><i>Quyền riêng tư</i>]
    SaveChecklistNhaTrang[Cập nhật Checklist Nha Trang]
    
    Scenario1_Weather{Dự báo thời tiết Fansipan<br/>chuyển từ nắng sang lạnh/mưa?}
    WeatherWarning[Cảnh báo đỏ trên đầu màn hình<br/><i>System Explicit Feedback</i>]
    UpdateWeatherPack[Nút: Cập nhật hành lý mới<br/>So sánh Trước/Sau giữ ấm]
    
    Scenario2_Weight{Hành lý Vietjet vượt 7kg<br/>hoặc chứa đồ cấm bay?}
    WeightWarning[Thanh đo cân nặng báo Đỏ<br/>Gắn tag đỏ cạnh đồ cấm bay<br/><i>System Implicit/Explicit Feedback</i>]
    OptimizeFlight[Nút: Tối ưu hóa theo luật bay<br/>Gợi ý thuê đồ tại điểm đến]
    
    Scenario3_Survey{Thêm hoạt động phức tạp<br/>Trekking Cát Tiên mùa mưa?}
    MiniSurvey[Khảo sát nhanh độ khó<br/>Kinh nghiệm & Độ nhạy cảm da<br/><b>[Mức độ: Ask]</b>]
    CustomProtectiveList[AI gợi ý đồ bảo hộ chuyên dụng<br/>kèm giải thích chống vắt]
    
    SaveChecklist[Cập nhật Checklist]
    End([Hoàn thành chuẩn bị hành trang])

    %% Gán class màu sắc cho từng node
    class Start,End startEnd;
    class OnboardingWelcome,OnboardingPerms,OnboardingInput,UserSelectsLangbiang,DraftChecklist,UserEditChecklist,ConfirmMainChecklist,TripActive,EditItinerary,UpdateRentList,SaveChecklistNhaTrang,CustomProtectiveList happyPath;
    class AIProcessing,CheckContext,AdjustTrekkingChecklist,AIDetectChange feedback;
    class AskLangbiang,AskReasonRemove,AskRentBuy,ShowShopping,AskSavePrefs,MiniSurvey aiAsk;
    class RemoveTrekking,RemoveMotionSickness,Scenario1_Weather,WeatherWarning,UpdateWeatherPack,Scenario2_Weight,WeightWarning,OptimizeFlight,Scenario3_Survey,SaveChecklist recovery;

    %% Thiết lập các đường nối liên kết (Flow logic)
    Start --> OnboardingWelcome
    OnboardingWelcome --> OnboardingPerms
    OnboardingPerms --> OnboardingInput
    OnboardingInput --> AIProcessing
    AIProcessing --> CheckContext
    
    CheckContext -->|Thiếu thông tin| AskLangbiang
    AskLangbiang --> UserSelectsLangbiang
    UserSelectsLangbiang --> DraftChecklist
    CheckContext -->|Đủ thông tin| DraftChecklist
    
    DraftChecklist --> UserEditChecklist
    UserEditChecklist --> RemoveTrekking
    RemoveTrekking -->|Có| AskReasonRemove
    AskReasonRemove --> ChooseJeep
    ChooseJeep --> AdjustTrekkingChecklist
    AdjustTrekkingChecklist --> ConfirmMainChecklist
    RemoveTrekking -->|Không| ConfirmMainChecklist

    ConfirmMainChecklist --> TripActive
    TripActive --> EditItinerary
    EditItinerary --> AIDetectChange
    
    AIDetectChange --> AskRentBuy
    AskRentBuy -->|Chọn: Mua sắm| ShowShopping
    AskRentBuy -->|Chọn: Thuê ngoài| UpdateRentList
    
    AskRentBuy --> RemoveMotionSickness
    RemoveMotionSickness -->|Đồng ý| AskSavePrefs
    AskSavePrefs --> SaveChecklistNhaTrang
    
    ConfirmMainChecklist --> Scenario1_Weather
    Scenario1_Weather -->|Có| WeatherWarning
    WeatherWarning --> UpdateWeatherPack
    UpdateWeatherPack --> SaveChecklist
    
    ConfirmMainChecklist --> Scenario2_Weight
    Scenario2_Weight -->|Có| WeightWarning
    WeightWarning --> OptimizeFlight
    OptimizeFlight --> SaveChecklist
    
    ConfirmMainChecklist --> Scenario3_Survey
    Scenario3_Survey -->|Có| MiniSurvey
    MiniSurvey --> CustomProtectiveList
    CustomProtectiveList --> SaveChecklist

    SaveChecklistNhaTrang --> End
    SaveChecklist --> End
```

---

## 📖 Giải Thích Chi Tiết Các Nhánh Rẽ Trên Sơ Đồ

### 1. Vòng Đời Trải Nghiệm Cơ Bản (Happy Path)
*   **Onboarding (Welcome $\rightarrow$ Permissions $\rightarrow$ Input):** Giúp người dùng hình thành mô hình tâm trí (Mental Model) đúng đắn về AI: biết rõ AI có thể làm gì (phân tích thời tiết, lịch trình) và không thể làm gì (không tự biết tủ đồ cá nhân). Xin quyền truy cập tường minh trước khi bắt đầu.
*   **AI Processing & Draft Checklist:** AI tự động nhóm đồ dùng theo các mục logic và giải thích lý do đề xuất thông qua lớp thông tin Explainability (nhấp chọn để xem tại sao đề xuất món đồ này).

### 2. Nhánh Xử Lý Khi Thiếu Dữ Kiện (Ask Scenario)
*   **Hỏi để làm rõ (Langbiang - Đà Lạt):** Do địa danh Đà Lạt có nhiều hình thức tham quan, AI kích hoạt trạng thái **Ask** để hỏi phương thức di chuyển tại Langbiang (Trekking hay đi xe Jeep) để tránh gợi ý sai hoặc thừa đồ.

### 3. Nhánh Cập Nhật Khi Thay Đổi Lịch Trình (Adaptability & Privacy)
*   **Tự động phát hiện (Nha Trang):** Khi người dùng tự thêm hoạt động lặn biển, AI tự động so sánh danh sách và hiển thị bảng đối chiếu giúp người dùng dễ theo dõi các món đồ đề xuất thêm.
*   **Hỏi ý kiến trước khi lưu trữ (Ghi nhớ thói quen):** Khi người dùng bỏ thuốc say tàu, AI hỏi xem có muốn lưu lựa chọn này cho các chuyến đi sau không để đảm bảo quyền riêng tư tối đa.

### 4. Nhánh Khôi Phục Lỗi và Giới Hạn Tự Chủ (Failure, Recovery & Agency)
*   **Khôi phục do ngoại cảnh (Thời tiết thay đổi đột ngột tại Fansipan):** Hệ thống không tự ý sửa danh sách đồ người dùng đang chuẩn bị mà đưa ra cảnh báo đỏ nổi bật, cho phép người dùng một chạm để cập nhật sang danh sách đồ ấm.
*   **Khôi phục do vi phạm luật bay (Cân nặng & Đồ cấm bay):** AI cảnh báo bằng thanh đo trọng lượng màu đỏ và đề xuất giải pháp thuê đồ cắm trại tại điểm đến để tối ưu hành lý xách tay dưới 7kg.
*   **Khảo sát ngắn trước khi gợi ý hoạt động khó (Cát Tiên):** AI không áp đặt danh sách đồ dã ngoại chuyên nghiệp đắt tiền mà đưa ra câu hỏi khảo sát ngắn về kinh nghiệm và độ nhạy cảm da để đề xuất chính xác các món đồ chống vắt.
