'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.'''

def solution(number):
    C = 0 #Refers to empty variable which will be used to add up numbers
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0: #Test to check if number in range is a multiple of 5 or 3
            C += i #Will add number to empty variable
        else:
            pass
        number -= 1 #Reduces number after each iteration
    return C