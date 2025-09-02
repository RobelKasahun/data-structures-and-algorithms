'''
    - Linear time
    Big-O of n ---> O(n)
'''
def print_numbers(n):
    for i in range(n):
        print(i)

print_numbers(n=10)
print()

'''
    - Linear time
    - Drop Constants
        = O(n) + O(n)
        = O(2n)
        = O(n)      ---> Constant dropped 
'''
def print_numbers(n):
    # O(n)
    for i in range(n):
        print(i)
        
    # O(n)
    for j in range(n):
        print(j)
print()

'''
    - Quadratic time
        = O(n) * O(n)
        = O(n^2)
'''
def print_numbers(n):
    # O(n)
    for i in range(n):
        # O(n)
        for j in range(n):
            print(i, j)
        print()
    
print_numbers(10)
print()

'''
    - Drop Non-Dominants
        = ( O(n) * O(n) ) + O(n)
        = (O(n^2) + O(n))
        = O(n^2) --> Dropped the Non-Dominant [ O(n) ]
'''
def print_numbers(n):
    # O(n)
    for i in range(n):
        # O(n)
        for j in range(n):
            print(i, j)
        print()
    print()
    
    # O(n)
    for k in range(n):
        print(k)
print()

'''
    - Constant time O(1)
        = O(1)
'''
def add(n):
    # O(1)
    return n + n + n 
print()

'''
    - Logarithmic time
        - O(log n)
        
    - Binary Search Algorithm
'''
print()

'''
    - Different terms for inputs
        = O(a) + O(b) + O(c)
        = O(a + b + c)
'''
def print_numbers(a, b, c):
    # O(a)
    for i in range(a):
        print(i)
        
    # O(b)
    print()
    for j in range(b):
        print(j)
        
    # O(c)
    print()
    for k in range(c):
        print(k)

print_numbers(1, 2, 3)
print()

'''
    - Different terms for inputs
        = O(a * b * c)
'''
def print_numbers(a, b, c):
    for i in range(a):
        for j in range(b):
            for k in range(c):
                print(i, j, k)
            print()
        print()

print_numbers(1, 2, 3)
print()

'''
    - Big-O of Lists
        - append()                  -> O(1)
        - pop(0)                    -> O(n)
        - insert(index, value)      -> O(n)
'''
print()

'''
    - Wraping up Big-O
        - When n is 100
              Constant
            - O(1)              -> 1
              
              Divide and Conquer
            - O(log n)          -> 7
            
              Proportional (Linear / Straight line)
            - O(n)              -> 100

              Loop within a loop
            - O(n^2)            -> 10,000
            
        - When n is 1000
              Constant
            - O(1)              -> 1

              Divide and Conquer
            - O(log n)          -> 10

              Proportional (Linear / Straight line)
            - O(n)              -> 1,000

              Loop within a loop
            - O(n^2)            -> 1,000,000
'''

'''
    Omega           ---> Best Case 
    Theta           ---> Average Case
    Omicron         ---> O(n), O(logn) Worst Case
'''
print()

'''
    - Time Complexity
        - Linear Time ----> O(n)
'''
def print_items(n):
    print('[', end='')
    for i in range(n):
        if i != n - 1:
            print(i, end=', ')
        else:
            print(i, end='')
    print(']')
        
print_items(10)
print()

'''
    - Linear Time: [ Drop Constants ]
        - O(n) + O(n) + O(n)
        - O(3n)
        - Linear Time: ----> O(n)          ---> Dropped the constant [3]
'''
def print_items(n):
    for i in range(n):
        print(i, end=' ')
    print()
    
    for j in range(n):
        print(j, end=' ')
    print()
        
    for k in range(n):
        print(k, end=' ')
    print()
    
print_items(10)
print()

'''
    - Quadratic Time 
        - O(n) * O(n)
        - O(n^2)
        - O(n^2)            ---> Quadratic Time
'''
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
        print()
    print()
print()
print()

'''
    - Drop Non-dominant
        - O(n) * O(n) + O(n)
        - O(n^2) + O(n)
        - O(n^2)            ----> Non-dominant term dropped
'''
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
        print()
    print()
    
    for k in range(n):
        print(k)
print()

'''
    - Constant Time
        - O(1)
'''
def add(n):
    return n + n + n

print(add(10))
print()

'''
    - Logarithmic Time
        - log(n)
'''
print()

'''
    - Different Terms for input
        - O(a) + O(b) + O(c)
        - O(a + b + c)
'''
def print_items(a, b, c):
    for i in range(a):
        print(i, end=' ')
    print()
    
    for j in range(b):
        print(j, end=' ')
    print()
    
    for k in range(c):
        print(k, end=' ')
    print()

print_items(1, 2, 3)
print()

'''
    - Big-O of Lists
        - append(data)                  ----> O(1)
        - insert(1, data)               ----> O(n)
'''

'''
    - O(1)          n = 100 ----> 1             n = 1,000 ----> 1
    - O(logn)       n = 100 ----> 7             n = 1,000 ----> 10   
    - O(n)          n = 100 ----> 100           n = 1,000 ----> 1,000
    - O(n^2)        n = 100 ----> 10,000        n = 1,000 ----> 1,000,000
'''
    

    
    

