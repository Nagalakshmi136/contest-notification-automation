from selenium.webdriver.support.ui import WebDriverWait
from app.utils.urls import GFG_URL
from datetime import datetime
from app.config.config_loader import GFG_CONTESTS_XPATH, GFG_DATE_FORMAT
from app.data_fetchers.data_fetcher_base import DataFetcher
from app.utils.webdriver_utils import open_webdriver
from app.utils.date_utils import convert_to_datetime
from app.utils.data_processor import process_contest_data
from app.data_classes.contest_dataclass import ContestDetails
from app.utils import validators

class GFG(DataFetcher):
    """
    A class for fetching contest data available from GeeksforGeeks website.
    """
    def __init__(self):
        """
        Initializes the GeeksforGeeks data fetcher with the GeeksforGeeks URL.
        """
        self.url = GFG_URL

    def fetch_data(self) -> list[ContestDetails]:
        """Fetches the contest data available from the GeeksforGeeks website.
        
        Return:
        -------                 
        ``list[ContestDetails]``         
            A list of contest details available from the GeeksforGeeks website.  
        """
        with open_webdriver(True) as driver:
            driver.get(self.url)
            wait = WebDriverWait(driver, 60)
            contest_details = []
            contests = validators.find_elements_by_xpath(wait, GFG_CONTESTS_XPATH)
            for contest in contests:
                contest_date, contest_time = convert_to_datetime(
                    contest.text.replace("\n", ""), GFG_DATE_FORMAT
                )
                if contest_date == datetime.now().date():
                    contest_details.append(
                        ["GeeksforGeeks", contest_date, contest_time, None]
                    )
            return process_contest_data(contest_details)
