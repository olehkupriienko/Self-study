from decimal import *
# from math import *
d = Decimal(input())
# result = exp(d) + ln(d) + log10(d) + sqrt(d)
result2 = d.exp() + d.ln() + d.log10() + d.sqrt()
print(result2)

