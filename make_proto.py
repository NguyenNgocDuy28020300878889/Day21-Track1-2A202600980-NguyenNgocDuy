import re

with open('onboarding.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the permission screen completely
content = re.sub(r'<!-- Screen 2: Permissions -->.*?<!-- Screen 3: Input', '<!-- Screen 3: Input', content, flags=re.DOTALL)

# 2. Change Welcome Screen button
content = re.sub(r'onclick="nextScreen\(\'screen-permissions\'\)">Tiếp tục', 'onclick="nextScreen(\'screen-input\')">Bắt đầu ngay', content)

# 3. Change Screen 3 (Input) back button
content = re.sub(r'onclick="prevScreen\(\'screen-permissions\'\)">Quay lại', 'onclick="prevScreen(\'screen-welcome\')">Quay lại', content)

# 4. Change Title of Screen 3
content = re.sub(r'<h1>Thông tin chuyến đi</h1>', '<h1>Thông tin chuyến đi (Tối giản)</h1>', content)

# 5. Add Contextual Permission to Checklist Screen
checklist_btn_insert = '''
                <div class="input-group" style="margin-top: 15px; padding: 15px; background: rgba(16, 185, 129, 0.1); border-left: 4px solid #10b981; border-radius: 4px;">
                    <p style="font-size: 13px; color: #10b981; font-weight: bold; margin-bottom: 8px;">Contextual Permission (Day 20)</p>
                    <p style="font-size: 14px; margin-bottom: 10px;">Dữ liệu thời tiết hiện tại đang dùng phỏng đoán. Bật GPS để lấy thời tiết chính xác tại vị trí của bạn.</p>
                    <button class="btn" style="background: white; color: #10b981; border: 1px solid #10b981; padding: 8px 12px; font-size: 13px;" onclick="alert('Đã cấp quyền GPS thành công!')">Cấp quyền GPS ngay</button>
                </div>

                <div class="btn-container" style="margin-top: 15px;">
'''
content = re.sub(r'<div class="btn-container" style="margin-top: 15px;">', checklist_btn_insert, content)

# 6. Change the final button to say Core Action
content = re.sub(r'Xác nhận checklist', 'Xác nhận checklist (Core Action)', content)

# Add "Redesign Day 20" label on the phone header
content = re.sub(r'<div class="header">', '<div class="header" style="position: relative;"><span style="position: absolute; top: 10px; right: 10px; font-size: 10px; background: #10b981; color: white; padding: 2px 6px; border-radius: 4px;">DAY 20 REDESIGN</span>', content)

with open('prototype_day20.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Created prototype_day20.html")
