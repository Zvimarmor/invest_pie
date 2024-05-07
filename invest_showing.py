import matplotlib.pyplot as plt
import random
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

    def pie_chart(self):
        labels = []
        sizes = []
        colors = []

        for i in self.invest_list:
            labels.append(i.invest_name)
            sizes.append(i.invest_amount)
            colors.append((random.random(), random.random(), random.random()))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

        plt.axis('equal') 
        plt.show()

def build_portfolio_from_user(self):
    investor = input("Enter investor name: ")
    invest_policy = input("Enter investment policy: ")
    if invest_policy not in investment_policies:
        print("Invalid investment policy")
        return
    account_number = random.randint(1000, 9999) # Generate random account number between 1000 and 9999
    my_portfolio = portfolio(investor, invest_policy, account_number)
    print ("your account number is: ", account_number)
    return my_portfolio

        
def main():
    my_portfolio = build_portfolio_from_user()
    my_portfolio.add_invest("Vanguard Total Bond Market Index Fund", "Bonds", 10000, "https://investor.vanguard.com/mutual-funds/profile/VBMFX")
    my_portfolio.add_invest("Vanguard Total Stock Market Index Fund", "Stocks", 20000, "https://investor.vanguard.com/mutual-funds/profile/VTSAX")
    my_portfolio.add_invest("Vanguard Total International Stock Index Fund", "Stocks", 30000, "https://investor.vanguard.com/mutual-funds/profile/VTIAX")
    my_portfolio.show_portfolio()
    my_portfolio.pie_chart()
