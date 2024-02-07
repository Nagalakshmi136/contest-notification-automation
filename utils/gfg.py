from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from constants import GFG
import calendar
from datetime import datetime
def get_data(driver):
    today = datetime.now()
    driver.get(GFG)
    wait = WebDriverWait(driver,500)
    contest_paths = '//div[@id="eventsLanding_eachEventContainer__O5VyK"]/a'
    contests = wait.until(EC.presence_of_all_elements_located((By.XPATH,contest_paths)))
    contest_details = []
    for i in range(min(5,len(contests))):
        if 'Weekly' in contests[i].text:
            contest = contests[i].text.split('IST')[0].replace('\n',' ')
            contest_date = contest.split(',')[0].split(' ')
            if calendar.month_name[today.month] == contest_date[0] and today.day==int(contest_date[1]):
                contest_details.append(contest)
    return contest_details

            
