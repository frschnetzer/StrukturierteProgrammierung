import random
def main():
    def oneWillWin(n,m):
        players = []
        for i in range(n):
            players.append(i)
        counter = 0
        #start = random.choice(players)
        start = 6
        while(len(players) >= 1):
            for i in players[start:]: #TODO: finde heraus wie im "Kreis" gehen
                if counter == m:
                    players.remove(i)
                    print(f"Removed: {i}")
                    counter = 0
                    start = i
                else:
                    counter += 1
        return players

    n = 7
    m = 3
    print(oneWillWin(n,m))
main()