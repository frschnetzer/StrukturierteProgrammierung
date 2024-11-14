def main():
    def find_minima_maxima(entry_list):
        maxima, minima = [], []
        previous_Numb = entry_list[0]

        for i in range(1, len(entry_list) - 1): # start from 2 position and end before last position is reached
            current_number = entry_list[i]
            next_number = entry_list[i+1]

            if current_number > previous_Numb and current_number > next_number: # maxima
                maxima.append(current_number)
            elif current_number < previous_Numb and current_number < next_number: #minima
                minima.append(current_number)
            previous_Numb = current_number

        return maxima, minima
    
    print(find_minima_maxima([1,3,5,4,6,5,1,2,1,1]))
    print(find_minima_maxima([0,2,1,4,6,5,1,2,1,1]))
    print(find_minima_maxima([1,3,5,4,6,5,6,2,1,1]))
main()