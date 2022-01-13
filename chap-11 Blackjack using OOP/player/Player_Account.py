class Player_Account:
    '''
    Class to manage the Player account
    '''

    def __init__(self,owner,balance):
        '''
        Initializer method to player account to begin the game with certain amount
        '''
        self.owner = owner
        self.balance = balance

    def deposit(self,balance):
        '''
        Method to update the player's balance with the winnings from the hand
        '''
        self.balance += balance
        return '\nAmount added to players pot !'

    def withdraw_amt(self,amount):
        '''
        Method to update the player's balance after the putting the pot for next hand
        '''
        if self.balance<amount:
            return '\nFunds Unavailable'
        else:
            self.balance -= amount
            return '\nMoney added to hand !'

    def __str__(self):
        return f"\nAccount owner : {self.owner} has outstanding balance of {self.balance}"
        