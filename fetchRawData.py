import json
import datetime
import pymssql
import requests
import pandas as pd
from pandas.io.json import json_normalize

from insertToDB import InsertToDB
from dataPreprocess import DataPreprocess



class FetchRawData:
    # 獲取藝文活動資料 from 政府開放平台
    def get_activity_data_by_url(self, activityType):
        defaultUrl = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?'

        params = dict(
            method='doFindTypeJ',
            category=activityType
        )

        requestsUrl = requests.get(url=defaultUrl, params=params)
        data = requestsUrl.json()
        return data

    # 獲取所有藝文類型的活動資料
    def get_all_activity_data(self, activityList):
        for activityType in activityList:
            data = FetchRawData.get_activity_data_by_url(self, activityType)
            FetchRawData.preprocess(self, data)
            print('done Activity category of ' + str(activityType))
        print('save all activity done...')

    # 資料前處理並放入DB
    def preprocess(self, metaData):
        sizeSave = 0
        info_Dataframe = pd.DataFrame()
        showInfoList = []

        for data in metaData:
            infoDict = {}
            for info in data:
                DataPreprocess.data_to_mssqlForamt(self, dict=infoDict, info=info, infoData=data[info])

            df = json_normalize(infoDict)
            info_Dataframe = info_Dataframe.append(df)

        sizeSave = sizeSave + info_Dataframe.shape[0]
        showInfoList.extend(DataPreprocess.showInfo_preProcess(self, info_Dataframe))

        insertToDB = InsertToDB()
        insertToDB.insert_rawData_to_db(info_Dataframe)
        insertToDB.insert_showInfo_to_db(showInfoList)


