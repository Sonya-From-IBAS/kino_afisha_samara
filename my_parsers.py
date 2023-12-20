from bs4 import BeautifulSoup


def parse_ekino(page: str) -> list:
    """
    The function that parses the website of the Ekino cinema

    Args:
        page (str): the html code of the page

    Returns:
        list: the array of dictionaries,
        where the keys are the address, the name of the cinema, the link, the picture, the genre,
        the sessions of the films
        and the value is their values
    """
    soup = BeautifulSoup(page, "lxml")
    content = []
    movies = soup.find_all("a", attrs={"class": "releases-item"})

    for movie in movies:
        try:
            info = {}
            info["address"] = f'Самара, {soup.find("div", attrs={"class": "footer__address-title"}).find("span").text}'
            info['cinema'] = "Ёкино"
            info["title"] = movie.find(
                "div", attrs={"class": "releases-item-description__title"}).text.strip()
            info["href"] = f'https://ёкино.рф{movie["href"]}'
            info["img"] = movie.find(
                "img", attrs={"class": "releases-item__poster-img"})["src"]
            info["genre"] = movie.find(
                "div", attrs={"class": "releases-item-description__badge"}).find("span").text
            info["sessions"] = []
            sessions = movie.find_all(
                "div", attrs={"class": "seance-item__item"})
            for s in sessions:
                info["sessions"].append([s.find("div", attrs={"class": "seance-item__time"}).text,
                                         s.find("div", attrs={"class": "seance-item__description"}).find_all(
                                             "span")[2].text.replace("\u2009₽", " рублей"),
                                         s.find("div", attrs={
                                                "class": "seance-item__description"}).find_all("span")[0].text
                                         ])
            if (len(info["sessions"]) != 0):
                content.append(info)

        except:
            pass
    return content


def parse_ambar(page: str) -> list:
    """
    The function that parses the website of the Ambar cinema

    Args:
        page (str): the html code of the page

    Returns:
        list: the array of dictionaries,
        where the keys are the address, the name of the cinema, the link, the picture, the genre,
        the sessions of the films
        and the value is their values
    """
    soup = BeautifulSoup(page, "lxml")
    content = []
    movies = soup.find_all("div", attrs={"class": "schedule_bable__film"})

    for movie in movies:
        try:
            info = {}
            info["address"] = "Самара, Южное ш., 5, ТК «Амбар»"
            info['cinema'] = "Ambar cinema"
            info["title"] = movie.find(
                "div", attrs={"class": "title"}).text.split(" (")[0].strip()
            info["href"] = f'https://ambarcinema.ru{movie.find("div", attrs={"class": "left"}).find("a")["href"]}'
            info["img"] = f'https://ambarcinema.ru{movie.find("div", attrs={"class": "img"}).find("img")["src"]}'
            info["genre"] = movie.find("div", attrs={"class": "desc genre"}).find(
                "div", attrs={"class": "field"}).text
            info["sessions"] = []
            sessions = movie.find_all("li", attrs={"class": "schedule-item"})
            for s in sessions:
                info["sessions"].append([s.find("a", attrs={"class": "time"}).text,
                                        s.find("span", attrs={
                                               "class": "price_show"}).text,
                                        f'{movie.find("div", attrs={"class": "title"}).text.split("D")[0][-1]}D'
                                         ])
            if (len(info["sessions"]) != 0):
                content.append(info)

        except:
            pass
    return content


def parse_zoom(page: str) -> list:
    """
    The function that parses the website of the Zoom cinema

    Args:
        page (str): the html code of the page

    Returns:
        list: the array of dictionaries,
        where the keys are the address, the name of the cinema, the link, the picture, the genre,
        the sessions of the films
        and the value is their values
    """
    soup = BeautifulSoup(page, "lxml")
    content = []
    movies = soup.find_all("div", attrs={"class": "movies__card"})

    for movie in movies:
        try:
            info = {}
            info["address"] = soup.find(
                "div", attrs={"class": "bottom__contacts-item"}).text
            info['cinema'] = "Zoom Cinema"
            info["href"] = movie.find(
                "a", attrs={"class": "movies__image"})["href"]
            info["img"] = movie.find("a", attrs={"class": "movies__image"})[
                "style"].split('"')[1]
            title = movie.find(
                "a", attrs={"class": "movies__title"}).find("span").text
            if "предсеанс" in title:
                info["title"] = title.split("предсеанс").strip()
            else:
                info["title"] = title.strip()
            info["genre"] = movie.find(
                "div", attrs={"class": "movies__genres"}).text.strip()
            info["sessions"] = []
            sessions = movie.find_all("div", attrs={"class": "shows__item"})
            for s in sessions:
                info["sessions"].append([
                    s.find("div", attrs={"class": "shows__time"}).text,
                    f"{s.find('div', attrs={'class':'shows__price'}).text} рублей",
                    s.find("div", attrs={"class": "shows__type"}).text])

            content.append(info)

        except:
            pass
    return content


def parse_kinomax(page: str) -> list:
    """
    The function that parses the website of the Ambar cinema

    Args:
        page (str): the html code of the page

    Returns:
        list: the array of dictionaries,
        where the keys are the address, the name of the cinema, the link, the picture, the genre,
        the sessions of the films
        and the value is their values
    """
    soup = BeautifulSoup(page, "lxml")
    content = []
    movies = soup.find_all("div", attrs={"class": "f+8kryKK3ho97tZqpYoKtg=="})

    for movie in movies:
        try:
            info = {}
            info["address"] = soup.find(
                "div", attrs={"class": "_6z8xFjZc5TVh+kCCBM1FKw=="}).text
            info['cinema'] = "Киномакс"
            title = movie.find("a", attrs={"class": "_5uPuhE3DwKjj8AJsJwUecg=="}).find(
                "h4").text.strip()
            if "(предсеанс. обсл)" in title:
                info["title"] = title.split("(предсеанс. обсл)").strip()
            else:
                info["title"] = title.strip()
            info["href"] = f'https://kinomax.ru{movie.find("a", attrs={"class": "t7kUnSdcINMNiSF38GqNxg=="})["href"]}'
            info["img"] = movie.find(
                "img", attrs={"class": "VfkmF-EkVmemxG349BvcSA=="})["src"]
            info["genre"] = movie.find(
                "div", attrs={"class": "sTUFxkIWBwEem6l1TpFg7w=="}).find("div").text
            info["sessions"] = []
            sessions = movie.find_all(
                "a", attrs={"class": "W+TmjEcF8G5yUSHJQRcvSw=="})
            for s in sessions:

                info["sessions"].append([s.find("span", attrs={"class": "v69CDo-9TnnL2QVdJPMpqw=="}).text,
                                        s.find("span", attrs={"class": "y0gUE2sdwIMyWc990NQPSA=="}).text.replace(
                                            "₽", " рублей"),
                                        s.find("span", attrs={
                                               "class": "_4OZn-x4FepV07ugMGctC1A=="}).text
                                         ])

            content.append(info)

        except:
            pass
    return content


def parse_gudok_and_cosmoport(page: str) -> list:
    """
    The function that parses the website of the Gudok cinema or Cosmoport cinema 

    Args:
        page (str): the html code of the page

    Returns:
        list: the array of dictionaries,
        where the keys are the address, the name of the cinema, the link, the picture, the genre,
        the sessions of the films
        and the value is their values
    """
    soup = BeautifulSoup(page, "lxml")
    content = []
    movies = soup.find_all("div", attrs={"class": "showtimes_item"})

    for movie in movies:
        try:
            info = {}
            info["address"] = soup.find(
                "span", attrs={"class": "theaterInfo_dataAddr"}).text.replace("&nbsp;", " ")

            if "8325966" in page:
                info["cinema"] = "Мягкий кинотеатр Гудок"
            else:
                info["cinema"] = "Мягкий кинотеатр Космопорт"

            info["title"] = movie.find(
                "span", attrs={"class": "showtimesMovie_name"}).text
            info["href"] = movie.find(
                "a", attrs={"class": "showtimesMovie_link"})["href"]
            info["img"] = movie.find(
                "source", attrs={"type": "image/jpeg"})["srcset"]
            info["genre"] = movie.find(
                "span", attrs={"class": "showtimesMovie_categories"}).text.strip()
            info["sessions"] = []
            sessions = movie.find_all(
                "a", attrs={"class": "showtimes_session"})
            for s in sessions:

                info["sessions"].append([
                    s.find("span", attrs={"class": "session_time"}).text,
                    s.find('span', attrs={'class': 'session_price'}).text.replace(
                        '₽', 'рублей'),
                    movie.find("span", attrs={"class": "showtimes_format"}).text])

            content.append(info)

        except:
            pass
    return content


def parse_kinosamara(page: str) -> list:
    """
    The function that parses the website of the Samara cinema

    Args:
        page (str): the html code of the page

    Returns:
        list: the array of dictionaries,
        where the keys are the address, the name of the cinema, the link, the picture, the genre,
        the sessions of the films
        and the value is their values
    """
    soup = BeautifulSoup(page, "lxml")
    content = []
    movies = soup.find_all("a", attrs={"class": "releases-item"})

    for movie in movies:
        try:
            info = {}
            info["address"] = soup.find(
                "div", attrs={"class": "header__text-addition"}).text

            info['cinema'] = "Кинотеатр Самара"
            title = movie.find(
                "div", attrs={"class": "releases-item-description__title"}).text

            if "&" in title:
                info["title"] = title.split("&").strip()
            else:
                info["title"] = title.strip()

            info["href"] = f'https://kinosamara.ru{movie["href"]}'
            info["img"] = movie.find(
                "img", attrs={"class": "releases-item__poster-img"})["data-src"]
            info["genre"] = movie.find(
                "div", attrs={"class": "releases-item-description__badge"}).find("span").text
            info["sessions"] = []
            sessions = movie.find_all("div", attrs={"class": "seance-item"})
            for s in sessions:
                info["sessions"].append([s.find("div", attrs={"class": "seance-item__time"}).text,
                                         s.find("div", attrs={"class": "seance-item__wrapper"}).find_all(
                                             "span")[2].text.replace("\u2009₽", " руйблей"),
                                         s.find("div", attrs={
                                                "class": "seance-item__wrapper"}).find_all("span")[0].text
                                         ])
            if (len(info["sessions"]) != 0):
                content.append(info)

        except:
            pass
    return content


# The dictionary of methods to avoid unnecessary conditional operators
method = {
    "ekino": parse_ekino,
    "ambar": parse_ambar,
    "zoom": parse_zoom,
    "kinomax": parse_kinomax,
    "gudok": parse_gudok_and_cosmoport,
    "kosmoport": parse_gudok_and_cosmoport,
    "kinosamara": parse_kinosamara
}
