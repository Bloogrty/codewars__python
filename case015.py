# name:Mumbling
# link:https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/python

def accum(st):

  result = []

  # create loop
  for i in range(len(st)):
    char = st[i]
    repeated = char.upper() + char.lower() * i
    result.append(repeated)

  
  # join
  return "-".join(result)