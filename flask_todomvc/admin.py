""" admin.py """
from .extensions import db
from .models import Todo, User, Role
from flask.ext.superadmin import Admin, model, BaseView, AdminIndexView
from flask_security.core import current_user


class AuthMixin(object):
    def is_accessible(self):
        return (current_user.is_authenticated()
                    and current_user.has_role('Admin'))

class AdminIndexView(AuthMixin, AdminIndexView):
    pass

class DefaultModelAdmin(AuthMixin, model.ModelAdmin):
    session = db.session

class UserModelAdmin(DefaultModelAdmin):
    exclude = ['password', ]


def register_admin(app):
    admin = Admin(
        app,
        name="Todo MVC Administration",
        index_view=AdminIndexView()
    )
    admin.register(Todo, DefaultModelAdmin)
    admin.register(User, UserModelAdmin)
    admin.register(Role, DefaultModelAdmin)
    #admin.add_view(ProtectedModelView(Todo, db.session))
    #admin.add_view(ProtectedModelView(User, db.session, category='Users'))
    #admin.add_view(ProtectedModelView(Role, db.session, category='Users'))
