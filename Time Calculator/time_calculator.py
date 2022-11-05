def add_time(start, duration, day=""):
    #day_name = {"": 0,"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
    day_name = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    hour = start.split(":")[0]
    minutes_sun = start.split(":")[1]
    minutes = minutes_sun.split(" ")[0]
    sun = minutes_sun.split(" ")[1]
    
    durh = int(duration.split(":")[0])
    durm = int(duration.split(":")[1])
          
    new_min = int(minutes) + durm
    days = 0
    days_count = ""
    if new_min >= 60:
        durh += new_min / 60
        new_min = new_min % 60

    new_hour = int(hour) + int(durh)

    if new_hour >= 24:
        days = int(new_hour / 24)
        new_hour = new_hour % 24
          
    if new_hour >= 12:
        new_hour = new_hour - 12
        if sun == "AM":
            sun = "PM"
        else:
            sun = "AM"
            days += 1
  
    if days >= 2:
        days_count = " (" + str(days) + " days later)"
    elif days >= 1:
        days_count = " (next day)"

    if len(str(new_min)) < 2:
        final_minute = "0" + str(new_min)
    else:
        final_minute = str(new_min)

    if new_hour == 0:
      new_hour = 12
    else:
      new_hour = new_hour
      
    if day.lower() in day_name:
      day = ", " + day_name[(day_name.index(day.lower()) + int(days))%7].capitalize()
      
    return str(new_hour)+":" + str(final_minute)+" "+ sun + day + (days_count)
    # print(str(new_hour)+":" + str(final_minute)+" "+ sun + day + (days_count))


