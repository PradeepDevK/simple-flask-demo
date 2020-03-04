from flask import Flask, request, make_response
app = Flask(__name__)

#Simple get api
@app.route('/')
def hello_world():
    return 'Hello World, My first app in Flask'
app.add_url_rule('/', 'hello', hello_world)
app.view_functions['hello'] = hello_world

#Flask routers with HTTP methods
@app.route('/api/v1/userTest', methods=['GET', 'POST'])
def userTest():
    if request.method == 'GET':
        return 'Its a GET request'
    if request.method == 'POST':
        return 'Its a POST request'

#variables in the routes
@app.route('/api/v1/varTest/<string:name>')
def varTest(name):
    return 'variable value is %s!' % name

if __name__ == '__main__':
    app.run(debug = True)
