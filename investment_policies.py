# Description: This file contains the investment policies for the investment portfolio.

class invest_policy:
    def __init__(self, invest_policy_name):
        self.invest_policy_name = invest_policy_name
        self.total_bonds = 0
        self.total_stocks = 0
        self.Dividend_stocks = 0
        self.growth_stocks = 0
        self.total_cash = 0
        self.total_real_estate = 0
        self.total_alternative = 0
        self.money_fund = 0
        self.gold = 0
        self.foreign_exchange = 0
        self.crypto = 0

    def add_invest_type(self, invest_type, invest_percent):
        if invest_type == "Bonds":
            self.total_bonds = invest_percent
        if invest_type == "Dividend Stocks":
            self.Dividend_stocks = invest_percent
            self.total_stocks += invest_percent
        elif invest_type == "Growth Stocks":
            self.growth_stocks = invest_percent
            self.total_stocks += invest_percent
        elif invest_type == "Stocks":
            self.total_stocks = invest_percent
        elif invest_type == "Cash":
            self.total_cash = invest_percent
        elif invest_type == "Real Estate":
            self.total_real_estate = invest_percent
        elif invest_type == "Alternative":
            self.total_alternative = invest_percent
        elif invest_type == "Money Fund":
            self.money_fund = invest_percent
        elif invest_type == "Gold":
            self.gold = invest_percent
        elif invest_type == "Foreign Exchange":
            self.foreign_exchange = invest_percent
        elif invest_type == "Crypto":
            self.crypto = invest_percent
        else:
            print("Invalid invest type")
        return  
    

investment_policies = {}
Conservative_policy = invest_policy("Conservative")
Conservative_policy.add_invest_type("Bonds", 70)
Conservative_policy.add_invest_type("Stocks", 20)
Conservative_policy.add_invest_type("Cash", 10)
investment_policies["Conservative"] = Conservative_policy

moderate_policy = invest_policy("Moderate")
moderate_policy.add_invest_type("Bonds", 40)
moderate_policy.add_invest_type("Stocks", 50)
moderate_policy.add_invest_type("Cash", 10)
investment_policies["Moderate"] = moderate_policy

Aggressive_policy = invest_policy("Aggressive")
Aggressive_policy.add_invest_type("Bonds", 20)
Aggressive_policy.add_invest_type("Stocks", 70)
Aggressive_policy.add_invest_type("Cash", 10)
investment_policies["Aggressive"] = Aggressive_policy 

Income_policy = invest_policy("Income")
Income_policy.add_invest_type("Dividend Stocks", 40)
Income_policy.add_invest_type("Bonds", 40)
Income_policy.add_invest_type("Real Estate", 10)
Income_policy.add_invest_type("Cash", 10)
investment_policies["Income"] = Income_policy

Growth_policy = invest_policy("Growth")
Growth_policy.add_invest_type("Growth Stocks", 70)
Growth_policy.add_invest_type("Stocks", 20)
Growth_policy.add_invest_type("Cash", 10)
investment_policies["Growth"] = Growth_policy

Warren_Buffett_policy = invest_policy("Warren Buffett")
Warren_Buffett_policy.add_invest_type("Stocks", 90)
Warren_Buffett_policy.add_invest_type("Bonds", 10)
investment_policies["Warren Buffett"] = Warren_Buffett_policy

Ray_Dalio_policy = invest_policy("Ray Dalio")
Ray_Dalio_policy.add_invest_type("Stocks", 30)
Ray_Dalio_policy.add_invest_type("Bonds", 55)
Ray_Dalio_policy.add_invest_type("Gold", 7.5) 
Ray_Dalio_policy.add_invest_type("Alternative", 7.5)
investment_policies["Ray Dalio"] = Ray_Dalio_policy

John_Bogle_policy = invest_policy("John Bogle")
John_Bogle_policy.add_invest_type("Stocks", 50)
John_Bogle_policy.add_invest_type("Bonds", 30)
John_Bogle_policy.add_invest_type("Foreign Exchange", 20)

Benjamin_Graham_policy = invest_policy("Benjamin Graham")
Benjamin_Graham_policy.add_invest_type("Stocks", 50)
Benjamin_Graham_policy.add_invest_type("Bonds", 50)