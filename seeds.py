from app import db
from app.models import User, Student

Student.query.delete()
User.query.delete()

user = User(username='Default User')
db.session.add(user)
db.session.commit()

users = User.query.all()
print(users)

student1 = Student(first_name='Harry', last_name="Potter", wand="Elder Wand", patronus="Stag", house="Gryffindor", user=user)
db.session.add(student1)
student2 = Student(first_name='Hermione', last_name="Grainger", wand="Dragon Heartstring", patronus="Otter", house="Gryffindor", user=user)
db.session.add(student2)
student3 = Student(first_name='Ron', last_name="Weasley", wand="Unicorn Hair", patronus="Jack Russell Terrier", house="Gryffindor", user=user)
db.session.add(student3)
db.session.commit()

students = Student.query.all()
print(students)

student_user = Student.query.get(1).user
print(user.username)