import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def install_requirements():
    requirements_path = os.path.join('requirement.txt')  # ระบุที่อยู่ไฟล์ requirements.txt

    # สร้างหน้าต่าง "กำลังโหลด..."
    loading_window = tk.Toplevel(root)
    loading_window.title("กำลังโหลด...")
    loading_window.geometry("300x100")  # กำหนดขนาดหน้าต่าง
    loading_window.resizable(False, False)  # ไม่ให้ปรับขนาด

    # คำนวณตำแหน่งให้อยู่กลางจอ
    loading_window.update_idletasks()
    screen_width = loading_window.winfo_screenwidth() # ความกว้างของหน้าจอ
    screen_height = loading_window.winfo_screenheight() # ความสูงของหน้าจอ

    # กำหนดขนาด Window
    window_width = 300
    window_height = 100

    # คำนวณตำแหน่ง x, y ของหน้าต่างให้แสดงกลาง
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)

    # กำหนดขนาดและตำแหน่งของ Window
    loading_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    # เพิ่มข้อความ
    label = tk.Label(loading_window, text="กำลังติดตั้งแพ็กเกจ...\nโปรดรอสักครู่", padx=20, pady=10)
    label.pack()

    loading_window.update()  # อัปเดต GUI ให้แสดงผลทันที

    # รันคำสั่งติดตั้ง pip
    result = subprocess.run(
        ['pip', 'install', '-r', requirements_path, '--no-input'],
        capture_output=True,
        text=True
    )

    # รันคำสั่ง playwright install
    result1 = subprocess.run(
        ['playwright', 'install'],
        capture_output=True,
        text=True
    )

    # ปิดหน้าต่างโหลด
    loading_window.destroy()

    # ตรวจสอบว่าการติดตั้งสำเร็จหรือไม่
    if result.returncode == 0 and result1.returncode == 0:
        messagebox.showinfo("สำเร็จ", "ติดตั้งแพ็กเกจเรียบร้อยแล้ว!")
    else:
        messagebox.showerror("ล้มเหลว", f"การติดตั้งล้มเหลว:\n{result.stderr}\n{result1.stderr}")

# สร้างหน้าต่าง tkinter
root = tk.Tk()
root.withdraw()  # ซ่อนหน้าต่างหลัก

# ติดตั้งแล้วแสดงข้อความ
install_requirements()