
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from constants import CODING_NINJAS
from datetime import datetime

def get_data(driver):
    driver.get(CODING_NINJAS)
    wait = WebDriverWait(driver,500)
    contest_paths = '//div[@class="ng-star-inserted"]/div/div[@class="timer-text-color"]'
    contest_details = wait.until(EC.presence_of_all_elements_located((By.XPATH,contest_paths)))
    contest_time = "-1"
    if int(contest_details[0].text)<16:
        contest_time = contest_details[0].text+contest_details[1].text
    return contest_time