import calendar
def get_quarters_day(date_obj):
        month = date_obj.month
        quarter = (month -1)//3+1
        year = date_obj.year
        month_day = date_obj.day
        first_month_of_quarter = 3 * quarter - 2
        second_month_of_quarter = 3 * quarter - 1
        last_month_of_quarter = 3 * quarter

        if month == first_month_of_quarter:
            return month_day
        if month == second_month_of_quarter:
            return calendar.monthrange(year,first_month_of_quarter)[1]+month_day
        if month == last_month_of_quarter:
            return calendar.monthrange(year,first_month_of_quarter)[1]+calendar.monthrange(year,second_month_of_quarter)[1]+month_day