from urllib.request import urlopen
from datetime import date
import re
from prayers import Prayers

SOURCES = {
    "https://www.uppsalamoske.se/bontider/": r"(?<={today}</td>).*?(?=<\/tr>)".format(today=date.today()),
    "https://www.muslimpro.com/Prayer-times-Stockholm-Sweden-2673730": r"<tr class='active'>.*?<\/tr>"
}

class prayerTimes():
    # We assign prayer_times as the function to automatically execute it when a class is defined
    def __init__(self):
        self.prayer_times = self.retrieve_data()

    """
        A function that requests source code of two URLs and grabs the data of the prayers today
    """
    def retrieve_data(self) -> list:
        for url, pattern in SOURCES.items():
            if prayers := re.findall(pattern, urlopen(url).read().decode("utf-8"), re.DOTALL):
                return re.findall(r"\d\d:\d\d", prayers[0])

        return []
            

if __name__ == "__main__":
    client = prayerTimes()
    print(client.prayer_times)
