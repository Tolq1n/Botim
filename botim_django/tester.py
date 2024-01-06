import calendar

yy = 2023
mm = 12
# month
# display the calendar
print( calendar. month (yy, mm))
from datetime import datetime, timedelta
from pprint import pprint

SHORT_DAY_NAMES_EN = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

SHORT_DAY_NAMES_RU = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

SHORT_DAY_NAMES_UZ = ['Du', 'Se', 'Chor', 'Pay', 'Jum', 'Shan', 'Yak']

def get():
    language = 'ru'
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    
    # Data for the current week
    days_of_week_current = [start_of_week + timedelta(days=x) for x in range(7)]
    SHORT_DAY_NAMES = SHORT_DAY_NAMES_UZ if language == 'uz' else SHORT_DAY_NAMES_RU if language == 'ru' else SHORT_DAY_NAMES_EN
    week_data_current = [{'id': day.weekday(), 'day': day.strftime('%Y-%m-%d'), 'name': name} for day, name in zip(days_of_week_current, SHORT_DAY_NAMES)]
    
    # Data for the next week
    start_of_next_week = start_of_week + timedelta(days=7)
    days_of_week_next = [start_of_next_week + timedelta(days=x) for x in range(7)]
    week_data_next = [{'id': day.weekday(), 'day': day.strftime('%Y-%m-%d'), 'name': name} for day, name in zip(days_of_week_next, SHORT_DAY_NAMES)]
    
    # Combine current and next week's data
    combined_week_data = {
        'current_week': week_data_current,
        'next_week': week_data_next
    }
    
    pprint(combined_week_data)

get()
