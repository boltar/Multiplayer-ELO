from python.elo import ELOMatch, ELOPlayer
import re, datetime

games = ["seven_wonders", "incan_gold", "kings_guild", "nimmt", "kingdomino", "in_the_year_of_the_dragon","carcassonne"]
players = ["jules0821", "boltar", "dastica", "Seba", "fliptable", "greg_jed", "Michael_888", "melindamcd", "MissDeal","lindaj", "sojomojo"]


players_regex = "(jules0821)|(boltar)|(dastica)|(Seba)|(fliptable)|(greg_jed)|(Michael_888)|(melindamcd)|(MissDeal)|(lindaj)|(sojomojo)"
regex = re.compile(players_regex)
match = ELOMatch()
match.setK(60)



def print_elos(match, ratings):
    for k, v in ratings.items():
        if any(k == x.name for x in match.players):
            print(f'{k:<10}\t{v:>5d}', end='\t')
        else:
            print(f'{k:<10}\t    ', end='\t')
    print()


def update_elos(elo_match, old_ratings):
    new_ratings = old_ratings

    for p in elo_match.players:
        new_ratings[p.name] = match.getELO(p.name)
    return new_ratings

def main():
    for game in games:
        path = game + '.txt'
        game_file = open(path, 'r')
        record = game_file.read()
        place = 0
        ratings = {}
        for i in players:
            ratings[i] = 1000

        print(f'--- {game} ---')
        with open(path, 'r') as fp:
            for line in fp:
                if line.strip() == "":  #if we come to a blank line, calculate elos
                    if match.players:
                        match.calculateELOs()
                        ratings = update_elos(match, ratings)
                        print_elos(match, ratings)
                        match.reset()
                    else:
                        place = 0
                player_match = re.search(regex, line)
                if player_match:        # if we have a player name match
                    place = place + 1   # assign place in, starting with 1
                    player_name = player_match.group()
                    #print(f"player {player_name}")
                    match.addPlayer(player_name, place, ratings[player_name])

            fp.close()


if __name__ == "__main__":
    main()
