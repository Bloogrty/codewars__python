# Name: Twice as old
# Link: https://www.codewars.com/kata/5b853229cfde412a470000d0/train/python

def twice_as_old(dad_years_old, son_years_old):
  diff = son_years_old * 2 - dad_years_old

  if diff < 0:
    return -diff
  else:
    return diff
    