from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()

class Etfs(db.Model):
    __tablename__ = 'etfs'
    ID = db.Column(db.Integer, primary_key=True)
    Date_Inserted = db.Column('Date Inserted', db.Date, nullable=False)
    Symbol = db.Column(db.Text, nullable=False)
    Price = db.Column(db.DECIMAL(10, 2), nullable=False)
    Type = db.Column(db.Text, nullable=False)
    Strike = db.Column(db.DECIMAL(10, 2), nullable=False)
    Exp_Date = db.Column('Exp Date', db.Date, nullable=False)
    DTE = db.Column(db.Integer, nullable=False)
    Bid = db.Column(db.DECIMAL(10, 2), nullable=False)
    Midpoint = db.Column(db.DECIMAL(10, 2), nullable=False)
    Ask = db.Column(db.DECIMAL(10, 2), nullable=False)
    Last = db.Column(db.DECIMAL(10, 2), nullable=False)
    Volume = db.Column(db.Integer, nullable=False)
    Open_Int = db.Column('Open Int', db.Integer, nullable=False)
    Vol_OI = db.Column('Vol/OI', db.DECIMAL(10, 2), nullable=False)
    IV = db.Column(db.DECIMAL(5, 2), nullable=False)
    Time = db.Column(db.Time, nullable=False)

class Indices(db.Model):
    __tablename__ = 'indices'
    ID = db.Column(db.Integer, primary_key=True)
    Date_Inserted = db.Column('Date Inserted', db.Date, nullable=False)
    Symbol = db.Column(db.Text, nullable=False)
    Price = db.Column(db.DECIMAL(10, 2), nullable=False)
    Type = db.Column(db.Text, nullable=False)
    Strike = db.Column(db.DECIMAL(10, 2), nullable=False)
    Exp_Date = db.Column('Exp Date', db.Date, nullable=False)
    DTE = db.Column(db.Integer, nullable=False)
    Bid = db.Column(db.DECIMAL(10, 2), nullable=False)
    Midpoint = db.Column(db.DECIMAL(10, 2), nullable=False)
    Ask = db.Column(db.DECIMAL(10, 2), nullable=False)
    Last = db.Column(db.DECIMAL(10, 2), nullable=False)
    Volume = db.Column(db.Integer, nullable=False)
    Open_Int = db.Column('Open Int', db.Integer, nullable=False)
    Vol_OI = db.Column('Vol/OI', db.DECIMAL(10, 2), nullable=False)
    IV = db.Column(db.DECIMAL(5, 2), nullable=False)
    Time = db.Column(db.Time, nullable=False)


class Stocks(db.Model):
    __tablename__ = 'stocks'
    ID = db.Column(db.Integer, primary_key=True)
    Date_Inserted = db.Column('Date Inserted', db.Date, nullable=False)
    Symbol = db.Column(db.Text, nullable=False)
    Price = db.Column(db.DECIMAL(10, 2), nullable=False)
    Type = db.Column(db.Text, nullable=False)
    Strike = db.Column(db.DECIMAL(10, 2), nullable=False)
    Exp_Date = db.Column('Exp Date', db.Date, nullable=False)
    DTE = db.Column(db.Integer, nullable=False)
    Bid = db.Column(db.DECIMAL(10, 2), nullable=False)
    Midpoint = db.Column(db.DECIMAL(10, 2), nullable=False)
    Ask = db.Column(db.DECIMAL(10, 2), nullable=False)
    Last = db.Column(db.DECIMAL(10, 2), nullable=False)
    Volume = db.Column(db.Integer, nullable=False)
    Open_Int = db.Column('Open Int', db.Integer, nullable=False)
    Vol_OI = db.Column('Vol/OI', db.DECIMAL(10, 2), nullable=False)
    IV = db.Column(db.DECIMAL(5, 2), nullable=False)
    Time = db.Column(db.Time, nullable=False)

