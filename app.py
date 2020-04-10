import config as cfg
from flask import Flask, jsonify
# from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from model import Stocks, Etfs, Indices

app = Flask(__name__)

# mysql = MySQL(app)
# app.config['MYSQL_USER'] = cfg.dbLogin['user']
# app.config['MYSQL_PASSWORD'] = cfg.dbLogin['pass']
# app.config['MYSQL_HOST'] = cfg.dbLogin['host']
# app.config['MYSQL_DB'] = cfg.dbLogin['db']

app.config['SQLALCHEMY_DATABASE_URI'] = cfg.sqlalchemy['url']
db = SQLAlchemy(app)
ma = Marshmallow(app)

class EtfsSchema(ma.ModelSchema):
    class Meta:
        model = Etfs

class IndicesSchema(ma.ModelSchema):
    class Meta:
        model = Indices

class StocksSchema(ma.ModelSchema):
    class Meta:
        model = Stocks


@app.route('/')
def index():
    return 'Nothing can be found here be on your way!'

'''
Get request for all Stocks from all dates
'''
@app.route('/stocks', methods=['GET'])
def get_all_stocks():
    stocks = Stocks.query.all()
    stocks_schema = StocksSchema(many=True)
    output = stocks_schema.dump(stocks)
    return jsonify(output)
'''
Get request for stocks on specific date
'''
@app.route('/stocks/<dateInserted>', methods=['GET'])
def get_date_stocks(dateInserted):
    stocks = Stocks.query.filter_by(Date_Inserted = dateInserted)
    stocks_schema = StocksSchema(many=True)
    output = stocks_schema.dump(stocks)
    return jsonify(output)


@app.route('/etfs', methods=['GET'])
def get_all_etfs():
    etfs = Etfs.query.all()
    etfs_schema = EtfsSchema(many=True)
    output = etfs_schema.dump(etfs)
    return jsonify(output)

@app.route('/etfs/<dateInserted>', methods=['GET'])
def get_date_etfs(dateInserted):
    etfs = Etfs.query.filter_by(Date_Inserted = dateInserted)
    etfs_schema = EtfsSchema(many=True)
    output = etfs_schema.dump(etfs)
    return jsonify(output)


@app.route('/indices', methods=['GET'])
def get_all_indices():
    indices = Indices.query.all()
    indices_schema = IndicesSchema(many=True)
    output = indices_schema.dump(indices)
    return jsonify(output)

@app.route('/indices/<dateInserted>', methods=['GET'])
def get_date_indices(dateInserted):
    indices = Indices.query.filter_by(Date_Inserted = dateInserted)
    indices_schema = IndicesSchema(many=True)
    output = indices_schema.dump(indices)
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)