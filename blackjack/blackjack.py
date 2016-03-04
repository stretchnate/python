import dealer
import game

player = []
_dealer = []
total = 0
d_total = 0

def main():
    play_again = 'Y'
    while(play_again.upper() == 'Y'):
        clean()
        deal()
        total = game.totalCards(player)
        d_total = game.totalCards(_dealer)

        print('\nplayer total = '+str(total)+' ('+player[0]+', '+player[1]+')\n')
        print('dealer is showing '+_dealer[0]+'\n')

        total = game.playerProcess(player)
        if(total < 22):
            game.dealerProcess(_dealer)

        game.findWinner(player, _dealer)

        play_again = raw_input('Play Again (y/n)?');

def deal():
    dealer.deal(player)
    dealer.deal(_dealer)
    dealer.deal(player)
    dealer.deal(_dealer)

def clean():
    global player
    global _dealer
    global total
    global d_total

    player  = []
    _dealer = []
    total   = 0
    d_total = 0


main()
