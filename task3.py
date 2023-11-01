#!python3

"""
Create a function that determines the length of a hypotenuse given the lengths of 2
shorter sides
2 input parameters
float: the length of one side of a right triangle
float: the length of the other side of a right triangle

return: float value for the length of the hypotenuse rounded to 2 decimals
        None if the hypotenuse does not exist

Sample assertions:
assert hypotenuse(6,8) == 10
(2 points)
"""

from math import sqrt
def hypotenuse(a,b):
    c = round(sqrt(a*2 + b*2), 2)
    return c

if __name__ == "__main__":
    print(hypotenuse(6,8)) == 5.29
    print(hypotenuse(5,12)) == 5.83
    print(hypotenuse(4,6)) == 4.47
    print(hypotenuse(-3,4)) == 1.41