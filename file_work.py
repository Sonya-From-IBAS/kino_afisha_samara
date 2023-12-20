import os
import datetime
import ast

from my_loader import executor


def read_sessions_from_file(year: int, month: int, day: int) -> list:
    """
    The function that reads cinemas poster data on a specific date

    Args:
        year (int): date year
        month (int): date month
        day (int): date day

    Returns:
        list: the array of dictionaries
    """
    with open(os.path.join('sessions', f"{year}-{month}-{day}.txt"), 'r', encoding='utf-8') as file:
        data = file.read()
    return ast.literal_eval(data)


def write_sessions_to_file() -> None:
    """
    The function that writes cinemas posters for the next 3 days in files
    """
    dates = []
    current_date = datetime.date.today()
    dates.append(current_date)

    for i in range(1, 3):
        dates.append(current_date + datetime.timedelta(days=i))

    for date in dates:
        data = executor(date.year, date.month, date.day)
        with open(os.path.join('sessions', f"{date.year}-{date.month}-{date.day}.txt"), 'w', encoding='utf-8') as file:
            file.write(str(data))
            