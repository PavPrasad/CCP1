from flask import Flask, request, flash, render_template
from flask_restful import Api

#flask need to import targets to use as funcitons
from add.app.app import Add
from sub.app.app import Sub
from mul.app.app import Mul
from div.app.app import Div
from exp.app.app import Exp
from mod.app.app import Mod
from equ.app.app import Equ

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)

api.add_resource(Add, '/add/<int:num1>/<int:num2>')
api.add_resource(Sub, '/sub/<int:num1>/<int:num2>')
api.add_resource(Mul, '/mul/<int:num1>/<int:num2>')
api.add_resource(Div, '/div/<int:num1>/<int:num2>')
api.add_resource(Exp, '/exp/<int:num1>/<int:num2>')
api.add_resource(Mod, '/mod/<int:num1>/<int:num2>')
api.add_resource(Equ, '/equ/<int:num1>/<int:num2>')


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
            Sub_instance = Sub()
            result = Sub_instance.get(number_1, number_2)
        elif operation == 'multiply':
            Mul_instance = Mul()
            result = Mul_instance.get(number_1, number_2)
        elif operation == 'divide':
            Div_instance = Div()
            result = Div_instance.get(number_1, number_2)
        elif operation == 'exponent':
            Exp_instance = Exp()
            result = Exp_instance.get(number_1, number_2)
        elif operation == 'modulus':
            Mod_instance = Mod()
            result = Mod_instance.get(number_1, number_2)
        elif operation == 'equals':
            Equ_instance = Equ()
            result = Equ_instance.get(number_1, number_2)
    except Exception as e:
        number_1 = "Error"
        number_2 = "Error"
        result = f"Error: {e}"

    flash(
        f'The result of operation {operation} on {number_1} and {number_2} is {result}'
    )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5050, host="0.0.0.0")
