import requests

def get_exchange_rates(currency_main,currency_convert):
    headers= {
     "apikey": "tdaZVBN91gy4QOXEsAiZY9PWWMENGZ5p"
    }
    payload ={}
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency_main}&symbol={currency_convert}"
    response = requests.request("GET", url, headers=headers, data = payload)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data['rates'][currency_convert]
    else:
        raise Exception(f"Error getting exchange rates: {response.status_code}!")
    
def calculate_profit(amount,buy,sell,exchange_rate):
    if buy == sell:
        return amount,0.0
    
    buy = amount/exchange_rate
    sell = amount/exchange_rate

    profit = sell - buy

    return round(profit,2)


#Test Case
amount = int(input("Enter Amount : "))
buy = input("Enter Currency to buy : ")
sell = input('Enter Currency to sell : ')

exchange_rate = get_exchange_rates(buy,sell)
profit = calculate_profit(amount,buy,sell,exchange_rate)
print(f"Profit from buying {amount} {buy} and selling in {sell} is : {profit}")