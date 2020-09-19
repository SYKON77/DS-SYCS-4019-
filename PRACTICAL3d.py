#PRACTICAL3d (1)
def factor(num):
    if num < 0:
        print('Factorial does not exist')
    elif num == 0:
        print('The Factorial of 0 is 1')
    else:
        if num == 1:
            return num
        else:
            return num * factor(num-1) 

print(factor(6))

#PRACTICAL3d (2)

def factor(num):
    factorial = 1
    if num < 0:
        print("factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
           factorial = factorial*i
        print("The factorial is: ",factorial)

factor(88)
