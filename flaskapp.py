from flask import Flask
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        data = pd.read_csv('users.csv')  
        data = data.to_dict('records')
        return {'data': data}, 200

class Name(Resource):
    def get(self, name):
        data = pd.read_csv('users.csv')  
        data = data.to_dict('records')
        for entry in data:
            if entry['name'] == name:
                return {'data': entry}, 200
        return {'message': 'Bu isimle ilgili giriş bulunamadı!'}, 404

api.add_resource(Users, '/users')
api.add_resource(Name, '/isim/<string:name>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)