from python.elo import ELOMatch, ELOPlayer
import re, datetime

players = ["jules0821", "boltar", "dastica", "Seba", "fliptable", "greg_jed"]
ratings = {}
for i in players:
    ratings[i] = 1000

players_regex = "(jules0821)|(boltar)|(dastica)|(Seba)|(fliptable)|(greg_jed)"
regex = re.compile(players_regex)
match = ELOMatch()
match.setK(60)

path = 'nimmt.txt'
game_file = open(path, 'r')
record = game_file.read()
place = 0

def print_elos(ratings):
    for k,v in ratings.items():
        print(f'{k}\t{v}', end='\t')
    print()
def update_elos(elo_match, old_ratings):
    new_ratings = {}

    for key in old_ratings:
        new_ratings[key] = match.getELO(key)
    return new_ratings

with open(path, 'r') as fp:
    for line in fp:
        #print(line.strip())
        if line.strip() == "":
            #print("new game!")
            if match.players:
                match.calculateELOs()
                ratings = update_elos(match, ratings)
                print_elos(ratings)
                match.reset()
            else:
                place = 0
        player_match = re.search(regex, line)
        if player_match:
            place = place + 1
            player_name = player_match.group()
            # print(f"player {player_name}")
            match.addPlayer(player_name, place, ratings[player_name])

