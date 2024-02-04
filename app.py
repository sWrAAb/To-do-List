import os
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'to-do.db')
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/To-do-List', methods=['POST', 'GET'])
def TodoList():
    return render_template('To-do-List.html')

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

def create_app():
    # Check if the database file exists
    if not os.path.exists('todo.db'):
        with app.app_context():
            # Create the database tables
            print('Creating Database')
            db.create_all()

    return app

create_app()


if __name__ == '__main__':
    app.run(debug=True)
