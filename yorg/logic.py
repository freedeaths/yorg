from sys import exit
from racing.game.game import Game, GameLogic


class _Logic(GameLogic):
    '''This class defines the logics of the game.'''

    def on_start(self):
        GameLogic.on_start(self)
        try:
            car = game.options['car']
        except KeyError:
            car = ''
        try:
            track = game.options['track']
        except KeyError:
            track = ''
        if car and track:
            self.mdt.fsm.demand('Loading', 'tracks/track_' + track, car)
        else:
            self.mdt.fsm.demand('Menu')
        base.accept('escape-up', self.on_exit)

    def on_exit(self):
        if game.options['open_browser_at_exit']:
            eng.open_browser('http://www.ya2.it')
        exit()