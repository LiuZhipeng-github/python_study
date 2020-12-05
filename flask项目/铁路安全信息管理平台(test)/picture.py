import pyecharts.options as opts
from pyecharts.charts import Line ,Pie
import pandas as pd
import datetime,json
import pymysql
from flask import request
from flask_paginate import get_page_args,Pagination
class picture(object):
    def __init__(self):
        today = datetime.date.today()
        first = today.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        self.table_name = '`2020-05`'
        # self.last_month = lastMonth.strftime("%Y-%m")
        self.last_month = '2020-06'

        self.conn = pymysql.connect(host='localhost', user="root", passwd='love530.', db='test')
        self.cursor = self.conn.cursor()
    def picture1(self):
        df = pd.read_sql(f"select * from {self.table_name} where 检查时间 LIKE '%{self.last_month}%'", self.conn)
        df['time'] = pd.to_datetime(df['检查时间'])
        df['time'] = df['time'].apply(lambda x: x.strftime('%Y%m%d'))
        ya = []
        for i in df['time'].unique():
            i = str(i)
            try:
                bkk = df[df['time'] == i]['性质'].value_counts()['A类']
                ya.append(str(bkk))
            except:
                bkk = 0
                ya.append(str(bkk))
        # print(ya, len(ya))
        yb = []
        for i in df['time'].unique():
            i = str(i)
            try:
                bkk = df[df['time'] == i]['性质'].value_counts()['B类']
                yb.append(str(bkk))

            except:
                bkk = 0
                yb.append(str(bkk))
        # print(yb, len(yb))
        yc = []
        for i in df['time'].unique():
            i = str(i)
            try:
                bkk = df[df['time'] == i]['性质'].value_counts()['C类']
                yc.append(str(bkk))
                print(yc)
            except:
                bkk = 0
                yc.append(str(bkk))
        print(yc, len(yc))
        yd = []
        for i in df['time'].unique():
            i = str(i)
            try:
                bkk = df[df['time'] == i]['性质'].value_counts()['D类']
                yd.append(str(bkk))
            except:
                bkk = 0
                yd.append(str(bkk))
        x = df['time'].unique()
        # chart = picture(x,ya,yb,yc,yd)
        a = []
        for i in x:
            a.append(str(i))
        c=(

            Line(init_opts=opts.InitOpts(page_title=f"现场安全信息性质分布(月)"))
                .add_xaxis(a)
                .add_yaxis("A类", ya)
                .add_yaxis("B类", yb)
                .add_yaxis("C类", yc)
                .add_yaxis("D类", yd)
                .set_global_opts(
                title_opts=opts.TitleOpts(title=f"现场安全信息性质分布(月)", subtitle=f"统计时间：{self.last_month}"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), name="日期"),
                # toolbox_opts=opts.ToolBoxFeatureSaveAsImageOpts(background_color= "auto",type_='jpg'),
                toolbox_opts=opts.ToolboxOpts(is_show=True,
                                              feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {},
                                                       "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]},
                                                       "dataView": {}}),
                )
        )
        print('已画图成功')
        return c
    def picture2(self):
        df = pd.read_sql(f"select * from {self.table_name} where 检查时间 LIKE '%{self.last_month}%'", self.conn)
        df['time'] = pd.to_datetime(df['检查时间'])
        df['time_H'] = df['time'].apply(lambda x: x.hour)
        x = df['time_H'].sort_values(ascending=True).unique()
        ya = []
        for i in x:
            try:
                bkk = df[df['time_H'] == i]['性质'].value_counts()['A类']
                ya.append(str(bkk))
            except:
                bkk = 0
                ya.append(str(bkk))
        # print(ya, len(ya))
        yb = []
        for i in x:
            try:
                bkk = df[df['time_H'] == i]['性质'].value_counts()['B类']
                yb.append(str(bkk))
            except:
                bkk = 0
                yb.append(str(bkk))
        # print(yb, len(yb))
        yc = []
        for i in x:
            try:
                bkk = df[df['time_H'] == i]['性质'].value_counts()['C类']
                yc.append(str(bkk))
            except:
                bkk = 0
                yc.append(str(bkk))
        # print(yc, len(yc))
        yd = []
        for i in x:
            try:
                bkk = df[df['time_H'] == i]['性质'].value_counts()['D类']
                yd.append(str(bkk))
            except:
                bkk = 0
                yd.append(str(bkk))
        # print(yd, len(yd))
        a = []
        for i in x:
            m = str(i)+':00'
            a.append(m)
        e = (
            Line()
            .add_xaxis(a)
            .add_yaxis("A类", ya)
            .add_yaxis("B类", yb)
            .add_yaxis("C类", yc)
            .add_yaxis("D类", yd)
            .set_global_opts(
                title_opts=opts.TitleOpts(title=f"现场安全信息性质分布(时)", subtitle=f"统计时间：{self.last_month}"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                xaxis_opts=opts.AxisOpts(name="时间"),
                toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {}, "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]}, "dataView": {}}))
            # .render(f"safe_message_hour_{self.table_name}.html")

        )
        print('已画图成功')
        return e
    def picture3(self):
            df = pd.read_sql(f"select * from {self.table_name} where 检查时间 LIKE '%{self.last_month}%'", self.conn)
            group = df.groupby(by=df['录入科室']).count()['性质']
            x = group.index.tolist()
            y = group.values.tolist()
            # print(x)
            # print(y)
            c=(
                Line(init_opts=opts.InitOpts())
                    .add_xaxis(x)
                    .add_yaxis("数量", y)
                    .set_global_opts(
                    title_opts=opts.TitleOpts(title="现场安全信息车间统计分布", subtitle=f"统计时间：{self.last_month}"),
                    tooltip_opts=opts.TooltipOpts(trigger="axis"),
                    toolbox_opts=opts.ToolboxOpts(is_show=True,
                                                  feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {},
                                                           "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]},
                                                           "dataView": {}}),
                    # xaxis_opts=opts.AxisOpts(name_rotate=60, name="车间名称",axislabel_opts={"rotate": 45}))
                    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30), name="车间名称"))
                    # .render(f"safe_message_chejian_.html")

            )
            print('已画图成功')
            return c
    def picture4(self):
        df = pd.read_sql(f"select * from {self.table_name} where 检查时间 LIKE '%{self.last_month}%'", self.conn)
        group = df.groupby(by=df['责任人岗位']).count()['性质']
        x = group.index.tolist()
        y = group.values.tolist()
        c=(
            Line(init_opts=opts.InitOpts())
                .add_xaxis(x)
                .add_yaxis("数量", y)
                .set_global_opts(
                title_opts=opts.TitleOpts(title="现场安全信息责任人岗位统计分布", subtitle=f"统计时间：{self.last_month}"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(is_show=True,
                                              feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {},
                                                       "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]},
                                                       "dataView": {}}),
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=20), name="责任人岗位"))
        )
        print('已画图成功')
        return c
    def half_year(self):
        df = pd.read_sql(f"select * from {self.table_name}", self.conn)
        df['time'] = pd.to_datetime(df['检查时间'])
        df['time'] = df['time'].apply(lambda x: x.strftime('%Y-%m'))
        print(df['time'].unique()[-6:])
        timelist = df['time'].unique()[-6:].tolist()
        ya = []
        yb = []
        yc = []
        yd = []
        for i in timelist:
            group = df[df['time'] == i]['性质'].value_counts()['A类']
            ya.append(str(group))
            group = df[df['time'] == i]['性质'].value_counts()['B类']
            yb.append(str(group))
            group = df[df['time'] == i]['性质'].value_counts()['C类']
            yc.append(str(group))
            try:
                group = df[df['time'] == i]['性质'].value_counts()['D类']
                yd.append(str(group))
            except:
                group = 0
                yd.append(str(group))
        print(ya)
        print(yb)
        print(yc)
        print(yd)
        c = (

            Line(init_opts=opts.InitOpts(page_title=f"现场安全信息性质分布(半年)"))
                .add_xaxis(timelist)
                .add_yaxis("A类", ya)
                .add_yaxis("B类", yb)
                .add_yaxis("C类", yc)
                .add_yaxis("D类", yd)
                .set_global_opts(
                title_opts=opts.TitleOpts(title=f"现场安全信息性质分布(半年)", subtitle=f"统计时间：{self.last_month}"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), name="日期"),
                # toolbox_opts=opts.ToolBoxFeatureSaveAsImageOpts(background_color= "auto",type_='jpg'),
                toolbox_opts=opts.ToolboxOpts(is_show=True,
                                              feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {},
                                                       "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]},
                                                       "dataView": {}}),
            )
        )
        print('已画图成功')
        return c
    def half_year_score(self):
        df = pd.read_sql(f"select * from {self.table_name}", self.conn)
        df['time'] = pd.to_datetime(df['检查时间'])
        df['time'] = df['time'].apply(lambda x: x.strftime('%Y-%m'))
        print(df['time'].unique()[-6:])
        timelist = df['time'].unique()[-6:].tolist()
        ya = []
        yb = []
        for i in timelist:
            group = df[df['time'] == i]['分值'].sum()
            ya.append(str(group))
            group = df[df['time'] == i]['考核分'].sum()
            yb.append(str(int(group)))
        print(ya)
        print(yb)
        c = (

            Line(init_opts=opts.InitOpts(page_title=f"现场安全信息性质分布(月)"))
                .add_xaxis(timelist)
                .add_yaxis("分值", ya)
                .add_yaxis("考核分", yb)
                .set_global_opts(
                title_opts=opts.TitleOpts(title=f"现场安全信息性质分布(月)", subtitle=f"统计时间：{self.last_month}"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), name="日期"),
                # toolbox_opts=opts.ToolBoxFeatureSaveAsImageOpts(background_color= "auto",type_='jpg'),
                toolbox_opts=opts.ToolboxOpts(is_show=True,
                                              feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {},
                                                       "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]},
                                                       "dataView": {}}),
            )
        )
        print('已画图成功')
        return c
    def pie_class(self):
        df = pd.read_sql(f"select * from {self.table_name} where 检查时间 LIKE '%{self.last_month}%'", self.conn)
        class_ = df['分类'].unique().tolist()
        print(class_)
        y = []
        for i in class_:
            group = df['分类'].value_counts()[i]
            y.append(str(group))
        c = (
            Pie()
                .add("", [list(z) for z in zip(class_, y)])
                .set_colors(["orange", "purple", "pink"])
                .set_global_opts(title_opts=opts.TitleOpts(
                title="分类",
                pos_left=60,
                title_textstyle_opts=opts.TextStyleOpts(color="black"),
            ),
            )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        return c
    def pie_denger(self):
        df = pd.read_sql(f"select * from {self.table_name} where 检查时间 LIKE '%{self.last_month}%'", self.conn)
        class_ = df['风险因素'].unique().tolist()
        print(class_)
        y = []
        for i in class_:
            group = df['风险因素'].value_counts()[i]
            y.append(str(group))
        c = (
            Pie()
                .add(
                "",
                [list(z) for z in zip(class_, y)],
                radius=["40%", "75%"],
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="风险因素分类"),
                legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
            )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        return c
    def pie_room(self):
        df = pd.read_sql(f"select * from {self.table_name} where 检查时间 LIKE '%{self.last_month}%'", self.conn)
        class_ = df['责任科室'].unique().tolist()
        print(class_)
        y = []
        for i in class_:
            group = df['责任科室'].value_counts()[i]
            y.append(str(group))
        print(y)
        c = (
            Pie()
                .add(
                "",
                [list(z) for z in zip(class_, y)],
                radius=["40%", "60%"],
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="风险因素分类"),
                legend_opts=opts.LegendOpts(orient="horizontal", pos_bottom=0),
            )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

        )
        return c
    def pie_face(self):
        df = pd.read_sql(f"select * from {self.table_name} where 检查时间 LIKE '%{self.last_month}%'", self.conn)
        e = 0
        rel = df['责任人政治面貌'].fillna(value='群众')
        face = ['党员', '团员', '群众', '工商联']
        rel = rel.tolist()
        print(len(rel))
        face_num = []
        for j in face:
            for i in rel:
                a = i.count(j, 0, len(i))
                e = e + a
            face_num.append(str(e))
            e = 0
        c = (
            Pie()
                .add(
                "",
                [list(z) for z in zip(face, face_num)],
                radius=["40%", "60%"],
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="风险因素分类"),
                legend_opts=opts.LegendOpts(orient="horizontal", pos_bottom=0),
            )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        return c
    def people(self):
        df = pd.read_sql(f"select * from `2020-05` where 检查时间 LIKE '%{self.last_month}%'", self.conn)
        group = df.groupby(by=df['责任人']).count()['性质'].sort_values(ascending=False)[:3]
        a = group.index.tolist()
        people = locals()
        for i in range(3):
            people['e' + str(i)] = []
            c = a[i]
            people['e' + str(i)].append(c)
            try:
                akk = df[df['责任人'] == c]['性质'].value_counts()['A类']
                people['e' + str(i)].append(akk)
            except:
                akk = 0
                people['e' + str(i)].append(akk)

            try:
                bkk = df[df['责任人'] == c]['性质'].value_counts()['B类']
                people['e' + str(i)].append(bkk)
            except:
                bkk = 0
                people['e' + str(i)].append(bkk)

            try:
                ckk = df[df['责任人'] == c]['性质'].value_counts()['C类']
                people['e' + str(i)].append(ckk)
            except:
                ckk = 0
                people['e' + str(i)].append(ckk)
            try:
                dkk = df[df['责任人'] == c]['性质'].value_counts()['D类']
                people['e' + str(i)].append(dkk)
            except:
                dkk = 0
                people['e' + str(i)].append(dkk)
            sum = akk + bkk + ckk + dkk
            people['e' + str(i)].append(sum)
            d = df[df['责任人'] == c]['责任人岗位'].unique()
            people['e' + str(i)].append(str(d[0]))
            e = df[df['责任人'] == c]['录入科室'].unique()
            people['e' + str(i)].append(str(e[0]))
        return (people['e' + '0'], people['e' + '1'], people['e' + '2'])
    def room(self):
        df = pd.read_sql(f"select * from `2020-05` where 检查时间 LIKE '%{self.last_month}%'", self.conn)
        group = df.groupby(by=df['录入科室']).count()['性质'].sort_values(ascending=False)[:3]
        a = group.index.tolist()
        room = locals()
        for i in range(3):
            room['e' + str(i)] = []
            c = a[i]
            room['e' + str(i)].append(c)
            try:
                akk = df[df['录入科室'] == c]['性质'].value_counts()['A类']
                room['e' + str(i)].append(akk)
            except:
                akk = 0
                room['e' + str(i)].append(akk)

            try:
                bkk = df[df['录入科室'] == c]['性质'].value_counts()['B类']
                room['e' + str(i)].append(bkk)
            except:
                bkk = 0
                room['e' + str(i)].append(bkk)

            try:
                ckk = df[df['录入科室'] == c]['性质'].value_counts()['C类']
                room['e' + str(i)].append(ckk)
            except:
                ckk = 0
                room['e' + str(i)].append(ckk)
            try:
                dkk = df[df['录入科室'] == c]['性质'].value_counts()['D类']
                room['e' + str(i)].append(dkk)
            except:
                dkk = 0
                room['e' + str(i)].append(dkk)
            sum = akk + bkk + ckk + dkk
            room['e' + str(i)].append(sum)


        return (room['e' + '0'], room['e' + '1'], room['e' + '2'])
    def edit(self):
        data = request.form.get("to_edit")
        sql = (f"select * from {self.table_name} where id=%s" % data)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        data = list(data)
        return data
    def month_search(self):
        month_se = request.form.get('month')
        sql = ("select * from {} where 检查时间 LIKE '%{}%'".format(self.table_name, month_se))
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
    def more_people(self):
        more = request.form.get('more')
        print(more)
        sql = ("select * from {} where 责任人 LIKE '%{}%'".format(self.table_name, more))
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
    def more_room(self):
        more = request.form.get('more')
        print(more)
        sql = ("select * from {} where 录入科室 LIKE '%{}%'".format(self.table_name, more))
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
    def delete_(self):
        data = json.loads(str(request.form.get('data')))
        userId = data['x']
        print(userId)
        sql = (f"delete from {self.table_name} where id=%s" % userId)
        print('删了')
        self.cursor.execute(sql)
        self.conn.commit()
    def show_details(self):
        val = request.form.get("details")
        print(val)
        sql = (f"select * from {self.table_name} where id=%s" % val)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        data = list(data)
        return data
    def add_new(self):
        description = request.form.get('description')
        time = request.form.get('time')
        day_time = request.form.get('day_time')
        jianchaname = request.form.get('jianchaname')
        jianchagangwei = request.form.get('jianchagangwei')
        lurukeshi = request.form.get('lurukeshi')
        zerendanwei = request.form.get('zerendanwei')
        zerenname = request.form.get('zerenname')
        zerengangwei = request.form.get('zerengangwei')
        zerenpolitics = request.form.get('zerenpolitics')
        amdday_final = request.form.get('amdday_final')
        amdrequest = request.form.get('amdrequest')
        amdtime = request.form.get('amdtime')
        amdday = request.form.get('amdday')
        amd = request.form.get('amd')
        relook = request.form.get('relook')
        advice = request.form.get('advice')
        fengixan = request.form.get('fengixan')
        denger_point = request.form.get('denger_point')
        denger = request.form.get('denger')
        xingzhi = request.form.get('xingzhi')
        grade = request.form.get('grade')
        message = request.form.get('message')
        point = request.form.get('point')
        testgrade = request.form.get('testgrade')
        special = request.form.get('special')
        zerenroom = request.form.get('zerenroom')
        reporttime = request.form.get('reporttime')
        keshi_time = request.form.get('keshi_time')
        banzu_time = request.form.get('banzu_time')
        sort = request.form.get('sort')
        question_number = request.form.get('question_number')

        amdtime = amdday + ' ' + amdtime
        time = day_time + ' ' + time

        pos = str(day_time).rfind("-")
        table = str(day_time)[:pos]
        print(table)

        sql = (f"select id from {self.table_name} order by id desc limit 0,1;")
        self.cursor.execute(sql)
        Index = self.cursor.fetchone()[0] + 1

        T = (str(Index), str(description), str(time), str(jianchaname), str(jianchagangwei), str(lurukeshi),
             str(zerendanwei), str(zerenname), str(zerengangwei), str(zerenpolitics), str(amdday_final),
             str(amdrequest), str(amdtime), str(amd), str(relook), str(advice), str(fengixan), str(denger_point),
             str(denger), str(xingzhi), str(grade), str(message), str(point), str(testgrade), str(special),
             str(zerenroom), str(reporttime), str(keshi_time), str(banzu_time), str(sort), str(question_number))
        print(T)
        sql = (
                f"insert into {self.table_name} values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" % T)

        self.cursor.execute(sql)
        self.conn.commit()