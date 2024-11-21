def main():
    def calculate_arithmetic(entry_list):
        if len(entry_list) > 0:
            min, max = 0,0
            length = len(entry_list) #get the length of list
            sum = 0
            for i in entry_list:
                sum+=i
                if i < min:
                    min = i
                elif i > max:
                    max = i        
            return sum/length, min, max
        return None
    
    print(calculate_arithmetic([3, 5, 7, 8, 1, -1, 4, 0]))
    print(calculate_arithmetic([6, 5, 7, 3, 1, -1, -2, 0]))
main()