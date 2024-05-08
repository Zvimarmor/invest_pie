# Description: This file contains the investment policies for the investment portfolio.

class invest_policy:
    def __init__(self, invest_policy_name):
        self.invest_policy_name = invest_policy_name
        invests_type = ["Bonds", "Dividend Stocks", "Growth Stocks", "Stocks", "Cash", "Real Estate", "Alternative", "Money Fund", "Gold", "Foreign Exchange", "Crypto"]
        self.invests_dict = {keys: 0 for keys in invests_type}

    def add_invest_type(self, invest_type, invest_percent):
        if invest_type in self.invests_dict:
            self.invests_dict[invest_type] = invest_percent
        else:
            print("Investment type not found")
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