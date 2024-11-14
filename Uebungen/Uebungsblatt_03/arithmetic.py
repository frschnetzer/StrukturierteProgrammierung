def main():
    def find_minima_maxima(entry_list):
        maxima, minima = [], []
        previous_Numb = entry_list[0]
        for i in range(1, len(entry_list) - 1):
            current_number = entry_list[i]
            next_number = entry_list[i+1]
            if current_number > previous_Numb and current_number > next_number: # maxima
                maxima.append(current_number)
            elif current_number < previous_Numb and current_number < next_number: #minima
                minima.append(current_number)
            previous_Numb = current_number
        return maxima, minima
    
    def calculate_arithmetic(entry_list):
        length = len(entry_list) #get the length of list
        sum = 0
        for i in entry_list:
            sum+=i
        maxima, minima = find_minima_maxima(entry_list)
        return sum/length, maxima, minima
    
    print(calculate_arithmetic([3, 5, 7, 8, 1, -1, 4, 0]))
    print(calculate_arithmetic([6, 5, 7, 3, 1, -1, -2, 0]))
main()