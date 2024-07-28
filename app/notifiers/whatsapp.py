from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from typing import Tuple, List
from app.data_classes.contest_dataclass import ContestDetails
from app.utils.urls import WHATSAPP_URL
from app.utils.webdriver_utils import open_webdriver
from selenium.webdriver.remote.webelement import WebElement
from app.config.config_loader import (
    WHATSAPP_MESSAGE_TEXTFIELD_XPATH,
    WHATSAPP_SEARCH_BOX_XPATH,
)
from datetime import date
from app.utils import validators
from app.utils.exceptions import ContactNotFoundException


class WhatsappNotifier:
    """
    A class for sending Contest details via WhatsApp Web.
    """

    def __init__(
        self,
        target_date: str = date.today().strftime("%d-%m-%Y"),
    ):
        """
        Initialize the WhatsappNotifier object.

        Parameters:
        ----------
            target_date: ``str``
                The target date from which the contest data is fetched to sent.
        """
        self.target_date = target_date

    def send_message(
        self,
        input_field: WebElement,
        contest_data: List[ContestDetails],
        source_platform: str,
    ) -> None:
        """Sends the contest data to the input field of the given contact or group in WhatsApp web.

        Parameters:
        -----------
        input_field: `WebElement`
            The WebElement object of the input field in the WhatsApp web.
        contest_data: `List[ContestDetails]`
            The list of contest details to be sent.
        source_platform: `str`
            The name of the platform from which the contest data is fetched.
        """
        header = f"contest data from {source_platform}: "
        input_field.send_keys(header + Keys.ENTER)

        if not contest_data:
            no_data_message = f"No contests available for the date {self.target_date}."
            input_field.send_keys(no_data_message + Keys.ENTER)
        else:
            for data_entry in contest_data:
                for line in str(data_entry).split("\n"):
                    input_field.send_keys(line + Keys.SHIFT + Keys.ENTER)
                input_field.send_keys(Keys.ENTER)

    def find_contact(self, wait: WebDriverWait, contact_names: str) -> None:
        """
        Find and select the contact or group with the given name.

        Parameters:
        ----------
            wait: ``WebDriverWait``
                The WebDriverWait object.
            contact_names: ``str``
                The name of the contact or group to find.

        Raises:
        -------
            ``ContactNotFoundException``
                If the contact or group is not found.

        """
        search_box = validators.find_element_by_xpath(wait, WHATSAPP_SEARCH_BOX_XPATH)
        search_box.send_keys(contact_names)
        try:
            contact = validators.find_element_by_xpath(
                wait, f'//span[@title="{contact_names}"]'
            )
            contact.click()

        except Exception as exc_info:
            raise ContactNotFoundException(contact_names) from exc_info

    def send_notification(
        self,
        contact_name: str,
        contest_data: List[Tuple[str, List[ContestDetails]]],
    ) -> None:
        """Sends a WhatsApp message to the given contact list or group with the contest data.

        Parameters:
        -----------
        contact_name: `str`
            The name of the contact or group to send the message to.
        contest_data: `List[Tuple[str, List[ContestDetails]]]`
            A list of tuples containing the source platforms and contest data.
        """
        with open_webdriver(True) as driver:
            driver.get(WHATSAPP_URL)
            wait = WebDriverWait(driver, 60)
            self.find_contact(wait, contact_name)
            input_field = validators.find_element_by_xpath(
                wait, WHATSAPP_MESSAGE_TEXTFIELD_XPATH
            )

            for source_platform, data in contest_data:
                self.send_message(input_field, data, source_platform)

            # Wait for 30 seconds before quitting the driver
            time.sleep(60)
            print("Message sent successfully!")
