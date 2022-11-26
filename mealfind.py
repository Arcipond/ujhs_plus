from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
import lxml
import re, os

class mealfind:
    def __init__(self):
        data_meal = ""

    def find(meal_date): #meal_date = yyyy-mm-dd
        
        date = meal_date[2:4]+meal_date[5:7]+meal_date[8:10]
        url = "https://open.neis.go.kr/hub/mealServiceDietInfo?&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7531047&MLSV_YMD="
        url += str(date)+"&KEY="
        url += os.environ['meal_key']

        xml = requests.get(url)
        soup = bs(xml.text, "lxml")
        make = soup.findAll('ddish_nm')

        data_meal = []
        p=re.compile('[ a-zA-Z가-힗]+')
        q=re.compile('[0-9]|[.]')

        for i in range(2):
            if(i+1 > len(make)):
                data_meal.append("None")
            else:
                t_list=''.join(p.findall(make[i].text[9:-3])).split()
                data_meal.append(t_list)

        return data_meal
    

    