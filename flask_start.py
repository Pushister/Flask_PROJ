from flask import Flask
from flask import request, render_template
from database_function import DBManager
from worker import get_bank_data_task
import al_db
import models_db
from sqlalchemy import select
from sqlalchemy.orm import Session

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        with Session(al_db.engine) as session:
            query = select(models_db.User)
            result = session.execute(query).fetchall()
        return str(result)
        #conn = al_db.engine.connect()
        #res_1 = select([models_db.User])
        #result = conn.execute(res_1)
        #data_res = result.fetchall()
        #print(result)
        #pass
    else:
        pass
    return "OK"


@app.route("/logout", methods=['GET'])
def logout():
    get_bank_data_task()
    return "Logout"


@app.route("/register", methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['psw']
        email = request.form['email']

        with Session(al_db.engine) as session:
            record = models_db.UserName(username=username,
                                        password=password,
                                        email=email
                                        )
            session.add(record)
            session.commit()

        return "Thank you"

    return render_template('registr_form.html')


@app.route("/user_page", methods=['GET'])
def user_page():
    return "OK"


@app.route("/currency", methods=['GET', 'POST'])
def currency_converter():

    if request.method == 'POST':
        user_bank = request.form['bank']
        user_currency_1 = request.form['currency_1']
        user_date = request.form['date']
        user_currency_2 = request.form['currency_2']

        with Session(al_db.engine) as session:
            statement_1 = select(models_db.User).filter_by(bank=user_bank,
                                                           currency=user_currency_1,
                                                           date_exchange=user_date)
            currency_1 = session.scalars(statement_1).first()

            statement_2 = select(models_db.User).filter_by(bank=user_bank,
                                                           currency=user_currency_2,
                                                           date_exchange=user_date)
            currency_2 = session.scalars(statement_2).first()

        #with DBManager() as db:
        #    buy_rate_1, sale_rate_1 = db.get_result(f'SELECT buy_rate, sale_rate FROM currency WHERE '
        #                                            f'bank = "{user_bank}" and date_excange = '
        #                                            f'"{user_date}" and currency = "{user_currency_1}"')
        #    buy_rate_2, sale_rate_2 = db.get_result(f'SELECT buy_rate, sale_rate FROM currency WHERE '
        #                                            f'bank = "{user_bank}" and date_excange = '
        #                                            f'"{user_date}" and currency = "{user_currency_2}"')

        buy_rate_1, sale_rate_1 = currency_1.buy_rate, currency_1.sale_rate
        buy_rate_2, sale_rate_2 = currency_2.buy_rate, currency_2.sale_rate
        cur_exchange_buy = float(buy_rate_2) / float(buy_rate_1)
        cur_exchange_sale = float(sale_rate_2) / float(sale_rate_1)

        return render_template('data_form.html',
                               cur_excange_buy=cur_exchange_buy,
                               cur_excange_sale=cur_exchange_sale,
                               user_currency_1=user_currency_1,
                               user_currency_2=user_currency_2
                               )
    else:
        return render_template('data_form.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)


