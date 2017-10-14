mode = input()
score = int(input())
if mode == "C":
    if score >= 80:
        print("A")
    elif score >= 75:
        print("B+")
    elif score >= 70:
        print("B")
    elif score >= 65:
        print("C+")
    elif score >= 60:
        print("C")
    elif score >= 55:
        print("D+")
    elif score >= 50:
        print("D")
    else:
        print("F")
if mode == "A":
    if score >= 50:
        print("AP")
    else:
        print("AF")
