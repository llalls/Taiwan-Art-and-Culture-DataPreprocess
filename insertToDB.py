import json
import datetime
import pymssql
import pandas as pd
from pandas.io.json import json_normalize



class InsertToDB:
    __connect = None

    def __init__(self):
        self.__connect = pymssql.connect(
            host='**********',                          # your mssql ip host
            user='**********',                          # your mssql user
            password='**********',                      # your mssql password
            database="**********")                      # your mssql connect database

    def __del__(self):
        self.__connect.close()

    # 活動資料放入MSSQL
    def insert_rawData_to_db(self, info_Dataframe):
        cursor = self.__connect.cursor()

        db_query = """INSERT INTO activityInfo(
                version, UID, title, category,
                showUnit, descriptionFilterHtml, discountInfo, imageUrl,
                masterUnit, subUnit, supportUnit, otherUnit,
                webSales, sourceWebPromote, comment, editModifyDate,
                sourceWebName, startDate, endDate, hitRate, showInfo)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        for index, row in info_Dataframe.iterrows():
            cursor.execute(db_query, (row.version, row.UID, row.title, row.category, row.showUnit, row.descriptionFilterHtml,
                                        row.discountInfo, row.imageUrl, row.masterUnit, row.subUnit, row.supportUnit,
                                        row.otherUnit, row.webSales, row.sourceWebPromote, row.comment, row.editModifyDate,
                                        row.sourceWebName, row.startDate, row.endDate, row.hitRate, row.showInfo_string))

        self.__connect.commit()
        cursor.close()

    # showInfo資料放入MSSQL
    def insert_showInfo_to_db(self, showInfo_List):
        cursor = self.__connect.cursor()

        db_query = """INSERT INTO showInfo(
                UID, time, location, locationName, onSales, price, latitude, longitude, endTime)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        for i in showInfo_List:
            test = tuple(i)
            cursor.execute(db_query, test)

        self.__connect.commit()
        cursor.close()