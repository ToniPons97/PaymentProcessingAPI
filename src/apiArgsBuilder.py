from flask_restful import reqparse

def buildArgsParser():
    paymentArgs = reqparse.RequestParser()
    paymentArgs.add_argument("CreditCardNumber", type=str, help="CreditCardNumber is required and must be of type string." , required=True)
    paymentArgs.add_argument("CardHolder", type=str, help="CardHolder is required and must be of type string.", required=True)
    paymentArgs.add_argument("ExpirationDate", type=str, help="ExpirationDate is required and must be of type string.", required=True)
    paymentArgs.add_argument("SecurityCode", type=str, help="SecurityCode is not required but must be of type string if provided.", required=False)
    paymentArgs.add_argument("Amount", type=float, help="Amount is required (type = float).", required=True)
    return paymentArgs
