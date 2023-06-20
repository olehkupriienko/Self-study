from typing import Union

test1 = "07:00"  # 15
test2 = "01:23"  # "I don't see the sun!"
test3 = "12:15"
test4 = "18:02"
test5 = "05:59"


def sun_angle(time: str):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    if hours < 6 or (hours >= 18 and minutes > 0):
        return "I don't see the sun!"
    else:
        result = (hours * 60 + minutes - 360) * 0.25
        return result if result % 1 != 0 else int(result)


print(sun_angle(test1))
print(sun_angle(test2))
print(sun_angle(test3))
print(sun_angle(test4))
print(sun_angle(test5))
