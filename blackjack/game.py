import dealer

#process player cards/hand
def playerProcess(player):
    total = totalCards(player)
    while total < 21:
        choice = raw_input('What would you like to do hit (h) or stay (s)? ')

        if choice.upper() == 'H':
            dealer.deal(player)
            total = totalCards(player)
            getIndividualTotal(player, 'player')
        elif choice.upper() == 'S':
            print('player stays with '+str(total)+'\n')
            break;
        else:
            print('You must choose to hit (h) or stay (s)')

    return total

#get individual total of player or dealer
def getIndividualTotal(individual, who):
    msg = ' '
    msg += listCards(individual)

    total = totalCards(individual)
    print(who+' total = '+str(total)+msg+'\n')

# process dealers game
def dealerProcess(_dealer):
    d_total = totalCards(_dealer)
    while d_total < 21:
        choice = d_total < 17

        if choice:
            print('dealer hits on '+str(d_total))
            dealer.deal(_dealer)
            d_total = totalCards(_dealer)
            getIndividualTotal(_dealer, 'dealer')
        else:
            print('dealer stays with '+str(d_total)+' '+listCards(_dealer))
            break;

    return d_total

#list cards of persons hand
def listCards(person):
    cards = '('
    # for card in person:
        # cards = cards + ', '+card
    cards += ', '.join(person)

    cards += ')'
    return cards

#get total value of hand
def totalCards(person):
    total  = 0
    values = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'J' : 10, 'Q' : 10, 'K' : 10, 'A' : 11}
    for card in person:
        card_split = card.split('[')
        val = values[card_split[0]]
        if(val == 11 and total > 10):
            val = 1

        total += val

    return total

#determine winner of hand
def findWinner(player, _dealer):
    getIndividualTotal(player, 'player')
    getIndividualTotal(_dealer, 'dealer')
    d_total = totalCards(_dealer)
    p_total = totalCards(player)

    if d_total > 21:
        print('Dealer Busts, You Win!')
    elif p_total > 21:
        print('You Bust, You Lose!')
    elif d_total < p_total:
        print('You Win!')
    elif d_total > p_total:
        print('You Lose!')
    else:
        print('Push!')