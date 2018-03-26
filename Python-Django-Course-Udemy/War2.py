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
        deck=[]

    def createDeck(self):
        for item in SUITE:
            for card in RANKS:
                deck+="".join(item,card)
        return deck

    def shuffling(self):
        deck=shuffle(deck)
        return deck

    def split(self, player):
        if player=='player1':
            player.hand=deck[::2]
        else:
            player.hand=deck[1::2]
        return player.hand

class Hand(Deck):
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self):
        hand=self.hand

    def play_card(self):
        return hand.pop(0)

    def add_card(self, cards):
        for item in cards:
            hand.append(item)
        return hand

class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name):
        name=self.name

    def check_hand(self):
        if len(Player.hand)==0:
            print("You have lost the game, {}".format(Player.name))



######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

def begin_game():
    Player1=Player(name=input("Player 1, please enter your name: "))
    Player2=Player(name=input("Player 2, please enter your name: "))

def setup():
    print("creating deck...")
    deck=Deck.createDeck()
    print("shuffling deck...")
    deck=Deck.shuffling(deck)
    print("dealing cards to {} and {}...".format(Player1.name, Player2.name))
    Player1.hand=Deck.split("player1")
    Player2.hand=Deck.split("player2")
    print("Cards dealt. Let's begin!")

def round():
    tableau=[]
    P1card=Player1.play_card()
    P2card=Player2.play_card()
    tableau.append(P1card)
    tableau.append(P2card)
    results=compare (P1card, P2card, tableau)
    results.add_card(tableau)

def compare(p1card, p2card, tableau):
    if p1card > p2card:
        return Player1
    elif P2card > P1P1card:
        return Player2
    else:
        war(tableau)
def war(tableau):
    for i in range(3):
        tableau.append(Player1.play_card())
        tableau.append(Player2.play_card())

    p1card=Player1.play_card()
    p2card=Player2.play_card()
    results = compare(p1card, p2card, tableau)
    return results.add_card(tableau)




# Use the 3 classes along with some logic to play a game of war!
