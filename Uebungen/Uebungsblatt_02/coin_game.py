def main():
    def coin_game():        
        firstline = [1,2,3]
        secondline = [4,5,6,7]
        thirdline = [8,9,10,11,12]        
        isPlayer1 = True

        while firstline or secondline or thirdline: #solange mind eine liste noch ein element beinhaltet
            entries = list(map(int, input().split())) # get input as list of int                  
            for i in entries: # iterating throught the input list
                if i in firstline: # check if i is in one of the lists
                    firstline.remove(i) # remove i
                elif i in secondline:
                    secondline.remove(i)
                else:
                    thirdline.remove(i)
            if isPlayer1:
                isPlayer1 = False
            else:
                isPlayer1 = True
        if isPlayer1:
            return "Player 1"
        return "Player 2"

    print(f"Winner is: {coin_game()}")

main()