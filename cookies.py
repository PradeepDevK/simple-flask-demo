from flask import Flask, render_template, make_response, request, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexCookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readCookie.html'))
        resp.set_cookie('userID', user)
        return resp

@app.route('/getCookie')
def getCookie():
    name = request.cookies.get('userID')
    return '<h1>Welcome '+ name + '</h1>'

if __name__ == '__main__':
    app.run(debug = True)
