""" models.py """
from flask_security import RoleMixin, UserMixin
from .extensions import db


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    order = db.Column(db.Integer)
    completed = db.Column(db.Boolean)

    def __unicode__(self):
        return self.title

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "order": self.order,
            "completed": self.completed}

    def from_json(self, source):
        if 'title' in source:
            self.title = source['title']
        if 'order' in source:
            self.order = source['order']
        if 'completed' in source:
            self.completed = source['completed']

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id')))


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)

    def __unicode__(self):
        return self.description


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(32))
    current_login_ip = db.Column(db.String(32))
    login_count = db.Column(db.Integer)

    roles = db.relationship(
        'Role', secondary=roles_users,
        backref=db.backref('users', lazy='dynamic'))

    def __unicode__(self):
        return self.email
