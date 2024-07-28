from selenium.webdriver.support.ui import WebDriverWait
from app.utils.urls import LEET_CODE_URL
from app.utils.webdriver_utils import open_webdriver
from app.data_fetchers.data_fetcher_base import DataFetcher
from app.config.config_loader import LEETCODE_CONTESTS_XPATH
from app.utils.data_processor import process_contest_data
from app.utils.date_utils import parse_duration
from datetime import datetime
from app.utils import validators
from app.data_classes.contest_dataclass import ContestDetails


class LeetCode(DataFetcher):
    """
    A class for fetching contest data available from LeetCode website.
    """
    def __init__(self):
        """
        Initializes the LeetCode data fetcher with the LeetCode URL.
        """
        self.url = LEET_CODE_URL

    def fetch_data(self) -> list[ContestDetails]:
        """Fetches the contest data available from the LeetCode website.
        Return:
        -------                 
        ``list[ContestDetails]``        
            A list of contest details available from the LeetCode website.  
        """
        with open_webdriver(True) as driver:
            driver.get(self.url)
            wait = WebDriverWait(driver, 70)
            contest_details = []
            contests = validators.find_elements_by_xpath(wait, LEETCODE_CONTESTS_XPATH)
            for contest in contests:
                contest_date, contest_time = parse_duration(
                    contest.text.replace("Starts in ", "")
                )
                if contest_date == datetime.now().date():
                    contest_details.append(
                        ["LeetCode", contest_date, contest_time, None]
                    )
            return process_contest_data(contest_details)
