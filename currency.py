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
        #print(data)
        return data['rates'][currency_convert]
    else:
        raise Exception(f"Error getting exchange rates: {response.status_code}!")
    
def calculate_profit(amount,buy,sell,exchange_rate):
    if buy == sell:
        return amount,0.0
    
    buy = amount*exchange_rate
    # print(buy)
    sell = amount/exchange_rate
    # print(sell)
    profit = buy

    return round(profit,2)


#Test Case
amount = int(input("Enter Amount : "))
original = amount
buy_currencies = ['GBP','USD','EUR' ]
selling_currency = 'PKR'
original_curr = selling_currency

total_profit = 0.0
for currency in buy_currencies:
    exchange_rate = get_exchange_rates(selling_currency,currency)
    profit = calculate_profit(amount,selling_currency, currency, exchange_rate)
    print(f"Buying {amount} {selling_currency}  for {currency}: {profit}")
    amount = profit
    selling_currency= currency
    total_profit = profit

# print(f"Total profit: {total_profit}")

exchange_rate = get_exchange_rates(selling_currency,original_curr)
profit = calculate_profit(amount,selling_currency,original_curr,exchange_rate)

print(f"Converting it back to original : {profit} {original_curr}")

profit -= original

print(f"Total profit: {profit} {original_curr}")