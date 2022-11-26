from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
import re, os

class mealfind:
    def __init__(self):
        data_meal = ""

    def find(self, meal_date): #yyyy-mm-dd
        date = meal_date[2:4]+meal_date[5:7]+meal_date[8:10]
        url = "https://open.neis.go.kr/hub/mealServiceDietInfo?&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7531047&MLSV_YMD="
        url += str(date)+"&KEY="
        url += os.environ['meal_key']

        html = requests.get(url)
        soup = bs(html.text, 'html.parser')
        make = soup.findAll('ddish_nm')

        data_meal = []
        p=re.compile('[ a-zA-Z가-힗()]+')
        q=re.compile('[0-9]|[.]')

        for i in range(2):
            if(i+1 > len(make)):
                data_meal.append("None")
            else:
                t_list=make[i].text.split('<br/>')
                temp_save=[]
                for j in t_list:
                    temp_save.append([''.join(p.findall(j)),''.join(q.findall(j))])
                data_meal.append(temp_save)

        return data_meal
