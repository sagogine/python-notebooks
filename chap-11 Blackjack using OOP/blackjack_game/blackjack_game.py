from blackjack_game.game_setup import Game_Setup
from blackjack_game.hand import Hand

class BlackJack_Game:

    def __init__(self,game_setup:Game_Setup):
        self.player = game_setup.player
        self.deck = game_setup.deck
        self.player_hand = Hand(self.player.hand)
        self.dealer_cards = []
        self.dealer_hand = Hand(self.dealer_cards)
        self.play_game()

    
    def play_game(self):
        
        play = True
        while play:
            self.deal_the_cards("player")
            self.deal_the_cards("dealer")
            game_on = True
            dealers_turn = False
            hand_amount=0
            print((self.player.player_account))
            while hand_amount==0:
                input_from_user =int(input("\nEnter the amount for this round : "))
                hand_amount = self.player.player_betting_amount_for_the_round(input_from_user)

            while game_on and hand_amount>0:
                
                self.print_player_hand_and_count()

                self.print_dealer_hand_and_count(dealers_turn)

                player_turn = self.player_draw()
                if(player_turn=='Stay'):
                    dealers_turn = self.dealer_draw()
                    if dealers_turn=='Bust':
                        self.dealer_bust(hand_amount)
                        break
                else:
                    self.player_bust()
                    break

                if(self.player_hand.get_hand_total() > self.dealer_hand.get_hand_total()):
                    print('\nPlayer won ! ')
                    self.player.player_account.deposit(hand_amount*2)
                    game_on = False
                elif(self.player_hand.get_hand_total() == self.dealer_hand.get_hand_total()):
                    print('\nGame drawn ! ')
                    self.player.player_account.deposit(hand_amount)
                    game_on = False
                else:
                     print("\nHand lost. Money Gone !")
                     game_on = False

            self.player.hand=[]
            self.dealer_cards=[]
            want_to_play = input("\nContinue to play - Y or N")
            if(want_to_play == 'Y'):
                continue
            else:
                break
                    

    def dealer_draw(self):
        dealers_turn=True
        while self.dealer_hand.get_hand_total()<17:
            self.print_dealer_hand_and_count(dealers_turn)
            self.dealer_hit()
            if self.dealer_hand.get_hand_total()>21:
                self.print_dealer_hand_and_count(dealers_turn)
                return "Bust"
            elif self.dealer_hand.get_hand_total() >=17 and self.dealer_hand.get_hand_total()<=21:
                self.print_dealer_hand_and_count(dealers_turn)
                return "Stay"

        return "Stay"


    def player_draw(self):
        while True:
            play_option = int(input("\nEnter 1: Hit or 2:Stand"))
            if play_option == 1:
                self.player_hit()
                if(self.player_hand.get_hand_total()>21):
                    self.print_player_hand_and_count()
                    return 'Bust'
                else:
                    self.print_player_hand_and_count()
                    
            else:
                return "Stay"  

    def print_player_hand_and_count(self):
        print("\nplayer hand")
        self.player.get_player_hand()

        print("\nplayer hand total")
        print(self.player_hand.get_hand_total())

    def print_dealer_hand_and_count(self,dealers_turn):
        print("\ndealer hand")
        self.get_dealer_hand(dealers_turn)
        if dealers_turn:
            print("\ndealer hand total")
            print(self.dealer_hand.get_hand_total())


    def dealer_bust(self,hand_amount):
        print('\nPlayer won ! ')
        self.player.player_account.deposit(hand_amount*2)                      

    def player_bust(self):
        print("\nHand lost. Money Gone !")

    def dealer_hit(self):
        self.dealer_cards.append(self.deck.deal_one())
        self.dealer_hand.set_hand(self.dealer_cards)

    def player_hit(self):
        self.player.hand.append(self.deck.deal_one())
        self.player_hand.set_hand(self.player.hand)

    def deal_the_cards(self,player_type:str):
        if player_type=='player':
            self.player.hand.extend(self.deck.remove_multiple_cards())
            self.player_hand.set_hand(self.player.hand)
        else:
            self.dealer_cards.extend(self.deck.remove_multiple_cards())
            self.dealer_hand.set_hand(self.dealer_cards)

    def get_dealer_hand(self,dealer_turn):
        if  not dealer_turn:
            print(self.dealer_cards[0])
            print("other card - X")
        else:
            for index in range(0,len(self.dealer_cards)):
                print(self.dealer_cards[index])