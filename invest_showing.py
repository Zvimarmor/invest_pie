import matplotlib.pyplot as plt
import random

class invest:
    def __init__(self, invest_name, invest_category, invest_amount, invest_url):
        self.invest_name = invest_name
        self.invest_category = invest_category
        self.invest_amount = invest_amount
        self.invest_url = invest_url

class portfolio:
    def __init__(self, investor, invest_policy):
        self.investor = investor
        self.invest_policy = invest_policy
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



portfolio_data = [
    ("עובר ושב", 21333),
    ("קרן שקלית", 9108),
    ("אלטשולר- מניות", 57999),
    ("IBI מניות", 20830),
    ("אלטשולר- סנופי", 18576),
    ("IBI סנופי", 35098)
]

# Create portfolio instance
my_portfolio = portfolio("Zvi", "Conservative")

# Add investments to portfolio
for name, amount in portfolio_data:
    my_portfolio.add_invest(name, "Stocks", amount, "http://www.example.com")

# Display pie chart
my_portfolio.pie_chart()
