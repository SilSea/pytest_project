import os
import subprocess

# กำหนด Path Gui
GUI_PATH = os.path.join('gui')

# เปิด GUI
subprocess.run(['python', GUI_PATH + '/setting.py'])