import pywhatkit
import pyautogui
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

today = date.today()

varDateDMY= today.strftime("%d-%m-%Y")

strImagePath =  "C:\\Users\\Armandp\\Desktop\\projects\\CFPR-Daily-Report\\" + varDateDMY + ".jpg"

PATH = "C:\\Program Files (x86)\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.maximize_window()

driver.get("http://mpv.cofopri.gob.pe/Consultas/FrmConsultaEstado.aspx")

link = driver.find_element_by_id("ContentPlaceHolder1_TxtNroExpediente")
link.send_keys("***")
link.send_keys(Keys.RETURN)

time.sleep(10)

myScreenshot = pyautogui.screenshot()
myScreenshot.save(strImagePath)

driver.close()

pywhatkit.sendwhatmsg_instantly("***", "Hola.  Reporte de Cofopri. Saludos. S.A.R.A")

pywhatkit.sendwhats_image("***", strImagePath)