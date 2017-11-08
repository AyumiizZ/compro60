xn = 2147483647; xn_1 = 1; S = 400
# print(abs(xn-xn_1))
while (abs(xn-xn_1) >= 1e-8):
    xn_1 = xn
    xn=0.5*(xn_1+S/xn_1)
print(xn)