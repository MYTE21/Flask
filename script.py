from flask import *

app = Flask(__name__)


@app.route('/admin')
def admin():
    return 'admin'


@app.route('/librarian')
def librarian():
    return 'librarian'


@app.route('/student')
def student():
    return 'student'


@app.route('/user/<name>')
def user(name):
    route_name = ['admin', 'librarian', 'student']
    for route in route_name:
        if name == route:
            return redirect(url_for(route))


if __name__ == '__main__':
    app.run(debug=True)