from flask import Flask, render_template
app = Flask(__name__)

#hardcode HTML
"""
@app.route('/')
def index():
    return '<html><body><h1>Hello guest!</h1></body></html>'
"""

#render html file
"""
@app.route('/hello/<user>')
def index(user):
    return render_template('hello.html', name = user)
"""
#if-else and endif using delimiter
@app.route('/hello/<int:score>')
def index(score):
    return render_template('hello.html', marks=score)

#forloop by passing dictionary
@app.route('/result')
def result():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('result.html', result = dict)

if __name__ == '__main__':
    app.run(debug = True)
