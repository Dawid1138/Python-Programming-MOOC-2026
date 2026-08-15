from datetime import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False
        
    control_str = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    day_str = pic[0:2]
    month_str = pic[2:4]
    year_str = pic[4:6]

    if pic[6] == "+":
        centry_str = "18"
    elif pic[6] == "-":
        centry_str = "19"
    elif pic[6] == "A":
        centry_str = "20"
    else:
        return False

    try:
        date_born = datetime(int(centry_str + year_str), int(month_str), int(day_str))
        long_number = int(day_str + month_str + year_str + pic[7:10])
    except:
        return False

    date_now = datetime.now()
    date_min = datetime(1800, 1, 1)
    if not (date_born <= date_now and date_born >= date_min):
        return False

    index_control_nummber = long_number % 31
    if pic[10] == control_str[index_control_nummber]:
        return True
    else:
        return False