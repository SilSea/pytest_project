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
sheetName = "login01"

# Login with valid username and valid password and valid national-ID
def test_login01_pos01(page: Page):
    # กำหนดชื่อ TestCase
    testCase = "pos01"
    # กำหนดชื่อ Image
    nameImage = sheetName + '_' + testCase + ".png"

    # กำหนดเว็ปทดสอบ
    page.goto("https://reg.rmutk.ac.th/registrar/login.asp")
    # กรอก Username, Password, National-ID
    page.locator('input[name="f_uid"]').fill("65502100005-5")
    page.locator('input[name="f_pwd"]').fill("1909802580627")
    page.locator('input[name="f_idcard"]').fill("1909802580627")
    page.locator('input[type="submit"][value=" เข้าสู่ระบบ "]').click()

    # Screenshot ภาพ
    images_path = os.path.join('images', nameImage)
    page.screenshot(path=images_path)

    # ตรวจสอบ PASS/FAILED
    try: # กรณี PASS
        assert page.wait_for_selector("text=เปลี่ยนรหัสผ่าน",timeout=5000).is_visible()
        testResult = 'PASS'
    except: # กรณี FAILED
        # แสดง GUI ถ้าผลลัพธ์ผิด
        start_gui("/" + nameImage)
        testResult = 'FAILED'
    
    # อัปเดต Excel ด้วยสถานะการทดสอบ
    update_excel_with_image(sheetName, testCase, testResult, images_path)
    # แสดง Failed
    if(testResult == "FAILED"):
        pytest.fail()

# Login with valid username and invalid password and invalid national-ID
def test_login01_neg01(page: Page):
    # กำหนดชื่อ TestCase
    testCase = "neg01"
    # กำหนดชื่อ Image
    nameImage = sheetName + '_' + testCase + ".png"

    # กำหนดเว็ปทดสอบ
    page.goto("https://reg.rmutk.ac.th/registrar/login.asp")
    # กรอก Username, Password, National-ID
    page.locator('input[name="f_uid"]').fill("65502100005-5")
    page.locator('input[name="f_pwd"]').fill("5555")
    page.locator('input[name="f_idcard"]').fill("5555")
    page.locator('input[type="submit"][value=" เข้าสู่ระบบ "]').click()

    # Screenshot ภาพ
    images_path = os.path.join('images', nameImage)
    page.screenshot(path=images_path)

    # ตรวจสอบ PASS/FAILED
    try: # กรณี PASS
        assert page.wait_for_selector("text=กรุณาป้อนรหัสประจำตัวและรหัสผ่านให้ถูกต้อง",timeout=5000).is_visible()
        assert error_message.evaluate('element => window.getComputedStyle(element).color') == "rgb(0,0,255)"
        testResult = 'PASS'
    except: # กรณี FAILED
        # แสดง GUI ถ้าผลลัพธ์ผิด
        start_gui("/" + nameImage)
        testResult = 'FAILED'
    
    # อัปเดต Excel ด้วยสถานะการทดสอบ
    update_excel_with_image(sheetName, testCase, testResult, images_path)
    # แสดง Failed
    if(testResult == "FAILED"):
        pytest.fail()

# Login with valid username and valid password and invalid national-ID
def test_login01_neg02(page: Page):
    # กำหนดชื่อ TestCase
    testCase = "neg02"
    # กำหนดชื่อ Image
    nameImage = sheetName + '_' + testCase + ".png"

    # กำหนดเว็ปทดสอบ
    page.goto("https://reg.rmutk.ac.th/registrar/login.asp")
    # กรอก Username, Password, National-ID
    page.locator('input[name="f_uid"]').fill("65502100005-5")
    page.locator('input[name="f_pwd"]').fill("1909802580627")
    page.locator('input[name="f_idcard"]').fill("5555")
    page.locator('input[type="submit"][value=" เข้าสู่ระบบ "]').click()

    # Screenshot ภาพ
    images_path = os.path.join('images', nameImage)
    page.screenshot(path=images_path)

    # ตรวจสอบ PASS/FAILED
    try: # กรณี PASS
        assert page.wait_for_selector("text=กรุณาป้อนรหัสประจำตัวและรหัสผ่านให้ถูกต้อง",timeout=5000).is_visible()
        testResult = 'PASS'
    except: # กรณี FAILED
        # แสดง GUI ถ้าผลลัพธ์ผิด
        start_gui("/" + nameImage)
        testResult = 'FAILED'
    
    # อัปเดต Excel ด้วยสถานะการทดสอบ
    update_excel_with_image(sheetName, testCase, testResult, images_path)
    # แสดง Failed
    if(testResult == "FAILED"):
        pytest.fail()

# Login with invalid username and valid password and valid national-ID
def test_login01_neg03(page: Page):
    # กำหนดชื่อ TestCase
    testCase = "neg03"
    # กำหนดชื่อ Image
    nameImage = sheetName + '_' + testCase + ".png"

    # กำหนดเว็ปทดสอบ
    page.goto("https://reg.rmutk.ac.th/registrar/login.asp")
    # กรอก Username, Password, National-ID
    page.locator('input[name="f_uid"]').fill("5555")
    page.locator('input[name="f_pwd"]').fill("1909802580627")
    page.locator('input[name="f_idcard"]').fill("5555")
    page.locator('input[type="submit"][value=" เข้าสู่ระบบ "]').click()

    # Screenshot ภาพ
    images_path = os.path.join('images', nameImage)
    page.screenshot(path=images_path)

    # ตรวจสอบ PASS/FAILED
    try: # กรณี PASS
        assert page.wait_for_selector("text=กรุณาป้อนรหัสประจำตัวและรหัสผ่านให้ถูกต้อง",timeout=5000).is_visible()
        testResult = 'PASS'
    except: # กรณี FAILED
        # แสดง GUI ถ้าผลลัพธ์ผิด
        start_gui("/" + nameImage)
        testResult = 'FAILED'
    
    # อัปเดต Excel ด้วยสถานะการทดสอบ
    update_excel_with_image(sheetName, testCase, testResult, images_path)
    # แสดง Failed
    if(testResult == "FAILED"):
        pytest.fail()

# Login with invalid username and invalid password and valid national-ID
def test_login01_neg04(page: Page):
    # กำหนดชื่อ TestCase
    testCase = "neg04"
    # กำหนดชื่อ Image
    nameImage = sheetName + '_' + testCase + ".png"

    # กำหนดเว็ปทดสอบ
    page.goto("https://reg.rmutk.ac.th/registrar/login.asp")
    # กรอก Username, Password, National-ID
    page.locator('input[name="f_uid"]').fill("5555")
    page.locator('input[name="f_pwd"]').fill("5555")
    page.locator('input[name="f_idcard"]').fill("1909802580627")
    page.locator('input[type="submit"][value=" เข้าสู่ระบบ "]').click()

    # Screenshot ภาพ
    images_path = os.path.join('images', nameImage)
    page.screenshot(path=images_path)

    # ตรวจสอบ PASS/FAILED
    try: # กรณี PASS
        assert page.wait_for_selector("text=กรุณาป้อนรหัสประจำตัวและรหัสผ่านให้ถูกต้อง",timeout=5000).is_visible()
        testResult = 'PASS'
    except: # กรณี FAILED
        # แสดง GUI ถ้าผลลัพธ์ผิด
        start_gui("/" + nameImage)
        testResult = 'FAILED'
    
    # อัปเดต Excel ด้วยสถานะการทดสอบ
    update_excel_with_image(sheetName, testCase, testResult, images_path)
    # แสดง Failed
    if(testResult == "FAILED"):
        pytest.fail()

# Login with invalid username and invalid password and invalid national-ID
def test_login01_neg05(page: Page):
    # กำหนดชื่อ TestCase
    testCase = "neg05"
    # กำหนดชื่อ Image
    nameImage = sheetName + '_' + testCase + ".png"

    # กำหนดเว็ปทดสอบ
    page.goto("https://reg.rmutk.ac.th/registrar/login.asp")
    # กรอก Username, Password, National-ID
    page.locator('input[name="f_uid"]').fill("5555")
    page.locator('input[name="f_pwd"]').fill("5555")
    page.locator('input[name="f_idcard"]').fill("5555")
    page.locator('input[type="submit"][value=" เข้าสู่ระบบ "]').click()

    # Screenshot ภาพ
    images_path = os.path.join('images', nameImage)
    page.screenshot(path=images_path)

    # ตรวจสอบ PASS/FAILED
    try: # กรณี PASS
        assert page.wait_for_selector("text=กรุณาป้อนรหัสประจำตัวและรหัสผ่านให้ถูกต้อง",timeout=5000).is_visible()
        testResult = 'PASS'
    except: # กรณี FAILED
        # แสดง GUI ถ้าผลลัพธ์ผิด
        start_gui("/" + nameImage)
        testResult = 'FAILED'
    
    # อัปเดต Excel ด้วยสถานะการทดสอบ
    update_excel_with_image(sheetName, testCase, testResult, images_path)
    # แสดง Failed
    if(testResult == "FAILED"):
        pytest.fail()