# 计算最后一个周五的日期
from datetime import datetime, timedelta
weekdays = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
]

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(datetime)
    days_go = (7 + day_num - day_num_target) % 7
    if days_go == 0:
        days_go = 7
    target_date = start_date - timedelta(days=days_go)
    return target_date