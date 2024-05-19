import random
from investment_policies import *
from invest_showing import *

USER_COUNTER = 0

class user:
    """
    Represents an individual investor with their name, account number, investment policy and investment portfolio.
    """

    def __init__(self):
        """
        Initializes the user with their name, account number, investment policy, and portfolio.
        """
        global USER_COUNTER
        USER_COUNTER += 1

        #initialize the user with their name
        self.name = input("Enter your name: ")
        print("Do you want to see the available investment policies? (yes/no)")
        answer = input()
        if answer.lower() == "yes":
            print("Available investment policies are: ")
            for i in investment_policies:
                print(i)

        #initialize the user with their investment policy
        user_invest_request = input("Enter the name of the investment policy you want to use: ")
        if user_invest_request in investment_policies:
            self.investment_policy = investment_policies[user_invest_request]
        elif user_invest_request in ["other", "Other", "OTHER"]:
            self.investment_policy = build_new_investment_policy(input("Enter the name of the new investment policy: "))
        else:
            print("Sorry, the investment policy you entered is not available. Please try again.")
            return

        self.account_number = USER_COUNTER
        self.portfolio = portfolio(self.name, self.investment_policy, self.account_number)
        print("The investment types in your policy are: ")
        self.investment_policy.print_all_invest_types()

        for invest in self.investment_policy.invests_dict:
            if self.investment_policy.invests_dict[invest] != 0:
                print("Enter the amount you have right now in", invest)
                invest_amount = float(input())
                #todo: add error handling
                self.portfolio.add_invest(invest, invest, invest_amount)

    def fix_portfolio_by_policy(self):
        """
        Fixes the portfolio by the investment policy.
        """
        answer = []
        for invest in self.portfolio.invest_list:
            invest_differece = invest.invest_amount/self.portfolio.invest_total * 100 - self.investment_policy.invests_dict[invest.invest_name]
            if invest_differece != 0:
                answer.append((invest.invest_name, invest_differece * self.portfolio.invest_total / 100))
        return answer


def main():
    """
    Main function to run the program.
    """
    current_user = user()
    to_print_chart = input("Do you want to see the pie chart of your portfolio? (yes/no)")
    if to_print_chart.lower() == "yes":
        current_user.portfolio.pie_chart()
    things_to_change = current_user.fix_portfolio_by_policy()
    if things_to_change:
        print("You need to change the following investments: ")
        for invest in things_to_change:
            print(invest[0], "by", invest[1])
    else:
        print("Your portfolio is perfect")

    
if __name__ == "__main__":
    while True:
        main()
        print("Do you want to create another user? (yes/no)")
        answer = input()
        if answer.lower() == "no":
            break
    print("Number of users created: ", USER_COUNTER)

    