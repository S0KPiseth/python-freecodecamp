def get_time(n):
    time = n[-2:-1]+n[-1]
    if not time.isdigit():
        real_time = n[0: n.index(time)]
        time_list = real_time.split(':')
        return time_list, time
    else:
        time_list = n.split(':')
        return time_list
def get_day(current, duration):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = (days.index(current.capitalize()) + duration)%7
    return days[day]

def add_time(start, duration, day=None):
    meridiems = ["AM", "PM"]
    nod =''
    

    real_start, orgin_md = get_time(start)
    real_duration = get_time(duration)
    time = orgin_md
    s_hour= int(real_start[0])
    s_minute= int(real_start[1])
    d_hour= int(real_duration[0])
    d_minute= int(real_duration[1])
    total_hour = (s_hour+d_hour)
    total_minute = (s_minute+d_minute)
    if total_minute >=60:
        add_hour = total_minute//60
        total_hour += add_hour
        total_minute %=60
    if total_hour%12 ==0 and total_hour!=0:
        display_hour = 12
    else:
        display_hour = total_hour%12
    if total_hour >=12:
        index = meridiems.index(orgin_md)
        time = meridiems[(index+(total_hour//12))%2]

    if total_hour>=12 and time == "AM":

        if (total_hour- s_hour)%24 ==0:
            display_nod =1
        else:
            display_nod=(total_hour- s_hour)//24 +1
        
        nod = "next day" if display_nod==1 else f"{display_nod} days later"
        if day:
            which_day = get_day(day,display_nod)
    elif day:
        which_day = day

    if day:
        new_time=f'{display_hour}:{str(total_minute).zfill(2)} {time}, {which_day}'
        if nod:
            new_time=f'{display_hour}:{str(total_minute).zfill(2)} {time}, {which_day} ({nod})'
    else:
        new_time=f'{display_hour}:{str(total_minute).zfill(2)} {time}'

        if nod:
            new_time=f'{display_hour}:{str(total_minute).zfill(2)} {time} ({nod})'
    
    return new_time

print(add_time('11:55 AM', '12:05'))