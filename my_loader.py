import time
import multiprocessing

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from my_parsers import method


def data_loader(data: list) -> list:
    """
        The function that uses the selenium framework to get html code from website,
        and then uses a parser to get the necessary data

    Args:
        data (list): the list of data,
        data[0] - url,
        data[1] - parse function

    Returns:
        list: the array of dictionaries
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(data[0])
    time.sleep(1.5)
    page = driver.page_source
    driver.quit()
    result = method[data[1]](page)
    return result


def load_all_data(year: int, month: int, day: int) -> list:
    """
    The function that uses the multiprocessing library to get data from all cinemas using the data_loader

    Args:
        year (int): date year
        month (int): date month
        day (int): date day

    Returns:
        list: the array of arrays containing dictionaries
    """
    urls = [(f"https://ёкино.рф/?date={year}-{month}-{day}", "ekino"),
            (f"https://ambarcinema.ru/schedule/?date={day}.{month}.{year}", "ambar"),
            (f"https://zoomcinema.ru/samara/date/{year}-{month}-{day}#/", "zoom"),
            (f"https://kinomax.ru/samara/{year}-{month}-{day}", "kinomax"),
            (f"https://smr.kinoafisha.info/cinema/8325966/schedule/?date={year}{month}{day}&order=movie", "gudok"),
            (f"https://smr.kinoafisha.info/cinema/5981923/schedule/?date={year}{month}{day}&order=movie", "kosmoport"),
            (f"https://kinosamara.ru/?date={year}-{month}-{day}",
             "kinosamara"),
            ]
    try:
        with multiprocessing.Pool(4) as p:
            results = p.map(data_loader, urls)
        return results
    
    except Exception as e:
        print(e)


def executor(year: int, month: int, day: int) -> list:
    """
    The function to get all the data and bring it to a convenient view

    Args:
        year (int): date year
        month (int): date month
        day (int): date day

    Returns:
        list: the array of dictionaries
    """
    response = load_all_data(year, month, day)

    sessions = []
    for i in response:
        for j in i:
            sessions.append(j)
    return sessions