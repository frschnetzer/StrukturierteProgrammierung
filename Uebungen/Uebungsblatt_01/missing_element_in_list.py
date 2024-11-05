# finden der fehlenden numer in einer liste
def find_missing_number():
    comparer = 0
    isFound = True
    list =  [2,3,0,1]
    while isFound == True:
        for i in list:
            if comparer == i:
                isFound = True
                comparer +=1
            else:
                isFound = False
    return comparer

numbers = [2,3,0,1]
print(f"Missing number is: {find_missing_number()}")