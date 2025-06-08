# name:Find the stray number
# link:https://www.codewars.com/kata/57f609022f4d534f05000024/train/python

def stray(arr):
  if len(arr) < 3:
    return None
  sortedArray = sorted(arr)
  if sortedArray[0] == sortedArray[1]:
    return sortedArray[-1]
  else: return sortedArray[0]