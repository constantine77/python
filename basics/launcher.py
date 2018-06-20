###########Algorithms with Python3(from Zero to Hero)#########
#https://www.youtube.com/watch?v=KdZ4HF1SrFs


#Python assignment operators:
def assignment_operators():
    x = y = z = 0
    print("Cascade assignment: x = {} y = {} z = {}".format(x,y,z))
    x,y,z = 1,2,3
    print("Many to many assignment: x = {} y = {} z = {}".format(x,y,z))
#Arithmetic operators:
def arithmetic_operators():
    #Exponent:
    a = 3
    b = 3
    exp_result = a**b
    print("Exponential_calculation: {}".format(exp_result))
    #Division
    x = 5
    y = 3
    div_result = x/y
    print("Simple division as float result is {}".format(div_result))
    #Floor Division: the digits after the decimal point are removed.
    c = 5
    d = 3
    floor_div_result = x//y
    print("Floor division result is {}".format(floor_div_result))
    #Modulus % oparator:
    e = 9
    f = 2
    mod_result = 9 % 2
    '''Notes:
    9 divided by 2 is equal to 4.
    4 times 2 is 8
    9 minus 8 is 1 - the remainder.
    '''
    print("Modulus result is {}".format(mod_result))
#SWAP TWO VARIABLES:
#create a temporary variable and swap the values(with one temp variable)
def swap_two_variables():
    x = 5
    y = 10
    print("Input values X is {} and Y is {}".format(x,y))
    temp = x
    x = y
    y = temp
    print("The value of X after swapping is ",x,
          "and the value of Y after swapping is ",y)
#create a temporary variable and swap the values(w/o temp variables)
def swap_two_variables_no_temp():
    x = 5
    y = 10
    x,y = y,x
    print("The value of X after swapping is {}"
          " and the value of Y after swapping is {}".format(x,y))
#LOOPS:
#http://anh.cs.luc.edu/handsonPythonTutorial/whilestatements.html
#while loop(expression): statement(s)
#The while loop tells the computer to do something as long as the condition is met.
#https://www.python-course.eu/python3_loops.php
def loop_while_exm():
    temperature = 115
    while temperature > 112:
        print(temperature)
        temperature -= 1
    print("The tea is cool enough!")
def loop_while_break_exm2():
    temperature = 115
    while temperature > 110:
        print(temperature)
        temperature -= 1
        if temperature == 111:
            break
    print("The tea is cool enough!")
def loop_while_continue_exm():
    temperature = 110
    while temperature < 117:
        print(temperature)
        temperature += 1
        if temperature == 112:
            print("Perfect temperature!!!")
            continue
    else:
        print("Temperature is too high!!!")
def loop_for_exm():
    brands = ["Apple", "IBM", "Google"]
    numbers = [1,2,3,4,5,6,7]
    for brand in brands:
        print(brand)
    sum = 0
    for number in numbers:
        sum = sum + number
    print(sum)
    for i in range(1,10,2):
        print(i)

'''
********ALGEBRA LOGIC LAW*************
http://tech.jonathangardner.net/wiki/Python/Tutorial/Basic_Types_and_Operators/Boolean_Operators#DeMorgan.27s_Laws
TRUE = 1 and FALSE = 0
0 + x = x - false + something = something
1 + x = 1 - true + something = true
0 * x = 0
1 * x = x
A * A = A
A + A = A
A + A(none A) = 1 
A * A(none A) = 0
De Morgan's Laws:
# First law
!(a && b) == !a || !b
# Second law
!(a || b) == !a && !b
"not (A and B)" is the same as "(not A) or (not B)"
and also,
"not (A or B)" is the same as "(not A) and (not B)"
not a and not b <=> not (a or b)
not a or not b  <=> not (a and b)
For Instance:
a != 7 and a != 6
can be rewritten as:
not (a==7 or a==6)
'''
def logic_operation():
    flagIsTrue = True
    flagIsFalse= False
    x = 11
    if x%2 == 0 or x%3 == 0:
        print(flagIsTrue)
    else:
        print(flagIsFalse)
#Task_One: If numbers negative print A, if numbers 0 to 5 -> print B, 5 to 10 print C, other print 10
def task_one():
    x = 9
    if x < 0:
        print("A")
    elif x < 5:
        print("B")
    elif x < 10:
        print("C")
    elif x > 10:
        print("D")
    else:
        print("Something strange in universe")
def binary_numbers():
    x = 0b10 #binary number
    print(x)
    z = 0xFA #hexadecimal number
    print(z)
    y = 127
    print(bin(y))

#Check maximum for two numbers:
def max2(x,y):
        if x > y:
            return x
        return y

def max3(x,y,z):
        return max2(x, max2(y,z))

#Brute Force Algorithms


#Factorize number


#Recursion Algorithms:
#https://pythonspot.com/recursion/
#https://hackernoon.com/algorithms-explained-recursion-54831247dd85
#http://openbookproject.net/thinkcs/python/english3e/recursion.html


#MUST READ:
#https://proglib.io/p/ds-cheatsheets/

#Group Theory(work in progress)
#http://www.sagemath.org/
#

def main():
    print(max(3,4,5))


if __name__ == "__main__":
    main()






