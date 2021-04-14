# first workshop

from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"  # 네이버 금융에서 환율정보를 실시간으로 가져온다

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser", from_encoding='euc-kr')

name_nation = soup.select('h3.h_lst > span.blind')
name_price = soup.select('span.value')

i = 0
for c_list in soup:
    try:
        if i == 0:
            num_USD = float(name_price[i].text.replace(',', ''))
        elif i == 1:
            # 사이트에 100엔 기준이라 되어 있어 후처리(수정)
            num_JPY = float(name_price[i].text.replace(',', ''))/100
        elif i == 2:
            num_EUR = float(name_price[i].text.replace(',', ''))
        elif i == 3:
            num_CNY = float(name_price[i].text.replace(',', ''))
        i = i + 1
    except IndexError:
        pass
# 그중 순서대로 USD, JPY, EUR, CNY만 가져와 각자 저장 후 출력한다.
print('USD:', num_USD)
print('JPY:', num_JPY)
print('EUR:', num_EUR)
print('CNY:', num_CNY)

# 1 미국 USD 1,124.50
# 2 일본 JPY(100엔 기준) 1,027.79
# 3 유럽연합 EUR 1,337.31
# 4 중국 CNY 171.59

print("--------------------------------------------")
money = input("원화: ")  # 외화로 환전할 원화 금액을 입력한다.

# 엔화(JPY) 변환
JPY = int(float(money)/num_JPY)
print(JPY, "엔")

# 달러(USD) 변환
USD = int(float(money)/num_USD)
print(USD, "달러")

# 유로(EUR) 변환
EUR = int(float(money)/num_EUR)
print(EUR, "유로")

# 위안(CNY) 변환
CNY = int(float(money)/num_CNY)
print(CNY, "위안")
# 입력한 원화가 4가지 외화로 환전되는 금액을 출력한다
print("--------------------------------------------")
