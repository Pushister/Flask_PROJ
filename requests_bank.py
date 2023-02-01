import requests
import datetime
from sqlalchemy.orm import Session
import models_db
import al_db


def get_privatbank_data():
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    db_date = datetime.datetime.now().strftime('%Y-%m-%d')
    r = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={current_date}')

    currency_info = r.json()

    saleRate_USD = 0
    purchaseRate_USD = 0

    for c in currency_info['exchangeRate']:
        if c['currency'] == 'USD':
            saleRate_USD = c['saleRate']
            purchaseRate_USD = c['purchaseRate']

    with Session(al_db.engine) as session:
        for c in currency_info['exchangeRate']:
            currency_name =  c['currency']
            if c.get('saleRate'):
                saleRate_currency =  c['saleRate']/saleRate_USD
                purchaseRate_currency = purchaseRate_USD / c['purchaseRate']
                print(f"{currency_name}, {saleRate_currency}, {purchaseRate_currency}")
                record = models_db.User(bank='PrivatBank',
                                        currency=currency_name,
                                        date_exchange=db_date,
                                        buy_rate=purchaseRate_currency,
                                        sale_rate=saleRate_currency
                                        )
                session.add(record)
                session.commit()