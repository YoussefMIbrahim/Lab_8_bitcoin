import requests 
from pprint import pprint 


def main():

    bitcoin = get_bitcoin_amount()
    # dollars_exchange_rate = request_bitcoin_rate()
    value_in_dollars = convert_bitcoin_value(bitcoin)
    print_results(bitcoin, value_in_dollars)


def get_bitcoin_amount():

    return float(input('Enter the number of bitcoin: '))

def print_results(bitcoin, value_in_dollars):

    print(f'{bitcoin} Bitcoin is equivalent to ${value_in_dollars}')


def request_bitcoin_rate():

    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    response = requests.get(coindesk_url)
    data = response.json()

    return data
    

def convert_bitcoin_value(bitcoin):
    
    dollars_exchange_rate = request_bitcoin_rate()['bpi']['USD']['rate_float']

    return bitcoin * dollars_exchange_rate


if __name__ == '__main__':
    main()