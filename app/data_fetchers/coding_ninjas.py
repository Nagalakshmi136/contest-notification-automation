from selenium.webdriver.support.ui import WebDriverWait
from app.utils.urls import CODING_NINJAS
from datetime import datetime
from app.utils.webdriver_utils import open_webdriver
from app.data_fetchers.data_fetcher_base import DataFetcher
from app.config.config_loader import (
    CODINGNINJAS_CONTESTS_XPATH,
    CODINGNINJAS_DATE_FORMAT,
)
from app.utils.date_utils import convert_to_datetime
from app.utils.data_processor import process_contest_data
from app.data_classes.contest_dataclass import ContestDetails
from app.utils import validators


class CodingNinjas(DataFetcher):
    """
    A class for fetching contest data available from Coding Ninjas website.
    """

    def __init__(self):
        """
        Initializes the Coding Ninjas data fetcher with the Coding Ninjas URL.
        """
        self.url = CODING_NINJAS

    def fetch_data(self) -> list[ContestDetails]:
        """Fetches the contest data available from the Coding Ninjas website.

        Return:
        -------
        ``list[ContestDetails]``
            A list of contest details available from the Coding Ninjas website.
        """
        with open_webdriver(True) as driver:
            driver.get(CODING_NINJAS)
            wait = WebDriverWait(driver, 60)
            contest_details = []
            print(CODINGNINJAS_CONTESTS_XPATH)
            contests = validators.find_elements_by_xpath(
                wait, CODINGNINJAS_CONTESTS_XPATH
            )
            print(len(contests))
            for contest in contests:
                contest_date, contest_time = convert_to_datetime(
                    contest.text, CODINGNINJAS_DATE_FORMAT
                )
                if contest_date == datetime.now().date():
                    contest_details.append(
                        ["coding Ninjas", contest_date, contest_time, "2:00 hr"]
                    )

            return process_contest_data(contest_details)
