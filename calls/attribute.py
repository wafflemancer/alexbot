from datetime import datetime
import math 
import re

attributes=["Nil","Chandra","Asvins","Brahma","Vayu","Surya","Agni","Varuna","Indra","Kubera","Marut","Yama"]
failure_message = 'use this format pls \'yyyy-mm-dd hh\''


def get_attributes(test_birthday):
    dp = _get_dateparts(test_birthday)
    if dp is None:
        return failure_message
    else:
        day, month, year, hour = dp
        out = _kubera_calc(day, month, year, hour, attributes)
    return out


def get_today():
    current_time = datetime.now()
    out = _kubera_calc(current_time.day, current_time.month,
                       current_time.year, current_time.hour, attributes, today=True)
    return out
    

def _get_dateparts(test_birthday):
    # get date
    test_date = test_birthday[0:10]
    pattern = re.compile(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))")
    # match the pattern
    match = re.search(pattern, test_date)
    if match is None:
        return None
    match = match[0]
    # get the year, month, date parts of match string
    year = int(match[0:4])
    month = int(match[5:7])
    day = int(match[8:10])

    # get hour
    test_hour = test_birthday[11:]
    try:
        # format hour and make sure it's correct
        hour = int(test_hour)
        if hour < 0 or hour > 24:
            return None
    except:
        return None
    return (day, month, year, hour)


def _kubera_calc(day,month,year,hour,attributes,today=False):

    start_day=6
    start_month=2
    start_year=1990
    
    if month>2:
        leapdays=int(math.ceil((year-start_year)/4))
    else:
        leapdays=int(math.floor((year-start_year)/4))
    nbr_days=leapdays+(year-start_year)*365+(day-start_day)
    
    y=month-start_month
    z=1
    
    if y<0:
        y=-y
        z=-1

    for x in range(y):
        if x==3 or x==5 or x==8 or x==10:
            nbr_days+=30*z
        else:
            if x==1:
                nbr_days+=28*z
            else:
                nbr_days+=31*z
    
    if nbr_days>0:
        nd="N"
        show_year=nd+str(math.floor(nbr_days/432))
    else:
        nd="D"
        show_year=nd+str(1000+(math.floor(nbr_days/432)))

    out = ("Year:", show_year, "\nMonth:", math.floor((nbr_days % 432)/36) % 12+1, attributes[(math.floor((nbr_days % 432)/36) % 12)], "\nDay:", ((((nbr_days % 432) % 36) % 432) % 12)+1, attributes[((((nbr_days % 432) % 36) % 432) % 12)], "\nHour:", (math.floor(hour/2)) % 12+1, attributes[(math.floor(hour/2)) % 12])
    out = [str(i) for i in out]
    out = ' '.join(out)
    if today:
        return 'Today is:\n{}'.format(out)
    else:
        return 'You were born on:\n{}'.format(out)
