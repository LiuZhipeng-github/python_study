from flask import Blueprint



tester = Blueprint('tester',__name__)
@tester.route("/to_chart1")
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