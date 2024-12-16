def SumRecursive_LeftToRight(inputList):
    if len(inputList) == 0: # abort condition
        return 0
    else:
        return inputList[0] + SumRecursive_LeftToRight(inputList[1:]) # with every loop we get the next element from list till we reach the end
    
def SumRecursive_RightToLeft(inputList):
    if len(inputList) == 0: # abort condition
        return 0
    else:        
        return inputList[-1] + SumRecursive_RightToLeft(inputList[:-1]) # start from last position to front and store also in last position

def SumRecursive_Middle(inputList):   
    median = (len(inputList))//2 # find middle of list
    # call left to right from start till median (exclusive) + call right to left from median (inclusive) till end
    return SumRecursive_RightToLeft(inputList[:median]) + SumRecursive_LeftToRight(inputList[median:])

def Middle_02(inputList, lb, ub): # solution with lower bound, upper bound
    if (ub-lb) == 1:
        return inputList[lb]
    else:
        median = (ub + lb) // 2 # find middle 
        return Middle_02(inputList, lb, median) + Middle_02( inputList, median, ub)

def TestLeftToRight():
    inputList = [0] # expected result 0
    print(f"Test for left to right: Input: {inputList} Output: {SumRecursive_LeftToRight(inputList)}")

    inputList = [1,2,3,4,5] # expected result 15
    print(f"Test for left to right: Input: {inputList} Output: {SumRecursive_LeftToRight(inputList)}")

    inputList = [0,1,2,3,4,5] # expected result 15
    print(f"Test for left to right: Input: {inputList} Output: {SumRecursive_LeftToRight(inputList)}")

def TestRightToLeft():
    inputList = [0] # expected result 0
    print(f"Test for right to left: Input: {inputList} Output: {SumRecursive_RightToLeft(inputList)}")

    inputList = [1,2,3,4,5] # expected result 15
    print(f"Test for right to left: Input: {inputList} Output: {SumRecursive_RightToLeft(inputList)}")

    inputList = [0,1,2,3,4,5] # expected result 15
    print(f"Test for right to left: Input: {inputList} Output: {SumRecursive_RightToLeft(inputList)}")

def TestMiddle():
    inputList = [0] # expected result 0
    print(f"Test for middle: Input: {inputList} Output: {SumRecursive_Middle(inputList)}")

    inputList = [1,2,3,4,5] # expected result 15
    print(f"Test for middle: Input: {inputList} Output: {SumRecursive_Middle(inputList)}")

    inputList = [0,1,2,3,4,5] # expected result 15
    print(f"Test for middle: Input: {inputList} Output: {SumRecursive_Middle(inputList)}")

def TestMiddle_02():
    inputList = [0] # expected result 0
    print(f"Test for middle_02: Input: {inputList} Output: {Middle_02(inputList, 0, len(inputList))}")

    inputList = [1,2,3,4,5] # expected result 15
    print(f"Test for middle_02: Input: {inputList} Output: {Middle_02(inputList, 0, len(inputList))}")

    inputList = [0,1,2,3,4,5] # expected result 15
    print(f"Test for middle_02: Input: {inputList} Output: {Middle_02(inputList, 0, len(inputList))}")

def main():
    TestLeftToRight()
    TestRightToLeft()
    TestMiddle()
    TestMiddle_02()
main()