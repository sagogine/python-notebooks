from Deck import Deck
from Card import Card

class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def remove_multiple_cards(self):
        player_card_list = []
        for i in range(0,3):
            player_card_list.append(self.remove_one())
        return player_card_list

    def add_cards(self,new_cards):
        if type(new_cards)== type([]):
            # incase of multiple cards
            self.all_cards.extend(new_cards)
        else:
            # incase of adding a single card
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
