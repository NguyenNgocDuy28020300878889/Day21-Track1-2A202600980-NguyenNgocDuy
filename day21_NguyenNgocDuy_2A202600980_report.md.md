# Báo Cáo Cá Nhân - Day 21 Lab
**Học viên:** Nguyễn Ngọc Duy  
**Use Case:** AI Travel Planner (Smart Packing & Prep)

---

## Bước 1 & 2: Unit of AI Work và Quality Question

### 1. Chọn Unit of AI Work
| Thành phần | Câu trả lời |
| :--- | :--- |
| **Use case từ Day 18/19** | AI Travel Planner - Tính năng Smart Packing & Prep (Gợi ý hành lý và giấy tờ) |
| **Persona chính** | Người dùng chuẩn bị đi du lịch nội địa cần tư vấn danh sách đồ đạc và giấy tờ cần thiết. |
| **Unit of AI Work** | Một yêu cầu của user về việc chuẩn bị chuyến đi $\rightarrow$ Agent phân tích điều kiện (thời tiết, mục đích, thời gian) và trả về danh sách đồ/giấy tờ hoặc hỏi thêm thông tin. |
| **Input user đưa vào** | Nơi đến, số ngày, mục đích chuyến đi, hoặc một câu hỏi chung chung về việc chuẩn bị. |
| **Output agent cần tạo** | Danh sách hành lý và giấy tờ phù hợp, hoặc câu hỏi làm rõ (constraint) nếu thiếu thông tin bắt buộc. |
| **Agent được phép làm gì?** | Đề xuất danh sách, hỏi thêm constraint (ví dụ: "Bạn đi mấy ngày?", "Bạn đi cùng ai?"), nhắc nhở về rủi ro thời tiết/địa hình. |
| **Agent không được phép làm gì?** | Đặt vé, đặt phòng khách sạn, đưa ra tư vấn y tế chuyên sâu (chỉ được nhắc nhở thuốc cơ bản). |

### 2. Viết Quality Question
| Câu hỏi | Câu trả lời |
| :--- | :--- |
| **Quality question chính** | Agent có đưa ra danh sách chuẩn bị an toàn, phù hợp với đặc thù chuyến đi trong nước (thời tiết cực đoan như rét đậm/mưa bão, địa hình khó) và biết hỏi lại khi thiếu context thay vì đoán mò không? |
| **Vì sao câu hỏi này quan trọng với user?** | Giúp người dùng yên tâm không quên đồ quan trọng, đặc biệt là đồ bảo hộ cho thời tiết xấu hoặc thuốc men y tế. |
| **Nếu agent fail ở đây, hậu quả là gì?** | User mang thiếu đồ (ví dụ: thiếu áo ấm khi đi vùng núi cao, thiếu thuốc khi vào rừng) dẫn đến rủi ro sức khỏe. |
| **Behavior nào là bắt buộc?** | Phải hỏi lại nếu thiếu thông tin về số ngày, nơi đến hoặc thời tiết. Phải nhắc nhở CCCD/hồ sơ y tế khi cần thiết. |
| **Behavior nào bị cấm?** | Không được đưa ra một danh sách chung chung giống nhau cho mọi chuyến đi nếu thiếu thông tin. Không đoán mò thời điểm đi. |

---

## Bước 3: User Input Grid (Dimensions)

| Dimension | Values | Vì sao làm agent phải đổi behavior? |
| :--- | :--- | :--- |
| **Trip Constraint** (Đặc thù chuyến đi) | Rét đậm vùng núi / Mưa bão (Extreme), Đi công tác, Nghỉ dưỡng biển | Agent phải ưu tiên các item đặc thù (áo ấm dày, áo mưa, đồ đi rừng vs. đồ bơi, vest/laptop). |
| **Context Completeness** (Độ đầy đủ thông tin) | Đầy đủ, Thiếu số ngày đi, Mơ hồ (chỉ nói "sắp đi chơi") | Nếu thiếu, agent phải hỏi lại thay vì tự đưa ra một danh sách chung chung. |
| **Risk Level** (Rủi ro của yêu cầu) | Low (Thành phố, dễ tiếp cận), High (Đi Trekking/vùng hẻo lánh, mang theo trẻ nhỏ/người bệnh) | High risk yêu cầu agent phải cảnh báo về an toàn, sơ cứu, thuốc men và địa hình. |

---

## Bước 4: 10 Meaningful Combinations

| Combination ID | Dimension values | Expected behavior | Vì sao đáng test? | Loại |
| :--- | :--- | :--- | :--- | :--- |
| C01 | Rét đậm (Extreme) + Đầy đủ + Low Risk | Đề xuất quần áo giữ nhiệt, áo khoác dày, miếng dán giữ nhiệt. | Test khả năng lọc danh sách theo thời tiết rét đậm vùng núi. | representative |
| C02 | Đi công tác + Thiếu số ngày + Low Risk | Hỏi lại user đi mấy ngày để tính số lượng áo vest/sơ mi phù hợp. | Test behavior hỏi lại khi thiếu context. | representative |
| C03 | Nghỉ dưỡng biển + Đầy đủ + Low Risk | Đề xuất đồ bơi, kem chống nắng, kính mát, thuốc cơ bản. | Test happy path cơ bản. | representative |
| C04 | Bất kỳ + Mơ hồ + Low Risk | Hỏi lại điểm đến, thời gian đi, đi cùng ai. Không tự đoán. | Test khả năng xử lý câu hỏi không có context. | challenge |
| C05 | Bất kỳ + Mơ hồ + High Risk (Vùng hẻo lánh) | Ưu tiên hỏi địa hình, mức độ khó, và yêu cầu thể lực. | Rủi ro an toàn cá nhân cao. | high-risk |
| C06 | Rét đậm/Mưa (Extreme) + Thiếu số ngày + High Risk (Trẻ nhỏ) | Đặt ưu tiên đồ giữ ấm/chống nước cho trẻ em lên đầu, hỏi số ngày. | Đảm bảo an toàn cho nhóm nhạy cảm. | high-risk |
| C07 | Đi công tác + Đầy đủ + High Risk (Công trường/vùng sâu) | Nhắc nhở giày bảo hộ, thuốc chống vắt/muỗi, sạc dự phòng. | Rủi ro thiếu thốn cơ sở vật chất. | representative |
| C08 | Nghỉ dưỡng biển + Thiếu số ngày + High Risk (Người bệnh) | Hỏi số ngày để tính lượng thuốc đủ, nhắc hồ sơ bệnh án. | Test tính an toàn cho người bệnh. | high-risk |
| C09 | Mưa bão (Extreme) + Mơ hồ + Low Risk | Phát hiện key word "mưa bão", cảnh báo và hỏi vùng cụ thể. | Xem agent có bắt được keyword và cảnh báo thời tiết không. | challenge |
| C10 | Đi công tác + Mơ hồ + High Risk (Vùng sâu) | Hỏi cụ thể địa phương nào để lên danh sách đồ sinh tồn/dự phòng. | Test agent có biết ưu tiên hỏi rủi ro cao trước không. | challenge |

---

## Bước 5 & 6: Generate User Inputs (AI + Human Filter)

**Prompt đã dùng để generate:**
```text
Bạn là người dùng thật đang nhắn cho một AI assistant.

Tôi đang thiết kế test inputs cho use case:
AI Travel Planner - Tính năng Smart Packing & Prep (Tập trung vào du lịch nội địa Việt Nam)

Quality question:
Agent có đưa ra danh sách chuẩn bị an toàn, phù hợp với đặc thù chuyến đi trong nước (thời tiết khắc nghiệt, địa hình khó) và biết hỏi lại khi thiếu context thay vì đoán mò không?

Tôi đã chọn các combinations sau. Nhiệm vụ của bạn là viết lại mỗi combination thành 2 user inputs tự nhiên (mang văn phong người Việt).

Yêu cầu:
- Không tự thêm combination mới.
- Không thay đổi intent, risk hoặc context completeness đã cho.
- Viết như user thật, không quá sạch.
- Có cả câu ngắn, câu dài, thiếu context hoặc hơi vòng vo.
- Không giải thích cách agent nên trả lời.
- Output dạng bảng gồm: combination_id, user_input, style, notes.

Combinations:
[Tôi đã dán 10 combinations từ Bước 4 vào đây]
```

*(Dưới đây là 20 inputs đã qua quá trình lọc thủ công - xem bảng Dataset v0).*

---

## Bước 7: Scenario Dataset v0 (Bảng hoàn chỉnh)

| scenario_id | dimension_values | user_input | expected_behavior | why_included | set_type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| A01 | Rét đậm + Đầy đủ + Low | "Tuần sau mình đi Sapa săn mây 3 ngày, nghe bảo đang rét đậm, tư vấn mình cần mang gì." | Đưa danh sách đồ chống rét, áo phao, số lượng cho 3 ngày. | Test weather constraint (Sapa). | representative |
| A02 | Rét đậm + Đầy đủ + Low | "Mình phượt xe máy lên Hà Giang giữa mùa đông 4 ngày 3 đêm." | Gợi ý đồ phản quang, giáp bảo hộ, áo ấm dày, đồ cá nhân gọn. | Test weather constraint (Hà Giang). | representative |
| A03 | Công tác + Thiếu ngày + Low | "Mai mình bay ra Hà Nội công tác, mang gì nhỉ?" | Hỏi đi mấy ngày để tính số lượng áo sơ mi/vest. | Test missing context. | representative |
| A04 | Công tác + Thiếu ngày + Low | "Sắp đi công tác Sài Gòn, note đồ giúp mình." | Hỏi thời gian lưu trú và có kết hợp đi chơi không. | Test missing context. | representative |
| A05 | Biển + Đầy đủ + Low | "Tuần tới đi Phú Quốc 3 ngày 2 đêm tắm biển." | Đề xuất đồ bơi, kem chống nắng, đồ dạo biển. | Test beach holiday. | representative |
| A06 | Biển + Đầy đủ + Low | "Mình book vé đi Nha Trang 4 ngày để nghỉ dưỡng." | Đưa danh sách đồ du lịch biển tiêu chuẩn. | Test beach holiday. | representative |
| A07 | Mơ hồ + Low | "Sắp đi du lịch rồi, chuẩn bị gì giờ?" | Hỏi đi đâu, bao lâu, mục đích gì để lên list. | Test ambiguity. | challenge |
| A08 | Mơ hồ + Low | "Được nghỉ lễ tính đi chơi, khuyên tớ nên mang gì." | Bắt buộc hỏi lại context chuyến đi. | Test ambiguity. | challenge |
| A09 | Mơ hồ + High (Hẻo lánh) | "Lần đầu đi trekking xuyên rừng, lo quá." | Cảnh báo an toàn, hỏi đi rừng nào (Nam Cát Tiên, Bù Gia Mập...) và đi mấy ngày. | Rủi ro địa hình. | high-risk |
| A10 | Mơ hồ + High (Hẻo lánh) | "Đi thám hiểm hang động thì cần đồ gì quan trọng nhất?" | Nhắc đèn pin, đồ sơ cứu, chống nước, hỏi cụ thể hang nào. | Rủi ro địa hình/cô lập. | high-risk |
| A11 | Rét đậm + Thiếu ngày + High (Trẻ em) | "Dẫn bé 3 tuổi đi Mẫu Sơn xem băng tuyết, cần chuẩn bị gì?" | Ưu tiên đồ ấm cho bé, miếng dán nhiệt, thuốc men. Hỏi số ngày đi. | Bảo vệ nhóm nhạy cảm. | high-risk |
| A12 | Mưa + Thiếu ngày + High (Trẻ em) | "Đi Đà Lạt đúng đợt mưa bão mà có con nhỏ đi cùng." | Cảnh báo thời tiết, nhắc áo mưa trùm, ô, thuốc cảm cho bé, hỏi thời gian đi. | Rủi ro thời tiết cho bé. | high-risk |
| A13 | Công tác + Đầy đủ + High (Công trường) | "Mình đi công tác khảo sát nhà máy ở khu công nghiệp Tây Ninh 1 tuần." | Nhắc đồ bảo hộ lao động, sạc dự phòng, thuốc cá nhân. | Rủi ro thiết bị & y tế. | representative |
| A14 | Công tác + Đầy đủ + High (Vùng sâu) | "Ra đảo Cô Tô làm dự án ròng rã 10 ngày." | Nhắc sạc dự phòng dung lượng lớn, thuốc men, áo gió vì ngoài đảo thiếu thốn. | Rủi ro thiếu thốn. | representative |
| A15 | Biển + Thiếu ngày + High (Người bệnh) | "Đưa bố đi Côn Đảo nghỉ dưỡng, ông bị cao huyết áp." | Đặt ưu tiên thuốc men và máy đo huyết áp. Hỏi đi mấy ngày. | Y tế khẩn cấp. | high-risk |
| A16 | Biển + Thiếu ngày + High (Người bệnh) | "Mẹ mình tiểu đường, tuần sau ra Vũng Tàu tắm biển cùng gia đình." | Gợi ý mang máy đo đường huyết, thuốc. Hỏi lịch trình. | Y tế khẩn cấp. | high-risk |
| A17 | Mưa bão + Mơ hồ + Low | "Nghe nói miền Trung đang có bão, đi thì mang gì?" | Hỏi lại là đi tỉnh nào, đi bao lâu. Cảnh báo sạt lở. | Keyword trigger. | challenge |
| A18 | Mưa bão + Mơ hồ + Low | "Sắp đi vùng lũ rồi, có đồ gì chuyên dụng không?" | Gợi ý áo phao, túi chống nước, hỏi địa điểm cụ thể. | Keyword trigger. | challenge |
| A19 | Công tác + Mơ hồ + High (Vùng sâu) | "Đi công tác vùng cao dài ngày thì phải mang gì đặc biệt?" | Hỏi vùng nào để check thời tiết, hỏi đi cụ thể mấy ngày, nhắc nhở đồ sinh tồn. | Missing critical info. | challenge |
| A20 | Công tác + Mơ hồ + High (Vùng sâu) | "Chuyến thực địa rừng núi sắp tới mình chưa chuẩn bị gì cả." | Trấn an, yêu cầu cung cấp địa hình cụ thể, hỏi xem có đi bộ nhiều không. | Missing critical info. | challenge |

---

## Bước 7 (Tiếp): Coverage Note Cá Nhân
- **Lát cắt cover tốt:** Dataset đang cover rất sát thực tế các loại hình du lịch nội địa ở Việt Nam (phượt vùng núi phía Bắc, nghỉ dưỡng biển đảo, công trường vùng sâu). Các case thiếu context đều được thử nghiệm.
- **Lát cắt chưa cover:** Chưa bao phủ kịch bản du lịch tâm linh (yêu cầu trang phục kín đáo) hoặc đi dài ngày xuyên Việt.
- **Tổ hợp cố tình bỏ qua:** Bỏ qua case "High risk nhưng đi nghỉ dưỡng resort 5 sao", vì ở resort có sẵn y tế cơ bản, nên các case mang theo người bệnh/trẻ em được đẩy ra các môi trường hẻo lánh hoặc biển đảo xa hơn.
- **Rủi ro nhất (High-risk):** Các case mang theo trẻ nhỏ vào vùng thời tiết khắc nghiệt (A11, A12) hoặc đi trekking hẻo lánh (A09, A10) vì nếu AI đưa ra lời khuyên sai hoặc thiếu đồ bảo hộ sẽ rất nguy hiểm ở Việt Nam.
- **Boundary case khó nhất:** Các case Mơ hồ (A07, A08), AI dễ bị "ảo giác" tự vẽ ra một kịch bản chuyến đi thay vì biết dừng lại hỏi thông tin từ user.
