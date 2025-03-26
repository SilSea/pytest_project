import pytest
import os
import openpyxl
import sys
import time
from playwright.sync_api import Page

# ค้นหา input_actual เพื่อ Import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'gui')))
# ค้นหา excel_update เพื่อ Import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'module')))
from input_actual import start_gui
from excel_update import update_excel_with_image

# กำหนด SheetName
sheetName = "logout01"
# กำหนด Username, Password, National-ID, Invaild และ Vaild สำหรับทดสอบ
userName = "5555"
passWord = "5555"
nationalID = "5555"
inVaild = "5555" #กำหนดสำหรับข้อมูลผิด

# Login with valid username and valid password and valid national-ID
def test_logout01_pos01(page: Page):
    # กำหนดชื่อ TestCase
    testCase = "pos01"
    # กำหนดชื่อ Image
    nameImage = sheetName + '_' + testCase + ".png"

    # กำหนดเว็ปทดสอบ
    page.goto("https://reg.rmutk.ac.th/registrar/login.asp")
    # กรอก Username, Password, National-ID
    page.locator('input[name="f_uid"]').fill(userName)
    page.locator('input[name="f_pwd"]').fill(passWord)
    page.locator('input[name="f_idcard"]').fill(nationalID)
    page.locator('input[type="submit"][value=" เข้าสู่ระบบ "]').click()

    # กด logout
    page.locator('a:has-text("ถอยกลับ")').click
    page.locator('a:has-text("ออกจากระบบ")').click

    # รอ 3 วินาที
    time.sleep(2)

    # Screenshot ภาพ
    images_path = os.path.join('images', nameImage)
    page.screenshot(path=images_path)

    # ตรวจสอบ PASS/FAILED
    try: # กรณี PASS
        assert page.title() == "มหาวิทยาลัยเทคโนโลยีราชมงคลกรุงเทพ"
        testResult = 'PASS'
    except AssertionError: # กรณี FAILED
        # แสดง GUI ถ้าผลลัพธ์ผิด
        start_gui("/" + nameImage)
        testResult = 'FAILED'

    # อัปเดต Excel ด้วยสถานะการทดสอบ
    update_excel_with_image(sheetName, testCase, testResult, images_path)
