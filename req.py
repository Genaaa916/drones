import requests
import bs4 as bs
import lxml.etree as le
import time
import json
import pilotinfo
import math


def find_info(serialnumber):
    url_info = "https://assignments.reaktor.com/birdnest/pilots/" + \
        str(serialnumber)
    info = requests.get(url_info).text
    info = bs.BeautifulSoup(info, 'lxml')
    print(info)
    return info


def in_ndz(center_x, center_y, radius, x, y):
    distance = math.sqrt((center_x - x) ** 2 + (center_y - y) ** 2)
    return distance <= radius


def get_pilot_info(pilot: pilotinfo.pilot):
    serial = pilot.serial
    pilot_url = f"https://assignments.reaktor.com/birdnest/pilots/{serial}"
    pilotlist.add_pilot(pilot)
    p_result = bs.BeautifulSoup(requests.get(
        pilot_url).text, 'html.parser')
    p_result_json = json.loads(p_result.string)
    pilot_contact = [p_result_json.get(
        "phoneNumber"), p_result_json.get("firstName"),
        p_result_json.get("lastName"),
        p_result_json.get("email")]
    pilot.lisaa_pilot_tiedot(pilot_contact)


def get_data():
    url = "https://assignments.reaktor.com/birdnest/drones"
    result = bs.BeautifulSoup(requests.get(url).text, 'lxml')
    soupy, serial, soupx = result.find_all("positiony"), result.find_all(
        "serialnumber"), result.find_all("positionx")
    result_y, result_x = [i.text for i in soupy], [i.text for i in soupx]
    result = result_y + result_x

    info = "no info"
    number = 1
    radius, center_x, center_y = 100000, 250000, 250000
    for i in range(len(result_x)):
        pilot_ = pilotinfo.pilot(serial[i].text)
        pilot_.lisaa_nro(number)
        pilot_.lisaa_x(float(result_x[i]))
        pilot_.lisaa_y(float(result_y[i]))
        number += 1
        """ TODO: the parsing below is not working, fix it """
        if in_ndz(center_y, center_x, radius, pilot_.x, pilot_.y):
            get_pilot_info(pilot_)
    if len(pilotlist.list) > 0:
        for i in pilotlist.list:
            if i not in pilotlist.printed_list:
                print(i)
                i.write_to_file()
                pilotlist.add_printed(i)
    time.sleep(10)
    get_data()


pilotlist = pilotinfo.pilot_list()
get_data()
