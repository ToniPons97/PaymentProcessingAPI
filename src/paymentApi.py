from flask import Flask
from flask_restful import Resource, Api, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardHolder = db.Column(db.String(30), nullable=False)
    expirationDate = db.Column(db.DateTime, nullable=False)
    securityCode = db.Column(db.String(3), nullable=True)
    amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Payment(Card holder = {name}, Expiration date = {expirationDate}, Security code = {securityCode}, Amoun = {amount})"


class 

#This should be ran once
db.create_all()






if __name__=="__main__":
    app.run(port=5001, debug=True)