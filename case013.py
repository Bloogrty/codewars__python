# name: Area or Perimeter
# link: https://www.codewars.com/kata/5ab6538b379d20ad880000ab/python

def area_or_perimeter(l , w):
  if l == w:
    return l * w
  
  if l != w:
    return  2 * (l+w)