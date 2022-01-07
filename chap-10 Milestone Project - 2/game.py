from Card import Card
from Deck import Deck
from player import Player

class Game:

    player_1_card_list=[]
    player_2_card_list=[] 

    def __init__(self):
        print('Game has started !')
        self.player_1 = Player("Player_1")
        self.player_2 = Player("Player_2")
        self.deck = Deck()
        self.deck.shuffle_deck()

    def distribute_the_deck(self):
        for index,item in enumerate(self.deck.deck_of_cards):
            if index%2==0:
                self.player_1.all_cards.append(item)
            else:
                self.player_2.all_cards.append(item)
        
    
    def play_game(self):
        iteration = 0
        game_on = True
        print('Game is running')
        player_1_cant_goto_war = False
        player_2_cant_goto_war = False
        while(game_on):
                iteration+=1
                print(f'Currently in iteration - {iteration}')
                war_on = self.game_logic()
                while(war_on):
                    print(f'A war has occured in iteration - {iteration}')
                    if len(self.player_1.all_cards)<5:
                        player_1_cant_goto_war = True
                        break
                    elif len(self.player_2.all_cards)<5:
                        player_2_cant_goto_war = True
                        break
                    self.player_1_card_list.extend(self.player_1.remove_multiple_cards())
                    self.player_2_card_list.extend(self.player_2.remove_multiple_cards())
                    war_on = self.game_logic()

                self.player_1_card_list.clear()
                self.player_2_card_list.clear()

                if len(self.player_1.all_cards)==0 or player_1_cant_goto_war:
                    print(f'{self.player_2.name} has won the game' )
                    print(f'The game has ended because a war has occurred and player didnt have enough cards : {player_1_cant_goto_war}')
                    break
                elif len(self.player_2.all_cards)==0 or player_2_cant_goto_war:
                    print(f'{self.player_1.name} has won the game' )
                    print(f'The game has ended because a war has occurred and player didnt have enough cards : {player_2_cant_goto_war}')
                    break


    def game_logic(self):
        war_on=False
        player_1_card = self.player_1.remove_one()
        player_2_card = self.player_2.remove_one()
        if player_1_card.value > player_2_card.value:
            self.player_1_card_list.extend([player_1_card,player_2_card])
            self.player_1.add_cards(self.player_1_card_list)
        elif player_1_card.value < player_2_card.value:
            self.player_2_card_list.extend([player_1_card,player_2_card])
            self.player_2.add_cards(self.player_2_card_list)
        elif player_1_card.value == player_2_card.value:
            print(f' player_1_card.value : {player_1_card.value} and player_2_card.value : {player_2_card.value} - A war is about to occur')
            self.player_2_card_list.extend([player_1_card,player_2_card])
            war_on = True
        return war_on


   # if __name__ == '__main__':
    #    Game("Hello")
