
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
    create List A with 10 elements

    :return:
    '''
    A =[ 0]*10
    B = [1,2,3,4,5,6,7,8]
    C = list(B) #create copy of list B
    D = []
    for k in range(len(C)):
        D[k].append




create_list()