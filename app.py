from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask.db"
db = SQLAlchemy(app)

class FlaskDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False) 
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = FlaskDB(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "Error adding the task"
    else:
        tasks = FlaskDB.query.order_by(FlaskDB.created_at).all()
        return render_template('index.html', tasks=tasks)

@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    task = FlaskDB.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['update-content']
        task.completed = 'completed' in request.form

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)

@app.route('/delete/<int:id>')
def delete(id):
    task_delete = FlaskDB.query.get_or_404(id)
    try:
        db.session.delete(task_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "Error deleting the task"

if __name__ == "__main__":
    app.run(debug=True)
