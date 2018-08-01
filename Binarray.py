'''Given an array of one's and zero's convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.'''

def binary_array_to_number(arr):
  # your code
  arr.reverse()
  decimal_num = 0
  for i in range(len(arr)):
      current_num = arr[i]
      binary_num = ((current_num * (2**i)))
      decimal_num += binary_num
  return decimal_num
      