'''Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.'''

def is_square(n):   
    if n < 0: #This ensures negative numbers are not seen as squares
        return False
    else:
        if (n**0.5) == ((n**0.5)//1): # This tests whether the square root of n is an integer
            return True
        else:
            return False