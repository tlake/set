'''

The deck consists of 81 cards varying in four features: 

number (one, two, or three); 
symbol (diamond, squiggle, oval); 
shading (solid, striped, or open); 
and color (red, green, or purple).

Each possible combination of features (e.g., a card with three striped 
green diamonds) appears precisely once in the deck.


A set consists of three cards which satisfy all of these conditions:

They all have the same number, or they have three different numbers.
They all have the same symbol, or they have three different symbols.
They all have the same shading, or they have three different shadings.
They all have the same color, or they have three different colors.

The rules of Set are summarized by: If you can sort a group of three cards into "Two of ____ and one of _____," then it is not a set.

'''

import random


class Card(object):
    def __init__(self, number, symbol, shading, color):
        self.number = number
        self.symbol = symbol
        self.shading = shading
        self.color = color

    def readout(self):
        properties = [self.number, self.symbol, self.shading, self.color]
        return ' '.join(properties)


def create_deck():
    new_deck = []
    card_number = 0
    for number in ['one', 'two', 'three']:
        for symbol in ['diamond', 'squiggle', 'oval']:
            for shading in ['solid', 'striped', 'open']:
                for color in ['red', 'green', 'purple']:
                    card_number += 1
                    new_deck.append(Card(number, symbol, shading, color))
    return new_deck


def deal_to_field(source_deck, field_deck):
    if len(source_deck) > 0:
        rando_card = random.randint(0, len(source_deck) - 1)
        field_deck.append(source_deck[rando_card])
        del source_deck[rando_card]
    else:
        print "No cards left in source deck!"


def show_field(field):
    print ""
    for i in range(len(field)):
        print i, ':', field[i].readout()
    print ""


def number_test(card1, card2, card3):
    if card1.number == card2.number and card2.number == card3.number:
        return True
    elif card1.number != card2.number and card2.number != card3.number \
        and card3.number != card1.number:
        return True
    else:
        return False


def symbol_test(card1, card2, card3):
    if card1.symbol == card2.symbol and card2.symbol == card3.symbol:
        return True
    elif card1.symbol != card2.symbol and card2.symbol != card3.symbol \
        and card3.symbol != card1.symbol:
        return True
    else:
        return False


def shading_test(card1, card2, card3):
    if card1.shading == card2.shading and card2.shading == card3.shading:
        return True
    elif card1.shading != card2.shading and card2.shading != card3.shading \
        and card3.shading != card1.shading:
        return True
    else:
        return False


def color_test(card1, card2, card3):
    if card1.color == card2.color and card2.color == card3.color:
        return True
    elif card1.color != card2.color and card2.color != card3.color \
        and card3.color != card1.color:
        return True
    else:
        return False


def test_for_set(card1, card2, card3):
    if not number_test(card1, card2, card3):
        print "The numbers don't make a set."
    elif not symbol_test(card1, card2, card3):
        print "The symbols don't make a set."
    elif not shading_test(card1, card2, card3):
        print "The shadings don't make a set."
    elif not color_test(card1, card2, card3):
        print "The colors don't make a set."
    else:
        return True


def play_set():
    # game setup
    deck = []
    deck = create_deck()
    field = []

    




