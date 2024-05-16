import random
from investment_policies import *
from invest_showing import *


class user:
    """
    Represents an individual investor with their name, account number, investment policy and investment portfolio.
    """
    def __init__(self, name, investment_policy, user_counter):
        """
        Initializes the user with their name, account number, investment policy, and portfolio.
        """
        self.name = name
        self.investment_policy = investment_policy
        self.account_number = user_counter + 1 
        user_counter += 1
        self.portfolio = portfolio(self.name, self.investment_policy, self.account_number)



    
if __name__ == "__main__":
    user_counter = 0
    user_name = input("Enter your name: ")
    print("Available investment policies are: ")
    for i in investment_policies:
        print(i)
    user_investment_policy = input("Enter the name of the investment policy you want to use: ")
    if user_investment_policy not in investment_policies:
        print("Investment policy not found")
        exit()
    user = user(user_name, investment_policies[user_investment_policy], user_counter)
    print("Welcome " + user.name + "! Your account number is: " + str(user.account_number))
