__author__ = 'alex'

hrs = raw_input("Enter Hours:")
h = float(hrs)

rate = raw_input("Enter Rate:")
r = float(rate)

if hrs > 40:
    total = (40 * r) + ((h - 40) * (1.5 * r))
else:
    total = (r * h)

print(total)
