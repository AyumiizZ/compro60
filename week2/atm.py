money = int(input("Input Money: "))
bank1000 = money//1000
money%=1000
bank500 = money//500
money%=500
bank100 = money//100
money%=100
bank50 = money//50
money%=50
bank20 = money//20
money%=20
coin10 = money//10
money%=10
coin1 = money//1
money%=1

if bank1000 > 1:
    print ("1000:\t{}\tnotes".format(bank1000))
elif bank1000 == 1:
    print ("1000:\t1\tnote")
if bank500 > 1:
    print ("500:\t{}\tnotes".format(bank500))
elif bank500 == 1:
    print ("500:\t1\tnote")
if bank100 > 1:
    print ("100:\t{}\tnotes".format(bank100))
elif bank100 == 1:
    print ("100:\t1\tnote")
if bank50 > 1:
    print ("50:\t{}\tnotes".format(bank50))
elif bank50 == 1:
    print ("50:\t1\tnote")
if bank20 > 1:
    print ("20:\t{}\tnotes".format(bank20))
elif bank20 == 1:
    print ("20:\t1\tnote")
if coin10 > 1:
    print ("10:\t{}\tcoins".format(coin10))
elif coin10 == 1:
    print ("10:\t1\tcoin")
if coin1 > 1:
    print ("1:\t{}\tcoins".format(coin1))
elif coin1 == 1:
    print ("1:\t1\tcoin")
