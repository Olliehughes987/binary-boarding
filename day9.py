# --- Day 9: Encoding Error --- #

def calculateNonValidNum(curr, preamble):
    start = 0
    sect = curr[start:preamble]
    # iterates through array after preamble, checking each value
    # against ones within the section defined by the preamble
    for target in curr[preamble:]:
        found = False
        
        for i in curr[:preamble]:
            # calculates the number needed for the current number to be valid
            y = target - i

            #checks if that number is in the current section of the array
            if str(y) in sect:
                # increases the start and preamble index by 1, so that the section moves forward 1 index in the array
                start += 1
                preamble += 1
                sect = curr[start:preamble]
                found = True
                break
            
        # If no valid combination is found, it prints the number and breaks out of the loop.
        if found == False:
            print("First non valid number:",target)
            break



def calculateSums(arr, targ, ind):
    # creates the section with first 2 elements inside.
    start = 0
    length = 2
    sect = arr[start:length]
    
    # while the sum of the section elements is not the target value,
    # increase the length of the section by adding more elements from the list.
    while sum(sect) != 217430975:
        sect = arr[start:length]
        # once the sum of the section is larger than the target, reset the length to 2
        # and increase the start index by 1.
        if(sum(sect) > 217430975):
            start += 1
            length = 2
            
        length += 1
    # prints the contiguous values and the total of the largest and smallest element combined.
    print("Contiguous values:",sect)
    sect.sort()
    print("Total of smallest and biggest element:",sect[0] + sect[-1])
        





with open('day9input.txt') as file:
    inputList = file.read().splitlines()

inputList = list(map(int, inputList))



calculateNonValidNum(inputList, 25)
calculateSums(inputList, 217430975, inputList.index(217430975))
