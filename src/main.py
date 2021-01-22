from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from apiArgsBuilder import buildArgsParser
from mainApiLogic import invalidAmount, invalidCreditCardNumber, invalidExpirationDate, invalidSecurityCode, gateway, invalidID
from datetime import datetime
import requests

app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

config = buildArgsParser()

resource_fields = {
    "id" : fields.Integer,
    "CreditCardNumber" : fields.String,
    "CardHolder" : fields.String,
    "ExpirationDate" : fields.DateTime,
    "SecurityCode" : fields.String,
    "Amount" : fields.Float,
    "PaymentGateway" : fields.String
}

config = buildArgsParser()

class PaymentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CreditCardNumber = db.Column(db.String(16), nullable=False)
    CardHolder = db.Column(db.String(30), nullable=False)
    ExpirationDate = db.Column(db.DateTime, nullable=False)
    SecurityCode = db.Column(db.String(3), nullable=True)
    Amount = db.Column(db.Float, nullable=False)
    PaymentGateway = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"Payment(Card holder = {name}, Expiration date = {expirationDate}, Security code = {securityCode}, Amoun = {amount})"

class Transaction(Resource):
    @marshal_with(resource_fields)
    def get(self, transaction_id):
        result = PaymentModel.query.filter_by(id=transaction_id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, transaction_id):
        args = config.parse_args()

        invalidID(transaction_id)

        invalidAmount(args["Amount"])
        validGateway = gateway(args["Amount"])

        cardNumber = invalidCreditCardNumber(args["CreditCardNumber"])

        invalidExpirationDate(args["ExpirationDate"])
        invalidSecurityCode(args["SecurityCode"])

        Transaction = PaymentModel(
            id=transaction_id, 
            CreditCardNumber = cardNumber,
            CardHolder=args["CardHolder"],
            ExpirationDate=datetime.strptime(args["ExpirationDate"], "%Y-%m"), 
            SecurityCode=args["SecurityCode"], 
            Amount=args["Amount"],
            PaymentGateway=validGateway
            )

        db.session.add(Transaction)
        db.session.commit()

        return Transaction, 201

db.create_all()
api.add_resource(Transaction, "/transaction/<int:transaction_id>")

if __name__ == "__main__":
    app.run(debug=True)