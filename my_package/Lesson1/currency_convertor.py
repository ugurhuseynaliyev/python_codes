def currencyConvertor():
    amount = float(input('Enter amount of money: '))
    source_currency = input('Enter source currency (AZN, USD, EUR): ')
    target_currency = input('Enter target currency (AZN, USD, EUR): ')
    target_currencies = ['AZN', 'USD', 'EUR']
    source_currencies = ['AZN', 'USD', 'EUR']

    if not(source_currency in source_currencies) or not(target_currency in target_currencies):
        print('Invalid input!')
    elif source_currency == 'AZN' and target_currency == 'USD':
        print(f'Converted from {source_currency} to {target_currency} => {round(amount * 0.5885, 2)} {target_currency}')
    elif source_currency == 'AZN' and target_currency == 'EUR':
        print(f'Converted from {source_currency} to {target_currency} => {round(amount * 0.5646, 2)} {target_currency}')
    elif source_currency == 'USD' and target_currency == 'AZN':
        print(f'Converted from {source_currency} to {target_currency} => {round(amount * 1.70035, 2)} {target_currency}')
    elif source_currency == 'USD' and target_currency == 'EUR':
        print(f'Converted from {source_currency} to {target_currency} => {round(amount * 0.944, 2)} {target_currency}')
    elif source_currency == 'EUR' and target_currency == 'AZN':
        print(f'Converted from {source_currency} to {target_currency} => {round(amount * 1.7713, 2)} {target_currency}')
    elif source_currency == 'EUR' and target_currency == 'USD':
        print(f'Converted from {source_currency} to {target_currency} => {round(amount * 1.059, 2)} {target_currency}')
currencyConvertor()