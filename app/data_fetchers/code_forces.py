from selenium.webdriver.support.ui import WebDriverWait
from app.utils.urls import CODE_FORCES
from datetime import datetime
from app.config.config_loader import CODEFORCES_CONTESTS_XPATH, CODEFORCES_DATE_FORMAT
from app.data_fetchers.data_fetcher_base import DataFetcher
from app.utils.webdriver_utils import open_webdriver
from app.utils.date_utils import convert_to_datetime
from app.utils.data_processor import process_contest_data
from app.data_classes.contest_dataclass import ContestDetails
from app.utils import validators


class CodeForces(DataFetcher):
    """
    A class for fetching contest data available from CodeForces website.
    """

    def __init__(self):
        """
        Initializes the CodeForces data fetcher with the CodeForces URL.
        """
        self.url = CODE_FORCES

    def fetch_data(self) -> list[ContestDetails]:
        """Fetches the contest data available from the CodeForces website.

        Return:
        -------
        ``list[ContestDetails]``
            A list of contest details available from the CodeForces website.
        """
        with open_webdriver() as driver:
            driver.get(CODE_FORCES)
            wait = WebDriverWait(driver, 30)
            contest_details = []
            no_of_contests = len(
                validators.find_elements_by_xpath(wait, CODEFORCES_CONTESTS_XPATH)
            )
            for i in range(2, no_of_contests + 1):
                contests = validators.find_elements_by_xpath(
                    wait, f"{CODEFORCES_CONTESTS_XPATH}[{i}]/td"
                )
                contest_date_time = contests[2].text.split("UTC")[0]
                contest_date, contest_time = convert_to_datetime(
                    contest_date_time, CODEFORCES_DATE_FORMAT
                )
                contest_duration = contests[3].text
                if contest_date == datetime.now().date():
                    contest_details.append(
                        ["code forces", contest_date, contest_time, contest_duration]
                    )

        return process_contest_data(contest_details)
