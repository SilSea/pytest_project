import os
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# กำหนด Path Assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

# กำหนด Path TestSheet
TEST_SHEET_PATH = os.path.realpath('testsheet_lab.xlsx')

# กำหนด Path Test_Scenario
TEST_SCENARIO_PATH = os.path.join('test_scenario')

# กำหนด Path Module
MODULE_PATH = os.path.join('module')

# สร้าง Function เข้าถึง Assets
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# สร้าง Window ขึ้นมา
window = Tk()

# Window Title
window.title("Project สิ้นใจ")

# กำหนดขนาด Window
window_width = 900
window_height = 500

# คำนวณตำแหน่ง x, y ให้อยู่กลางจอ
screen_width = window.winfo_screenwidth()  # ความกว้างของหน้าจอ
screen_height = window.winfo_screenheight()  # ความสูงของหน้าจอ

# คำนวณตำแหน่ง x, y ของหน้าต่างให้แสดงกลาง
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# กำหนดขนาดและตำแหน่งของ Window
window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Window Background
window.configure(bg = "#373838")

# ตั้งค่า Frame
canvas = Canvas(
    window,
    bg = "#373838", # สีพื้นหลัง
    height = 500, # ความสูง
    width = 900, # ความกว้าง
    bd = 0, # ความหนาของขอบของ widget
    highlightthickness = 0, # ความหนาของขอบ
    relief = "ridge" # ขอบ
)

# ปุ่ม Download Package
button_image_1 = PhotoImage( # โหลดภาพ
    file=relative_to_assets("button_1.png"))
# สร้างปุ่ม
button_1 = Button(
    image=button_image_1, # นำเข้ารูปภาพ
    command=lambda: subprocess.run(['python', MODULE_PATH + '/install.py']), # Event เมื่อกดปุ่ม
    highlightthickness = 0, # ความหนาของขอบ
    relief="ridge", # ขอบปุ่ม
    bg="black" # สีพื้นหลัง
)

# กำหนดลักษณะปุ่ม
button_1.place(
    x=40.0,
    y=125.0,
    width=250.0, # ความกว้าง
    height=250.0 # ความสูง
)

# ปุ่ม Run Test Scenario
button_image_2 = PhotoImage( # โหลดภาพ
    file=relative_to_assets("button_2.png"))
# สร้างปุ่ม
button_2 = Button(
    image=button_image_2, # นำเข้ารูปภาพ
    command=lambda: subprocess.run(['pytest', '-v', '--headed', TEST_SCENARIO_PATH]), # Event เมื่อกดปุ่ม
    highlightthickness = 0, # ความหนาของขอบ
    relief="ridge", # ขอบปุ่ม
    bg="black" # สีพื้นหลัง
)
# กำหนดลักษณะปุ่ม
button_2.place(
    x=325.0,
    y=125.0,
    width=250.0,
    height=250.0
)

# ปุ่ม OpenSheet
canvas.place(x = 0, y = 0)
button_image_3 = PhotoImage( # โหลดภาพ
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3, # นำเข้ารูปภาพ
    command=lambda: subprocess.run(['start', TEST_SHEET_PATH], shell=True), # Event เมื่อกดปุ่ม
    highlightthickness = 0, # ความหนาของขอบ
    relief="ridge", # ขอบปุ่ม
    bg="black" # สีพื้นหลัง
)
button_3.place(
    x=610.0,
    y=125.0,
    width=250.0,
    height=250.0
)

# กำหนด Header
canvas.create_rectangle(
    0.0,
    0.0,
    900.0,
    69.0,
    fill="#000000",
    outline="")

canvas.create_text(
    15.0,
    11.0,
    anchor="nw",
    text="Project สิ้นใจ",
    fill="#FFFFFF",
    font=("Sarabun", 36 * -1, "bold")
)

# กำหนด Footer
canvas.create_rectangle(
    0.0,
    431.0,
    900.0,
    500.0,
    fill="#000000",
    outline="")
canvas.create_text(
    25.0,
    439.0,
    anchor="nw",
    text="โปรดเมตตา นักศึกษา ตาดำๆ ด้วยครับ XD",
    fill="#FFFFFF",
    font=("Sarabun", 36 * -1, "bold")
)

window.resizable(False, False)
# เริ่มต้น loop ของ Tkinter
window.mainloop()
