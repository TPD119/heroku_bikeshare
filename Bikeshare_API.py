#!/usr/bin/env python
# coding: utf-8

import requests
import json
import pandas as pd
import datetime
from pprint import pprint
import time


def BikerData():

    url = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Transportation_WebMercator/MapServer/5/query?where=1%3D1&outFields=OBJECTID,ID,ADDRESS,TERMINAL_NUMBER,LATITUDE,LONGITUDE,NUMBER_OF_BIKES,NUMBER_OF_EMPTY_DOCKS&outSR=4326&f=json"

    response = requests.get(url)
    data = response.json()
 

    address = []
    term_id = []
    lat = []
    lng = []
    num_bikes = []
    num_empty_docks = []
    obj_id = []
    term_num = []
    time_stamp = []


    now = datetime.datetime.now()
    time = pd.Timestamp(now.year,now.month,now.day,now.hour,now.minute)
    for index,item in enumerate(data["features"]):
        address.append(data["features"][index]["attributes"]["ADDRESS"])
        term_id.append(data["features"][index]["attributes"]["ID"])
        lat.append(data["features"][index]["attributes"]["LATITUDE"])
        lng.append(data["features"][index]["attributes"]["LONGITUDE"])
        num_bikes.append(data["features"][index]["attributes"]["NUMBER_OF_BIKES"])
        num_empty_docks.append(data["features"][index]["attributes"]["NUMBER_OF_EMPTY_DOCKS"])
        obj_id.append(data["features"][index]["attributes"]["OBJECTID"])
        term_num.append(data["features"][index]["attributes"]["TERMINAL_NUMBER"])
        time_stamp.append(time)


    # build a dataframe from the cities, lon,and pressure lists
    biker_data = {"time":time_stamp,"term_id": term_id, "address": address, "lat": lat, "long": lng, "num_bikes":num_bikes,"num_empty_docks":num_empty_docks, "obj_id":obj_id,"term_num":term_num}

    biker_data = pd.DataFrame(biker_data)

    #with open('bike_data.csv', 'w') as f:
    #    biker_data.to_csv(f, header=True,index=False)

    with open('bike_data.csv', 'a') as f:
        biker_data.to_csv(f, header=False,index=False)

while(True):
    BikerData()
    time.sleep(60)



