import tkinter as tk
import os
import subprocess
import sys
from tkinter import ttk
from PIL import Image, ImageTk

# สั่งติดตั้ง Package Excel Edit
subprocess.run(['pip', 'install', 'openpyxl', '-q', '--no-input'])

# ดึงที่อยู่ Module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'module')))
from excel_update import update_name_env

# กำหนด Path Gui
GUI_PATH = os.path.join('gui')

# กำหนด Path Icon
ICON_FILE = os.path.abspath("gui/assets/icon/icon.png")

# เมื่อกดปุ่ม
def on_submit(event=None):
    # ดึงข้อมูลจาก Dropdown และ ช่องกรอกข้อมูล
    testerName_value = entry.get()
    os_value = os_dropdown.get()
    browser_value = browser_dropdown.get()

    # ตรวจสอบว่าไฟล์ logs.txt มีอยู่หรือไม่
    setting_file_path = os.path.join('logs', 'setting.txt')
    # บันทึกข้อความลงในไฟล์
    with open(setting_file_path, "w", encoding="utf-8") as file:
        file.write(f"Tester Name: {testerName_value}\nOS: {os_value}\nBrowser: {browser_value}")

    # ปิดหน้าต่างหลังจากกดปุ่ม
    root.destroy()

    # อัพเดตข้อมูลลง Excel
    update_name_env()

    # เปิด GUI
    subprocess.run(['python', GUI_PATH + '/gui.py'])

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("ยินดีต้อนรับ")
root.geometry("400x250")
# โหลดไอคอนจากไฟล์ภาพที่ต้องการ (เช่น .png หรือ .jpg)
image = Image.open(ICON_FILE)
photo = ImageTk.PhotoImage(image)
# กำหนดไอคอนสำหรับหน้าต่าง
root.iconphoto(True, photo)

# ช่องกรอกชื่อ
entry_label = tk.Label(root, text="กรุณากรอกขื่อผู้ทดสอบ:")
entry_label.pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# ให้ cursor focus ที่ช่องกรอกข้อความ
entry.focus()

# Dropdown OS
os_dropdown_label = tk.Label(root, text="OS Test Environment:")
os_dropdown_label.pack(pady=5)
os_dropdown = ttk.Combobox(root, values=["Windows 10", "Windows 11", "Mac", "Linux"], state="readonly")
os_dropdown.pack(pady=5)
os_dropdown.current(0)  # ตั้งค่าเริ่มต้น

# Dropdown Browser
browser_dropdown_label = tk.Label(root, text="Browser Test Environment:")
browser_dropdown_label.pack(pady=5)
browser_dropdown = ttk.Combobox(root, values=["Chromium", "Firefox"], state="readonly")
browser_dropdown.pack(pady=5)
browser_dropdown.current(0)

# ปุ่มกดยืนยัน
submit_button = tk.Button(root, text="ยืนยัน", command=on_submit)
submit_button.pack(pady=10)

# เมื่อกด Enter จะเรียกฟังก์ชัน onsubmit
entry.bind("<Return>", on_submit)

# เริ่มโปรแกรม
root.mainloop()
