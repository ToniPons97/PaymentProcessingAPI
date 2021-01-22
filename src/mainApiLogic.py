from flask_restful import abort
from processCreditCardNumber import isValid, formatCreditCardNumber
from datetime import datetime

def invalidID(transaction_id):
    if transaction_id < 0 or type(transaction_id) != int:
        abort(400, message="id should be a positiva integer.")

def invalidAmount(amount):
    if amount <= 10:
        abort(400, message="Invalid Amount. Transfer amount must be at least 10.")

def invalidCreditCardNumber(creditCardNumber):
    if not isValid(creditCardNumber):
        abort(400, message="Invalid credit card number.")
    else:
        return formatCreditCardNumber(creditCardNumber)

def invalidExpirationDate(dateString):
    try:
        date_obj = datetime.strptime(dateString, "%Y-%m")
        if not (date_obj > datetime.now()):
            abort(400, message="Provided expiration date is in the past.")
    except ValueError:
        abort(400, message="Provided expiration date is in the wrong format.")

def invalidSecurityCode(securityCode):
    securityCode = str(securityCode).strip()

    if not (securityCode.isdigit() and len(securityCode) == 3):
        abort(400, message="Invalid security code. Security code must be provided as a string and should be a valid security code (3-digit code).")

def gateway(amount):
    options = ["PremiumPaymentGateway", "ExpensivePaymentGateway", "CheapPaymentGateway"]
    if amount <= 20:
        return options[2]
    elif amount <= 500 and amount > 20:
        return options[1]
    else:
        return options[0]

    