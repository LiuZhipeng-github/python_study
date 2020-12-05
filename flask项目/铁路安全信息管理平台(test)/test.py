import pymysql,json,re
import pandas as pd
import datetime
import pyecharts.options as opts
from pyecharts.charts import Line ,Tab,Bar,Pie
month = datetime.datetime.now().strftime("%Y-%m")
conn = pymysql.connect(host='localhost', user="root", passwd='love530.', db='test')
cursor = conn.cursor()
last_month = '2020-07'
table_name = '`2020-05`'
df = pd.read_sql(f"select * from {table_name} where 检查时间 LIKE '%{last_month}%'", conn)
e=0
rel = df['责任人政治面貌'].fillna(value='群众').unique()
face=['党员','团员','群众','工商联']
rel = rel.tolist()
print(len(rel))
face_num=[]
for j in face:
    for i in rel:
        a=i.count(j,0,len(i))
        e=e+a
    face_num.append(str(e))
    e=0
c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(face,face_num)],
        radius=["40%", "60%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="风险因素分类"),
        legend_opts=opts.LegendOpts(orient="horizontal",pos_bottom=0),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_radius.html")
)


# df['time'] = pd.to_datetime(df['检查时间'])
# df['time'] = df['time'].apply(lambda x: x.strftime('%Y-%m'))
# print(df['time'].unique()[-6:])
# timelist = df['time'].unique()[-6:].tolist()
# ya = []
# yb =[]
# # yc =[]
# # yd =[]
# for i in timelist:
#     group = df[df['time'] == i]['分值'].sum()
#     ya.append(str(group))
#     group = df[df['time'] == i]['考核分'].sum()
#     # group = df[df['time'] == i]['性质'].value_counts()['B类']
#     yb.append(str(int(group)))
#     # group = df[df['time'] == i]['性质'].value_counts()['C类']
#     # yc.append(str(group))
#     # try:
#     #     group = df[df['time'] == i]['性质'].value_counts()['D类']
#     #     yd.append(str(group))
#     # except:
#     #     group=0
#     #     yd.append(str(group))
# print(ya)
# print(yb)
# # print(yc)
# # print(yd)
# c = (
#
#     Line(init_opts=opts.InitOpts(page_title=f"现场安全信息性质分布(月)"))
#         .add_xaxis(timelist)
#         .add_yaxis("分值", ya)
#         .add_yaxis("考核分", yb)
#         # .add_yaxis("C类", yc)
#         # .add_yaxis("D类", yd)
#         .set_global_opts(
#         title_opts=opts.TitleOpts(title=f"现场安全信息性质分布(月)", subtitle=f"统计时间：{last_month}"),
#         tooltip_opts=opts.TooltipOpts(trigger="axis"),
#         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), name="日期"),
#         # toolbox_opts=opts.ToolBoxFeatureSaveAsImageOpts(background_color= "auto",type_='jpg'),
#         toolbox_opts=opts.ToolboxOpts(is_show=True,
#                                       feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {},
#                                                "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]},
#                                                "dataView": {}}),
#     )
#     .render("half-year.html")
# )
# print('已画图成功')
# # group = df.groupby(by=df['录入科室']).count()['性质'].sort_values(ascending=False)[:3]
# # a = group.index.tolist()
# room = locals()
# for i in range(3):
#     room['e' + str(i)] = []
#     c = a[i]
#     room['e' + str(i)].append(c)
#     try:
#         akk = df[df['录入科室'] == c]['性质'].value_counts()['A类']
#         room['e' + str(i)].append(akk)
#     except:
#         akk = 0
#         room['e' + str(i)].append(akk)
#
#     try:
#             bkk = df[df['录入科室'] == c]['性质'].value_counts()['B类']
#             room['e' + str(i)].append(bkk)
#     except:
#             bkk = 0
#             room['e' + str(i)].append(bkk)
#
#     try:
#         ckk = df[df['录入科室'] == c]['性质'].value_counts()['C类']
#         room['e' + str(i)].append(ckk)
#     except:
#             ckk = 0
#             room['e' + str(i)].append(ckk)
#     try:
#             dkk = df[df['录入科室'] == c]['性质'].value_counts()['D类']
#             room['e' + str(i)].append(dkk)
#     except:
#             dkk = 0
#             room['e' + str(i)].append(dkk)
#     sum = akk + bkk + ckk + dkk
#     room['e' + str(i)].append(sum)
    # d = df[df['录入科室'] == c]['录入科室岗位'].unique()
    # room['e' + str(i)].append(str(d[0]))
    # e = df[df['录入科室'] == c]['录入科室'].unique()
    # room['e' + str(i)].append(str(e[0]))

