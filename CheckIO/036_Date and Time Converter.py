def date_time(time: str) -> str:
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
              8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    date, time = time.split(' ')
    day, month, year = map(int, date.split('.'))
    hour, minute = map(int, time.split(':'))
    reformat_date = f'{day} {months[month]} {year} year {hour} ' \
                    + ('hour' if hour == 1 else 'hours') \
                    + f' {minute}' \
                    + (' minute' if minute == 1 else ' minutes')
    return reformat_date


print(date_time("01.01.2000 00:00"))
print(date_time("19.09.2999 01:59"))
print(date_time("21.10.1999 18:01"))
print(date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes")
print(date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes")
print(date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute")
