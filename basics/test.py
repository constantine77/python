
#Data Structures in Python

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
    create List with 10 elements
    :return:
    '''
    A=[0]*10
    top = 0
    x = int(input())
    while x != 0:
        A[top]=x
    print(A)

create_list()