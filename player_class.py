class Player:
	'''
	This class is for creating a player
	'''
	def __init__(self,name):
		self.name = name
		self.deck_card = [] # A new player has no cards

	def remove_one(self):
		'''
		Note we remove one card from the list of deck_cards
		We state 0 to remove from the top of the deck
		We'll assume -1 is the bottom of the deck
		'''
		return self.deck_card.pop(0)

	def add_cards(self,new_cards):
		if type(new_cards) == type([]):
			self.deck_card.extend(new_cards)
		else:
			self.deck_card.append(new_cards)

	def __str__(self):
		return f'Player {self.name} has {len(self.deck_card)} cards.'