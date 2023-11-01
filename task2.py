#!python3
"""
Create a function that calculates the amount of compound interest 
earned.
t = time in years
P = amount invested
n = # of compounding periods per year (how often interest is calculated)
Output should be rounded to 2 decimal places
r = rate of interest as a percentage
"""

def compoundInterest(P,r,t,n):
    A = P*(1+r/n)**(n*t)
    return A


print(compoundInterest(1000,0.04,2,4)) == 1082.86
print(compoundInterest(2500,0.042,20,12)) == 5782.43
print(compoundInterest(83,7,0.05,365)) == 117.78
print(compoundInterest(10000,0.03,10,2)) == 13468.55
