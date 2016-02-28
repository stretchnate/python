# import math
import random

deck = [
        ['2','3','4','5','6','7','8','9','10','J','Q','K','A'],
        ['Spades','Hearts','Clubs','Diamonds']
    ]

def deal(person):
    card = random.choice(deck[0]) + '[' + random.choice(deck[1])+']'
    if card not in person:
        person.append(card)

    return person

