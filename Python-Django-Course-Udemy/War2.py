#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("Creating new deck")
        self.allcards=[(s,r) for s in SUITE for r in RANKS]

    def shuffling(self):
        print("Shuffling deck")
        shuffle(self.allcards)


    def split(self):
        return(self.allcards[:26],self.allcards[26:])

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards=cards

    def __str__(self):
        return ("Contains {} cards".format(len(self.cards)))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name=name
        self.hand=hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has played {}".format(self.name, drawn_card))
        print("/n")
        return drawn_card

    def draw_war_cards(self):
        war_cards=[]
        if len(self.hand.cards)<3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
#create deck and split in half
player = input("Player, please enter your name: ")
d=Deck()
d.shuffling()
half1, half2=d.split()
#Player creation
comp=Player("computer",Hand(half1))
user=Player(player,Hand(half2))

#set round counts
round = 0
war_count=0

while user.still_has_cards() and comp.still_has_cards():
    round+=1
    print("It's time for a new round.")
    print("Here are the current standings: ")
    print(user.name+" has "+str(len(user.hand.cards))+" cards remaining.")
    print(comp.name+" has "+str(len(comp.hand.cards))+" cards remaining.")
    print('/n')

    #cards on table represented by a list
    tableau=[]

    #cards being played
    c_card=comp.play_card()
    u_card=user.play_card()

    #add cards to the tableau list
    tableau.append(c_card)
    tableau.append(u_card)

    #Check for War!
    if c_card[1]==u_card[1]:
        war_count+=1
        print("We have a war!")
        print('Each player places 3 cards "face down" and one card face up.')
        tableau.extend(user.draw_war_cards())
        tableau.extend(comp.draw_war_cards())

        c_card=comp.play_card()
        u_card=user.play_card()

        tableau.append(c_card)
        tableau.append(u_card)

        if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
            print(user.name+' has the higher card. adding to hand')
            user.hand.add(tableau)
        else:
            print(comp.name+' has the higher card. adding to hand...')
            comp.hand.add(tableau)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
            print(user.name+' has the higher card. adding to hand...')
            user.hand.add(tableau)
        else:
            print(comp.name+' has the higher card. adding to hand...')
            comp.hand.add(tableau)

print("Great game! This game lasted {} rounds.".format(str(round)))
print("A war happend {} times.".format(str(war_count)))



# Use the 3 classes along with some logic to play a game of war!
