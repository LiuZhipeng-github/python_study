from flask import request,flash,session,jsonify,Blueprint
import pymysql,json
from flask_paginate import get_page_args,Pagination
from flask import Flask, render_template
import os
import pandas as pd
from sqlalchemy import create_engine
from functools import wraps
import pyecharts.options as opts
from pyecharts.charts import Line ,Pie
import datetime
from jump import jump
import picture
from  user import user
from pic import tester
from session import is_login,session_
from CURD import curd_
#------------ 初始化声明-------------
conn = pymysql.connect(host='localhost', user="root", passwd='love530.', db='test')
cursor = conn.cursor()
app = Flask(__name__)
# 设置密钥
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = '\xc9ixnRb\xe40\xd4\xa5\x7f\x03\xd0y6\x01\x1f\x96\xeao+\x8a\x9f\xe4'
# ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])
app.register_blueprint(user)
app.register_blueprint(session_)
app.register_blueprint(tester)
app.register_blueprint(curd_)
app.register_blueprint(jump)
#------------定义全局变量----------------
#上个月的日期
today = datetime.date.today()
first = today.replace(day=1)
# lastMonth = first - datetime.timedelta(days=1)
# last_month = lastMonth.strftime("%Y-%m")
table_name = '`2020-05`'
last_month = '2020-06'

# ------------错误处理--------------
@app.errorhandler(404)
def miss(e):
    return render_template('all-admin-404.html'),404
@app.errorhandler(500)
def miss(e):
    return render_template('all-admin-500.html'),500

# -----------相关函数---------------
# def is_login(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         user = session.get('user')
#         if not user:
#             return render_template('all-admin-login.html')
#         return func(*args,**kwargs)
#     return inner
# def picture1():
#     df = pd.read_sql(f"select * from {table_name} where 检查时间 LIKE '%{last_month}%'", conn)
#     df['time'] = pd.to_datetime(df['检查时间'])
#     df['time'] = df['time'].apply(lambda x: x.strftime('%Y%m%d'))
#     ya = []
#     for i in df['time'].unique():
#         i = str(i)
#         try:
#             bkk = df[df['time'] == i]['性质'].value_counts()['A类']
#             ya.append(str(bkk))
#         except:
#             bkk = 0
#             ya.append(str(bkk))
#     # print(ya, len(ya))
#     yb = []
#     for i in df['time'].unique():
#         i = str(i)
#         try:
#             bkk = df[df['time'] == i]['性质'].value_counts()['B类']
#             yb.append(str(bkk))
#
#         except:
#             bkk = 0
#             yb.append(str(bkk))
#     # print(yb, len(yb))
#     yc = []
#     for i in df['time'].unique():
#         i = str(i)
#         try:
#             bkk = df[df['time'] == i]['性质'].value_counts()['C类']
#             yc.append(str(bkk))
#             print(yc)
#         except:
#             bkk = 0
#             yc.append(str(bkk))
#     print(yc, len(yc))
#     yd = []
#     for i in df['time'].unique():
#         i = str(i)
#         try:
#             bkk = df[df['time'] == i]['性质'].value_counts()['D类']
#             yd.append(str(bkk))
#         except:
#             bkk = 0
#             yd.append(str(bkk))
#     x = df['time'].unique()
#     # chart = picture(x,ya,yb,yc,yd)
#     a = []
#     for i in x:
#         a.append(str(i))
#     c=(
#
#         Line(init_opts=opts.InitOpts(page_title=f"现场安全信息性质分布(月)"))
#             .add_xaxis(a)
#             .add_yaxis("A类", ya)
#             .add_yaxis("B类", yb)
#             .add_yaxis("C类", yc)
#             .add_yaxis("D类", yd)
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title=f"现场安全信息性质分布(月)", subtitle=f"统计时间：{last_month}"),
#             tooltip_opts=opts.TooltipOpts(trigger="axis"),
#             xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), name="日期"),
#             # toolbox_opts=opts.ToolBoxFeatureSaveAsImageOpts(background_color= "auto",type_='jpg'),
#             toolbox_opts=opts.ToolboxOpts(is_show=True,
#                                           feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {},
#                                                    "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]},
#                                                    "dataView": {}}),
#             )
#     )
#     print('已画图成功')
#     return c
# def picture2():
#     df = pd.read_sql(f"select * from {table_name} where 检查时间 LIKE '%{last_month}%'", conn)
#     df['time'] = pd.to_datetime(df['检查时间'])
#     df['time_H'] = df['time'].apply(lambda x: x.hour)
#     x = df['time_H'].sort_values(ascending=True).unique()
#     ya = []
#     for i in x:
#         try:
#             bkk = df[df['time_H'] == i]['性质'].value_counts()['A类']
#             ya.append(str(bkk))
#         except:
#             bkk = 0
#             ya.append(str(bkk))
#     # print(ya, len(ya))
#     yb = []
#     for i in x:
#         try:
#             bkk = df[df['time_H'] == i]['性质'].value_counts()['B类']
#             yb.append(str(bkk))
#         except:
#             bkk = 0
#             yb.append(str(bkk))
#     # print(yb, len(yb))
#     yc = []
#     for i in x:
#         try:
#             bkk = df[df['time_H'] == i]['性质'].value_counts()['C类']
#             yc.append(str(bkk))
#         except:
#             bkk = 0
#             yc.append(str(bkk))
#     # print(yc, len(yc))
#     yd = []
#     for i in x:
#         try:
#             bkk = df[df['time_H'] == i]['性质'].value_counts()['D类']
#             yd.append(str(bkk))
#         except:
#             bkk = 0
#             yd.append(str(bkk))
#     # print(yd, len(yd))
#     a = []
#     for i in x:
#         m = str(i)+':00'
#         a.append(m)
#     e = (
#         Line()
#         .add_xaxis(a)
#         .add_yaxis("A类", ya)
#         .add_yaxis("B类", yb)
#         .add_yaxis("C类", yc)
#         .add_yaxis("D类", yd)
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title=f"现场安全信息性质分布(时)", subtitle=f"统计时间：{last_month}"),
#             tooltip_opts=opts.TooltipOpts(trigger="axis"),
#             xaxis_opts=opts.AxisOpts(name="时间"),
#             toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {}, "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]}, "dataView": {}}))
#         # .render(f"safe_message_hour_{table_name}.html")
#
#     )
#     print('已画图成功')
#     return e
# def picture3():
#         df = pd.read_sql(f"select * from {table_name} where 检查时间 LIKE '%{last_month}%'", conn)
#         group = df.groupby(by=df['录入科室']).count()['性质']
#         x = group.index.tolist()
#         y = group.values.tolist()
#         # print(x)
#         # print(y)
#         c=(
#             Line(init_opts=opts.InitOpts())
#                 .add_xaxis(x)
#                 .add_yaxis("数量", y)
#                 .set_global_opts(
#                 title_opts=opts.TitleOpts(title="现场安全信息车间统计分布", subtitle=f"统计时间：{last_month}"),
#                 tooltip_opts=opts.TooltipOpts(trigger="axis"),
#                 toolbox_opts=opts.ToolboxOpts(is_show=True,
#                                               feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {},
#                                                        "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]},
#                                                        "dataView": {}}),
#                 # xaxis_opts=opts.AxisOpts(name_rotate=60, name="车间名称",axislabel_opts={"rotate": 45}))
#                 xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30), name="车间名称"))
#                 # .render(f"safe_message_chejian_.html")
#
#         )
#         print('已画图成功')
#         return c
# def picture4():
#     df = pd.read_sql(f"select * from {table_name} where 检查时间 LIKE '%{last_month}%'", conn)
#     group = df.groupby(by=df['责任人岗位']).count()['性质']
#     x = group.index.tolist()
#     y = group.values.tolist()
#     c=(
#         Line(init_opts=opts.InitOpts())
#             .add_xaxis(x)
#             .add_yaxis("数量", y)
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title="现场安全信息责任人岗位统计分布", subtitle=f"统计时间：{last_month}"),
#             tooltip_opts=opts.TooltipOpts(trigger="axis"),
#             toolbox_opts=opts.ToolboxOpts(is_show=True,
#                                           feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {},
#                                                    "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]},
#                                                    "dataView": {}}),
#             xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=20), name="责任人岗位"))
#     )
#     print('已画图成功')
#     return c
# def half_year():
#     df = pd.read_sql(f"select * from {table_name}", conn)
#     df['time'] = pd.to_datetime(df['检查时间'])
#     df['time'] = df['time'].apply(lambda x: x.strftime('%Y-%m'))
#     print(df['time'].unique()[-6:])
#     timelist = df['time'].unique()[-6:].tolist()
#     ya = []
#     yb = []
#     yc = []
#     yd = []
#     for i in timelist:
#         group = df[df['time'] == i]['性质'].value_counts()['A类']
#         ya.append(str(group))
#         group = df[df['time'] == i]['性质'].value_counts()['B类']
#         yb.append(str(group))
#         group = df[df['time'] == i]['性质'].value_counts()['C类']
#         yc.append(str(group))
#         try:
#             group = df[df['time'] == i]['性质'].value_counts()['D类']
#             yd.append(str(group))
#         except:
#             group = 0
#             yd.append(str(group))
#     print(ya)
#     print(yb)
#     print(yc)
#     print(yd)
#     c = (
#
#         Line(init_opts=opts.InitOpts(page_title=f"现场安全信息性质分布(半年)"))
#             .add_xaxis(timelist)
#             .add_yaxis("A类", ya)
#             .add_yaxis("B类", yb)
#             .add_yaxis("C类", yc)
#             .add_yaxis("D类", yd)
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title=f"现场安全信息性质分布(半年)", subtitle=f"统计时间：{last_month}"),
#             tooltip_opts=opts.TooltipOpts(trigger="axis"),
#             xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), name="日期"),
#             # toolbox_opts=opts.ToolBoxFeatureSaveAsImageOpts(background_color= "auto",type_='jpg'),
#             toolbox_opts=opts.ToolboxOpts(is_show=True,
#                                           feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {},
#                                                    "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]},
#                                                    "dataView": {}}),
#         )
#     )
#     print('已画图成功')
#     return c
# def half_year_score():
#     df = pd.read_sql(f"select * from {table_name}", conn)
#     df['time'] = pd.to_datetime(df['检查时间'])
#     df['time'] = df['time'].apply(lambda x: x.strftime('%Y-%m'))
#     print(df['time'].unique()[-6:])
#     timelist = df['time'].unique()[-6:].tolist()
#     ya = []
#     yb = []
#     for i in timelist:
#         group = df[df['time'] == i]['分值'].sum()
#         ya.append(str(group))
#         group = df[df['time'] == i]['考核分'].sum()
#         yb.append(str(int(group)))
#     print(ya)
#     print(yb)
#     c = (
#
#         Line(init_opts=opts.InitOpts(page_title=f"现场安全信息性质分布(月)"))
#             .add_xaxis(timelist)
#             .add_yaxis("分值", ya)
#             .add_yaxis("考核分", yb)
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title=f"现场安全信息性质分布(月)", subtitle=f"统计时间：{last_month}"),
#             tooltip_opts=opts.TooltipOpts(trigger="axis"),
#             xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), name="日期"),
#             # toolbox_opts=opts.ToolBoxFeatureSaveAsImageOpts(background_color= "auto",type_='jpg'),
#             toolbox_opts=opts.ToolboxOpts(is_show=True,
#                                           feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {},
#                                                    "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]},
#                                                    "dataView": {}}),
#         )
#     )
#     print('已画图成功')
#     return c
# def pie_class():
#     df = pd.read_sql(f"select * from {table_name} where 检查时间 LIKE '%{last_month}%'", conn)
#     class_ = df['分类'].unique().tolist()
#     print(class_)
#     y = []
#     for i in class_:
#         group = df['分类'].value_counts()[i]
#         y.append(str(group))
#     c = (
#         Pie()
#             .add("", [list(z) for z in zip(class_, y)])
#             .set_colors(["orange", "purple", "pink"])
#             .set_global_opts(title_opts=opts.TitleOpts(
#             title="分类",
#             pos_left=60,
#             title_textstyle_opts=opts.TextStyleOpts(color="black"),
#         ),
#         )
#             .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#     )
#     return c
# def pie_denger():
#     df = pd.read_sql(f"select * from {table_name} where 检查时间 LIKE '%{last_month}%'", conn)
#     class_ = df['风险因素'].unique().tolist()
#     print(class_)
#     y = []
#     for i in class_:
#         group = df['风险因素'].value_counts()[i]
#         y.append(str(group))
#     c = (
#         Pie()
#             .add(
#             "",
#             [list(z) for z in zip(class_, y)],
#             radius=["40%", "75%"],
#         )
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title="风险因素分类"),
#             legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
#         )
#             .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#     )
#     return c
# def pie_room():
#     df = pd.read_sql(f"select * from {table_name} where 检查时间 LIKE '%{last_month}%'", conn)
#     class_ = df['责任科室'].unique().tolist()
#     print(class_)
#     y = []
#     for i in class_:
#         group = df['责任科室'].value_counts()[i]
#         y.append(str(group))
#     print(y)
#     c = (
#         Pie()
#             .add(
#             "",
#             [list(z) for z in zip(class_, y)],
#             radius=["40%", "60%"],
#         )
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title="风险因素分类"),
#             legend_opts=opts.LegendOpts(orient="horizontal", pos_bottom=0),
#         )
#             .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#
#     )
#     return c
# def pie_face():
#     df = pd.read_sql(f"select * from {table_name} where 检查时间 LIKE '%{last_month}%'", conn)
#     e = 0
#     rel = df['责任人政治面貌'].fillna(value='群众').unique()
#     face = ['党员', '团员', '群众', '工商联']
#     rel = rel.tolist()
#     print(len(rel))
#     face_num = []
#     for j in face:
#         for i in rel:
#             a = i.count(j, 0, len(i))
#             e = e + a
#         face_num.append(str(e))
#         e = 0
#     c = (
#         Pie()
#             .add(
#             "",
#             [list(z) for z in zip(face, face_num)],
#             radius=["40%", "60%"],
#         )
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title="风险因素分类"),
#             legend_opts=opts.LegendOpts(orient="horizontal", pos_bottom=0),
#         )
#             .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#     )
#     return c
# def people():
#     df = pd.read_sql(f"select * from `2020-05` where 检查时间 LIKE '%{last_month}%'", conn)
#     group = df.groupby(by=df['责任人']).count()['性质'].sort_values(ascending=False)[:3]
#     a = group.index.tolist()
#     people = locals()
#     for i in range(3):
#         people['e' + str(i)] = []
#         c = a[i]
#         people['e' + str(i)].append(c)
#         try:
#             akk = df[df['责任人'] == c]['性质'].value_counts()['A类']
#             people['e' + str(i)].append(akk)
#         except:
#             akk = 0
#             people['e' + str(i)].append(akk)
#
#         try:
#             bkk = df[df['责任人'] == c]['性质'].value_counts()['B类']
#             people['e' + str(i)].append(bkk)
#         except:
#             bkk = 0
#             people['e' + str(i)].append(bkk)
#
#         try:
#             ckk = df[df['责任人'] == c]['性质'].value_counts()['C类']
#             people['e' + str(i)].append(ckk)
#         except:
#             ckk = 0
#             people['e' + str(i)].append(ckk)
#         try:
#             dkk = df[df['责任人'] == c]['性质'].value_counts()['D类']
#             people['e' + str(i)].append(dkk)
#         except:
#             dkk = 0
#             people['e' + str(i)].append(dkk)
#         sum = akk + bkk + ckk + dkk
#         people['e' + str(i)].append(sum)
#         d = df[df['责任人'] == c]['责任人岗位'].unique()
#         people['e' + str(i)].append(str(d[0]))
#         e = df[df['责任人'] == c]['录入科室'].unique()
#         people['e' + str(i)].append(str(e[0]))
#     return (people['e' + '0'], people['e' + '1'], people['e' + '2'])
# def room():
#     df = pd.read_sql(f"select * from `2020-05` where 检查时间 LIKE '%{last_month}%'", conn)
#     group = df.groupby(by=df['录入科室']).count()['性质'].sort_values(ascending=False)[:3]
#     a = group.index.tolist()
#     room = locals()
#     for i in range(3):
#         room['e' + str(i)] = []
#         c = a[i]
#         room['e' + str(i)].append(c)
#         try:
#             akk = df[df['录入科室'] == c]['性质'].value_counts()['A类']
#             room['e' + str(i)].append(akk)
#         except:
#             akk = 0
#             room['e' + str(i)].append(akk)
#
#         try:
#             bkk = df[df['录入科室'] == c]['性质'].value_counts()['B类']
#             room['e' + str(i)].append(bkk)
#         except:
#             bkk = 0
#             room['e' + str(i)].append(bkk)
#
#         try:
#             ckk = df[df['录入科室'] == c]['性质'].value_counts()['C类']
#             room['e' + str(i)].append(ckk)
#         except:
#             ckk = 0
#             room['e' + str(i)].append(ckk)
#         try:
#             dkk = df[df['录入科室'] == c]['性质'].value_counts()['D类']
#             room['e' + str(i)].append(dkk)
#         except:
#             dkk = 0
#             room['e' + str(i)].append(dkk)
#         sum = akk + bkk + ckk + dkk
#         room['e' + str(i)].append(sum)
#
#
#     return (room['e' + '0'], room['e' + '1'], room['e' + '2'])

#------------跳板--------------------
@app.route('/')
def to_index():
    print(session.get('user'))
    df = pd.read_sql(f"select * from {table_name} where 检查时间 LIKE '%{last_month}%'", conn)
    safe_message_num = df['id'].count()
    groupA = df['性质'].value_counts()['A类']
    sum = df['性质'].count()
    safe_message_score = df['分值'].sum()
    return render_template('all-admin-index.html',sum=sum,group=groupA,safe_message_num=safe_message_num,safe_message_score=safe_message_score)
# @app.route('/to_login')
# def to_login():
#     return render_template('all-admin-login.html')
# @app.route('/to_register')
# def to_register():
#     return render_template('all-admin-register.html')
# @app.route('/logout')
# def logout():
#     session.clear()
#     return render_template('all-admin-login.html')
# @app.route('/to_search')
# @is_login
# def to_search():
#     global u
#     u = None
#     return render_template('all-admin-dataform.html')
# @app.route('/to_edit', methods=['POST', 'GET'])
# @is_login
# def to_edit():
#     data = request.form.get("to_edit")
#     print(data)
#     sql = (f"select * from {table_name} where id=%s" % data)
#     cursor.execute(sql)
#     data = cursor.fetchall()
#     data = list(data)
#
#     return render_template("all-travellog-manage-edit.html",data=data)
# @app.route('/to_add')
# @is_login
# def to_add():
#     return render_template('all-travellog-manage-edit.html')
# @app.route('/to_import')
# @is_login
# def to_import():
#     return render_template('all-admin-import.html')
# @app.route('/to_chart')
# @is_login
# def to_chart1():
#     return render_template('all-charts-chartjs.html')
# @app.route('/to_people_analyze')
# @is_login
# def to_people_analyze():
#     a,b,c=picture.picture().people()
#     return render_template('all-admin-people-analyze.html',a=a,b=b,c=c)
# @app.route('/to_room_analyze')
# @is_login
# def to_room_analyze():
#     a,b,c=picture.picture().room()
#     global u
#     u==None
#     return render_template('all-admin-room-analyze.html',a=a,b=b,c=c)
# #--------------执行后台函数--------------
# #注册
# @app.route('/all-admin-register', methods=['POST','GET'])
# def register():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         password2 = request.form.get('password2')
#         print(username)
#         print(password)
#         print(password2)
#         sql = """ select username from login where username='%s' """ % username
#         sql2 = """Insert into login(username,password) values ('%s','%s')""" % (username, password)
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         print(results)
#         if results:
#             flash('该用户名已存在', category='register')
#             print('该用户名已存在')
#             return render_template('all-admin-register.html')
#         else:
#             if (results == '' or password == ''):
#                 flash('用户名密码不能为空', category='register')
#                 return render_template('all-admin-register.html')
#             else:
#                 if (password == password2):
#                     cursor.execute(sql2)
#                     conn.commit()
#                     return render_template('all-admin-login.html')
#                 else:
#                     print('注册失败')
#                     flash('注册失败', category='register')
#                     return render_template('all-admin-register.html')
#     else:
#         print('失败')
#         return render_template('all-admin-register.html')
#登陆
# @app.route('/all-admin-login', methods=['POST','GET'])
# def login_():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         print(username)
#         print(password)
#         sql = """ select username,password from login where username='%s' and password='%s' """ % (username, password)
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         print(results)
#         if results:
#             print('success')
#             session['user'] = username
#             session.get(username)
#             df = pd.read_sql(f"select * from {table_name} where 检查时间 LIKE '%{last_month}%'", conn)
#             safe_message_num = df['id'].count()
#
#             group = df['性质'].value_counts()['A类']
#             sum = df['性质'].count()
#             print(sum)
#             safe_message_score = df['分值'].sum()
#             return render_template('all-admin-index.html',sum=sum,safe_message_num=safe_message_num,group=group,safe_message_score=safe_message_score)
#         else:
#             flash('密码或用户名错误',category='login_error')
#             print('fail')
#             return render_template('all-admin-login.html')
#     else:
#         flash('登陆失败',category='login_error')
#         print('登陆失败')
#         return render_template('all-admin-login.html')
#姓名查询
# @app.route('/search_text',methods=['POST','GET'])
# #@is_login
# def search():
#     global name
#     # if request.method == 'POST':
#     name = request.form.get('jiancharen')
#     global danwei
#     danwei = request.form.get('jianchadanwei')
#
#     print(name)
#     print(danwei)
#     global u
#
#     if u == None:
#         sql = ("select * from {} where 检查人 LIKE '%{}%' and 录入科室 LIKE '%{}%'".format(table_name,name,danwei))
#         cursor.execute(sql)
#         u = cursor.fetchall()
#         page, per_page, offset = get_page_args(page_parameter='page',
#                                                per_page_parameter='per_page')
#         total = len(u)
#         print(total)
#         pagination_users = get_users(offset=offset, per_page=20)
#         pagination = Pagination(page=page, per_page=per_page, total=total,
#                                 css_framework='bootstrap4')
#         return render_template('all-admin-datalist.html',
#                                users=pagination_users,
#                                page=page,
#                                per_page=per_page,
#                                pagination=pagination,
#                                )
#     else:
#         page, per_page, offset = get_page_args(page_parameter='page',
#                                                per_page_parameter='per_page')
#         total = len(u)
#         print('total')
#         pagination_users = get_users(offset=offset, per_page=20)
#         pagination = Pagination(page=page, per_page=per_page, total=total,
#                                 css_framework='bootstrap4')
#         return render_template('all-admin-datalist.html',
#                                users=pagination_users,
#                                page=page,
#                                per_page=per_page,
#                                pagination=pagination,
#                                )
# #月份查询
# @app.route('/search_month',methods=['POST','GET'])
# # @is_login
# def search_month():
#     month_se = request.form.get('month')
#     sql = ("select * from {} where 检查时间 LIKE '%{}%'".format(table_name,month_se))
#     cursor.execute(sql)
#     data = cursor.fetchall()
#     return render_template('all-tables-data.html', users=data)
# #时间段查询
# @app.route('/people_more', methods=['POST', 'GET'])
# #@is_login
# def people_more():
#     # if request.method == 'POST':
#     more = request.form.get('more')
#     print(more)
#     sql = ("select * from {} where 责任人 LIKE '%{}%'".format(table_name,more))
#     cursor.execute(sql)
#     u = cursor.fetchall()
#     return render_template('all-tables-data.html',users=u)
#
# @app.route('/room_more', methods=['POST', 'GET'])
# # @is_login
# def room_more():
#     # if request.method == 'POST':
#     more = request.form.get('more')
#     print(more)
#     sql = ("select * from {} where 录入科室 LIKE '%{}%'".format(table_name,more))
#     cursor.execute(sql)
#     u = cursor.fetchall()
#     return render_template('all-tables-data.html',users=u)
# #删除
# @app.route('/del', methods=['POST', 'GET'])
# #@is_login
# def dele():
#     data = json.loads(str(request.form.get('data')))
#     userId = data['x']
#     print(userId)
#     sql = (f"delete from {table_name} where id=%s" % userId)
#     print('删了')
#     cursor.execute(sql)
#     conn.commit()
#     renew()
#     return jsonify('删除成功')
# #分页显示
# @app.route('/details', methods=['POST', 'GET'])
# #@is_login
# def deatils():
#     # val= json.loads(str(request.form.get('data')))
#     val = request.form.get("details")
#
#     print(val)
#     sql = (f"select * from {table_name} where id=%s" % val)
#     cursor.execute(sql)
#     data = cursor.fetchall()
#     data = list(data)
#     print(data)
#     return render_template("all-admin-details.html",data=data)
# #修改
# @app.route('/edit', methods=['POST', 'GET'])
# #@is_login
# def edit():
#     try:
#         if request.method == 'POST':
#             num = request.form.get('num')
#             amd_type = request.form.get('amd_type')
#             amd_content = request.form.get('amd_content')
#             amd_timetype = request.form.get('amd_timetype')
#             amd_date = request.form.get('amd_date')
#             amd_time = request.form.get('amd_time')
#             print(num,amd_type,amd_content,amd_timetype,amd_date,amd_time)
#
#             if amd_type != ''and amd_content!='':
#                 sql = (f"UPDATE {table_name} SET %s='%s' where id=%s") % (amd_type,amd_content,num)
#                 cursor.execute(sql)
#                 conn.commit()
#                 if amd_timetype != '' and amd_date != '':
#                     if amd_timetype != '整改期限':
#                         time = amd_date + ' ' + amd_time
#                         sql = (f"UPDATE {table_name} SET %s='%s' where id=%s") % (amd_timetype, time, num)
#                         cursor.execute(sql)
#                         conn.commit()
#                         renew()
#                         return "修改成功"
#                     else:
#                         time = amd_date
#                         sql = (f"UPDATE {table_name} SET %s='%s' where id=%s") % (amd_timetype, time, num)
#                         cursor.execute(sql)
#                         conn.commit()
#                         renew()
#                         return "修改成功"
#                 else:
#                     renew()
#                     return "修改成功"
#             else:
#                 if amd_timetype != '' and amd_date != '':
#                     if amd_timetype != '整改期限':
#                         time = amd_date + ' ' + amd_time
#                         sql = (f"UPDATE {table_name} SET %s='%s' where id=%s") % (amd_timetype, time, num)
#                         cursor.execute(sql)
#                         conn.commit()
#                         renew()
#                         return "修改成功"
#                     else:
#                         time = amd_date
#                         sql = (f"UPDATE {table_name} SET %s='%s' where id=%s") % (amd_timetype, time, num)
#                         cursor.execute(sql)
#                         conn.commit()
#                         renew()
#                         return "修改成功"
#                 else:
#                     return "修改失败"
#         else:
#             return "修改失败"
#     except:
#         return "修改失败，请刷新重试"
# #添加
# @app.route('/add', methods=['POST', 'GET'])
# #@is_login
# def add():
#     if request.method == 'POST':
#         description = request.form.get('description')
#         time = request.form.get('time')
#         day_time = request.form.get('day_time')
#         jianchaname = request.form.get('jianchaname')
#         jianchagangwei = request.form.get('jianchagangwei')
#         lurukeshi = request.form.get('lurukeshi')
#         zerendanwei = request.form.get('zerendanwei')
#         zerenname = request.form.get('zerenname')
#         zerengangwei = request.form.get('zerengangwei')
#         zerenpolitics = request.form.get('zerenpolitics')
#         amdday_final = request.form.get('amdday_final')
#         amdrequest = request.form.get('amdrequest')
#         amdtime = request.form.get('amdtime')
#         amdday = request.form.get('amdday')
#         amd = request.form.get('amd')
#         relook = request.form.get('relook')
#         advice = request.form.get('advice')
#         fengixan = request.form.get('fengixan')
#         denger_point = request.form.get('denger_point')
#         denger = request.form.get('denger')
#         xingzhi = request.form.get('xingzhi')
#         grade = request.form.get('grade')
#         message = request.form.get('message')
#         point = request.form.get('point')
#         testgrade = request.form.get('testgrade')
#         special = request.form.get('special')
#         zerenroom = request.form.get('zerenroom')
#         reporttime = request.form.get('reporttime')
#         keshi_time = request.form.get('keshi_time')
#         banzu_time = request.form.get('banzu_time')
#         sort = request.form.get('sort')
#         question_number = request.form.get('question_number')
#
#         amdtime = amdday + ' ' + amdtime
#         time = day_time + ' ' + time
#
#         pos = str(day_time).rfind("-")
#         table = str(day_time)[:pos]
#         print(table)
#
#         sql = (f"select id from {table_name} order by id desc limit 0,1;")
#         cursor.execute(sql)
#         Index = cursor.fetchone()[0] + 1
#
#         T = (str(Index), str(description), str(time), str(jianchaname), str(jianchagangwei), str(lurukeshi),
#              str(zerendanwei), str(zerenname), str(zerengangwei), str(zerenpolitics), str(amdday_final),
#              str(amdrequest), str(amdtime), str(amd), str(relook), str(advice), str(fengixan), str(denger_point),
#              str(denger), str(xingzhi), str(grade), str(message), str(point), str(testgrade), str(special),
#              str(zerenroom), str(reporttime), str(keshi_time), str(banzu_time), str(sort), str(question_number))
#         print(T)
#         sql = (
#                     f"insert into {table_name} values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" % T)
#
#         cursor.execute(sql)
#         conn.commit()
#         renew()
#         flash('添加成功', category='add_error')
#         return render_template('all-travellog-manage-edit.html')
#     else:
#         print('失败')
#         flash('添加成功', category='add_error')
#         return render_template('all-travellog-manage-edit.html')
# #导入
# @app.route('/import', methods=['POST'], strict_slashes=False)
# #@is_login
# def ins():
#     if request.method == 'POST':
#         file_dir = '/Users/liuzhipeng/Downloads/test/static/file' # 拼接成合法文件夹地址
#         if not os.path.exists(file_dir):
#             os.makedirs(file_dir)  # 文件夹不存在就创建
#         f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
#         if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
#             fname = f.filename
#             file_name = os.path.join(file_dir, fname)
#             f.save(os.path.join(file_dir, fname))  # 保存文件到upload目录
#             import_file(file_name)
#             flash('导入成功', category='import_error')
#             return render_template('all-admin-import.html')
#         else:
#             flash('文件导入失败，请注意文件格式', category='import_error')
#             return render_template('all-admin-import.html')
#     else:
#         flash('导入失败，请重试', category='import_error')
#         return render_template('all-admin-import.html')
# @app.route("/to_chart1")
# def show_pyecharts1():
#     pic1 = picture.picture().picture1()
#     pic2 = picture.picture().picture2()
#     pic3 = picture.picture().half_year()
#     pic4 = picture.picture().half_year_score()
#     return render_template(
#         "all-charts-time.html",
#         data1=pic1.dump_options(),
#         data2 = pic2.dump_options(),
#         data3 =pic3.dump_options(),
#         data4 = pic4.dump_options(),
#       )
# @app.route("/to_chart2")
# def show_pyecharts2():
#     data='89'
#     pic1 = picture.picture().pie_class()
#     pic2 = picture.picture().pie_denger()
#     return render_template(
#         "all-charts-class.html",
#         data1=pic1.dump_options(),
#         data2=pic2.dump_options(),
#         data=data
#       )
# @app.route("/to_chart3")
# def show_pyecharts3():
#     data='89'
#     pic1 = picture.picture().pie_room()
#     pic3 = picture.picture().picture3()
#     return render_template(
#         "all-charts-room.html",
#         data1=pic1.dump_options(),
#         data2 =pic3.dump_options(),
#         data=data
#       )
# @app.route("/to_chart4")
# def show_pyecharts4():
#     data='89'
#     pic1 = picture.picture().pie_face()
#     pic4 = picture.picture().picture4()
#     return render_template(
#         "all-charts-other.html",
#         data1=pic1.dump_options(),
#         data2=pic4.dump_options(),
#         data=data
#       )
#-------------自定义函数-------------
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
# def import_file(file_name):
#         engine = create_engine("mysql+pymysql://{}:{}@{}/{}?charset={}".format('root', 'love530.', '127.0.0.1:3306', 'test', 'utf8mb4'))
#         df = pd.read_excel(file_name)
#         print('1')
#         try:
#             sql4 = (f"ALTER  TABLE {table_name} test DROP id;")
#             cursor.execute(sql4)
#             sql3 = (f"alter table {table_name} add id int first;")
#             cursor.execute(sql3)
#             df.to_sql(name='2020-05', con=engine, if_exists='replace', index=True, index_label='id')
#             print('2')
#         except:
#             df.to_sql(name='2020-05', con=engine, if_exists='replace', index=True, index_label='id')
#             sql2 = (f"ALTER TABLE {table_name} DROP id;")
#             cursor.execute(sql2)
#             sql = (f"ALTER  TABLE {table_name} ADD id mediumint(6) PRIMARY KEY NOT NULL AUTO_INCREMENT FIRST;")
#             cursor.execute(sql)
#             print('3')
# def get_users(offset=0, per_page=10):
#     return u[offset: offset + per_page]
# def renew():
#     global u
#     global name
#     global danwei
#     print(name)
#     sql = ("select * from {} where 检查人 LIKE '%{}%' and 录入科室 LIKE '%{}%'".format(table_name,name, danwei))
#     # print(name_form)
#     cursor.execute(sql)
#     u = cursor.fetchall()
#---------------运行-----------------
if __name__ == '__main__':
    app.run(debug=True)
    cursor.close()
    conn.close()
    print('bye')
