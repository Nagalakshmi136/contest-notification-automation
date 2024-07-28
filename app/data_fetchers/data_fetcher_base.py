from abc import ABC, abstractmethod


class DataFetcher(ABC):
    """
    Abstract base class for data fetchers.

    Implementing classes should provide an implementation of the `fetch_data` method
    that retrieves data from a web page using a Selenium WebDriver instance.
    """

    @abstractmethod
    def fetch_data(self) -> str:
        """
        Fetches data from a web page using the given web driver.

        Returns:
            A string containing the fetched data.
        """
        pass
