# Chip Class

class Chip:
    
    def __init__(self,total):
        self.total = total
        self.bet = 0
        
    def win_bet(self, bet):
        self.bet = bet * 2
        self.total += self.bet
    
    def lose_bet(self, bet):
        self.bet = bet
        self.total = self.total - self.bet