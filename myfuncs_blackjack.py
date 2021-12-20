#input chips and bet

def chips_and_bet():

    while True:
        try:
            pl_chips = int(input('Place amount of chips: '))
        except:
            print('error in inputting chips amount')
        else:
            print('Thank you!')
            break

    while True:
        try:
            pl_bet = int(input('Place your bet: '))
        except:
            print('error in inputting bet')
        else:
            if pl_bet > pl_chips:
                print('Bet is greater than your chips.')
            else:
                print('Bet placed.')
                break



#display cards by hands --> single player
def disp_hands(disp_player, disp_dealer, playing):
    ctr = 0
    if disp_player == True:
        print('This are the players cards: ')
        for cards in player_hand.cards:
            print(player_hand.cards[ctr])
            ctr += 1
        print(f"Total Value is {player_hand.value} ")
            
    ctr = 0
    if (disp_dealer == True) and not playing:
        print('This are the dealer cards: ')
        for cards in dealer_hand.cards:
            print(dealer_hand.cards[ctr])
            ctr += 1
        print(f"Total Value is {dealer_hand.value} ")
    elif disp_dealer == True and playing:
        print('This is the card of the dealer: ')
        print(dealer_hand.cards[0])

def check_hit_stand():
    print('Hit or stand question is answerable by Y or N. If Y, Hit. If N, Stand.')
    while True:
        try:
            answer = input('Are you going to hit (Y/N)? ')
        except:
            print('There is error in your answer')
        else:
            if  answer.upper() == 'N':
                print('STAND. It is the dealers turn.')
                break
            elif answer.upper() == 'Y':
                break
            else:
                print('The choices are only Y or N. Choose Again!')

    return answer

def create_player():
    
    while True:
        try:
            name = input('Enter name of player: ')
        except:
            print('error in entering name')
        else:
            print('Thank you!')
            return name

def get_chips():
    while True:
        try:
            pl_chips = int(input('Place amount of chips: '))
        except:
            print('error in inputting chips amount')
        else:
            print('Thank you!')
            return pl_chips


def get_bet():
    while True:
        try:
            pl_bet = int(input('Place your bet: '))
        except:
            print('error in inputting bet')
        else:
            if pl_bet > pl_chips:
                print('Bet is greater than your chips.')
            else:
                print('Bet placed.')
                return pl_bet



