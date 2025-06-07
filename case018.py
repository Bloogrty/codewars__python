# name:Invert values
# link: https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/python


def invert(lst):
  result = []
  for i in range(len(lst)):
    result.append(lst[i] * -1)

  return result