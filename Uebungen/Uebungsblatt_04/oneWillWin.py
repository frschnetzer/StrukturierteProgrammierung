import random
def main():
    def oneWillWin(n,m):
        positionList = [True] * n        
        currentPosition = 0
        number_active_position = n

        while number_active_position > 1:
            i = 1
            while i < m: # step till m is reached
                currentPosition = (currentPosition + 1) % n # increasing and keep in ring
                if positionList[currentPosition] == True: # 
                    i += 1

            positionList[currentPosition] = False 
            number_active_position -= 1           

            while positionList[currentPosition] == False:
                currentPosition = (currentPosition + 1) % n            
            
        return currentPosition
    
    def oneWillWin_02(n,m):
        positionList = [True] * n        
        currentPosition = 0
        number_active_position = n

        while number_active_position > 1:
            i = 1
            while i < m: # step till m is reached
                currentPosition = (currentPosition + 1) % n # increasing and keep in ring
                if positionList[currentPosition] == True: # 
                    i += 1

            positionList[currentPosition] = False 
            number_active_position -= 1           

            while positionList[currentPosition] == False:
                currentPosition = (currentPosition + 1) % n            
            
        return currentPosition
    
    n = 7
    m = 3
    print(oneWillWin(n,m))
main()