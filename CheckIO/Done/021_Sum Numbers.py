test = 'This picture is an oil on canvas ' \
       'painting by Danish artist Anna ' \
       'Petersen between 1845 and 1910 year'


def sum_numbers(text: str) -> int:
    # your code here
    lst = [int(i) for i in text.split(' ') if i.isdigit()]
    return sum(lst)


print(sum_numbers(test))
