""" admin.py """
from .extensions import db
from .models import Todo, User, Role
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security.core import current_user



def register_admin(app):

    class ProtectedModelView(ModelView):
        def is_accessible(self):
            # TODO: check role
            return current_user.is_authenticated()

    admin = Admin(app)
    admin.add_view(ProtectedModelView(Todo, db.session))
    admin.add_view(ProtectedModelView(User, db.session, category='Users'))
    admin.add_view(ProtectedModelView(Role, db.session, category='Users'))
