from blackjack_carddeck.deck import Deck
from blackjack_carddeck.card import Card
from player.Player_Account import Player_Account

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.player_account:Player_Account = Player_Account(name,0)

    def initial_money(self,amount):
        self.player_account.balance = amount

    def player_won_the_hand(self,amount):
        self.player_account.deposit(amount)
        return True

    def player_betting_amount_for_the_round(self,amount):
        value = self.player_account.withdraw_amt(amount)
        if value == '\nFunds Unavailable':
            return 0
        else:
            return amount

    def __str__(self):
        return f"\nplayer - {self.name} has outstanding balance of {self.player_account.balance}"

    def get_player_hand(self):
        print(f"\nplayer - {self.name} has ")
        for index in range(0,len(self.hand)):
            print(str(self.hand[index]))


