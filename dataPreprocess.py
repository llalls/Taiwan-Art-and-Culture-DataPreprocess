import json
import datetime
import pymssql
import pandas as pd
from pandas.io.json import json_normalize



class DataPreprocess:
    # 處理 activityInfo 資料
    def data_to_mssqlForamt(self, dict, info, infoData):
        # handle some category type is List
        if type(infoData) == list:
            if info == 'showInfo':
                dict['showInfo_string'] = str(infoData)
            else:
                infoData = str(infoData)

        if info == 'startDate':
            if infoData != '':
                infoData = datetime.datetime.strptime(infoData, '%Y/%m/%d')

        if info == 'endDate':
            if infoData != '':
                infoData = datetime.datetime.strptime(infoData, '%Y/%m/%d')

        dict[info] = infoData

    # 處理 showInfo 資料
    def showInfo_preProcess(self, info_Dataframe):
        showInfo_list = []
        for index, row in info_Dataframe.iterrows():
            for i in row['showInfo']:
                time = datetime.datetime.strptime(i['time'], '%Y/%m/%d %H:%M:%S')
                if i['onSales'] == 'Y':
                    onSales = 1
                else:
                    onSales = 0
                try:
                    latitude = float(i['latitude'])
                except:
                    latitude = None
                try:
                    longitude = float(i['longitude'])
                except:
                    longitude = None
                try:
                    endTime = datetime.datetime.strptime(i['endTime'], '%Y/%m/%d %H:%M:%S')
                except:
                    endTime = None

                showInfo_list.append([row['UID'], time, i['location'], i['locationName'], onSales, i['price'], 
                                        latitude, longitude, endTime])
        return showInfo_list

