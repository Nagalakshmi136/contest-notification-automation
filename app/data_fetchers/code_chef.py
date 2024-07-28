from selenium.webdriver.support.ui import WebDriverWait
from app.utils.urls import CODE_CHEF
from datetime import datetime, date
from app.utils.webdriver_utils import open_webdriver
from app.data_fetchers.data_fetcher_base import DataFetcher
from app.config.config_loader import CODECHEF_CONTESTS_XPATH
from app.utils.data_processor import process_contest_data
from app.data_classes.contest_dataclass import ContestDetails
from app.utils import validators


class CodeChef(DataFetcher):
    """
    A class for fetching contest data available from CodeChef website.
    """

    def __init__(self):
        """
        Initializes the CodeChef data fetcher with the CodeChef URL.
        """
        self.url = CODE_CHEF

    def fetch_data(self) -> list[ContestDetails]:
        """Fetches the contest data available from the CodeChef website.

        Return:
        -------
        ``list[ContestDetails]``
            A list of contest details available from the CodeChef website.
        """
        with open_webdriver(True) as driver:
            driver.get(self.url)
            wait = WebDriverWait(driver, 60)
            contest_details = []
            no_of_contests = len(
                validators.find_elements_by_xpath(wait, CODECHEF_CONTESTS_XPATH)
            )
            for i in range(1, no_of_contests + 1):
                contests = validators.find_elements_by_xpath(
                    wait, f"{CODECHEF_CONTESTS_XPATH}[{i}]/td"
                )   
                contest_date = datetime.strptime(
                    contests[2].text.split("\n")[0], "%d %b %Y"
                ).date()
                contest_time = contests[2].text.split("\n")[1]
                contest_duration = contests[3].text
                if contest_date == date.today():
                    contest_details.append(
                        ["code chef", contest_date, contest_time, contest_duration]
                    )
            return process_contest_data(contest_details)
