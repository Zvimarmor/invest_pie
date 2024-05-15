import random
from investment_policies import *
from invest_showing import *

USER_COUNTER = 0

class user:
    """
    Represents an individual investor with their name, account number, investment policy and investment portfolio.
    """
    def __init__(self, name, age, account_number):
        self.name = input("Enter your name: ")
        self.account_number = USER_COUNTER + 1
        USER_COUNTER += 1
        self.portfolio = portfolio(self.name, investment_policies["Conservative"], self.account_number)

        

        