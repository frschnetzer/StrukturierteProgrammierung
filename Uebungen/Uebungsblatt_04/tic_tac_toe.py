def main():
    def draw_board(board):
        print("\n")
        print('\t _________________')
        print("\t|     |     |     |")
        print("\t|  {}  |  {}  |  {}  |".format(board[0], board[1], board[2]))
        print('\t|_____|_____|_____|')

        print("\t|     |     |     |")
        print("\t|  {}  |  {}  |  {}  |".format(board[3], board[4], board[5]))
        print('\t|_____|_____|_____|')

        print("\t|     |     |     |")
        print("\t|  {}  |  {}  |  {}  |".format(board[6], board[7], board[8]))
        print('\t|_____|_____|_____|')

    def switch_Player(isPlayer1):
        if isPlayer1:
            print(f"It's Player 1's turn")
            symbol = "X"
        else:
            print(f"It's Player 2's turn")
            symbol = "O"
        return isPlayer1, symbol

    def tic_tac_toe():
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        wins = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7], [1,4,7], [2,5,8], [3,6,9]]

        list_player1 = []
        list_player2 = []

        isPlayer1 = True
        symbol = ""
        while " " in board:
            draw_board(board)
            isPlayer1, symbol = switch_Player(isPlayer1)

            x = int(input()) #ausgehend, dass korrekte daten eingegeben werden
            while((x > 9 or x < 0) or (x in list_player1 or x in list_player2)):
                print("Entry is not valid")
                x = int(input())

            board[x-1] = symbol            

            if isPlayer1: #currentplayer is player 1
                list_player1.append(x)
            else:
                list_player2.append(x)

            isPlayer1 = not isPlayer1 

            for x in wins: # get every possible win and check if one player has combination               
                if all(y in list_player1 for y in x):
                    draw_board(board)
                    return "Winner is Player 1"
                
                if all(y in list_player2 for y in x):
                    draw_board(board)
                    return "Winner is Player 2"
                
        draw_board(board)
        return "It's a draw!"            

    print(tic_tac_toe())
main()