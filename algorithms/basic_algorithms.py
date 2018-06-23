
#Basic Algorithms in Python
# 1. list_search - Linear Search Algorithm
# 2. list_reverse - List Reverse
# 3. list_left_shift - Shift first element from left to right
# 3. list_right_shift - Shift first element from right to left
# 4. list_sieve - Sieve of Eratosthenes
import random

def list_generator(list_size:int):
    """
    Generates List with random integers from 1 to 100
    :param list_size:
    :return:
    """
    A = [0]*list_size
    for i in range(list_size):
        A[i] = random.randint(1,101)
    print("List generated with following params: ",A)
    return A


def list_search(A:list, N:int, x:int):
    """
    Linear Search Algorithm:
    Search int x in List A from 0 to N index. Return index x from A or -1 if can't
    find int x. If List has the similar elements, return the first element.
    :param A:
    :param N:
    :param x:
    :return:
    """
    for i in range(N):
        if A[i] == x:
            return print("The number is in index: ",i)
    return print("The number is not in the index: ",-1)

def list_reverse(A:list,N:int):
    """
    Reverse List Algorithm
    :param A:
    :param N:
    :return:
    """
    print("Input List: ",A)
    B = [0]*N
    for i in range(N):
        B[i] = A[N - 1 - i]
    return print("Reverse List",B)

def list_left_shift():
    """
    Shift first element from left to right
    :return:
    """
    A = [1,2,3,4,5]
    N = len(A)
    print("List lenght: ",N)
    print("Original List A: ",A)
    tmp = A[0]
    for i in range(N-1):
        A[i] = A[i+1]
    print(A)
    A[N-1] = tmp
    print("List with shift element",A)

def list_right_shift():
    """
    Shift last element from right to left
    :return:
    """
    A = [1,2,3,4,5]
    N = len(A)
    print("List lenght: ",N)
    print("Original List A: ",A)
    tmp = A[N-1]
    for i in range(N-2,-1,-1):
        A[i+1] = A[i]
    A[0] = tmp
    print("Shift element from right to left: ",A)

def list_sieve():
    """
    Sieve of Eratosthenes:
    prove whether a number is a prime number
    2, 3, 5, 7, 11 (9 is divisible by 3) and so on.
    A prime number can be divided, without a remainder,
    only by itself and by 1. For example,
    17 can be divided only by 17 and by 1.
    :return:
    """
    list_length = 20
    N = list_length
    A = [True]*N
    A[0]=A[1]=False
    for i in range(2,N):
        if A[i]:
            for m in range(2*i,N,i):
                A[m]=False
    for i in range(N):
        print(i,"-","prime number" if A[i] else "composite number")
    print(A)



def main():
    list_sieve()


if __name__ == "__main__":
    main()