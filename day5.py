# --- Day 5: Binary Boarding --- #
# https://adventofcode.com/2020/day/5
# I managed to solve part 1 pretty easily, working out the max ID was 913.
# The second half of the question took a bit of tweaking, however I managed to come up with the
# solution.


import math

takenSeats = []

def calculateSeatID(curr):
    #calculate the row
    row = calculateAxis(curr[:7], 0, 127, "F", "B")
    
    #calculate the column
    col = calculateAxis(curr[7:], 0, 7, "L", "R")

    return row * 8 + col


# takes in min and max values, aswell as the value to split the first and second half of the array
def calculateAxis(code, minimum, maximum, first, second):
    difference = (maximum - minimum) + 1
    for i in code:
        #difference always halves every time, no matter which value it is
        difference //= 2
        if i == first:
            maximum -= difference
        elif i == second:
            minimum += difference
    return minimum


with open('input.txt') as file:
    for line in file:
        takenSeats.append(calculateSeatID(line))


#Sort the array so its easier to search for missing value
takenSeats.sort()

print("Maximum possible seat ID:", max(takenSeats))

# Iterates through the array and checks for any missing ids by comparing the next item
# to its expected value.
for i in range(len(takenSeats) - 1):
    if (takenSeats[i] + 1) != takenSeats[i+1]:
        print("Missing seat:", takenSeats[i] + 1)
        break

