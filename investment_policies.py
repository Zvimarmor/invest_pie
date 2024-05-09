# This file contains definitions of various investment policies for an investment portfolio.

# Define a class to represent an investment policy
class invest_policy:
    def __init__(self, invest_policy_name):
        self.invest_policy_name = invest_policy_name
        invests_type = ["Bonds", "Dividend Stocks", "Growth Stocks", "Stocks", "Cash", "Real Estate", "Alternative", "Money Fund", "Gold", "Foreign Exchange", "Crypto"]
        self.invests_dict = {keys: 0 for keys in invests_type}

    # Method to add or update the percentage of a specific investment type
    def add_invest_type(self, invest_type, invest_percent):
        if invest_type in self.invests_dict:
            self.invests_dict[invest_type] = invest_percent
        else:
            print("Investment type not found")
        return  
    
# Function to build a new investment policy
def build_new_investment_policy(invest_policy_name):
    new_investment_policy = invest_policy(invest_policy_name)
    total_percent = 0
    for i in new_investment_policy.invests_dict:
        while True:
            user_input = input("type number of wanted percentage for " + i + " or enter to keep the same. Total percentage left: " + str(100 - total_percent) + ": ")
            if not user_input.isdigit() and user_input != "":
                print("Invalid input")
                return
            if user_input == "":
                user_input = 0
            user_input = float(user_input)
            if user_input >= 0:
                new_investment_policy.add_invest_type(i, float(user_input))
                total_percent += float(user_input)
                if total_percent == 100:
                    print("Perfect! Your investment policy is ready")
                    return new_investment_policy
                if total_percent > 100:
                    print("Total percentage exceeds 100, please try running the program again")
                    return
                break

    return new_investment_policy

# Dictionary to store predefined investment policies
investment_policies = {}

# Define and instantiate predefined investment policies
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
