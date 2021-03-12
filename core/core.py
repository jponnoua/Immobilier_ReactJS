from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

class Appartment: 
    def __init__(self, in_value, in_property_tax, in_coownership_tax, in_monthly_rental_value):
        self.m_value = in_value
        self.m_property_tax = in_property_tax
        self.m_coownership_tax = in_coownership_tax
        self.m_monthly_rental_value = in_monthly_rental_value

class Bank:
    def __init__(self, in_interest_rate, in_insurance_rate, in_loan, in_loan_duration):
        self.m_interest_rate = in_interest_rate
        self.m_insurance_rate = in_insurance_rate
        self.m_loan = in_loan
        self.m_loan_duration = in_loan_duration

    def amortization_table_get(self):
        self.m_amortization_table = 0

    m_debt_ratio_max = 0.33

class Personal:
    def __init__(self, in_income, in_savings):
        self.m_income = in_income
        self.m_savings = in_savings

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('connect')
def test_connect():
    print('Client ' + request.sid + ' connected')
    emit('connection_valid', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client ' + request.sid + ' disconnected')

if __name__ == '__main__':
    socketio.run(app, port=5000)