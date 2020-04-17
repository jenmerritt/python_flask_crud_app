from app import app, db
from app.models import User, Student
from flask import render_template, redirect, request

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

@app.route('/students/new')
def new():
    return render_template('new.html')

@app.route('/students', methods=['POST'])
def create():
  user = User.query.get(1)
  first_name = request.form['first_name']
  last_name = request.form['last_name']
  house = request.form['house']
  wand = request.form['wand']
  patronus = request.form['patronus']
  new_student = Student(user_id=user.id, first_name=first_name, last_name=last_name, wand=wand, patronus=patronus, house=house)
  db.session.add(new_student)
  db.session.commit()
  return redirect('/students')

@app.route('/students/<int:student_id>/delete', methods=['POST'])
def destroy(student_id):
    student = Student.query.get(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/students')

