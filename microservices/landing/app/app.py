from webbrowser import Opera
from flask import Flask,request,flash,render_template
from flask_restful import Api

#flask need to import targets to use as funcitons
from add.app.app import Add





app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)


api.add_resource(Add, '/add/<int:num1>/<int:num2>')
#api.add_resource(Subtraction, '/subtract/<int:num1>/<int:num2>')
#api.add_resource(Multiplication, '/multiply/<int:num1>/<int:num2>')
#api.add_resource(Division, '/divide/<int:num1>/<int:num2>')



def minus(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

@app.route('/', methods=['POST', 'GET'])
def index():
    operation = request.form.get('operation')
    try:
        number_1 = int(request.form.get("first"))
        number_2 = int(request.form.get('second'))
        result = 0
        if operation == 'add':
            Add_instance = Add()
            result = Add_instance.get(number_1, number_2)
        elif operation == 'minus':
            result =  minus(number_1, number_2)
        elif operation == 'multiply':
            result = multiply(number_1, number_2)
        elif operation == 'divide':
            result = divide(number_1, number_2)
    except Exception as e:
        number_1 = "Error"
        number_2 = "Error"
        result = f"Error: {e}"


    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )