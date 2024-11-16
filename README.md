# flask-task-app
A simple Flask learning project which performs CRUD operations on tasks.

### Features
Create and update tasks.
Mark task as completed or pending.
Delete tasks.

### Project Setup 
##### Step 1: Clone the repository:
```
git clone https://github.com/SruthiKrish19/flask-task-app.git
```

##### Step 2: Create a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

##### Step 3: Install dependencies:
```
pip3 install -r requirements.txt
```

##### Step 4: Create the database:
Open a Python shell and run the following commands:
```
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
...     exit()
```

##### Step 5: Run the Flask app:
```
flask run
```
alternatively you can use
```
python app.py
```
Open the app in your browser: ```http://127.0.0.1:5000/```

### Demo Video
[Click here](https://drive.google.com/file/d/1XsuEwC-55cpowqzKAvwy-B7xEUn1zS5E/view?usp=sharing) to view the demo video!
