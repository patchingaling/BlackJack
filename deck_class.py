import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen': 10,'King':10, 'Ace':11}

class Deck:
    '''
    This will create the deck of cards and shuffle it
    '''
    def __init__(self):
        '''
        This happen only once. Creation of the deck of cards
        '''
        self.deck_card = []
        for suit in suits:
            for rank in ranks:
                # This assume all the cards has already been defined!
                self.deck_card.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck_card)

    def deal_one(self):
        return self.deck_card.pop()