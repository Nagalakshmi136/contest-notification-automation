from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from constants import CODE_CHEF
from datetime import datetime

def get_data(driver):
    driver.get(CODE_CHEF)
    wait = WebDriverWait(driver,500)
    contests = []
    all_contests = '//div[@class="_contest-tables__container_ioa8k_225"]/div[3]/div[2]/div/div/table/tbody/tr'
    no_of_contests = len(wait.until(EC.presence_of_all_elements_located((By.XPATH,all_contests))))
    for i in range(1,no_of_contests+1):
        contest_details = wait.until(EC.presence_of_all_elements_located((By.XPATH,f'//div[@class="_contest-tables__container_ioa8k_225"]/div[3]/div[2]/div/div/table/tbody/tr[{i}]/td')))
        contest_date = contest_details[2].text.replace('\n',' ')
        if int(contest_date.split(' ')[0]) == datetime.now().day:
            contests.append(contest_date)
    return contests

                
