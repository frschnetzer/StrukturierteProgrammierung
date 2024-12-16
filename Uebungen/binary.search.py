def binary_search(values, value):
    pos = len(values) //2 # mitte herausbekommen    
    while values[pos] != value:  
        if value < values[pos]:
            return binary_search(values[:pos - 1], value)
        else:
            return binary_search(values[pos + 1:], value)

values = [1,2,3,40,51,62,73,80]
print(binary_search(values, 62))