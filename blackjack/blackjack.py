import dealer
import game

player = []
_dealer = []
def main():
    dealer.deal(player)
    dealer.deal(_dealer)
    dealer.deal(player)
    dealer.deal(_dealer)

    total = game.totalCards(player)
    d_total = game.totalCards(_dealer)

    print('\nplayer total = '+str(total)+' ('+player[0]+', '+player[1]+')\n')
    print('dealer is showing '+_dealer[0]+'\n')

    total = game.playerProcess(player, total)
    if(total < 22):
        d_total = game.dealerProcess(_dealer, d_total)

    game.findWinner(d_total, total)

main()
