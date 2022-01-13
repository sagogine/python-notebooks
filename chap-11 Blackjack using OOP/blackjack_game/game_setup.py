from player.player import Player
from blackjack_carddeck.deck import Deck
from blackjack_carddeck.card import Card

class Game_Setup:

    def __init__(self):
        
        # get the name
        name = self.get_player_name()
        self.player = Player(name)

        # get the initial amount
        amount = self.get_player_initial_balance()
        self.player.initial_money(amount)

        # get the deck
        self.deck = Deck()

        # shuffle the deck
        self.deck.shuffle_deck()

    def get_player_name(self):
        while True:
            name = input('\nInput yout name : ')
            if(name != ''):
                break
        return name

    def get_player_initial_balance(self):
        while True:
            amount = int(input('\nHow much money you want to beging the game with : '))
            if amount>0:
                break
        return amount
    
    def __str__(self):
        return f"player details : {str(self.player)}"