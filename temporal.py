from flask import Flask,render_template,request
import dateparser
from quarters.quarters_day import get_quarters_day

app = Flask(__name__)

@app.route('/')
def date_input():
    return render_template('date_input.html')

@app.route('/temporal',methods = ['POST', 'GET'])
def temporal_data():
    if request.method == 'POST':
        input_date = request.form['input_date']
        date_obj = dateparser.parse(input_date)
        date_year = date_obj.year
        date_month = date_obj.month
        date_qtr = (date_month -1)//3+1
        qtr_day = get_quarters_day(date_obj)

        context = {
            "YearMonthNum":"{}{}".format(date_year,date_month),
            "Calendar_Quarter":"Qtr{}".format(date_qtr),
            "MonthNum":"{}".format(date_month),
            "MonthName":"{}".format(date_obj.strftime("%B")),
            "MonthShortName":"{}".format(date_obj.strftime("%b")),
            "WeekNum":"{}".format(date_obj.strftime("%V")),
            "DayNumOfYear":"{}".format(date_obj.timetuple().tm_yday),
            "DayNumOfMonth":"{}".format(date_obj.day),
            "DayNumOfWeek":"{}".format(date_obj.weekday()+1),
            "DayName":"{}".format(date_obj.strftime("%A")),
            "DayShortName":"{}".format(date_obj.strftime("%a")),
            "Quarter":"{}".format(date_qtr),
            "YearQuarterNum":"{}{}".format(date_year,date_qtr),
            "DayNumOfQuarter":"{}".format(qtr_day)
                }
        return render_template('temporal.html',result=context)
    return render_template('date_input.html')
   

if __name__ == '__main__':
   app.run()
