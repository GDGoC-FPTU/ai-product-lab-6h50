from PIL import Image, ImageDraw, ImageFont

width, height = 1200, 800
bg = (255, 255, 255)
img = Image.new('RGB', (width, height), color=bg)
d = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype('arial.ttf', 18)
except IOError:
    font = ImageFont.load_default()

x, y = 60, 60
line_height = 40

steps = [
    '1. Tài xế báo sự cố sạc pin',
    '2. Hệ thống lấy vị trí + pin',
    '3. AI tạo draft hướng dẫn',
    '4. Dispatcher review & duyệt',
    '5. Gửi nháp hoặc dispatch mobile charger'
]

for i, step in enumerate(steps, start=1):
    d.rectangle((x-20, y-10, width-60, y+30), outline='black', width=2)
    d.text((x, y), f'{i}. {step}', fill='black', font=font)
    y += line_height + 40

footer = 'Bottleneck: Step 3 và 4 cần AI hỗ trợ + Human-in-the-loop để đảm bảo an toàn'
d.text((60, y + 40), footer, fill='black', font=font)
img.save('04-workflow-diagram.png')
