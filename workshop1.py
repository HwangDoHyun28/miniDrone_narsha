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
# 엔화(JPY) 최소 화폐
while(JPY > 0):
    a, JPY = divmod(JPY, 10000)
    b, JPY = divmod(JPY, 5000)
    c, JPY = divmod(JPY, 2000)
    d, JPY = divmod(JPY, 1000)
    e, JPY = divmod(JPY, 500)
    f, JPY = divmod(JPY, 100)
    g, JPY = divmod(JPY, 50)
    h, JPY = divmod(JPY, 10)
    i, JPY = divmod(JPY, 5)
    # divmod함수를 이용해 몫과 나머지를 얻어서 각 지폐(동전)가 필요한 수를 몫으로, 나머지는 다름 지페 단위로 넘기는 과정을 통해 필요한 최소 지폐(동전)의 개수를 구할 수 있도록 했다.
    j, JPY = divmod(JPY, 1)
print("10000엔:", a, "장(개)")
print("5000엔:", b, "장(개)")
print("2000엔:", c, "장(개)")
print("1000엔:", d, "장(개)")
print("500엔:", e, "장(개)")
print("100엔:", f, "장(개)")
print("50엔:", g, "장(개)")
print("10엔:", h, "장(개)")
print("5엔:", i, "장(개)")
print("1엔:", j, "장(개)")  # 필요한 지폐(동전) 수 출력
print("Total: ", a+b+c+d+e+f+g+h+i+j, "장(개)")  # 개수 합계 출력
print("--------------------------------------------")

# 달러(USD) 최소 화폐
while(USD > 0):
    a, USD = divmod(USD, 100)
    b, USD = divmod(USD, 50)
    c, USD = divmod(USD, 20)
    d, USD = divmod(USD, 10)
    e, USD = divmod(USD, 5)
    f, USD = divmod(USD, 2)
    # divmod함수를 이용해 몫과 나머지를 얻어서 각 지폐(동전)가 필요한 수를 몫으로, 나머지는 다름 지페 단위로 넘기는 과정을 통해 필요한 최소 지폐(동전)의 개수를 구할 수 있도록 했다.
    g, USD = divmod(USD, 1)
print("100달러:", a, "장(개)")
print("50달러:", b, "장(개)")
print("20달러:", c, "장(개)")
print("10달러:", d, "장(개)")
print("5달러:", e, "장(개)")
print("2달러:", f, "장(개)")
print("1달러:", g, "장(개)")  # 필요한 지폐(동전) 수 출력
print("Total: ", a+b+c+d+e+f+g, "장(개)")  # 개수 합계 출력
print("--------------------------------------------")

# 유로(EUR) 최소 화폐
while(EUR > 0):
    a, EUR = divmod(EUR, 500)
    b, EUR = divmod(EUR, 200)
    c, EUR = divmod(EUR, 100)
    d, EUR = divmod(EUR, 50)
    e, EUR = divmod(EUR, 20)
    f, EUR = divmod(EUR, 10)
    g, EUR = divmod(EUR, 5)
    h, EUR = divmod(EUR, 2)
    # divmod함수를 이용해 몫과 나머지를 얻어서 각 지폐(동전)가 필요한 수를 몫으로, 나머지는 다름 지페 단위로 넘기는 과정을 통해 필요한 최소 지폐(동전)의 개수를 구할 수 있도록 했다.
    i, EUR = divmod(EUR, 1)
print("500유로:", a, "장(개)")
print("200유로:", b, "장(개)")
print("100유로:", c, "장(개)")
print("50유로:", d, "장(개)")
print("20유로:", e, "장(개)")
print("10유로:", f, "장(개)")
print("5유로:", g, "장(개)")
print("2유로:", h, "장(개)")
print("1유로:", i, "장(개)")  # 필요한 지폐(동전) 수 출력
print("Total: ", a+b+c+d+e+f+g+h+i, "장(개)")  # 개수 합계 출력
print("--------------------------------------------")

# 위안(CNY) 최소 화폐
while(CNY > 0):
    a, CNY = divmod(CNY, 100)
    b, CNY = divmod(CNY, 50)
    c, CNY = divmod(CNY, 20)
    d, CNY = divmod(CNY, 10)
    e, CNY = divmod(CNY, 5)
    # divmod함수를 이용해 몫과 나머지를 얻어서 각 지폐(동전)가 필요한 수를 몫으로, 나머지는 다름 지페 단위로 넘기는 과정을 통해 필요한 최소 지폐(동전)의 개수를 구할 수 있도록 했다.
    f, CNY = divmod(CNY, 1)
print("100위안:", a, "장(개)")
print("50위안:", b, "장(개)")
print("20위안:", c, "장(개)")
print("10위안:", d, "장(개)")
print("5위안:", e, "장(개)")
print("1위안:", f, "장(개)")  # 필요한 지폐(동전) 수 출력
print("Total: ", a+b+c+d+e+f, "장(개)")  # 개수 합계 출력
