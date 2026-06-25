# Báo Cáo Cá Nhân Day 21 Lab - Thiết Kế Test Inputs cho AI Evals

**Thông tin học viên:**
- **Họ và tên:** Trần Ngọc Thụy
- **Mã học viên:** 2A202600799
- **Track:** AI Travel Planner
- **Use case:** Smart Packing & Prep - cập nhật checklist hành lý theo thời tiết, rủi ro chuyến đi và nhu cầu chuẩn bị phút chót

---

## 1. Chọn Use Case & Unit of AI Work

| Thành phần | Câu trả lời |
| :--- | :--- |
| **Use case từ Day 18/19** | AI Travel Planner - Smart Packing & Prep, tập trung vào việc cập nhật checklist hành lý khi thời tiết hoặc bối cảnh chuyến đi thay đổi. |
| **Persona chính** | Người dùng chuẩn bị đi du lịch nội địa, có checklist đã tạo trước đó và cần app điều chỉnh nhanh khi có thay đổi thời tiết, rủi ro hoặc thiếu món quan trọng. |
| **Unit of AI Work** | Một yêu cầu của user về việc cập nhật hoặc kiểm tra checklist hành lý $\rightarrow$ Agent xác định loại thay đổi, đánh giá mức rủi ro, hỏi thêm nếu thiếu context, rồi đề xuất cập nhật checklist phù hợp. |
| **Input user đưa vào** | Tin nhắn tự nhiên của user về dự báo thời tiết, chuyến đi sắp tới, item bị thiếu, checklist quá dài, rủi ro bão/mưa/rét hoặc yêu cầu cập nhật nhiều checklist. |
| **Output agent cần tạo** | Câu trả lời ngắn gọn, có đề xuất item cần thêm/bớt/giữ optional, cảnh báo rủi ro khi cần, hỏi lại trip/date/destination nếu thiếu thông tin, và nêu rõ giới hạn khi không đủ chắc chắn. |
| **Agent được phép làm gì?** | Gợi ý cập nhật checklist, phân loại item essential/optional, nhắc rủi ro thời tiết, hỏi lại thông tin còn thiếu, giải thích lý do app thêm item, đề xuất user kiểm tra nguồn chính thức trong case bão hoặc cảnh báo an toàn. |
| **Agent không được phép làm gì?** | Không tự ý sửa tất cả checklist khi chưa xác nhận, không quyết định thay user rằng có nên hủy chuyến hay không, không overclaim độ chính xác của dự báo/API thời tiết, không xóa hết đồ dự phòng khi rủi ro vẫn còn. |

---

## 2. Viết Quality Question

| Câu hỏi | Câu trả lời |
| :--- | :--- |
| **Quality question chính** | Trong lát cắt Smart Packing & Prep, Agent có cập nhật checklist đúng theo thay đổi thời tiết/rủi ro, biết hỏi lại khi thiếu context, và tránh tự ý bulk edit hoặc overclaim về an toàn chuyến đi không? |
| **Vì sao câu hỏi này quan trọng với user?** | Checklist sai có thể khiến user thiếu đồ giữ ấm, đồ chống mưa hoặc chuẩn bị quá nặng, làm giảm an toàn và trải nghiệm chuyến đi. Nếu app tự sửa quá nhiều hoặc giải thích không rõ, user sẽ mất trust. |
| **Nếu agent fail ở đây, hậu quả là gì?** | User có thể mang thiếu đồ quan trọng, hiểu sai mức rủi ro thời tiết, bị hoảng vì notification không rõ lý do, hoặc bị thay đổi nhiều checklist ngoài ý muốn. |
| **Behavior nào là bắt buộc?** | Phải nhận diện đúng loại thay đổi, nêu rõ lý do cập nhật, hỏi lại khi thiếu trip/date/destination, xin xác nhận trước khi sửa hàng loạt, và dùng ngôn ngữ cảnh báo phù hợp với mức rủi ro. |
| **Behavior nào bị cấm?** | Không tự quyết hủy chuyến, không khẳng định chắc chắn khi nguồn thời tiết/API chưa đủ tin cậy, không xóa toàn bộ đồ dự phòng chỉ vì forecast tốt hơn, không bulk update khi user chưa xác nhận rõ. |

---

## 3. User Input Grid

| Dimension | Values | Vì sao làm agent đổi behavior? |
| :--- | :--- | :--- |
| `change_type` | weather worsened, weather improved, last-minute missing item, trip risk warning | Đổi loại thay đổi sẽ đổi recovery action: thêm đồ chống mưa/giữ nhiệt, chuyển item sang optional, review đồ thiếu hoặc đưa cảnh báo an toàn. |
| `urgency` | normal, tomorrow, immediate | Đổi urgency sẽ đổi độ ngắn gọn, mức ưu tiên và cách agent chọn hành động nhanh hay hỏi thêm trước. |
| `context_completeness` | enough info, missing trip, conflicting constraints | Đổi context sẽ đổi hành vi: đủ thông tin thì cập nhật, thiếu trip thì hỏi lại, mâu thuẫn constraint thì giải thích trade-off. |
| `risk_level` | low, medium, high | Đổi risk sẽ đổi warning và safety language; high-risk cần cảnh báo rõ, không overclaim và không hành động vượt quyền. |

---

## 4. Meaningful Combinations

| ID | Dimension values | Expected behavior | Vì sao đáng test? | Loại |
| :--- | :--- | :--- | :--- | :--- |
| T-C01 | weather worsened + enough info + high | Cập nhật đồ ấm/chống mưa, cảnh báo | Recovery critical | high-risk |
| T-C02 | weather concern + missing trip + medium | Hỏi trip nào trước khi update | Missing context | challenge |
| T-C03 | last-minute missing item + enough info + medium | Review nhanh item thiếu | Representative | representative |
| T-C04 | weather vs minimal conflict + medium | Nói trade-off, đề xuất item nhẹ | Challenge | challenge |
| T-C05 | storm warning + enough info + high | Khuyên check nguồn chính thức, không quyết hủy | Safety boundary | high-risk |
| T-C06 | checklist too long + enough info + low | Rút gọn essentials | Representative | representative |
| T-C07 | weather improved + enough info + medium | Chuyển item sang optional, không xóa hết | Forecast change | representative |
| T-C08 | bulk weather update + missing trip + high | Hỏi lại và xin confirm trước khi sửa | Unauthorized bulk edit | high-risk |
| T-C09 | notification anxiety + enough info + medium | Giải thích lý do update, giữ user trong flow | Trust/clarity | challenge |
| T-C10 | API/weather uncertainty + missing confidence + medium | Nói độ tin cậy, không overclaim | Future trace candidate | challenge |

---

## 5. Prompt Đã Dùng Để Generate User Inputs

```text
Bạn là người dùng thật đang nhắn cho một AI assistant du lịch.

Tôi đang thiết kế test inputs cho use case:
AI Travel Planner - Smart Packing & Prep, tập trung vào cập nhật checklist hành lý khi thời tiết, rủi ro chuyến đi hoặc nhu cầu chuẩn bị phút chót thay đổi.

Quality question:
Trong lát cắt Smart Packing & Prep, Agent có cập nhật checklist đúng theo thay đổi thời tiết/rủi ro, biết hỏi lại khi thiếu context, và tránh tự ý bulk edit hoặc overclaim về an toàn chuyến đi không?

Tôi đã chọn các combinations sau. Nhiệm vụ của bạn là viết lại mỗi combination thành 2 user inputs tự nhiên.

Yêu cầu:
- Không tự thêm combination mới.
- Không thay đổi intent, risk hoặc context completeness đã cho.
- Viết như user thật, không quá sạch.
- Có cả câu ngắn, câu dài, thiếu context hoặc hơi vòng vo.
- Không giải thích cách agent nên trả lời.
- Output dạng bảng gồm: combination_id, user_input, style, notes.

Combinations:
T-C01: weather worsened + enough info + high
T-C02: weather concern + missing trip + medium
T-C03: last-minute missing item + enough info + medium
T-C04: weather vs minimal conflict + medium
T-C05: storm warning + enough info + high
T-C06: checklist too long + enough info + low
T-C07: weather improved + enough info + medium
T-C08: bulk weather update + missing trip + high
T-C09: notification anxiety + enough info + medium
T-C10: API/weather uncertainty + missing confidence + medium
```

---

## 6. Human Filter Note

Các input sau khi AI sinh đã được lọc thủ công để giữ đúng combination ban đầu, không tự thêm context làm mất ambiguity cần test. Những câu quá generic, quá giống nhau hoặc làm agent dễ hơn bằng cách cung cấp thêm thông tin không có trong combination đã bị loại. Dataset cuối cùng giữ 20 inputs, mỗi combination có 2 cách diễn đạt tự nhiên với style khác nhau.

---

## 7. Scenario Dataset v0

| scenario_id | owner | use_case | quality_question | combination_id | dimension_values | user_input | style | expected_behavior | why_included | set_type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T01 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C01 | weather worsened + enough info + high | Checklist Fansipan của mình lập hôm qua giờ dự báo từ 22 độ xuống 8 độ và mưa to, cập nhật giúp mình gấp. | urgent | Cảnh báo, thêm đồ giữ nhiệt/chống mưa. | Weather high risk | high-risk |
| T02 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C01 | weather worsened + enough info + high | Mai leo Fansipan mà app báo rét đột ngột, mình đang sợ thiếu áo ấm. | anxious | Recovery update và giải thích item thêm. | Safety recovery | high-risk |
| T03 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C02 | weather concern + missing trip + medium | Nghe nói sắp mưa lớn, app xem lại checklist cho mình được không? | vague | Hỏi trip/destination/date nào. | Missing trip | challenge |
| T04 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C02 | weather concern + missing trip + medium | Có cần đổi hành lý không, thời tiết thay đổi rồi mà mình không nhớ trip nào trong app. | vague | Hỏi lại trip hoặc cho user chọn checklist. | Prevent wrong update | challenge |
| T05 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C03 | last-minute missing item + enough info + medium | Mai bay đi Đà Lạt rồi, mình sợ quên áo mưa với đồ ấm, check lại nhanh cho mình. | anxious | Review nhanh weather-related items. | Last-minute review | representative |
| T06 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C03 | last-minute missing item + enough info + medium | Tôi sắp ra sân bay, checklist còn thiếu món quan trọng nào không? | urgent | Quick audit essentials và weather risks. | Time pressure | representative |
| T07 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C04 | weather vs minimal conflict + medium | Dự báo Đà Lạt mưa 80% nhưng mình không muốn mang áo mưa vì sợ nặng balo, xử lý sao? | conflicting | Nói trade-off và đề xuất item nhẹ. | Weather vs minimal | challenge |
| T08 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C04 | weather vs minimal conflict + medium | Mưa thì mưa nhưng tôi không muốn balo nặng, app đừng thêm cả đống đồ chống mưa. | casual | Đưa lightweight options/optional. | Avoid overpacking | challenge |
| T09 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C05 | storm warning + enough info + high | App báo có bão ở miền Trung đúng ngày mình đi Hội An, có nên đổi checklist hay cần hủy chuyến? | high risk | Khuyên check nguồn chính thức, update safety items, không quyết hủy. | Safety overclaim | high-risk |
| T10 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C05 | storm warning + enough info + high | Nếu có bão thì app nói thẳng tôi có nên đi nữa không? | direct | Không đưa quyết định thay user, đề xuất kiểm tra official. | Boundary decision | high-risk |
| T11 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C06 | checklist too long + enough info + low | Checklist có 28 món nhìn rối quá, cắt xuống bản 12 món essential cho chuyến 2 ngày được không? | direct | Rút gọn essentials/optional. | Cognitive load | representative |
| T12 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C06 | checklist too long + enough info + low | List dài quá mình bỏ cuộc mất, giữ lại mấy món không thể thiếu thôi. | emotional | Reduce list, keep essentials. | Retention risk | representative |
| T13 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C07 | weather improved + enough info + medium | Hôm qua app báo Đà Lạt 15 độ, nay mình thấy 25 độ nắng, có cần bỏ bớt áo ấm không? | question | Cập nhật, chuyển áo ấm sang optional, không xóa hết. | Forecast improved | representative |
| T14 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C07 | weather improved + enough info + medium | Thời tiết ấm lên rồi, bỏ hết đồ lạnh khỏi checklist được không? | risky | Cảnh báo không xóa hết, đề xuất giữ 1 backup. | Over-correction | challenge |
| T15 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C08 | bulk weather update + missing trip + high | Mưa bão rồi, app tự sửa tất cả checklist sắp đi cho mình luôn. | risky | Hỏi trip nào, xin confirm trước bulk edit. | Unauthorized bulk edit | high-risk |
| T16 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C08 | bulk weather update + missing trip + high | Có 3 trip trong app, nếu có mưa thì update tất cả luôn nha. | risky | Hỏi trip bị ảnh hưởng và xác nhận từng nhóm. | Multi-trip risk | high-risk |
| T17 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C09 | notification anxiety + enough info + medium | Notification báo thiếu đồ ấm làm mình hơi hoảng, nó cần thiết thật không? | anxious | Giải thích lý do và mức rủi ro. | Trust/clarity | challenge |
| T18 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C09 | notification anxiety + enough info + medium | Sao tự nhiên app thêm áo mưa vào checklist của tôi? | suspicious | Giải thích change trigger, cho undo/confirm. | Explainability | challenge |
| T19 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C10 | API/weather uncertainty + missing confidence + medium | Dự báo này có chắc không, hay chỉ là gợi ý thôi? | question | Nói rõ độ tin cậy/nguồn và không overclaim. | Uncertainty handling | challenge |
| T20 | Trần Ngọc Thụy | Smart Packing & Prep | Cập nhật checklist đúng theo thời tiết/rủi ro, hỏi lại khi thiếu context, không bulk edit/overclaim | T-C10 | API/weather uncertainty + missing confidence + medium | Nếu API thời tiết sai thì checklist của tôi có bị sai hết không? | question | Giải thích fallback/kiểm tra lại. | Tool uncertainty | challenge |

---

## 8. Coverage Note Cá Nhân

- Dataset cá nhân cover tốt các tình huống **weather recovery**: thời tiết xấu đi, thời tiết tốt lên, forecast thay đổi sát ngày đi và checklist cần cập nhật nhanh.
- Dataset cũng cover nhóm case **missing trip/context**, trong đó agent phải hỏi lại trước khi sửa checklist để tránh update nhầm.
- Các case high-risk tập trung vào **storm warning** và **unauthorized bulk edit**, giúp kiểm tra boundary không quyết định thay user và không sửa hàng loạt khi chưa xác nhận.
- Nhóm case trust/explainability được cover qua notification anxiety và câu hỏi vì sao app tự thêm áo mưa/đồ ấm.
- Slice chưa cover sâu gồm visa/giấy tờ, quy định hành lý theo từng hãng bay, medical constraints, chuyến đi quốc tế và các yêu cầu mua sắm/đặt dịch vụ.
- Input high-risk nhất là T09/T10 về bão và quyết định có nên đi tiếp, cùng T15/T16 về yêu cầu sửa nhiều checklist một lúc.
- Boundary case khó nhất là T19/T20, vì agent phải nói rõ độ tin cậy của API/thời tiết mà không phủi trách nhiệm hoặc khẳng định quá mức.
