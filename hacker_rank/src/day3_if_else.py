# !/bin/python3
#
# Objective In this challenge, we're getting started with conditional statements. Check out the
# Tutorial tab for learning materials and an instructional video!
#
# Task
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.
import sys

def isEven(n):
    return n % 2 == 0

N = int(input().strip())
# Check constraint: 1 <= N <= 100
if not(1 <= N <= 100):
    raise AssertionError("Make sure 1 <= N <= 100.")
string1 = "Weird"
string2 = "Not Weird"

if (not isEven(N)) or (isEven(N) and 6 <= N <= 20):
    print(string1)
elif isEven(N) and (2 <= N<=5 or N>20):
    print(string2)
else:
    print("something is wrong with input")