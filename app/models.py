from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


class Ideas(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))


class List(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Idea_list =  Ideas.query.all()