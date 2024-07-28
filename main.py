import logging
from app.utils.types.contest_sources import ContestSource
from typing import List, Tuple
from app.notifiers.whatsapp import WhatsappNotifier
from app.data_classes.contest_dataclass import ContestDetails
from datetime import date

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def fetch_all_contest_data() -> List[Tuple[str, List[ContestDetails]]]:
    """
    Fetches contest data from various sources.

    Returns:
    -------
    ``List[Tuple[str, List[IpoDataInfo]]]``
        A list of tuples where each tuple contains the source name and the list of contest data.
    """
    contest_data = []
    for source in ContestSource:
        try:
            logging.info(f"Fetching data from {source.source_name}")
            data = source.fetcher.fetch_data()
            contest_data.append((source.source_name, data))
        except Exception as e:
            logging.error(f"Failed to fetch data from {source.source_name}: {e}")

    return contest_data


def main():
    """
    Main function to fetch contest data and notify via WhatsApp.
    """
    try:
        contest_data = fetch_all_contest_data()
        if contest_data:
            notifier = WhatsappNotifier(target_date=date.today().strftime("%d-%m-%Y"))
            notifier.send_notification("Contests", contest_data)
            logging.info("Notification sent successfully.")
        else:
            logging.warning("No contest data fetched.")
    except Exception as e:
        logging.error(f"An error occurred during the process: {e}")


if __name__ == "__main__":
    main()
