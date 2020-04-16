from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    students = db.relationship('Student', backref='user', lazy='dynamic')
    def __repr__(self):
        return '<User {}>'.format(self.username)
    

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    wand = db.Column(db.String(64))
    patronus = db.Column(db.String(64))
    house = db.Column(db.String(64))
    def __repr__(self):
        return '<Student {}>'.format(self.last_name)