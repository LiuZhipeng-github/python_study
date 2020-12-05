from pymysql import connect
import pandas as pd
from sqlalchemy import create_engine
import sys
import pyecharts.options as opts
from pyecharts.charts import Line
import re

class CZ(object):
    def __init__(self):
        # 创建连接
        print('------欢迎登陆现场检查信息系统------')
        # name = 'root'
        # password = 'love530.'
        name=input('请输入用户名：')
        password=input('请输入密码：')
        try:
            self.conn = connect(host='localhost', port=3306, user=str(name),password=str(password),database='safemessage', charset='utf8')
            # 获得cursor 对象
            self.cursor = self.conn.cursor()
            print('登陆成功')
        except:
            print('密码或用户名错误,请重新登录')
            sys.exit()
        while True:
            self.table_name=input('请输入要操作的数据的年月（202006）')
            self.table = str(self.table_name)+'table'
            a = self.table_exists()
            if a == 1:
                print(f'您现在正在操作{self.table_name}的数据')
                break;
            else:
                print('1、请重新输入')
                print('2、进入仅插入数据模式')
                b=input('请输入选择')
                if b == '2':
                    self.run2()
                else:
                    pass;

    def __del__(self):
        # 关闭cursor 对象
        try:
            self.cursor.close()
            self.conn.close()
        except:
            pass

    def table_exists(self):
        sql = "show tables;"
        self.cursor.execute(sql)
        tables = [self.cursor.fetchall()]
        table_list = re.findall('(\'.*?\')', str(tables))
        table_list = [re.sub("'", '', each) for each in table_list]
        if self.table in table_list:
            return 1  # 存在返回1
        else:
            return 0

    def import_message(self):
        '''插入Excel信息'''
        try:
            engine = create_engine("mysql+pymysql://{}:{}@{}/{}?charset={}".format('root', 'love530.', '127.0.0.1:3306', 'safemessage','utf8mb4'))
            file_name = input('请输入新插入文件的文件名')
            df = pd.read_excel(f"./{file_name}")

            try:
                sql4 = (f"ALTER  TABLE {self.table} DROP id;")
                self.cursor.execute(sql4)
                sql3 = (f"alter table {self.table} add id int first;")
                self.cursor.execute(sql3)
                df.to_sql(name=self.table, con=engine, if_exists='append', index=True, index_label='id')
            except:
                df.to_sql(name=self.table, con=engine, if_exists='append', index=True, index_label='id')
            sql2 = (f"ALTER TABLE {self.table} DROP id;")
            self.cursor.execute(sql2)
            sql = (f"ALTER  TABLE {self.table} ADD id mediumint(6) PRIMARY KEY NOT NULL AUTO_INCREMENT FIRST;")
            self.cursor.execute(sql)
            print('插入成功')
        except:
            print('找不到文件或插入文件失败')

    def show_message(self):
        '''显示序号'''

        sql = (f"select id from {self.table} order by id desc limit 0,1;")
        self.cursor.execute(sql)
        Index = self.cursor.fetchone()[0]
        print(Index)

        name = input('请输入要查询的检查人')
        question = input('请输入检查时间')
        sql = ("select * from {} where 检查人 LIKE '%{}%' and 检查时间 LIKE '%{}%'".format(self.table, name, question))
        try:
            self.cursor.execute(sql)
            print('Count',self.cursor.rowcount)
            row=self.cursor.fetchone()
            n=self.cursor.rowcount
            i=0
            print('共有{}条数据'.format(n))
            if not n==0:
                while row:
                    i=i+1
                    print('这是第{}条数据'.format(i))
                    print(f'Row{i}:',row)
                    row=self.cursor.fetchone()
            else:
                print('无此数据,请重新尝试查询')
        except:
            print('查询数据失败')

    def add_message(self):
        try:
            a = input('请输入问题')
            b = input('请输入检查时间')
            c = input('请输入检查人')
            d = input('请输入检查人岗位')
            e = input('请输入录入科室')
            f = input('责任单位')
            g = input('责任人')
            h = input('责任人岗位')
            i = input('责任人政治面貌')
            j = input('整改期限')
            k = input('整改要求')
            l = input('整改时间')
            m = input('整改情况')
            n = input('复查时间')
            o = input('复查意见')
            p = input('风险项')
            E = input('风险点')
            q = input('风险因素')
            r = input('性质')
            s = input('分值（必要填写）')
            t = input('信息点')
            u = input('考核标记')
            v = input('考核分（必要填写）')
            w = input('特殊标记')
            x = input('责任科室')
            y = input('上报时间')
            z = input('科室整改时间')
            A = input('班组整改时间')
            B = input('分类')
            C = input('问题编号（必要填写）')
            sql = (f"select id from {self.table} order by id desc limit 0,1;")
            self.cursor.execute(sql)
            Index = self.cursor.fetchone()[0]+1
            T = (str(Index),str(a),str(b),str(c),str(d),str(e),str(f),str(g),str(h),str(i),str(j),str(k),str(l),str(m),str(n),str(o),str(p),str(E),str(q),str(r),str(s),str(t),str(u),str(v),str(w),str(x),str(y),str(z),str(A),str(B),str(C))
            sql = (f"insert into {self.table} values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')"%T)
            self.cursor.execute(sql)
            self.conn.commit()
            print('插入成功')
        except:
            print('插入失败')

    def amd_message(self):
        '''修改信息'''
        try:
            num=input('请输入要修改的信息的序号')
            title = input('请输入要修改的类型')
            after = input('请输入修改后的内容')
            sql = (f"UPDATE {self.table} SET %s='%s' where id='%s'")%(title,after,num)
            self.cursor.execute(sql)
            self.conn.commit()
            print('修改成功')
        except:
            print('修改失败，请重新修改')

    def del_message(self):
        try:
            num = input('请输入要删除的信息的序号')
            num = str(num)
            sql = (f"delete from {self.table} where id=%s" % num)
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            print('错误删除')

    def deal_message(self):
        print('1: 增加一条信息')
        print('2: 删除一条信息')
        print('3: 修改一条信息')
        print('4：返回上层菜单')
        nnn=input('请输入您所要执行的功能对应的序号：')
        if nnn == '1':
            self.add_message()
        elif nnn == '2':
            self.del_message()
        elif nnn == '3':
            self.amd_message()
        elif nnn == '4':
            self.run()

    def safe_message_count(self):
        print('本月基本信息统计')
        print('*************************************')
        df = pd.read_sql(f'select * from {self.table}', self.conn)
        safe_message_num = df['id'].count()
        print('本月安全息息条数：',safe_message_num)
        print('*************************************')
        print('本月发生不同性质的安全问题总数')
        group = df.groupby(by='性质').count()['id']
        print(group)
        print('*************************************')
        safe_message_score = df['分值'].sum()
        print(f'本月安全信息总分值为{safe_message_score}分')
        df['time'] = pd.to_datetime(df['检查时间'])
        print('**************其他功能****************')
        print('1、查询本月趋势图')
        print('2、本月小时趋势图')
        print('3、责任车间统计')
        print('4、责任人岗位统计')
        print('5、返回主菜单')
        p = input('请输入选择编号')
        if p == '1':
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
                except:
                    bkk = 0
                    yc.append(str(bkk))
            # print(yc, len(yc))
            yd = []
            for i in df['time'].unique():
                i = str(i)
                try:
                    bkk = df[df['time'] == i]['性质'].value_counts()['D类']
                    yd.append(str(bkk))
                except:
                    bkk = 0
                    yd.append(str(bkk))
            # print(yd, len(yd))
            x = df['time'].unique()
            a = []
            for i in x:
                a.append(str(i))
            (
                Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
                .add_xaxis(a)
                .add_yaxis("A类", ya)
                .add_yaxis("B类", yb)
                .add_yaxis("C类", yc)
                .add_yaxis("D类", yd)
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="现场安全信息性质分布(月)", subtitle=f"统计时间：{self.table_name}"),
                    tooltip_opts=opts.TooltipOpts(trigger="axis"),
                    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), name="日期"),
                    # toolbox_opts=opts.ToolBoxFeatureSaveAsImageOpts(background_color= "auto",type_='jpg'),
                    toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {}, "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]}, "dataView": {}}))

            .render(f"safe_message_month_{self.table_name}.html")

            )
            print('已画图成功')

        elif p == '2':
            df['time_H'] = df['time'].apply(lambda x: x.hour)
            x = df['time_H'].sort_values(ascending=True).unique()
            # print(df['time'],x)
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
            (
                Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
                .add_xaxis(a)
                .add_yaxis("A类", ya)
                .add_yaxis("B类", yb)
                .add_yaxis("C类", yc)
                .add_yaxis("D类", yd)
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="现场安全信息性质分布(小时)", subtitle=f"统计时间：{self.table_name}"),
                    tooltip_opts=opts.TooltipOpts(trigger="axis"),
                    xaxis_opts=opts.AxisOpts(name="时间"),
                    toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {}, "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]}, "dataView": {}}))
                .render(f"safe_message_hour_{self.table_name}.html")

            )
            print('已画图成功')
        elif p == '3':
            group = df.groupby(by=df['录入科室']).count()['性质']
            x = group.index.tolist()
            y = group.values.tolist()
            # print(x)
            # print(y)
            (
                Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
                .add_xaxis(x)
                .add_yaxis("数量", y)
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="现场安全信息车间统计分布", subtitle=f"统计时间：{self.table_name}"),
                    tooltip_opts=opts.TooltipOpts(trigger="axis"),
                    toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {}, "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]}, "dataView": {}}),
                    # xaxis_opts=opts.AxisOpts(name_rotate=60, name="车间名称",axislabel_opts={"rotate": 45}))
                    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30),name="车间名称"))
                .render(f"safe_message_chejian_{self.table_name}.html")

            )
            print('已画图成功')
        elif p == '4':
            group = df.groupby(by=df['责任人岗位']).count()['性质']
            x = group.index.tolist()
            y = group.values.tolist()
            # print(x)
            # print(y)
            (
                Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
                    .add_xaxis(x)
                    .add_yaxis("数量", y)
                    .set_global_opts(
                    title_opts=opts.TitleOpts(title="现场安全信息责任人岗位统计分布", subtitle=f"统计时间：{self.table_name}"),
                    tooltip_opts=opts.TooltipOpts(trigger="axis"),
                    toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {'backgroundColor': 'white'}, "dataZoom": {}, "restore": {}, "magicType": {"show": True, "type": ["line", "bar"]}, "dataView": {}}),
                    # xaxis_opts=opts.AxisOpts(name_rotate=60, name="车间名称",axislabel_opts={"rotate": 45}))
                    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=20), name="责任人岗位"))
                    .render(f"safe_message_duty_{self.table_name}.html")

            )
            print('已画图成功')
        else:
            self.run()

    # @staticmethod你可以简单理解为不需要self，也不能调用需要self的方法，需要self的都是实例级别的方法
    def show_menus(self):
        print(f'------现场检查信息系统(日期:{self.table_name})------')
        print('1: 现场检查信息导入')
        print('2: 现场检查信息应急处理')
        print('3: 查询现场检查信息')
        print('4：安全信息综合情况统计')
        print('5: 退出系统')
        return input('请输入您所要执行的功能对应的序号：')

    def show_menus2(self):
        print(f'------(仅导入模式)现场检查信息系统(日期:{self.table_name})------')
        print('1: 现场检查信息导入')
        print('2: 退出系统')
        return input('请输入您所要执行的功能对应的序号：')

    def run2(self):
        while True:
            num = self.show_menus2()
            if num == '1':
                self.import_message()
            elif num =='2':
                 sys.exit()
            else:
                print('输入有误，请重新输入')

    def run(self):
        while True:
            num = self.show_menus()
            if num == '1':
                self.import_message()
            elif num == '2':
                self.deal_message()
            elif num == '3':
                self.show_message()
            elif num == '4':
                self.safe_message_count()
            elif num == '5':
                sys.exit()
            else:
                print('输入有误，请重新输入')


def main():
    # 创建一个对象
    cz = CZ()
    # 调用这个对象的run方法，让其运行
    cz.run()


if __name__ == '__main__':
    main()
