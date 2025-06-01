# name: Grasshopper - Grade book
# link: https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python

def get_grade(s1, s2, s3):
    total = (s1 + s2 + s3) / 3

    if total >= 90 and total <= 100:
        return "A"
    if total >= 80 and total < 90:
        return "B"
    if total >= 70 and total < 80:
        return "C"
    if total >= 60 and total < 70:
        return "D"
    if total >= 0 and total < 60:
        return "F"
    