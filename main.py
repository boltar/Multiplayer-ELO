from python.elo import ELOMatch, ELOPlayer
import re, datetime

games = ["seven_wonders", "incan_gold", "kings_guild", "nimmt"]
players = ["jules0821", "boltar", "dastica", "Seba", "fliptable", "greg_jed", "MissDeal", "dmz", "Michael_888", "melindamcd", "extraBebecito"]


players_regex = "(jules0821)|(boltar)|(dastica)|(Seba)|(fliptable)|(greg_jed)|(MissDeal)|(dmz)|(Michael_888)|(melindamcd)|(extraBebecito)"
regex = re.compile(players_regex)
match = ELOMatch()
match.setK(60)



def print_elos(ratings):
    for k, v in ratings.items():
        print(f'{k:<10}\t{v:>5d}', end='\t')
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
                if line.strip() == "":
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
                    #print(f"player {player_name}")
                    match.addPlayer(player_name, place, ratings[player_name])

            fp.close()


if __name__ == "__main__":
    main()
