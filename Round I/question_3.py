import datetime
import locale

def compute_prev_date(dates_list:list):
    locale.setlocale(locale.LC_ALL, '')
    prev_dates = []
    for date_str in dates_list:
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        prev_date = date - datetime.timedelta(days=1)
        prev_date_str = prev_date.strftime('%d %b %Y')
        prev_dates.append(prev_date_str)
    return prev_dates

print(compute_prev_date(['1999-01-21', '2022-12-30', '2099-12-21']))