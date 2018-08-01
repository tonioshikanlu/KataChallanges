'''Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!'''
def get_sum(a,b):
    sum = 0
    if a == b:
        return a
    if a < b:
        for i in range(a,b+1):
            sum += i
    else:
        if b < a:
            for i in range(b,a+1):
                sum += i
        
    return sum