# name:Difference of Volumes of Cuboids
# link:https://www.codewars.com/kata/58cb43f4256836ed95000f97/python


# def find_difference(a, b):
#   x,y,z = a
#   i,j,k = b
#   return abs((x * y * z) - (i * j * k))

# using loop
def find_difference(a, b):
  def multiply(arr):
    result = 1
    for i in arr:
      result *= i
    return result
  return (abs(multiply(a) - multiply(b)))