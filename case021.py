# name:How good are you really?
# link:https://www.codewars.com/kata/5601409514fc93442500010b/train/python

def better_than_average(class_points, your_points):
  total_class = sum(class_points)/len(class_points)
  return your_points > total_class