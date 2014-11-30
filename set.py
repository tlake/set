'''

The deck consists of 81 cards varying in four features: 

number (1, 2, or 3); 
symbol ('A', 'B', or 'C'); 
background bg_blue, bg_black, or bg_magenta); 
and foreground (fg_yellow, fg_cyan, or fg_white).

Each possible combination of features (e.g., a card with three striped 
green diamonds) appears precisely once in the deck.


A set consists of three cards which satisfy all of these conditions:

They all have the same number, or they have three different numbers.
They all have the same symbol, or they have three different symbols.
They all have the same background, or they have three different backgrounds.
They all have the same foregrounds, or they have three different foregrounds.

The rules of Set are summarized by: If you can sort a group of three cards into "Two of ____ and one of _____," then it is not a set.

'''

import colorama
import random
import os

# Initialize colorama's coloring functionalities
colorama.init(autoreset = True)

# Define color definitions
bg_blue = '\033[44m'
bg_black = '\033[40m'
bg_magenta = '\033[45m'
fg_yellow = '\033[33m'
fg_cyan = '\033[36m'
fg_white = '\033[37m'


class Card(object):
    def __init__(self, number, symbol, background, foreground):
        self.number = number
        self.symbol = symbol
        self.background = background
        self.foreground = foreground

    def readout(self):
        return colorama.Style.BRIGHT + self.background + \
            self.foreground + (self.number * self.symbol)


def create_deck():
    new_deck = []
    card_number = 0
    for number in [1, 2, 3]:
        for symbol in [' A ', ' B ', ' C ']:
            for background in [bg_blue, bg_black, bg_magenta]:
                for foreground in [fg_yellow, fg_cyan, fg_white]:
                    card_number += 1
                    new_deck.append(Card(number, symbol, background, foreground))
    return new_deck


def deal_to_field(source_deck, field_deck):
    if len(source_deck) > 0:
        rando_card = random.randint(0, len(source_deck) - 1)
        field_deck.append(source_deck[rando_card])
        del source_deck[rando_card]
    else:
        print "No cards left in source deck!"


def show_field(cards):
    print ""
    for i in range(len(cards)):
        print i, ':', cards[i].readout()
    print ""


def number_test(card1, card2, card3):
    if card1.number == card2.number and card2.number == card3.number:
        return True
    elif card1.number != card2.number and card2.number != card3.number \
        and card3.number != card1.number:
        return True
    else:
        print "The numbers don't make a set."
        return False

def symbol_test(card1, card2, card3): 
    if card1.symbol == card2.symbol and card2.symbol == card3.symbol: 
        return True 
    elif card1.symbol != card2.symbol and card2.symbol != card3.symbol \
        and card3.symbol != card1.symbol:
        return True
    else:
        print "The symbols don't make a set."
        return False

def background_test(card1, card2, card3):
    if card1.background == card2.background and card2.background == card3.background:
        return True
    elif card1.background != card2.background and card2.background != card3.background \
        and card3.background != card1.background:
        return True
    else:
        print "The backgrounds don't make a set."
        return False

def foreground_test(card1, card2, card3):
    if card1.foreground == card2.foreground and card2.foreground == card3.foreground:
        return True
    elif card1.foreground != card2.foreground and card2.foreground != card3.foreground \
        and card3.foreground != card1.foreground:
        return True
    else:
        print "The foregrounds don't make a set." 
        return False 

def test_for_set(card1, card2, card3):
    if number_test(card1, card2, card3) and symbol_test(card1, card2, \
        card3) and background_test(card1, card2, card3) and foreground_test( \
        card1, card2, card3):
        return True
    else:
        return False


def play_set():
    # game setup
    deck = []
    deck = create_deck()
    field = []

    os.system('clear')

    for i in range(0, 12):
        deal_to_field(deck, field)

    # execution of game
    while len(field) > 0:
        show_field(field)
        
        mode_select = raw_input("Would you like to declare a set, " + \
            "deal three more cards, or check on the status of the " \
            "deck? (set/deal/check) ")

        if mode_select not in ['set', 'deal', 'check']:
            print '\n', 'Invalid action.'

        elif mode_select == 'deal':
            for i in range(0, 3):
                deal_to_field(deck, field)

        elif mode_select == 'check':
            print '\n', 'There are ' + str(len(deck)) + ' cards left ' \
                + 'in the deck, and ' + str(len(field)) + ' cards on ' \
                + 'the field.'
        else:

            print "You will be prompted to make three selections."
            print "Use the index numbers on the left for your choices.", \
                "\n"

            choice1 = raw_input(" First Choice: ")
            choice2 = raw_input("Second Choice: ")
            choice3 = raw_input(" Third Choice: ")

            # error handling to catch nonvalid card selections
            if ( \
                choice1 not in range(len(field)) or \
                choice2 not in range(len(field)) or \
                choice3 not in range(len(field)) \
                ) \
                or ( \
                choice1 == choice2 or \
                choice2 == choice3 or \
                choice3 == choice1 \
                ):

                print '\n', 'Please enter three different, valid ' \
                    + 'card indices.'

            else:

                choice1 = int(choice1)
                choice2 = int(choice2)
                choice3 = int(choice3)

                print ""

                holding = []
                if test_for_set(field[choice1], field[choice2], \
                    field[choice3]):
                    print "\n--- You made a set! ---\n"
                    for i in range(len(field)):
                        if i not in [choice1, choice2, choice3]:
                            holding.append(field[i])
                    field = holding
                    if len(field) < 10 and len(deck) > 0:
                        for i in range(0, 3):
                            deal_to_field(deck, field)

        if len(field) < 1 and len(deck) < 1:
            print "Congratulations! The game ends in VICTORY!"


