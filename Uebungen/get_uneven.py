def main():
    def getUneven(input_list):
        unevenList = []
        for i in input_list:
            if i % 2 != 0:
                unevenList.append(i)
        return unevenList
    numberList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    print(f"All uneven numbers: {getUneven(numberList)}")
main()