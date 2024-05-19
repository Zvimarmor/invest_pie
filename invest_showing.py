# This file defines classes and functions related to investment portfolios and policies.
#The main function build_portfolio_from_user() builds a portfolio based on user input regarding investor name
# and investment policy and shows the investment distribution in the portfolio using a pie chart.

import matplotlib.pyplot as plt
import random
from investment_policies import build_new_investment_policy
from investment_policies import investment_policies

# Define a class to represent an individual investment
class invest:
    """
    Represents an individual investment with its name, category and amount.
    """
    def __init__(self, invest_name, invest_category, invest_amount):
        self.invest_name = invest_name
        self.invest_category = invest_category
        self.invest_amount = invest_amount

# Define a class to represent an investment portfolio
class portfolio:
    """
    Represents an investment portfolio for a specific investor.
    """
    def __init__(self, investor, invest_policy, account_number):
        """
        Initializes the portfolio with investor details, investment policy, and account number.
        """
        self.investor = investor
        self.invest_policy = invest_policy
        self.account_number = account_number  
        self.invest_list = []
        self.invest_total = 0
    
    def add_invest(self, invest_name, invest_category, invest_amount):
        """
        Adds a new investment to the portfolio.
        """
        self.invest_list.append(invest(invest_name, invest_category, invest_amount))
        self.invest_total += invest_amount

    def delete_invest(self, invest_name):
        """
        Deletes an investment from the portfolio.
        """
        for i in self.invest_list:
            if i.invest_name == invest_name:
                self.invest_total -= i.invest_amount
                self.invest_list.remove(i)
                return

    def change_invest_amount(self, invest_name, invest_amount):
        """
        Changes the amount of a specific investment in the portfolio.
        """
        for i in self.invest_list:
            if i.invest_name == invest_name:
                self.invest_total -= i.invest_amount
                i.invest_amount = invest_amount
                self.invest_total += invest_amount
                return

    def __str__(self):
        """
        Returns a string representation of the portfolio.
        """
        return (self.investor, self.invest_policy, self.invest_list, self.invest_total)       
            
    def get_invest_list(self):
        """
        Returns the list of investments in the portfolio.
        """
        return self.invest_list
            
    def get_invest_total(self):
        """
        Returns the total investment amount in the portfolio.
        """
        return self.invest_total
            
    def show_portfolio(self):
        """
        Prints details of the portfolio including investor information and investments.
        """
        print("Investor: ", self.investor)
        print("Account Number: ", self.account_number)
        print("Invest Policy: ", self.invest_policy)
        print("Invest Total: ", self.invest_total)
        for i in self.invest_list:
            print("Invest Name: ", i.invest_name)
            print("Invest Category: ", i.invest_category)
            print("Invest Amount: ", i.invest_amount)
            print("Invest URL: ", i.invest_url)
            print("\n")

    def build_portfolio_from_invest_policy(self):
        """
        Builds the portfolio based on the specified investment policy.
        """
        for invest_name, invest_amount in self.invest_policy.invests_dict.items():
            if invest_amount != 0:
                self.add_invest(invest_name, invest_name, invest_amount)
        return

    def pie_chart(self):
        """
        Generates a pie chart representing the investment distribution in the portfolio.
        """
        labels = []
        sizes = []
        colors = []

        plt.suptitle(self.investor + "'s Portfolio. Account Number: " + str(self.account_number), fontsize=14)
        plt.title("Investment policy: " + self.invest_policy.invest_policy_name, fontsize=10)
        for i in self.invest_list:
            labels.append(i.invest_name)
            sizes.append(i.invest_amount)
            colors.append((random.random(), random.random(), random.random()))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

        plt.axis('equal') 
        plt.show(block=False)
        return

# Function to build a portfolio based on user input
def build_portfolio_from_policy():
    """
    Builds a portfolio based on user input regarding investor name and investment policy.
    """
    investor = input("Enter investor name: ")
    while True:
        user_input = input("Do you want to see the investment policies? (yes/no): ")
        user_input = user_input.lower()
        if user_input == "yes":
            print("Investment Policies: ")
            for i in investment_policies:
                print(i)
        invest_policy_name = input("Enter investment policy: ")
        if invest_policy_name == "Other" or invest_policy_name == "other":
            invest_policy_name = (investor + "'s policy")
            invest_policy = build_new_investment_policy(invest_policy_name)
            investment_policies[invest_policy_name] = invest_policy
            break
        if invest_policy_name in investment_policies:
            invest_policy = investment_policies[invest_policy_name]
            break
        else:
            print("Invalid investment policy")

    my_portfolio = portfolio(investor, invest_policy, account_number = 0)
    my_portfolio.build_portfolio_from_invest_policy()
    return my_portfolio


# Main function to run the program
def main():
    """
    Main function to execute the program.
    """
    my_portfolio = build_portfolio_from_policy()
    my_portfolio.pie_chart()


if __name__ == "__main__":
    main()
