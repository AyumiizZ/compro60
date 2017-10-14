def sum_of_plus(array_of_number):
    answer_01 = 0
    if(len(array_of_number)==0):
        answer_01 = 0
    else:
        for number in array_of_number:
            answer_01 += number 

def sum_of_minus(array_of_number):
    answer = 0
    if(len(array_of_number)==0):
        return 0
    else:
        for number in array_of_number:
            answer -= number 
    return answer

def multi(array_of_number): 
    answer_03 = 1
    if(len(array_of_number)==0):
        None
    else:
        for number in array_of_number:
            answer_03 *= number 


def sum_of_divided(array_of_number):
    global answer_04
    if(len(array_of_number)==0):
        None
    else:
        for number in array_of_number:
            answer_04 += 1.0/number
    print("In loop is {}".format(answer_04))

def sum_of_mod_by_two(array_of_number):
    answer = 0
    if(len(array_of_number)==0):
        None
    else:
        for number in array_of_number:
            answer += (number%2)

array_of_number = []
while True:
    data = input()
    if(data.lower()=="end"):
        if(len(array_of_number)==0):
            exit()
        else:
            break
    array_of_number.append(float(data))

answer_01 = 0
sum_of_plus(array_of_number)
print("first answer is {}".format(answer_01))

print("second answer is {}".format(sum_of_minus(array_of_number)))

global answer_03
multi(array_of_number)
print("third answer is {}".format(answer_03))

sum_of_divided(array_of_number)
print("forth answer is {}".format(answer_04))

print("fifth answer is {}".format(sum_of_mod_by_two(array_of_number)))
