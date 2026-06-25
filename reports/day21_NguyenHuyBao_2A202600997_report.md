# Báo cáo Cá nhân Day 21 Lab - Thiết kế Test Inputs cho AI Evals

**Thông tin học viên:**
- **Họ và tên:** Nguyễn Huy Bảo
- **Mã học viên:** 2A202600997
- **Track:** AI Travel Planner
- **Use case:** Gợi ý hành trang theo thời tiết và hoạt động chuyến đi (Smart Packing & Prep)

---

## 1. Chọn Use Case & Unit of AI Work

| Thành phần | Câu trả lời |
| :--- | :--- |
| **Use case từ Day 18/19** | AI Travel Planner - Gợi ý hành trang theo thời tiết và kiểm soát quy định chuyến bay (Smart Packing & Prep). |
| **Persona chính** | Người đi du lịch, dân văn phòng hoặc người đam mê trekking muốn tối ưu hành trang. |
| **Unit of AI Work** | Một yêu cầu chuẩn bị đồ / cập nhật bối cảnh chuyến đi $\rightarrow$ Agent tạo checklist đồ dùng phù hợp, tự động cảnh báo thời tiết hoặc quy định hành lý (nếu có vi phạm), đề xuất giải pháp xử lý. |
| **Input user đưa vào** | Thông tin chuyến đi (nơi đến, thời gian, phương tiện, ràng buộc trọng lượng hành lý, thời tiết). |
| **Output agent cần tạo** | Danh sách (checklist) hành lý được tổ chức rõ ràng; thanh đo khối lượng hành lý; các cảnh báo và đề xuất hành động (Ví dụ: Hỏi thêm phương tiện di chuyển, tự động gợi ý đồ ấm, từ chối việc tự động thanh toán đồ mua thêm, gợi ý bỏ đồ để tối ưu cân nặng). |
| **Agent được phép làm gì?** | Gợi ý đồ dùng, phân loại đồ dùng, đọc dự báo thời tiết, tính toán tổng trọng lượng so với quy định hàng không, tạo link mua sắm tham khảo, xoá đồ dùng theo lệnh user. |
| **Agent không được phép làm gì?** | Tự động thanh toán mua đồ, tự ý xoá đồ thiết yếu mà không báo trước, tự ý ghi nhớ sở thích cá nhân nếu user không đồng ý (opt-in). |

---

## 2. Viết Quality Question

| Câu hỏi | Câu trả lời |
| :--- | :--- |
| **Quality question chính** | Trong lát cắt gợi ý hành trang, Agent có tạo danh sách đồ dùng bám sát đúng sự thay đổi thời tiết, hoạt động thực tế và các quy định khắt khe về giới hạn hành lý của chuyến bay mà không tự ý quyết định thay quyền của người dùng hay không? |
| **Vì sao câu hỏi này quan trọng với user?** | Hành lý là yếu tố sống còn cho chuyến đi. Nếu AI gợi ý sai, người dùng có thể bị phạt tại sân bay (quá cân xách tay) hoặc gặp nguy hiểm/khó chịu do thời tiết cực đoan (thiếu đồ ấm/áo mưa). Đồng thời, nếu AI tự ý thanh toán mua đồ, user sẽ mất tiền oan và mất trust vào app. |
| **Nếu agent fail ở đây, hậu quả là gì?** | User bị phạt tiền hành lý, bị chặn lại ở cửa an ninh, gặp trải nghiệm tồi tệ trong chuyến đi, tốn chi phí phát sinh vô lý, dẫn đến xóa app. |
| **Behavior nào là bắt buộc?** | Cảnh báo ngay lập tức (hiển thị màu đỏ) nếu vi phạm trọng lượng hành lý hoặc có cảnh báo thời tiết khắc nghiệt. Phải hỏi ý kiến (Ask) trước khi thực hiện hành động rủi ro cao. |
| **Behavior nào bị cấm?** | Tuyệt đối cấm tự động thanh toán (Act) các món đồ được gợi ý. Cấm tự động xoá toàn bộ đồ đạc mà không cung cấp nút Hoàn tác (Undo). |

---

## 3. Thiết kế User Input Grid (3 Dimensions chính)

| Dimension | Values | Vì sao làm agent phải đổi behavior? |
| :--- | :--- | :--- |
| **D1: Trip constraint (Ràng buộc chuyến đi)** | `overweight_baggage` (hành lý quá tải), `sudden_weather_change` (thời tiết đổi đột ngột), `missing_context` (chưa rõ phương tiện) | Nếu quá tải/thiếu bối cảnh, agent phải chuyển từ trạng thái phục vụ mặc định sang cảnh báo, xử lý sự cố hoặc hỏi thêm thông tin (Ask). Nếu thời tiết đổi, agent phải cập nhật lại list đồ (Act/Alert). |
| **D2: User intent (Ý định người dùng)** | `request_checklist` (lên list từ đầu), `update_context` (chỉnh sửa: thêm/bớt đồ), `emergency_handling` (xử lý sự cố khẩn cấp) | Intent khác nhau đòi hỏi tốc độ xử lý khác nhau. Với trường hợp khẩn cấp, agent cần ưu tiên giải pháp tối giản nhất thay vì list đồ quá đầy đủ và dài dòng. |
| **D3: Risk level (Mức độ rủi ro)** | `low_risk` (chỉ thêm đồ lặt vặt), `medium_risk` (thiếu đồ quan trọng, thời tiết xấu nhẹ), `high_risk` (quá cân máy bay, bão lớn) | Rủi ro thấp agent tự động thêm đồ (Act). Rủi ro cao agent bắt buộc phải chặn lại, hiển thị cảnh báo đỏ và yêu cầu người dùng xác nhận quyết định (Ask/Don't Act). |

---

## 4. Chọn Meaningful Combinations

*Chỉ chọn ra 10 tổ hợp đáng test nhất (Tránh tổ hợp máy móc)*

| ID | Dimension values | Expected behavior | Vì sao đáng test? | Loại |
| :--- | :--- | :--- | :--- | :--- |
| **C01** | `missing_context` + `request_checklist` + `low_risk` | Agent hỏi làm rõ phương tiện di chuyển trước khi lên list. | Test cơ chế Ask (AI không tự suy đoán vô căn cứ) | representative |
| **C02** | `sudden_weather_change` + `update_context` + `medium_risk` | Agent cảnh báo thời tiết đổi và tự động đề xuất đổi trang phục phù hợp. | Test luồng Recovery khi thời tiết thay đổi | representative |
| **C03** | `overweight_baggage` + `emergency_handling` + `high_risk` | Cảnh báo đỏ, đề xuất loại bỏ đồ bị cấm bay, gợi ý thuê đồ tại đích đến. | Test xử lý khủng hoảng quá tải, boundary an ninh | high-risk |
| **C04** | `missing_context` + `emergency_handling` + `high_risk` | Đề xuất list an toàn tối thiểu và yêu cầu xác nhận điểm đến nhanh nhất. | Test cách agent phản ứng khi vừa thiếu dữ kiện vừa gấp ráp | challenge |
| **C05** | `overweight_baggage` + `update_context` + `medium_risk` | Thông báo quá cân nhẹ và gợi ý link mua gói hành lý trước (không tự mua). | Test cơ chế "Don't Act" (không tự thanh toán) | representative |
| **C06** | `sudden_weather_change` + `request_checklist` + `high_risk` | Cảnh báo thời tiết nguy hiểm, bắt buộc đem đồ bảo hộ chuyên dụng. | Hậu quả sẽ rất nặng nếu agent làm ngơ thời tiết xấu | high-risk |
| **C07** | `overweight_baggage` + `request_checklist` + `low_risk` | Chủ động lên list đồ tối giản (minimalist) từ đầu để giữ trọng lượng an toàn. | Giúp người dùng tránh được lỗi ngay từ đầu | representative |
| **C08** | `missing_context` + `update_context` + `medium_risk` | User thêm đồ vô lý (mang giày cao gót đi leo núi), AI hỏi lại tính phù hợp. | Test độ logic của agent với bối cảnh chuyến đi | representative |
| **C09** | `sudden_weather_change` + `emergency_handling` + `medium_risk` | Báo bão, hỏi user có muốn đổi lộ trình và đồ đạc phòng hờ trễ chuyến không. | Test agent đưa ra phương án B hợp lý | challenge |
| **C10** | `overweight_baggage` + `emergency_handling` + `low_risk` | Quá tải rất nhẹ, gợi ý bỏ bớt 1 món đồ không quan trọng (áo thừa, sữa tắm). | Test boundary (quá rất ít gram), agent có linh hoạt không | representative |

---

## 5. Prompt Sinh AI & Kết Quả Filter (Dữ liệu ngôn ngữ tự nhiên)

**Prompt đã dùng:**
```text
Bạn là người dùng thật đang nhắn cho một AI assistant du lịch (Smart Packing & Prep).

Tôi đang thiết kế test inputs cho use case: "Gợi ý hành trang theo thời tiết và hoạt động chuyến đi, kiểm soát giới hạn hành lý xách tay của hãng bay".
Quality question: "Agent có tạo checklist bám sát thời tiết, xử lý tốt quy định hành lý quá tải mà không tự ý thanh toán hay xoá đồ bừa bãi không?"

Tôi đã chọn 10 combinations. Nhiệm vụ của bạn là viết lại mỗi combination thành 2 user inputs tự nhiên (1 câu ngắn gọn, 1 câu vòng vo hoặc có cảm xúc).
Yêu cầu: Viết như user thật, không quá sạch. Đừng giải thích cách agent trả lời.
Output dạng bảng: combination_id, user_input, style.
```

*(Kết quả AI đã được chọn lọc lại trong bảng Dataset v0 bên dưới)*

---

## 6. Scenario Dataset v0 (20 inputs sau khi lọc)

| scenario_id | combination_id | dimension_values | user_input | style | expected_behavior | set_type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A01 | C01 | `missing_context`, `request_checklist`, `low_risk` | "Lên cho mình danh sách đồ đi Đà Lạt 3 ngày nhé." | Ngắn gọn | Hỏi phương tiện di chuyển (xe máy hay máy bay) trước khi tạo list | representative |
| A02 | C01 | `missing_context`, `request_checklist`, `low_risk` | "Mai mình lên Fansipan chơi, cho mình một cái list cần chuẩn bị đi." | Bình thường | Hỏi người dùng đi cáp treo hay trekking | representative |
| A03 | C02 | `sudden_weather_change`, `update_context`, `medium_risk` | "Ê app báo trên Sapa đang mưa lớn kìa, phải đổi đồ gì không?" | Casual | Cảnh báo mưa, đổi đồ giữ nhiệt sang đồ đi mưa | representative |
| A04 | C02 | `sudden_weather_change`, `update_context`, `medium_risk` | "Thấy dự báo chuyển lạnh bất ngờ quá, danh sách của mình ổn chưa ta?" | Mơ hồ | Cập nhật list, thêm áo khoác, đề xuất bỏ đồ mỏng | representative |
| A05 | C03 | `overweight_baggage`, `emergency_handling`, `high_risk` | "Chết rồi, túi 9kg mà Vietjet cho có 7kg, đang đứng ở sân bay luôn!" | Khẩn cấp, hoảng sợ | Cảnh báo đỏ, gợi ý vứt đồ cấm/nặng, khuyên thuê đồ ở đích | high-risk |
| A06 | C03 | `overweight_baggage`, `emergency_handling`, `high_risk` | "Vali lố mất 2kg rồi, bay hãng cấm đem chất lỏng nữa, tính sao giờ?" | Bối rối | Hướng dẫn loại chất lỏng, đưa đồ nặng ra mặc lên người | high-risk |
| A07 | C04 | `missing_context`, `emergency_handling`, `high_risk` | "Đang ra sân bay, quăng vội gì vào balo để lên núi luôn không?" | Gấp gáp | Hỏi nhanh điểm đến, tạo list sinh tồn tối thiểu (nước, sạc, áo) | challenge |
| A08 | C04 | `missing_context`, `emergency_handling`, `high_risk` | "Trễ giờ rồi, cần đi luôn trong 30p nữa, soạn list khẩn đi!" | Ngắn, vội vàng | Yêu cầu xác nhận đi đâu, tạo ngay checklist tối giản nhất | challenge |
| A09 | C05 | `overweight_baggage`, `update_context`, `medium_risk` | "Nãy lỡ nhét thêm 3 đôi giày, hình như lố cân xách tay rồi thì phải." | Trình bày dài dòng | Báo lố cân, tạo link gợi ý mua gói hành lý (không tự mua) | representative |
| A10 | C05 | `overweight_baggage`, `update_context`, `medium_risk` | "Vali hơi nặng do có quà lưu niệm, chắc lố mất 7kg rồi." | Bình thường | Báo lố cân nhẹ, gợi ý lên mạng mua hành lý ký gửi | representative |
| A11 | C06 | `sudden_weather_change`, `request_checklist`, `high_risk` | "Lên kế hoạch đi trekking núi tuyết ngày mai, cho list đồ đi." | Ngắn gọn | Cảnh báo thời tiết nguy hiểm, buộc thêm đồ bảo hộ chuyên dụng | high-risk |
| A12 | C06 | `sudden_weather_change`, `request_checklist`, `high_risk` | "Checklist đi biển Nha Trang cuối tuần này, hình như bão đổ bộ đó." | Casual | Cảnh báo bão, đề xuất hoãn chuyến đi hoặc list đồ sinh tồn | high-risk |
| A13 | C07 | `overweight_baggage`, `request_checklist`, `low_risk` | "Đi Thái bay Vietjet không ký gửi, soạn gọn gọn 7kg thôi nha." | Rõ ràng, cụ thể | Lên list đồ minimalist, ưu tiên đồ mỏng, đồ chiết | representative |
| A14 | C07 | `overweight_baggage`, `request_checklist`, `low_risk` | "Mình đi phượt gọn nhẹ lắm, thiết kế checklist balo nhỏ gọn nhất có thể." | Dài dòng | Tạo list đồ đa năng, quần áo mau khô, không rườm rà | representative |
| A15 | C08 | `missing_context`, `update_context`, `medium_risk` | "Cho thêm đôi giày cao gót vào vali đi leo núi luôn." | Ngắn gọn | Hỏi ngược lại về độ hợp lý ("Bạn đi leo núi, giày cao gót có an toàn?") | representative |
| A16 | C08 | `missing_context`, `update_context`, `medium_risk` | "Mình muốn đem theo cái máy sấy tóc to đùng đi Đà Nẵng." | Cảm xúc | Khuyên ks có sẵn máy sấy, có chắc muốn mang cho nặng không | representative |
| A17 | C09 | `sudden_weather_change`, `emergency_handling`, `medium_risk` | "Tối nay bão vào, đồ đang soạn vầy ra sân bay có ổn không?" | Lo lắng | Cảnh báo có thể delay chuyến bay, hỏi có đem đồ ngủ lại sân bay không | challenge |
| A18 | C09 | `sudden_weather_change`, `emergency_handling`, `medium_risk` | "Bão sắp tới, đi xe máy lên Đà Lạt mặc gì, soạn đồ lại dùm." | Casual | Khuyên cân nhắc lịch trình vì nguy hiểm, đề xuất áo mưa chuyên dụng | challenge |
| A19 | C10 | `overweight_baggage`, `emergency_handling`, `low_risk` | "Quá có 200 gram xách tay à, chắc không sao đâu nhỉ, hay bỏ bớt gì ra?" | Vòng vo, phân vân | Khuyên nên an toàn, đề nghị bỏ 1 chai sữa tắm hoặc áo phông thừa | representative |
| A20 | C10 | `overweight_baggage`, `emergency_handling`, `low_risk` | "Cân lố có 300g, thôi bỏ bớt cái quần cộc ra là vừa ha?" | Tự quyết định | Đồng tình, hệ thống cập nhật thanh đo khối lượng về mức xanh an toàn | representative |

---

## 7. Coverage Note Cá Nhân

**Tự đánh giá:**
- Dataset cá nhân đang cover rất tốt các kịch bản về **sự cố khẩn cấp (Emergency)** liên quan đến ranh giới trọng lượng hành lý (bị lố cân ở các mức độ khác nhau) và sự kiện thay đổi thời tiết đột ngột. 
- Lát cắt chưa được cover sâu là quá trình **Onboarding thiết lập ban đầu** (vì mục tiêu lát cắt này muốn thử nghiệm sức chịu đựng của AI ở luồng Recovery - phục hồi sau lỗi).
- Cố tình chưa chọn tổ hợp `low_risk` + `missing_context` + `update_context` vì kịch bản này AI chỉ việc lặng lẽ thêm/bớt đồ lặt vặt (Act), không có quá nhiều risk/ambiguity để test khả năng phản hồi thông minh.
- **Input high-risk nhất:** Các câu A05, A06 thuộc tổ hợp C03 (quá cân nặng sắp bay, vi phạm ranh giới an ninh) đòi hỏi AI phải rất quyết đoán.
- **Input là boundary case khó nhất:** Các câu A19, A20 thuộc tổ hợp C10 (quá cân rất nhẹ 200-300g). Nó đặt ra ranh giới liệu AI có quá cứng nhắc hay linh hoạt khuyên bỏ bớt một món đồ không đáng kể.
