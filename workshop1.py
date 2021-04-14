from bs4 import BeautifulSoup
import urllib.request as req


def realtime_financial_data():
    result_dict = dict()

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
                result_dict[2] = num_USD
            elif i == 1:
                # 사이트에 100엔 기준이라 되어 있어 후처리(수정)
                num_JPY = float(name_price[i].text.replace(',', ''))/100
                result_dict[1] = num_JPY
            elif i == 2:
                num_EUR = float(name_price[i].text.replace(',', ''))
                result_dict[3] = num_EUR
            elif i == 3:
                num_CNY = float(name_price[i].text.replace(',', ''))
                result_dict[4] = num_CNY
            i = i + 1
        except IndexError:
            pass

        return result_dict


def converted_money_f(convert_num, korean_money, financial_dict):
    money = korean_money
    if convert_num == 1:
        JPY = int(float(money)/financial_dict[1])+1
        print(JPY, "엔")
        return JPY

    elif convert_num == 2:
        USD = int((float(money)/financial_dict[2])*100)+1
        print(USD/100, "달러")
        return USD

    elif convert_num == 3:
        EUR = int((float(money)/financial_dict[3])*100)+1
        print(EUR/100, "유로")
        return EUR

    else:
        CNY = int((float(money)/financial_dict[4])*10)+1
        print(CNY/10, "위안")
        return CNY


def min_counts(convert_num, converted_money):
    if convert_num == 1:
        JPY = converted_money
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

    elif convert_num == 2:
        USD = converted_money
        # 달러(USD) 최소 화폐
        while(USD > 0):
            a, USD = divmod(USD, 10000)
            b, USD = divmod(USD, 5000)
            c, USD = divmod(USD, 2000)
            d, USD = divmod(USD, 1000)
            e, USD = divmod(USD, 500)
            f, USD = divmod(USD, 200)
            g, USD = divmod(USD, 100)
            h, USD = divmod(USD, 50)
            i, USD = divmod(USD, 25)
            j, USD = divmod(USD, 10)
            k, USD = divmod(USD, 5)
            l, USD = divmod(USD, 1)
            # divmod함수를 이용해 몫과 나머지를 얻어서 각 지폐(동전)가 필요한 수를 몫으로, 나머지는 다름 지페 단위로 넘기는 과정을 통해 필요한 최소 지폐(동전)의 개수를 구할 수 있도록 했다.

        # 센트가 들어와 있지 않음 1(0.01), 5(0.05), 10(0.10), 25(0.25), 50(0.50)
        print("100달러:", a, "장(개)")
        print("50달러:", b, "장(개)")
        print("20달러:", c, "장(개)")
        print("10달러:", d, "장(개)")
        print("5달러:", e, "장(개)")
        print("2달러:", f, "장(개)")
        print("1달러:", g, "장(개)")
        print("50센트:", h, "장(개)")
        print("25센트:", i, "장(개)")
        print("10센트:", j, "장(개)")
        print("5센트:", k, "장(개)")
        print("1센트:", l, "장(개)")  # 필요한 지폐(동전) 수 출력
        print("Total: ", a+b+c+d+e+f+g+h+i+j+k+l, "장(개)")  # 개수 합계 출력
        print("--------------------------------------------")

    elif convert_num == 2:
        EUR = converted_money
        while(EUR > 0):
            a, EUR = divmod(EUR, 50000)
            b, EUR = divmod(EUR, 20000)
            c, EUR = divmod(EUR, 10000)
            d, EUR = divmod(EUR, 5000)
            e, EUR = divmod(EUR, 2000)
            f, EUR = divmod(EUR, 1000)
            g, EUR = divmod(EUR, 500)
            h, EUR = divmod(EUR, 200)
            i, EUR = divmod(EUR, 100)
            j, EUR = divmod(USD, 50)
            k, EUR = divmod(USD, 20)
            l, EUR = divmod(USD, 10)
            m, EUR = divmod(USD, 5)
            n, EUR = divmod(USD, 2)
            # divmod함수를 이용해 몫과 나머지를 얻어서 각 지폐(동전)가 필요한 수를 몫으로, 나머지는 다름 지페 단위로 넘기는 과정을 통해 필요한 최소 지폐(동전)의 개수를 구할 수 있도록 했다.
            o, EUR = divmod(USD, 1)

        # 센트가 들어와 있지 않음 1(0.01), 2(0.02), 5(0.05), 10(0.10), 20(0.25), 50(0.50)
        print("500유로:", a, "장(개)")
        print("200유로:", b, "장(개)")
        print("100유로:", c, "장(개)")
        print("50유로:", d, "장(개)")
        print("20유로:", e, "장(개)")
        print("10유로:", f, "장(개)")
        print("5유로:", g, "장(개)")
        print("2유로:", h, "장(개)")
        print("1유로:", i, "장(개)")  # 필요한 지폐(동전) 수 출력
        print("50센트:", j, "장(개)")
        print("20센트:", k, "장(개)")
        print("10센트:", l, "장(개)")
        print("5센트:", m, "장(개)")
        print("2센트:", n, "장(개)")
        print("1센트:", o, "장(개)")
        print("Total: ", a+b+c+d+e+f+g+h+i+j+k+l+m+n+o, "장(개)")  # 개수 합계 출력
        print("--------------------------------------------")

    elif convert_num == 4:
        CNY = converted_money
        # 위안(CNY) 최소 화폐
        while(CNY > 0):
            a, CNY = divmod(CNY, 1000)
            b, CNY = divmod(CNY, 500)
            c, CNY = divmod(CNY, 200)
            d, CNY = divmod(CNY, 100)
            e, CNY = divmod(CNY, 50)
            f, CNY = divmod(CNY, 10)
            g, CNY = divmod(CNY, 5)
            h, CNY = divmod(CNY, 1)

            # divmod함수를 이용해 몫과 나머지를 얻어서 각 지폐(동전)가 필요한 수를 몫으로, 나머지는 다름 지페 단위로 넘기는 과정을 통해 필요한 최소 지폐(동전)의 개수를 구할 수 있도록 했다.

        # 1자오(0.1) 5자오(0.5)
        print("100위안:", a, "장(개)")
        print("50위안:", b, "장(개)")
        print("20위안:", c, "장(개)")
        print("10위안:", d, "장(개)")
        print("5위안:", e, "장(개)")
        print("1위안:", f, "장(개)")
        print("5자오:", g, "장(개)")
        print("1자오:", h, "장(개)")  # 필요한 지폐(동전) 수 출력
        print("Total: ", a+b+c+d+e+f+g+h, "장(개)")  # 개수 합계 출력


def convert_num_to_code(convert_num):
    code_dict = {1: "JPY", 2: "USD", 3: "EUR", 4: "CNY"}
    return code_dict[convert_num]


def main():

    korean_money = int(input(
        "input money based on the korean currency unit(Won) you want to convert: "))
    print(f"Your input was {korean_money}")

    print("""
        ----------------------------------
        1. JPY
        2. USD
        3. EUR
        4. CNY
        ----------------------------------
        """)
    convert_num = eval(input("input number of country you want to convert: "))
    if convert_num in [1, 2, 3, 4]:
        country_code = convert_num_to_code(convert_num)
    else:
        print("wrong input")
        return

    default_financial_dict = {1: 10.2308, 2: 1115.0, 3: 1333.32, 4: 170.58}
    print(f"""
        -------------------------------------------------------------------------
        1. real time basis
        2. {country_code}: {default_financial_dict[convert_num]}
        -------------------------------------------------------------------------
        """)
    realtime_or_not = eval(input("input number you want to choose: "))

    if realtime_or_not == 1:
        realtime_financial_dict = realtime_financial_data()
        converted_money = converted_money_f(
            convert_num, korean_money, realtime_financial_dict)
        min_counts(convert_num, converted_money)
    elif realtime_or_not == 2:
        converted_money = converted_money_f(
            convert_num, korean_money, default_financial_dict)
        min_counts(convert_num, converted_money)
    else:
        print("wrong input")
        return


if __name__ == "__main__":
    main()
