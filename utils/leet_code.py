from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from constants import LEET_CODE

def get_data(driver):
    driver.get(LEET_CODE)
    wait = WebDriverWait(driver,500)
    contest_paths = '//a[@class="h-full w-full"]/div/div[3][@class="absolute bottom-0 flex w-full items-end text-white neIP_ lc-md:h-16 lc-md:py-3 h-8 px-4 py-2"]/div[@class="flex items-center"]'
    contests = wait.until(EC.presence_of_all_elements_located((By.XPATH,contest_paths)))
    contest_dates = []
    for contest in contests:
        contest_day = int(contest.text.split(' ')[2].split('d')[0])
        if contest_day == 0:
            contest_dates.append(contest.text)
    return contest_dates

            
