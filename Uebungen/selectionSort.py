def selectionSort(values):
    i = 0    
    while i < len(values) - 1: # loops though list, verhindert dass an der letsten stelle nichts mehr gemacht werden muss
        minPos = i # suchraum wird bei jeder iteration verkleinert
        j = minPos + 1 
        while j < len(values):
            if values[j] < values[minPos]: # found minimum of the two compared values
                minPos = j
                # temp = values[i]
                # values[i] = values[minPos]
                # values[minPos] = temp
            j += 1
        values[i], values[minPos] = values[minPos], values[i] # python lösung
        i += 1
    return values

def main():
    values = [3,5,1,2,10]
    print(selectionSort(values))

main()