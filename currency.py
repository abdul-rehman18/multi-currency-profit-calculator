import requests

def get_exchange_rates(currency_main,currency_convert):
    api = 'tdaZVBN91gy4QOXEsAiZY9PWWMENGZ5p'
    url = f'https://api.exchangeratesapi.io/live?base={currency_main}&symbol={currency_convert}'
    response = requests.get(url,headers={'Authorization' : f'Bearer {api}'})

    if response.status_code == 200:
        data = response.json()
        return data['rates'][currency_convert]
    else:
        raise Exception(f"Error getting exchange rates: {response.status_code}!")
    
def calculate_profit(amount,buy,sell,exchange_rate):
    