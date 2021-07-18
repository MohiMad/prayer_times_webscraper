from prayerTimes import prayerTimes
from playsound import playsound
import schedule
import time
from prayers import Prayers

PRAYERS = prayerTimes().prayer_times

def playit():
    playsound('azan.mp3')

for prayer in PRAYERS:
    schedule.every().day.at(prayer).do(playit)
    print(f"Assigned {Prayers(PRAYERS.index(prayer)).name} at {prayer}")


while True:
    schedule.run_pending()
    time.sleep(1)
