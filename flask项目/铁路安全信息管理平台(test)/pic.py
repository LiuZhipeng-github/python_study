from flask import Blueprint,render_template,session
import picture
from session import is_login

tester = Blueprint('tester',__name__)

@tester.route("/to_chart1")
# @is_login
def show_pyecharts1():
    pic1 = picture.picture().picture1()
    pic2 = picture.picture().picture2()
    pic3 = picture.picture().half_year()
    pic4 = picture.picture().half_year_score()
    return render_template(
        "all-charts-time.html",
        data1=pic1.dump_options(),
        data2 = pic2.dump_options(),
        data3 =pic3.dump_options(),
        data4 = pic4.dump_options(),
      )
@tester.route("/to_chart2")
def show_pyecharts2():
    data='89'
    pic1 = picture.picture().pie_class()
    pic2 = picture.picture().pie_denger()
    return render_template(
        "all-charts-class.html",
        data1=pic1.dump_options(),
        data2=pic2.dump_options(),
        data=data
      )
@tester.route("/to_chart3")
def show_pyecharts3():
    data='89'
    pic1 = picture.picture().pie_room()
    pic3 = picture.picture().picture3()
    return render_template(
        "all-charts-room.html",
        data1=pic1.dump_options(),
        data2 =pic3.dump_options(),
        data=data
      )
@tester.route("/to_chart4")
def show_pyecharts4():
    data='89'
    pic1 = picture.picture().pie_face()
    pic4 = picture.picture().picture4()
    return render_template(
        "all-charts-other.html",
        data1=pic1.dump_options(),
        data2=pic4.dump_options(),
        data=data
      )