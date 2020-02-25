from docxtpl import DocxTemplate
import random
import datetime


def give_me_time():
    time_list = []
    start_time = "08:10 " + date_today
    while len(time_list) < 13:
        random_minutes = random.randrange(95, 120, 5)
        start_datetime_time = datetime.datetime.strptime(start_time, "%H:%M %d.%m.%y")
        next_datetime_time = start_datetime_time + datetime.timedelta(minutes=random_minutes)
        time_list.append(next_datetime_time.strftime('%H:%M %d.%m.%y'))
        start_time = str(next_datetime_time.strftime('%H:%M %d.%m.%y'))
    return time_list


date_today = datetime.datetime.now().strftime("%d.%m.%y")
date_tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d.%m.%y")

warehouse_territory_time_bypass = {'ГСМ': give_me_time()}

doc = DocxTemplate("test.docx")

context = {'date_today': date_today,
           'date_tomorrow': date_tomorrow,
           'time_bypass': warehouse_territory_time_bypass
           }
doc.render(context)
doc.save("generated_doc.docx")
