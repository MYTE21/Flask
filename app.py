"""
Flask: An instance of this class will be our WSGI application.
render_template: render_template is used to generate output from a template file.
request: The requests library is for your app to make HTTP request.
redirect: Returns a response object that, if called, redirects the client to the target location.
"""
from flask import Flask, render_template, request, redirect
# SQLAlchemy: An SQL toolkit that provides efficient and high-performing database access for relational databases.
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime   # datetime: Work with dates and times.


app = Flask(__name__)   # creates a Flask application object 'app' in the current Python module.
# SQLALCHEMY_DATABASE_URI: The database URI that should be used for the connection.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


# Create a model class
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as ex:
            ex_message = ex.args[0]
            return 'There was an issue adding your task...!', ex_message

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as ex:
        ex_message = ex.args[0]
        return 'There was a problem deleting the task...!', ex_message


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except Exception as ex:
            ex_message = ex.args[0]
            return 'There was a problem updating the task', ex_message
    else:
        return render_template('update.html', task=task)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
