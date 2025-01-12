#Make sure to not call your application flask.py because this would conflict with Flask itself.
#to activate venv use ".\env\Scripts\Activate"
#to run app use "python app.py"

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

#SQLAlchemy is an ORM (object relational mapper) ORM is a tool that allows developers to interact
#with databases using object-oriented programming instead of writing raw SQL queries.
#ORMs map database tables to Python classes, and rows to instances of those classes.
#Define tables as Python classes.
#Access rows as Python objects.

app = Flask(__name__, instance_relative_config=True)
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///test.db' #/// is relative path, //// is absolute path
db = SQLAlchemy(app)

#set local timezone
local_tz = pytz.timezone('Asia/Kolkata')

@app.cli.command("create-db")
def create_db():
    """Create the database tables."""
    db.create_all()
    print("Database tables created.")

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False) #so that empty tasks can't be created.
    data_created = db.Column(db.DateTime, default=datetime.now)
#should be date_created but accidentally pushed data_created in the db.
    def __repr__(self):
        return '<Task %r>' %self.id
    
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content'] #retrieves data from fields having name attribute 'content'.
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task.'
    else:
        try:
            tasks = Todo.query.order_by(Todo.data_created).all()
            # convert UTC to local timezone
            for task in tasks:
                task.data_created = task.data_created.replace(tzinfo=pytz.utc).astimezone(local_tz)
            return render_template('index.html', tasks=tasks)
        except:
            return 'There was an issue displaying your tasks.'
    
@app.route('/delete/<int:id>')
def delete(id):
    task_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task.'
    
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    update_task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        update_task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task.'
    else:
        return render_template('update.html', task=update_task)

if __name__ == "__main__":
    app.run()