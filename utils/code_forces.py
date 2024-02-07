from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from constants import CODE_FORCES
from datetime import datetime

def get_data(driver):
    driver.get(CODE_FORCES)
    wait = WebDriverWait(driver,500)
    contests = []
    all_contests = '//div[@class="contestList"]/div[@class="datatable"]/div[6]/table/tbody/tr'
    no_of_contests = len(wait.until(EC.presence_of_all_elements_located((By.XPATH,all_contests))))
    for i in range(2,no_of_contests+1):
        contest_details = wait.until(EC.presence_of_all_elements_located((By.XPATH,f'//div[@class="contestList"]/div[@class="datatable"]/div[6]/table/tbody/tr[{i}]/td')))
        contest_date = contest_details[2].text
        if int(contest_date.split('/')[1]) == datetime.now().day:
            contests.append(contest_date)
    
    return contests

                
