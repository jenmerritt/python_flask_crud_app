from app import app, db
from app.models import User, Student
from flask import render_template

@app.route('/')
def root():
    user = User.query.get(1)
    return render_template('root.html', user=user)

@app.route('/students')
def index():
    user = User.query.get(1)
    students = user.students
    return render_template('index.html', user=user, students=students)

@app.route('/students/<int:student_id>')
def show(student_id):
    student = Student.query.get(student_id)
    return render_template('show.html', student=student)

