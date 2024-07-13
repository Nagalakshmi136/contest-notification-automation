# Import the libraries
from selenium import webdriver
from config import CHROME_PROFILE_PATH
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import leet_code,code_chef,code_forces,gfg,coding_ninjas
import time

# Initializing web browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(CHROME_PROFILE_PATH)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
# Fetching data from websites
leet_code_data = leet_code.get_data(driver)
gfg_data = gfg.get_data(driver)
code_chef_data = code_chef.get_data(driver)
code_forces_data = code_forces.get_data(driver)
coding_ninjas_data = coding_ninjas.get_data(driver) 
# Sending data to whats app
url = "https://web.whatsapp.com/"
driver.get(url)
wait = WebDriverWait(driver,500)
search_box_path = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
search_box = wait.until(EC.presence_of_element_located((By.XPATH,search_box_path)))
search_box.send_keys("Contests")
# target = '"Ipo"'
contact_path = '//span[@title="Contests"]'
contact = wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
contact.click()
input_field_path = '//div[@class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt"][@contenteditable="true"][@title="Type a message"][@data-tab="10"]'
input_field = wait.until(EC.presence_of_element_located((By.XPATH,input_field_path)))
if len(leet_code_data)!=0:
    input_field.send_keys("Leet Code: "+"  ".join(leet_code_data)+Keys.ENTER)
if len(gfg_data)!=0:
    input_field.send_keys("Gfg: "+"  ".join(gfg_data)+Keys.ENTER)
if len(code_chef_data)!=0:
    input_field.send_keys("Code Chef: "+"  ".join(code_chef_data)+Keys.ENTER)
if len(code_forces_data):
    input_field.send_keys("Code Force: "+"  ".join(code_forces_data)+Keys.ENTER)
if coding_ninjas_data != "-1":
    input_field.send_keys("Coding Ninjas: "+coding_ninjas_data+Keys.ENTER)
time.sleep(5)
driver.quit()
