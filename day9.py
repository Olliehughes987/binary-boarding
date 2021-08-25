   
def calculateNonSum(curr, preamble):
    start = 0
    sub = curr[start:preamble]
    for target in curr[preamble:]:
        found = False
        for i in curr[:preamble]:
            y = target - i
            if str(y) in sub:
                start += 1
                preamble += 1
                sub = curr[start:preamble]
                found = True
                break
        if found == False:
            print("First non valid number:",target)
            targInd = curr.index(target)
            break



def calculateSums(arr, targ, ind):
    start = 0
    length = 2
    slice = arr[start:length]
    while sum(slice) != 217430975:
        slice = arr[start:length]
        if(sum(slice) > 217430975):
            start += 1
            length = 2
        length += 1
    print("Contiguous values:",slice)
    slice.sort()
    print("Total of smallest and biggest element:",slice[0] + slice[-1])
        





with open('day9input.txt') as file:
    inputList = file.read().splitlines()

inputList = list(map(int, inputList))



calculateNonSum(inputList, 25)
calculateSums(inputList, 217430975, inputList.index(217430975))
