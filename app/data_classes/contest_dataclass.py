from dataclasses import dataclass


@dataclass
class ContestDetails:
    """
    Represents the details of a contest.
    """

    platform: str
    contest_date: str
    contest_time: str
    contest_duration: str

    def __str__(self) -> str:
        """
        Returns a string representation of the ContestDetails object.
        """
        return (
            f"'PLATFORM NAME' : {self.platform},\n"
            f"'CONTEST DATE' : {self.contest_date},\n"
            f"'CONTEST TIME' : {self.contest_time},\n"
            f"'CONTEST DURATION' : {self.contest_duration},\n"
        )
