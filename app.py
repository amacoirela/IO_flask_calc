"""This is a script for a calculator app"""


from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/calculate')
def hello_world():  # put application's code here
    """this is the function which is used for creating a calculator"""
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)
    return f'{op}: {arg1} + {arg2} = {arg1 + arg2}'


if __name__ == '__main__':
    app.run()
