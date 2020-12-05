from flask import Blueprint,render_template,session
session_ = Blueprint('session_',__name__)
def is_login(func):
    def inner(*args,**kwargs):
        user = session.get('user')
        print(user)
        if not user:
            return render_template('all-admin-login.html')
            pass
        return func(*args,**kwargs)
        pass
    return inner
    pass
