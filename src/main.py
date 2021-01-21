from flask import Flask
from flask_restful import Resource, Api, abort
from flask_sqlalchemy import SQLAlchemy
from apiArgsBuilder import buildArgsParser
from processCreditCardNumber import isValid, formatCreditCardNumber
import datetime

app = Flask(__name__)
api = Api(app)

config = buildArgsParser()
customerInfo = {}

def invalidAmount(amount):
    if amount <= 0:
        abort(400, message="Invalid Amount. Amount should be a float greater than 0.")

def customerNotInDB(customer_id):
    if customer_id not in customerInfo:
        abort(404, message="Customer with id {}".format(customer_id) + " not present in database.")

def customerInDB(customer_id):
    if customer_id in customerInfo:
        abort(409, message="Customer with id {}".format(customer_id) + " already present in database.")

def invalidCreditCardNumber(creditCardNumber):
    if not isValid(creditCardNumber):
        abort(400, message="Invalid credit card number.")
    else:
        return formatCreditCardNumber(creditCardNumber)

def invalidExpirationDate(dateString):
    try:
        date_obj = datetime.datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S.%f")

        if not (date_obj > datetime.datetime.now()):
            abort(400, message="Provided expiration date is in the past.")
    except ValueError:
        abort(400, message="Provided expiration date is in the wrong format.")

def invalidSecurityCode(securityCode):
    securityCode = str(securityCode).strip()

    if not (securityCode.isdigit() and len(securityCode) == 3):
        abort(400, message="Invalid security code. Security code must be provided as a string and should be a valid security code (3-digit code).")
    

class ProcessPayment(Resource):
    def get(self, customer_id):
        customerNotInDB(customer_id)
        return customerInfo[customer_id]

    def put(self, customer_id):
        customerInDB(customer_id)
 
        args = config.parse_args()
        creditCardNumber = invalidCreditCardNumber(args["CreditCardNumber"])
        invalidAmount(args["Amount"])
        invalidExpirationDate(args["ExpirationDate"])
        invalidSecurityCode(args["SecurityCode"])

        args["CreditCardNumber"] = creditCardNumber
        
        customerInfo[customer_id] = args
        return customerInfo[customer_id], 201

    def delete(self, customer_id):
        customerNotInDB(customer_id)
        del customerInfo[customer_id]
        return "", 204

api.add_resource(ProcessPayment, "/Customer/<int:customer_id>")

if __name__ == "__main__":
    app.run(debug=True)