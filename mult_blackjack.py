import random
import card_class
import deck_class
import hand_class
import chip_class
import myfuncs_blackjack


#ask how many player
while True:
	try:
		players_ctr = int(input('How many players? '))
	except:
		print('Error in entering players!')
	else:
		print(f'We have {players_ctr} players.')
		break

#create player
cre_player = Y
ctr = 0
pl_hand = []
while cre_player = Y:
	while True:
		try:
			cre_player = input('Create a player (Y/N)? ')
		except:
			print('Error in creating a player')
		else:
			if cre_player.upper() == 'Y':
				name = create_player(ctr_player)
				pl_chips = get_chips()
				pl_bet = get_bet()
				pl_hand[ctr] = Hand(name)
				player_chip = Chip(pl_chips, pl_bet)
				ctr += 1
			elif cre_player.upper() == 'N':
				'Players are created.'
				break
			else:
				print('enter Y or N only.')
	        

player_chip = Chip(pl_chips)

playing = True

while playing:
    #shuffle the decks
    my_cards = Deck()
    my_cards.shuffle()

    #place players bet
    pl_bet = place_bet(player_chip.total)

    # Deal the dealers card
    dealer_hand = Hand()
    dealer_hand.add_card(my_cards.deal_one())
    dealer_hand.add_card(my_cards.deal_one())

    # Deal the player's cards
    player_hand = Hand()
    player_hand.add_card(my_cards.deal_one())
    player_hand.add_card(my_cards.deal_one())

    blackjack = 21
    hit_stand = ''
    while hit_stand.upper() != 'N':
        disp_hands(True, False, playing)
        if player_hand.value > blackjack:
            print("BUST!!!! You lose!")     
            player_chip.lose_bet(pl_bet) 
            print(f'players chip amount is {player_chip.total}')
            playing = False
            break
        else:
            hit_stand = check_hit_stand()
            if hit_stand.upper() == 'Y':
                player_hand.add_card(my_cards.deal_one())
                if player_hand.aces != 0:
                    player_hand.adjust_for_ace()
            else:
                playing = False
            
    if hit_stand.upper() == 'N':
        while True:
            disp_hands(False, True, playing)
            if dealer_hand.value < 17:
                dealer_hand.add_card(my_cards.deal_one())
                if dealer_hand.aces != 0:
                	dealer_hand.adjust_for_ace()
            elif dealer_hand.value > blackjack:
                if player_hand.value <= blackjack:
                    print("Dealer is BUST!")
                    if player_hand.value == blackjack:
                        print('BLACKJACK')
                        pl_bet = pl_bet + (pl_bet / 2)
                    print("Player wins")
                    player_chip.win_bet(pl_bet)
                    print(f'Player chip amount is {player_chip.total}')
                    break
                else:
                    print('Dealer wins')
                    player_chip.lose_bet(pl_bet)
                    print(f'Player chip amount is {player_chip.total}')
                    break
            else: 
                #(dealer_hand.value > 17) and (dealer_hand.value < blackjack)
                # player value is blackjack
                if dealer_hand.value >= 17:
                    if player_hand.value > dealer_hand.value:
                        if player_hand.value == blackjack:
                            print('BLACKJACK!')
                            pl_bet = pl_bet + (pl_bet / 2)
                        print('Player wins!')
                        player_chip.win_bet(pl_bet)
                        print(f'Player chip amount is {player_chip.total}')
                        break
                    elif dealer_hand.value <= blackjack and player_hand.value < dealer_hand.value:
                        print('Dealer wins!')
                        player_chip.lose_bet(pl_bet)
                        print(f'Player chip amount is {player_chip.total}')
                        break   
                    elif player_hand.value == dealer_hand.value:
                        print('The game is PUSH. No one wins!')
                        break
                    

    while True:
        try:
            try_again = input('Do you want to play again (Y/N): ')
        except:
            print('Error')
        else:
            if try_again.upper() != 'Y' and try_again.upper() != 'N':
                print('Answer only with Y or N')
            else:
                break

    if try_again.upper() == 'Y':
        playing = True
    else:
        break
