import requests
import bs4 as bs
import lxml.etree as le
import time
import pilotinfo
url = "https://assignments.reaktor.com/birdnest/drones"


def get_data(url):
    r = requests.get(url)
    r = r.text
    result = bs.BeautifulSoup(r, 'lxml')
    soupy = result.find_all("positiony")
    soupx = result.find_all("positionx")
    result_y = []
    result_x = []
    for i in soupy:
        result_y.append(i.text)
    for i in soupx:
        result_x.append(i.text)
    result = result_y + result_x

    print(result)

    number = 1
    pilotlist = []
    for i in range(len(result_x)):
        pilot_ = pilotinfo.pilot
        pilotinfo.pilot.lisaa_nro(number)
        number += 1
        pilotinfo.pilot.lisaa_x(float(result_x[i]))
        pilotinfo.pilot.lisaa_y(float(result_y[i]))
        pilotinfo.pilot.print()
        if pilot_.y in range(150000, 350000) and pilot_.x in range(150000, 350000):
            print(f"Pilot {pilot_.number} is in the zone!")
        else:
            print(f"Pilot {pilot_.number} is not in the zone!")
        pilotlist.append(pilot_)
        time.sleep(5)
    get_data(url)


get_data(url)
