import random

def CreateTeam(team):  
    goalies = []
    playerList = []
    for key, value in team.items(): # extract all players without goalies
        if value != 0: # when player is not goalie
            playerList.append((key,value))
        else:
            goalies.append((key, value)) # extract the goalies and create as much as we have goalies teams
    
    random.shuffle(goalies) # shuffling list to get a random choice of goalies
    team1 = [goalies[0]]
    team2 = [goalies[1]]

    sumTeam1 = 0
    sumTeam2 = 0
    random.shuffle(playerList) # shuffle the list of players to get random order
    for key, value in playerList:
        if sumTeam1 < sumTeam2:   # when abilities of team 2 is stronger, add new player to team1      
            team1.append((key, value))
            sumTeam1 += value
        else:
            team2.append((key,value))
            sumTeam2 += value   
    return team1, team2    

def main():   
    # team with uneven number of player
    team = {        
        "Maria": 0, "Max": 0,  # Tor -> 0
        "Xaver": 3, "Lucia": 3,  # A+ -> 3
        "Jenni": 2, "Hans": 2, "Otto": 2, "Franz": 2,  # A -> 2
        "Klaus": 1, "Monika": 1, "Gurdrun": 1, "Oskar": 1, "Ryan": 1, "Ben": 1, "Herlinde": 1  # B -> 1
        }    
    team1, team2 = CreateTeam(team)
    print(f"First Team: {team1}, Second Team: {team2}")
    
    #team with even number of players
    team = {        
        "Maria": 0, "Max": 0,  # Tor -> 0
        "Xaver": 3, "Lucia": 3,  # A+ -> 3
        "Jenni": 2, "Hans": 2, "Otto": 2, "Franz": 2,  # A -> 2
        "Klaus": 1, "Gurdrun": 1, "Oskar": 1, "Ryan": 1, "Ben": 1, "Herlinde": 1  # B -> 1
        }    
    team1, team2 = CreateTeam(team)
    print(f"First Team: {team1}, Second Team: {team2}")
main()