def main():
    def draw_board(board):
        print("----------------------------")
        print(f"|  {board[0]}  |  {board[1]}  |  {board[2]}  |")
        print("----------------------------")
        print(f"|  {board[3]}  |  {board[4]}  |  {board[5]}  |")
        print("----------------------------")
        print(f"|  {board[6]}  |  {board[7]}  |  {board[8]}  |")
        print("----------------------------")

    def switch_Player(isPlayer1):
        if isPlayer1:
            print(f"It's Player 1's turn")
            symbol = "X"
        else:
            print(f"It's Player 2's turn")
            symbol = "O"
        return isPlayer1, symbol

    def tic_tac_toe():
        board = ["none", "none", "none", "none", "none", "none", "none", "none", "none"]
        wins = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7], [1,4,7], [2,5,8], [3,6,9]]

        list_player1 = []
        list_player2 = []

        isPlayer1 = True
        symbol = ""
        while "none" in board:
            draw_board(board)
            isPlayer1, symbol = switch_Player(isPlayer1)

            x = int(input()) #ausgehend, dass korrekte daten eingegeben werden
            while(x > 9 or x < 0):
                print("Entry is not valid")
                x = int(input())

            board[x-1] = symbol            

            if isPlayer1: #currentplayer is player 1
                list_player1.append(x)
            else:
                list_player2.append(x)

            isPlayer1 = not isPlayer1 
            if list_player1 in wins:
                return "Winner is Player 1"
            elif list_player2 in wins:
                return "Winner is Player 2"
        return "It's a draw!"            

    print(tic_tac_toe())
main()