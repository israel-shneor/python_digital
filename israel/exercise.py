

from random import randint

from time import sleep
sum = int(input("how much"))

torot = sum//3

odef = sum%3
if odef>0:
    print(odef)

money = torot
i = 0
while money >0:
    i = i+1
    q1 = randint(1,6)
    q2 = randint(1, 6)
    print(f"q1: {q1} q2: {q2}")

    if q1 == q2:
        if q1 + q2 ==6:
            money = money+1000
        else:
            money  = money + 100
    elif q2 == 2:
            money = money + 40
    elif q1 == 1:
            money = money+20
    else:
        money = money-500
   # sleep(2)
    print(f"Tor: {i}, you earn {money} shekel")






