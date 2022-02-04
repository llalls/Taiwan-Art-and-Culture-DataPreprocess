import json
import datetime
import pymssql
import requests
import pandas as pd
from pandas.io.json import json_normalize

from insertToDB import InsertToDB
from dataPreprocess import DataPreprocess
from fetchRawData import FetchRawData



class Activity:
    def get_activity_data(self, targetActivityCategory):
        print('try to get all Activity data')

        FetchRawData.get_all_activity_data(self, targetActivityCategory)

        print('all done')


# activity category: 9, 10, 12, 18, 20 為空值
targetActivityCategory = [1, 2, 3, 4, 5, 6, 7, 8, 11, 13, 14, 15, 16, 17, 19]


Activity = Activity()
Activity.get_activity_data(targetActivityCategory)

