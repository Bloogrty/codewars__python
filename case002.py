# name: Beginner Series #2 Clock
# link: https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python

def past(h, m, s):
    milli = 1000
    second = s * milli
    minute = m * 60 * milli
    hour = h * 3600 * milli
    return hour + minute + second