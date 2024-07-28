from datetime import datetime, timedelta, date, time
import re


def convert_to_datetime(datetime_str: str, format: str) -> tuple[date, time]:
    """converts the datetime string in the given format to datetime object
    and returns date and time.

    Parameters:
    -----------
    datetime_str: `str`
        Input string to be converted to datetime object.
    format: `str`
        Format of the input string.

    Return:
    -------
    ``tuple[date,time]``
        A tuple containing two elements:
        - datetime.date object representing the date part of the future datetime.
        - datetime.time object representing the time part of the future datetime.

    """
    datetime_obj = datetime.strptime(datetime_str, format)
    return datetime_obj.date(), datetime_obj.time()


def parse_duration(duration_str: str) -> tuple[date, time]:
    """Parses a duration string in the format 'Xd Xh Xm Xs' and returns a future datetime object.

    The function extracts the number of days, hours, minutes, and seconds from the given duration string
    and calculates the future datetime from the current datetime.

    Parameters:
    ----------
    duration_str : ``str``
        A string representing the duration in the format 'Xd Xh Xm Xs'. For example, '1d 17h 0m 3s'.

    Returns:
    -------
    ``tuple``
        A tuple containing two elements:
        - datetime.date object representing the date part of the future datetime.
        - datetime.time object representing the time part of the future datetime.
    """

    # Extract the numbers from the duration string
    matches = re.findall(r"(\d+)", duration_str)

    # if len(matches) != 4:
    #     raise ValueError("Invalid duration format")

    days, hours, minutes, seconds = map(int, matches)

    datetime_obj = datetime.now() + timedelta(
        days=days, hours=hours, minutes=minutes, seconds=seconds
    )
    return datetime_obj.date(), datetime_obj.time()
