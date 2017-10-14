
def fn1(name_list):
    # In Chiang Rai or Chiang Mai

def fn2(name_list):
    # Name begins with Kan

def fn3(name_list):
    # Name ends with chai

def fn4(name_list):
    # Doesn't use mobile phone

def fn5(name_list):
    # Phone ends with odd number

# Do not edit codes below.
name_list = open('contact_list.txt').read().strip().split('\n')
fn_list = [fn1, fn2, fn3, fn4, fn5]
n = int(input("Which function? (1-5): "))
fn = fn_list[n-1]
search_result = fn(name_list)
for result in search_result:
    print(result)
