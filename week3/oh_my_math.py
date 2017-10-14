def my_ceiling(x):
    if x % 1 == 0:
        return x
    return int(x//1+1)
def my_floor(x):
    if x % 1 == 0:
        return x
    return int(x//1)
def my_fabs(x):
    if x < 0:
        return -1*x
    return x
def my_factorial(x):
    if x<0 or x%1!=0:
        return -1
    fac = 1
    while x>=1:
        fac *= x
        x-=1
    return fac
def my_pow(x,y):
    res = 1
    if y==0:
        return 1
    while y>0:
        res *= x
        y-=1
    return res    
def my_e():
    return my_pow((1+(1/10000)),10000)         
def my_pi():
    res = 3;count = 2;sign = 1
    while count < 100: 
        res += sign*(4/(count*(count+1)*(count+2)))
        sign *= -1
        count += 2
    return res
def my_radian(x):
    return x/180*my_pi()
def my_degree(x):
    return x/my_pi()*180
def my_exp(x):
    return my_pow(my_e(),x)
def my_sqrt(x):
    xn = 1000000;x0=0
    while (my_fabs(xn-x0) >= 1e-8):
        x0 = xn 
        xn = 0.5*(x0+x/x0)    
    if xn % 1 == 0:
        return int(xn)
    return xn
def my_sin(x):
    res = 0;sign = 1;count = 1
    while count <= 150:
        res += sign*(my_pow(x,count)/my_factorial(count))
        count += 2
        sign *= -1
    return res
def my_cos(x):
    res = 1;sign = -1;count = 2
    while count <= 150:
        res += sign*(my_pow(x,count)/my_factorial(count))
        count += 2
        sign *= -1
    return res
def my_tan(x):
    return my_sin(x)/my_cos(x)

print(my_sin(0.707))
print(my_sin(9))
