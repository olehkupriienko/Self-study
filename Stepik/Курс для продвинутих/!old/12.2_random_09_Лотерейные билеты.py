import random

lottery_tickets = []
while len(lottery_tickets) != 100:
    number = random.randint(1000000, 9999999)
    if number not in lottery_tickets:
        lottery_tickets.append(number)
print(*lottery_tickets, sep='\n')