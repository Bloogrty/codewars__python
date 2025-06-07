# name:altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# link:https://www.codewars.com/kata/56efc695740d30f963000557/train/python


def to_alternating_case(string):
  result = []
  for i in range(len(string)):
    if string[i].isupper():
      result.append(string[i].lower())
    else:
      result.append(string[i].upper())
  
  return "".join(result)
  