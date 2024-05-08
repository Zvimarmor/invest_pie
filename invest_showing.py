import matplotlib.pyplot as plt
import random
import investment_policies
from investment_policies import investment_policies

class invest:
    def __init__(self, invest_name, invest_category, invest_amount, invest_url):
        self.invest_name = invest_name
        self.invest_category = invest_category
        self.invest_amount = invest_amount
        self.invest_url = invest_url

        
class portfolio:
    def __init__(self, investor, invest_policy, account_number):
        self.investor = investor
        self.invest_policy = invest_policy
        self.account_number = account_number  
        self.invest_list = []
        self.invest_total = 0
    
    def add_invest(self, invest_name, invest_category, invest_amount, invest_url):
        self.invest_list.append(invest(invest_name, invest_category, invest_amount, invest_url))
        self.invest_total += invest_amount

    def delete_invest(self, invest_name):
        for i in self.invest_list:
            if i.invest_name == invest_name:
                self.invest_total -= i.invest_amount
                self.invest_list.remove(i)
                return

    def change_invest_amount(self, invest_name, invest_amount):
        for i in self.invest_list:
            if i.invest_name == invest_name:
                self.invest_total -= i.invest_amount
                i.invest_amount = invest_amount
                self.invest_total += invest_amount
                return

    def __str__(self):
        return (self.investor, self.invest_policy, self.invest_list, self.invest_total)       
            
    def get_invest_list(self):
        return self.invest_list
            
    def get_invest_total(self):
        return self.invest_total
            
    def show_portfolio(self):
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
        for i in investment_policies[self.invest_policy].invests_dict:
            if investment_policies[self.invest_policy].invests_dict[i] != 0:
                self.add_invest(i, i, investment_policies[self.invest_policy].invests_dict[i], "")
        return
    
    def pie_chart(self):
        labels = []
        sizes = []
        colors = []

        plt.title(self.investor + " account number: " + str(self.account_number))
        for i in self.invest_list:
            labels.append(i.invest_name)
            sizes.append(i.invest_amount)
            colors.append((random.random(), random.random(), random.random()))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

        plt.axis('equal') 
        plt.show()

def build_portfolio_from_user():
    investor = input("Enter investor name: ")
    while True:
        user_input = input("Do you want to see the investment policies? (y/n): ")
        if user_input not in ["y", "n", "Y", "N"]:
            print("Invalid input")
            continue
        if user_input == "y" or user_input == "Y":
            print("Investment Policies: ")
            for i in investment_policies:
                print(i)
        invest_policy = input("Enter investment policy: ")
        if invest_policy in investment_policies:
            break
        else:
            print("Invalid investment policy")
    
    account_number = random.randint(1000, 9999) # Generate random account number between 1000 and 9999
    my_portfolio = portfolio(investor, invest_policy, account_number)
    print ("your account number is: ", account_number)
    return my_portfolio
        
def main():
    my_portfolio = build_portfolio_from_user()
    my_portfolio.pie_chart()


if __name__ == "__main__":
    main()
