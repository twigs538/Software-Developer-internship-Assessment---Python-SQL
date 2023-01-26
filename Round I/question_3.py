from datetime import datetime, timedelta

def compute_prev_date(dates_list:list):
    """
    """
    out_date = []
    for i in range(len(dates_list)):
        x = datetime.fromisoformat(dates_list[i])
        x = x - timedelta(days=1)
        out_date.append(x.strftime("%d %b %Y"))

    return out_date
    return [ """your code here""" ]

print(compute_prev_date(['1999-01-21', '2022-12-30', '2099-12-21']))