# setze dame
# speichere position (board nxn größe)
# setze dame an nächster position (wenn nicht ende reihe, nächste spalte, wenn ende reihe, nächste reihe)
# überprüfe ob gültig (gleiche reihe, gleiche spalte, vertikal)
# wenn gültig, setze neue dame
# wenn nicht gültig, setze dame an neuer position
# wiederhohlen

def drawBoard(board):
    print("\n")
    print(' _________________')
    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(board[0], board[1], board[2]))
    print('|_____|_____|_____|')

    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(board[3], board[4], board[5]))
    print('|_____|_____|_____|')

    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(board[6], board[7], board[8]))
    print('|_____|_____|_____|')

def main():
    
    board = []

    

main()