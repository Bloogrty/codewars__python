# name: Transportation on vacation
# link: https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python

def rental_car_cost(d):
  # init
  basePrice = 40
  discount = 0

# discount logic
  if d >= 7:
    discount = 50
  elif d >= 3:
    discount = 20

  return d * basePrice - discount