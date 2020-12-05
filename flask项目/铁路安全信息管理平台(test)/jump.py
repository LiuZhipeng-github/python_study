from flask import Blueprint,render_template,request
from session import is_login
import pymysql
import datetime
import picture
today = datetime.date.today()
first = today.replace(day=1)
# lastMonth = first - datetime.timedelta(days=1)
# last_month = lastMonth.strftime("%Y-%m")
last_month = '2020-06'
table_name = '`2020-05`'
jump= Blueprint('jump',__name__)
conn = pymysql.connect(host='localhost', user="root", passwd='love530.', db='test')
cursor = conn.cursor()



@jump.route('/to_search',endpoint='1')
@is_login
def to_search():
    global u
    u = None
    return render_template('all-admin-dataform.html')

@jump.route('/to_add',endpoint='3')
@is_login
def to_add():
    return render_template('all-travellog-manage-edit.html')
@jump.route('/to_import',endpoint='4')
@is_login
def to_import():
    return render_template('all-admin-import.html')
