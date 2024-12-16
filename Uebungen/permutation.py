def perm(numbers, pos=0, results=None):
    if results is None:
        results = [] # when no results list exists, create new one. Gets called in the beginning

    if pos == len(numbers):
        results.append(numbers[:])  # Append a copy of the current permutation, call all elements from list
    else:
        for element in range(pos, len(numbers)):
            numbers[pos], numbers[element] = numbers[element], numbers[pos] # Swap position with element position
            perm(numbers, pos + 1, results) # calling function to create new permutation and 
            numbers[pos], numbers[element] = numbers[element], numbers[pos]  # Swap back
    
    return results

def main():
    numbers = [1,2,3,4]
    print(perm(numbers))
main()