hrs = int(input())
mins = int(input())
angle = (360/12)*(hrs-(11*mins)/60)
if angle > 180:
    angle = 180 - angle%180
print("{:.1f}".format(angle))
