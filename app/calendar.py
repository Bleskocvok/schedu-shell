
from typing import Optional
from datetime import datetime, timedelta
import re


class Date:
    def __init__(self, date: datetime):
        self.day = date.day
        self.month = date.month
        self.year = date.year

    def __repr__(self) -> str:
        return f"Date(datetime(year={self.year}, "\
                f"month={self.month}, day={self.day}))"

    def __str__(self) -> str:
        d = str(self.day).rjust(2, "0")
        m = str(self.month).rjust(2, "0")
        return f"{self.year}-{m}-{d}"


def today() -> Date:
    return Date(datetime.today())


def tomorrow() -> Date:
    return Date(datetime.today() + timedelta(days=1))


def yesterday() -> Date:
    return Date(datetime.today() + timedelta(days=-1))


def parse_date(input: str) -> Optional[Date]:
    if input.find('-') == -1:
        return None
    result = re.match("([0-9]{4})-([0-9]{1,2})-([0-9]{1,2})", input)
    if result is None:
        return None
    if len(result.groups()) == 3:
        g = result.groups()
        try:
            return Date(datetime(
                    year=int(g[0]),
                    month=int(g[1]),
                    day=int(g[2])))
        except ValueError:
            return None
    return None


def parse(input: str) -> Optional[Date]:
    error = lambda : None
    d = parse_date(input)
    if d is not None:
        return d
    map = {
        "today" : today,
        "tod" : today,
        "tomorrow" : tomorrow,
        "tom" : tomorrow,
        "yesterday" : yesterday,
        "yest" : yesterday,
        # days of the week
        # "monday" : monday,
        # "mon" : monday,
        # "tuesday" : tuesday,
        # "tue" : tuesday,
        # "wednesday" : wednesday,
        # "wed" : wednesday,
        # "thursday" : thursday,
        # "thu" : thursday,
        # "friday" : friday,
        # "fri" : friday,
        # "saturday" : saturday,
        # "sat" : saturday,
        # "sunday" : sunday,
        # "sun" : sunday
    }
    return map.get(input, error)()

