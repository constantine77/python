
#Data Structures in Python

import random

def simple_list_iteration():
    '''
    List iteration
    :return:
    '''
    A = [1,2,3,4,5]
    for x in A:
        print(x,type(x))
        x += 1
        print(x)

def list_index_iteration():
    '''
    List iteration with index
    :return:
    '''
    A = [1,2,3,4,5]
    for k in range(5): #from o to 4, k is index
        print(A[k])

def create_list():
    '''
    create List A with 10 elements

    :return:
    '''
    A =[ 0]*10
    B = [1,2,3,4,5,6,7,8]
    C = list(B) #create copy of list B
    D = []
    for k in range(len(C)):
        D[k].append

def copy_list():
    '''
    Copy List
    :return:
    '''
    list_size = 10

    A = [0]*list_size
    B = [0]*list_size

    for i in range(list_size):
        A[i] = random.randint(1,101) #generate random values of numbers between 1 and 100
    for i in range(list_size):
        B[i] = A[i]    #Assign the same values from List A to List B

    print(A,B)




copy_list()