import xml
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Valute():

    def __init__(self, CharCode, ID):
        self.CharCode = CharCode
        self.ID = ID
    def Request(self, ID):
        self.ID = ID

        url = "http://www.cbr.ru/scripts/XML_daily.asp?"

        today = datetime.today()
        today = today.strftime("%d/%m/%Y")

        payload = {"date_req": today}

        responce = requests.get(url, params=payload)

        xml = BeautifulSoup(responce.content, "lxml")

        return xml.find("valute", {'ID': id}).value.text


# print(getCourse("R01235"), "рублей за 1 доллар")
# print(getCourse("R01239"), "рублей за 1 евро")
# print(getCourse("R01375"), "рублей за 10 юаней")

valute1 = Valute('EUR', R01239)
valute1.Request('R01239')
