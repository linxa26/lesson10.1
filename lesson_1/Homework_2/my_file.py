weekdays = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
work = [True, True, True, True, True, False, False]
plans = ["за покупками", "отдыхать", "играть", "лениться", "гулять", "кутить", "страдать"]

for x in range(len(weekdays), len(work), len(plans)):

    if work[x] == True:
        print(f'{weekdays[x]} - это рабочий день, а вечером {plans[x]}')
    else:
        print(f'{weekdays[x]} - это выходной день, а вечером{plans[x]}')
