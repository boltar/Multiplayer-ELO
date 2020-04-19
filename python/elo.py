#ELO
#python 3.4.3
import math

class ELOPlayer:
    name      = ""
    place     = 0
    eloPre    = 0
    eloPost   = 0
    eloChange = 0
    
class ELOMatch:
    players = []
    K = 32
    
    def addPlayer(self, name, place, elo):
        player = ELOPlayer()
        
        player.name    = name
        player.place   = place
        player.eloPre  = elo
        
        self.players.append(player)
        
    def getELO(self, name):
        for p in self.players:
            if p.name == name:
                return p.eloPost
            
        return 1500;

    def getELOChange(self, name):
        for p in self.players:
            if p.name == name:
                return p.eloChange;
                
        return 0;

    def setK(self, new_k):
        self.K = new_k

    def reset(self):
        self.players = []

    def calculateELOs(self):
        n = len(self.players)
        K = self.K / (n - 1);
        
        for i in range(n):
            curPlace = self.players[i].place;
            curELO   = self.players[i].eloPre;
                        
            for j in range(n):
                if i != j:
                    opponentPlace = self.players[j].place
                    opponentELO   = self.players[j].eloPre  
                    
                    #work out S
                    if curPlace < opponentPlace:
                        S = 1.0
                    elif curPlace == opponentPlace:
                        S = 0.5
                    else:
                        S = 0.0
                    
                    #work out EA
                    EA = 1 / (1.0 + math.pow(10.0, (opponentELO - curELO) / 400.0))
                    
                    #calculate ELO change vs this one opponent, add it to our change bucket
                    #I currently round at this point, this keeps rounding changes symetrical between EA and EB, but changes K more than it should
                    self.players[i].eloChange += round(K * (S - EA))

                    #add accumulated change to initial ELO for final ELO   
                    
            self.players[i].eloPost = self.players[i].eloPre + self.players[i].eloChange


# match = ELOMatch()
# match.addPlayer("Tony", 2, 1000)
# match.addPlayer("David C", 3, 1000)
# match.addPlayer("Anj", 1, 1000)
# match.addPlayer("Seabass", 4, 1000)
# match.addPlayer("Craig", 5, 1000)
# match.addPlayer("Greg", 6, 1000)
#
# match.calculateELOs()
# t = match.getELO("Tony")
# print(f'{match.getELO("Anj")}')
# print(f'{match.getELO("Tony")}')
# print(f'{match.getELO("David C")}')
# print(f'{match.getELO("Seabass")}')
# print(f'{match.getELO("Craig")}')
# print(f'{match.getELO("Greg")}')