# name: Count the divisors of a number
# link: https://www.codewars.com/kata/542c0f198e077084c0000c2e/python

def divisors(n):
  result = 0
  for i in range(1, n + 1):
    if n % i == 0:
      result += 1
  return result