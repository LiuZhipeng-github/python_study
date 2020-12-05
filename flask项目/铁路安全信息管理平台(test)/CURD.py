from flask import Blueprint,render_template,session,request,flash,jsonify
import pymysql,os,json
import datetime
from flask_paginate import get_page_args,Pagination
import pandas as pd
from sqlalchemy import create_engine
from session import is_login
import picture


conn = pymysql.connect(host='localhost', user="root", passwd='love530.', db='test')
cursor = conn.cursor()
today = datetime.date.today()
first = today.replace(day=1)
# lastMonth = first - datetime.timedelta(days=1)
# last_month = lastMonth.strftime("%Y-%m")
last_month = '2020-06'
global u
u = None
name = None
danwei = None
room_=None
table_name = '`2020-05`'
ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])
curd_ = Blueprint('curd_',__name__)
#编辑
@curd_.route('/to_edit', methods=['POST', 'GET'],endpoint='12')
@is_login
def to_edit():
    data = picture.picture().edit()
    return render_template("all-travellog-manage-edit.html",data=data)



#关键字查询
@curd_.route('/search_text',endpoint='1',methods=['POST','GET'])
@is_login
def search():
    global name
    # if request.method == 'POST':
    name = request.form.get('jiancharen')
    global danwei
    danwei = request.form.get('jianchadanwei')

    print(name)
    print(danwei)
    global u

    if u == None:
        sql = ("select * from {} where 检查人 LIKE '%{}%' and 录入科室 LIKE '%{}%'".format(table_name,name,danwei))
        cursor.execute(sql)
        u = cursor.fetchall()
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        total = len(u)
        print(total)
        pagination_users = get_users(offset=offset, per_page=20)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
        return render_template('all-admin-datalist.html',
                               users=pagination_users,
                               page=page,
                               per_page=per_page,
                               pagination=pagination,
                               )
    else:
        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        total = len(u)
        print('total')
        pagination_users = get_users(offset=offset, per_page=20)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
        return render_template('all-admin-datalist.html',
                               users=pagination_users,
                               page=page,
                               per_page=per_page,
                               pagination=pagination,
                               )
#月份查询
@curd_.route('/search_month',endpoint='2',methods=['POST','GET'])
@is_login
def search_month():
    data = picture.picture().month_search()
    return render_template('all-tables-data.html', users=data)
#关键人物详情
@curd_.route('/people_more',endpoint='3', methods=['POST', 'GET'])
@is_login
def people_more():
    data = picture.picture().more_people()
    return render_template('all-tables-data.html',users=data)
#关键车间详情
@curd_.route('/room_more', endpoint='4',methods=['POST', 'GET'])
@is_login
def room_more():
    data = picture.picture().more_room()
    return render_template('all-tables-data.html',users=data)
#删除(renew)
@curd_.route('/del', endpoint='5',methods=['POST', 'GET'])
@is_login
def dele():
    picture.picture().delete_()
    renew()
    return jsonify('删除成功')
#分页显示
@curd_.route('/details', endpoint='6',methods=['POST', 'GET'])
@is_login
def deatils():
    # val= json.loads(str(request.form.get('data')))
    data = picture.picture().show_details()
    return render_template("all-admin-details.html",data=data)
#修改
@curd_.route('/edit', endpoint='7',methods=['POST', 'GET'])
@is_login
def edit():
    try:
        if request.method == 'POST':
            num = request.form.get('num')
            amd_type = request.form.get('amd_type')
            amd_content = request.form.get('amd_content')
            amd_timetype = request.form.get('amd_timetype')
            amd_date = request.form.get('amd_date')
            amd_time = request.form.get('amd_time')
            print(num,amd_type,amd_content,amd_timetype,amd_date,amd_time)

            if amd_type != ''and amd_content!='':
                sql = (f"UPDATE {table_name} SET %s='%s' where id=%s") % (amd_type,amd_content,num)
                cursor.execute(sql)
                conn.commit()
                if amd_timetype != '' and amd_date != '':
                    if amd_timetype != '整改期限':
                        time = amd_date + ' ' + amd_time
                        sql = (f"UPDATE {table_name} SET %s='%s' where id=%s") % (amd_timetype, time, num)
                        cursor.execute(sql)
                        conn.commit()
                        renew()
                        return "修改成功"
                    else:
                        time = amd_date
                        sql = (f"UPDATE {table_name} SET %s='%s' where id=%s") % (amd_timetype, time, num)
                        cursor.execute(sql)
                        conn.commit()
                        renew()
                        return "修改成功"
                else:
                    renew()
                    return "修改成功"
            else:
                if amd_timetype != '' and amd_date != '':
                    if amd_timetype != '整改期限':
                        time = amd_date + ' ' + amd_time
                        sql = (f"UPDATE {table_name} SET %s='%s' where id=%s") % (amd_timetype, time, num)
                        cursor.execute(sql)
                        conn.commit()
                        renew()
                        return "修改成功"
                    else:
                        time = amd_date
                        sql = (f"UPDATE {table_name} SET %s='%s' where id=%s") % (amd_timetype, time, num)
                        cursor.execute(sql)
                        conn.commit()
                        renew()
                        return "修改成功"
                else:
                    return "修改失败"
        else:
            return "修改失败"
    except:
        return "修改失败，请刷新重试"
#添加
@curd_.route('/add', endpoint='8',methods=['POST', 'GET'])
@is_login
def add():
    if request.method == 'POST':
        picture.picture().add_new()
        renew()
        flash('添加成功', category='add_error')
        return render_template('all-travellog-manage-edit.html')
    else:
        print('失败')
        flash('添加成功', category='add_error')
        return render_template('all-travellog-manage-edit.html')
#导入
@curd_.route('/import',endpoint='9', methods=['POST'], strict_slashes=False)
@is_login
def ins():
    if request.method == 'POST':
        file_dir = '/Users/liuzhipeng/Downloads/test/static/file' # 拼接成合法文件夹地址
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)  # 文件夹不存在就创建
        f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
        if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
            fname = f.filename
            file_name = os.path.join(file_dir, fname)
            f.save(os.path.join(file_dir, fname))  # 保存文件到upload目录
            import_file(file_name)
            flash('导入成功', category='import_error')
            return render_template('all-admin-import.html')
        else:
            flash('文件导入失败，请注意文件格式', category='import_error')
            return render_template('all-admin-import.html')
    else:
        flash('导入失败，请重试', category='import_error')
        return render_template('all-admin-import.html')
#关键人物
@curd_.route('/to_people_analyze',endpoint='10')
@is_login
def to_people_analyze():
    a,b,c=picture.picture().people()
    return render_template('all-admin-people-analyze.html',a=a,b=b,c=c)
#关键车间
@curd_.route('/to_room_analyze',endpoint='11')
@is_login
def to_room_analyze():
    a,b,c=picture.picture().room()
    global u
    u==None
    return render_template('all-admin-room-analyze.html',a=a,b=b,c=c)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
def import_file(file_name):
        engine = create_engine("mysql+pymysql://{}:{}@{}/{}?charset={}".format('root', 'love530.', '127.0.0.1:3306', 'test', 'utf8mb4'))
        df = pd.read_excel(file_name)
        print('1')
        try:
            sql4 = (f"ALTER  TABLE {table_name} test DROP id;")
            cursor.execute(sql4)
            sql3 = (f"alter table {table_name} add id int first;")
            cursor.execute(sql3)
            df.to_sql(name='2020-05', con=engine, if_exists='replace', index=True, index_label='id')
            print('2')
        except:
            df.to_sql(name='2020-05', con=engine, if_exists='replace', index=True, index_label='id')
            sql2 = (f"ALTER TABLE {table_name} DROP id;")
            cursor.execute(sql2)
            sql = (f"ALTER  TABLE {table_name} ADD id mediumint(6) PRIMARY KEY NOT NULL AUTO_INCREMENT FIRST;")
            cursor.execute(sql)
            print('3')
def get_users(offset=0, per_page=10):
    return u[offset: offset + per_page]
def renew():
    global u
    global name
    global danwei
    print(name)
    sql = ("select * from {} where 检查人 LIKE '%{}%' and 录入科室 LIKE '%{}%'".format(table_name,name, danwei))
    # print(name_form)
    cursor.execute(sql)
    u = cursor.fetchall()