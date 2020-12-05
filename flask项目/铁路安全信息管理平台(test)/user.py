
from flask import Blueprint,render_template,session,request,flash
import pymysql
import datetime
import pandas as pd
conn = pymysql.connect(host='localhost', user="root", passwd='love530.', db='test')
cursor = conn.cursor()
today = datetime.date.today()
first = today.replace(day=1)
# lastMonth = first - datetime.timedelta(days=1)
# last_month = lastMonth.strftime("%Y-%m")
last_month = '2020-06'
table_name = '`2020-05`'
user = Blueprint('user',__name__)
@user.route('/to_login')
def to_login():
    return render_template('all-admin-login.html')
@user.route('/to_register')
def to_register():
    return render_template('all-admin-register.html')
@user.route('/logout')
def logout():
    session.clear()
    return render_template('all-admin-login.html')
@user.route('/all-admin-login', methods=['POST','GET'])
def login_():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        sql = """ select username,password from login where username='%s' and password='%s' """ % (username, password)
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        if results:
            print('success')
            session['user'] = username
            df = pd.read_sql(f"select * from {table_name} where 检查时间 LIKE '%{last_month}%'", conn)
            safe_message_num = df['id'].count()
            group = df['性质'].value_counts()['A类']
            sum = df['性质'].count()
            print(sum)
            safe_message_score = df['分值'].sum()
            return render_template('all-admin-index.html',sum=sum,safe_message_num=safe_message_num,group=group,safe_message_score=safe_message_score)
        else:
            flash('密码或用户名错误',category='login_error')
            print('fail')
            return render_template('all-admin-login.html')
    else:
        flash('登陆失败',category='login_error')
        print('登陆失败')
        return render_template('all-admin-login.html')
@user.route('/all-admin-register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        print(username)
        print(password)
        print(password2)
        sql = """ select username from login where username='%s' """ % username
        sql2 = """Insert into login(username,password) values ('%s','%s')""" % (username, password)
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        if results:
            flash('该用户名已存在', category='register')
            print('该用户名已存在')
            return render_template('all-admin-register.html')
        else:
            if (results == '' or password == ''):
                flash('用户名密码不能为空', category='register')
                return render_template('all-admin-register.html')
            else:
                if (password == password2):
                    cursor.execute(sql2)
                    conn.commit()
                    return render_template('all-admin-login.html')
                else:
                    print('注册失败')
                    flash('注册失败', category='register')
                    return render_template('all-admin-register.html')
    else:
        print('失败')
        return render_template('all-admin-register.html')
# @user.route('/room_more', methods=['POST', 'GET'])
# @is_login
# def room_more():
#     # if request.method == 'POST':
#     more = request.form.get('more')
#     print(more)
#     sql = ("select * from {} where 录入科室 LIKE '%{}%'".format(table_name,more))
#     cursor.execute(sql)
#     u = cursor.fetchall()
#     return render_template('all-tables-data.html',users=u)