import tkinter as tk
import os
from tkinter import messagebox
from PIL import Image, ImageTk

# กำหนด Path Images
IMAGES_PATH = os.path.join('images')

# กำหนด Path Logs
LOGS_PATH = os.path.join('logs')

# กำหนด Path Icon
ICON_FILE = os.path.abspath("gui/assets/icon/icon.png")

# ฟังก์ชันสำหรับแสดงภาพตาม path ที่กำหนด
def display_image(imagesName):
    file_path = IMAGES_PATH + imagesName  # กำหนด path ของภาพที่นี่
    try:
        # โหลดภาพจาก Path Images
        image = Image.open(file_path)
        # ปรับขนาดภาพ
        image = image.resize((1000, 500), Image.Resampling.LANCZOS)
        # สร้างภาพลง GUI
        photo = ImageTk.PhotoImage(image)
        label_image.config(image=photo)
        label_image.image = photo  # เก็บการอ้างอิงให้ภาพไม่หาย
    except Exception as e:
        print("เกิดข้อผิดพลาด:", e)

# ฟังก์ชันสำหรับแสดงข้อความจากช่องกรอก และปิดหน้าต่างหลังจากกดปุ่ม
def show_text(event=None):

    # รับข้อความจากช่องกรอก
    entered_text = entry.get("1.0", tk.END).strip()

    # ตรวจสอบว่าไฟล์ logs.txt มีอยู่หรือไม่
    log_file_path = os.path.join(LOGS_PATH, "logs.txt")

    # บันทึกข้อความลงในไฟล์
    with open(log_file_path, "w", encoding="utf-8") as file:
        file.write(entered_text)  # เขียนข้อความที่กรอกลงในไฟล์

    # แสดงข้อความว่าอัปเดตข้อมูลแล้ว
    messagebox.showinfo("สำเร็จ", "อัปเดตข้อมูลแล้ว")

    # ปิดหน้าต่างหลังจากกดปุ่ม
    root.destroy()

def start_gui(imagesName):
    # สร้างหน้าต่างหลัก
    global root
    # สร้าง Window ขึ้นมา
    root = tk.Tk()
    # Window Title
    root.title("กรุณากรอกค่า Actual ที่เกิดขึ้น")
    # โหลดไอคอนจากไฟล์ภาพที่ต้องการ (เช่น .png หรือ .jpg)
    image = Image.open(ICON_FILE)
    photo = ImageTk.PhotoImage(image)
    # กำหนดไอคอนสำหรับหน้าต่าง
    root.iconphoto(True, photo)

    # เปิดหน้าต่างมาเต็มจอ
    root.state('zoomed')  # เปิดมาเต็มหน้าจอ

    # ทำให้หน้าต่างเด้งขึ้นมาเป็นหน้าต่างหลักสุด
    root.attributes("-topmost", 1)
    root.lift()

    # Label สำหรับแสดงข้อความด้านบน
    label_text = tk.Label(root, text="กรุณากรอกค่า Actual ที่เกิดขึ้น", font=("Sarabun", 24, "bold"))
    label_text.pack(pady=10)

    # Label สำหรับแสดงภาพ
    global label_image
    label_image = tk.Label(root)
    label_image.pack(pady=10)

    # เรียกใช้ฟังก์ชันแสดงภาพทันทีที่เริ่มโปรแกรม
    display_image(imagesName)

    # สร้างช่องกรอกข้อความ และปรับขนาดตัวอักษร
    global entry
    entry = tk.Text(root, width=40, height=3, font=("Sarabun", 32))  # ขนาดตัวอักษร 32
    entry.pack(pady=10)

    # ให้ cursor focus ที่ช่องกรอกข้อความ
    entry.focus()

    # สร้างปุ่มสำหรับแสดงข้อความ และปรับขนาด
    btn_show = tk.Button(root, text="อัปเดตค่า Actual", command=show_text, height=3, width=20, font=("Sarabun", 16, "bold"))  # ขนาดปุ่มใหญ่ขึ้น
    btn_show.pack(pady=10)

    # เมื่อกด Enter จะเรียกฟังก์ชัน show_text
    entry.bind("<Return>", show_text)

    # เริ่มโปรแกรม Tkinter
    root.wait_window(root)
