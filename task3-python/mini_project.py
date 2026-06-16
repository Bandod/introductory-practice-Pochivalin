RUB_RATE = 1.0
USD_RATE = 72.5
EUR_RATE = 83.2

def convert_currency(amount, from_curr, to_curr):
    rates = {'RUB': RUB_RATE, 'USD': USD_RATE, 'EUR': EUR_RATE}

    if from_curr not in rates or to_curr not in rates:
        return None
    amount_in_rub = amount * rates[from_curr]
    result = amount_in_rub /rates[to_curr]
    return round(result, 2)

print("=== Простой конвертер валют ===")
try:
    amount = float(input("Введите сумму:"))
except ValueError:
    print("Ощибка: сумма должна быть числом.")
else:
    from_currency = input("Из какой валюты (RUB, USD, EUR)?").upper()
    to_currency = input("В какую валюту (RUB, USD, EUR)?").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    
    if converted_amount is None:
        print("Недопустимый код валюты. Используйте RUB, USD или EUR.")
    else:
        print(f"Результат: {amount}{from_currency}={converted_amount}{to_currency}")
        
