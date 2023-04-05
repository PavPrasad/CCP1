from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Mul(Resource):

    def get(self, num1, num2):
        result = num1 * num2
        return result


api.add_resource(Mul, '/mul/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
