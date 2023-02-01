data = [
        {'bank': 'a1', 'currency': 'UAH', 'buy_rate': 1.05, 'sale_rate': 0.95},
        {'bank': 'a1', 'currency': 'USD', 'buy_rate': 1.05, 'sale_rate': 0.95},
        {'bank': 'a1', 'currency': 'EUR', 'buy_rate': 1.05, 'sale_rate': 0.95},
        {'bank': 'a1', 'currency': 'GPB', 'buy_rate': 1.05, 'sale_rate': 0.95},
    ]


for i in data:
    print(i['bank'])
    print(i['currency'])
    print(i['buy_rate'])
    print(i['sale_rate'])