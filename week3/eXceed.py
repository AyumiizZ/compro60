while True:
    distance = float(input("Input distance (m) : "))
    if distance == 0:
        print("You have 100% internet signal [{:.2f} m]\nYou : GG Ez kid".format(distance))
        break
    elif distance <= 1:
        print("You have 75% internet signal [In 0 - 1 : {:.5f} m]".format(distance))
    elif distance <= 2:
        print("You have 50% internet signal [In 1 - 2 : {:.2f} m]".format(distance))
    elif distance <= 10:
        print("You have 25% internet signal [In 2 - 10 : {:.2f} m]".format(distance))
    else:
        print("You : I need healing!!!\nYou do not have internet signal [{:.0f} m]".format(distance))

