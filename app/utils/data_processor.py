from typing import Any, List
from app.data_classes.contest_dataclass import ContestDetails


def process_contest_data(contests: List[List[str]]) -> List[ContestDetails]:
    """Process contest data and convert it into a list of ContestDetails objects.

    Parameters:
    -----------
    contests: ``List[List[str]]``
        A list of contest data, where each inner list contains
            the contest details in the following order:
            [platform, contest_date, contest_time, contest_duration]

    Return:
    -------
    ``List[ContestDetails]``
        A list of ContestDetails objects representing the processed contest data.
    """
    return [
        ContestDetails(
            platform=contest[0],
            contest_date=contest[1],
            contest_time=contest[2],
            contest_duration=contest[3],
        )
        for contest in contests
    ]
