from sqlalchemy import Column, Integer, String, Float
from al_db import Base


class User(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True, unique=True)
    bank = Column(String(50))
    currency = Column(String(120))
    date_exchange = Column(String(120))
    buy_rate = Column(Float)
    sale_rate = Column(Float)

    def __init__(self, bank, currency, date_exchange, buy_rate, sale_rate):
        self.bank = bank
        self.currency = currency
        self.date_exchange = date_exchange
        self.buy_rate = buy_rate
        self.sale_rate = sale_rate

    def __repr__(self):
        return f'<User {self.bank!r}>'


class UserName(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(50))
    password = Column(String(120))
    email = Column(String(120))

    def __init__(self, username, password, email=None, first_name=None, surname=None):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.surname = surname

    def __repr__(self):
        return f'<User{self.username!r}>'

