import random

deck = [
        ['2','3','4','5','6','7','8','9','10','J','Q','K','A'],
        ['Spades','Hearts','Clubs','Diamonds']
    ]

dealt = []

def deal(person):
    card = random.choice(deck[0]) + '[' + random.choice(deck[1])+']'

    while card in dealt:
        card = random.choice(deck[0]) + '[' + random.choice(deck[1])+']'

    dealt.append(card)
    person.append(card)

    return person

