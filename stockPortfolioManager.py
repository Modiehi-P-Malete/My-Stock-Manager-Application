class MyPortfolioManagerApplication:
#10.The class constructor method used to initialise the collection of portfolios and set the available
#balance to R10 000.
    def __init__(self):
        self.portfolios = {}
        # 
        self.availableBalance = 10000

#1. This will add a new portfolio to the catalogue, if the name already exists, the user will be asked for a different one.
    def addNewPortfolio(self, portfolioName):
        if portfolioName not in self.portfolios:
            self.portfolios[portfolioName] = {}
            print(f"\nPortfolio '{portfolioName}' has been added successfully to your portfolio list.")
        else:
            print("A portfolio with that name already exists. Please use a different name for your new portfolio.")

#2.This will add new stock to the specified portfolio. An error message will appear when the portfolio isn't found.
    def addPortfolioStock(self, portfolioName, stockName, shares):
        if portfolioName in self.portfolios:
            if stockName in self.portfolios[portfolioName]:
                print("Stock already exists in the portfolio you selected. Use 'Buy shares' to add more shares to your stock.")
            else:
                self.portfolios[portfolioName][stockName] = shares
                print(f"Stock '{stockName}' added to '{portfolioName}' with {shares} shares.")
        else:
            print("Portfolio not found. Try entering the portfolio name again.")

#3. This will add shares to an existing stock option and it will display an error message if the stock/portfolio isn't found.
    def buyShares(self, portfolioName, stockName, shares, pricePerShare):
        cost = shares * pricePerShare
        if cost > self.availableBalance:
            print("Insufficient funds.")
            return
        if portfolioName in self.portfolios and stockName in self.portfolios[portfolioName]:
            self.portfolios[portfolioName][stockName] += shares
            self.availableBalance -= cost
            print(f"Bought {shares} shares of '{stockName}' for R{cost}.")
        else:
            print("Portfolio or stock not found.")

#4. This option will enable users to sell shares from an existing option.
     # Appropriate error messages will pop up to let the user know their faults.
    def sellShares(self, portfolioName, stockName, shares, pricePerShare):
        if portfolioName in self.portfolios and stockName in self.portfolios[portfolioName]:
            if self.portfolios[portfolioName][stockName] >= shares:
                self.portfolios[portfolioName][stockName] -= shares
                sale_price = shares * pricePerShare
                self.availableBalance += sale_price
                print(f"Sold {shares} shares of '{stockName}' for R{sale_price} .")
            else:
                print("Insufficient shares to sell.")
        else:
            print("Portfolio or stock not found.")

#5. This will allow the user to deposit money and add to their available balance.
    def depositMoney(self, amount):
        self.availableBalance += amount
        print(f"Deposited R{amount}.")

#6. User will be able to withdraw from their available balance.
    # If the user enters an amount larger than their balance, an error message will pop up.
    def withdrawMoney(self, amount):
        if amount <= self.availableBalance:
            self.availableBalance -= amount
            print(f"Withdrew R{amount}.")
        else:
            print("Insufficient funds. Please check your balance & enter the proper amount to withdraw.")

#7. Allows user to view their balance.
    def showAvailBalance(self):
        print(f"Available balance: R{self.availableBalance}.")

#8. User can view all their existing portfolios. Otherwise, an error message appears.
    def showAllPortfolios(self):
        print("\nPortfolios:")
        if self.portfolios:
            for portfolio in self.portfolios:
                print(f"- {portfolio}")
        else:
            print("No portfolios found.")

#9. User may view their specified portfolio, if it exists.
    def showSpecificPortfolio(self, portfolioName):
        if portfolioName in self.portfolios:
            print(f"\nPortfolio: {portfolioName}")
            for stock, shares in self.portfolios[portfolioName].items():
                print(f"- {stock}: {shares} shares")
        else:
            print("Portfolio not found.")

# This is just a welcome message for the user to see before using my application.
def welcomeMessage(message):
    print("*" * (len(message) + 4))
    print(f"* {message} *")
    print("*" * (len(message) + 4))

def main():
    welcomeMessage("Welcome to Your Very Own Portfolio Manager Application!")
    print("coded by Modiehi Patience Malete")
    manager = MyPortfolioManagerApplication()

# Menu displayed to the user to choose their desired option(s).
    while True:
        print("\nMenu:")
        print("1. Add new portfolio")
        print("2. Add stock to portfolio")
        print("3. Buy shares")
        print("4. Sell shares")
        print("5. Deposit money")
        print("6. Withdraw money")
        print("7. Display available balance")
        print("8. Display all portfolios")
        print("9. Display specific portfolio")
        print("0. Exit")

        choice = input("Enter your desired option (0-9): ")

        if choice == '0':
            print("Exiting program...")
            break

        elif choice == '1':
            portfolioName = input("Enter portfolio name: ")
            manager.addNewPortfolio(portfolioName)

        elif choice == '2':
            portfolioName = input("Enter portfolio name: ")
            stockName = input("Enter stock name: ")
            try:
                shares = int(input("Enter number of shares: "))
                manager.addPortfolioStock(portfolioName, stockName, shares)
            except ValueError:
                print("Please enter a valid number of shares.")

        elif choice == '3':
            portfolioName = input("Enter portfolio name: ")
            stockName = input("Enter stock name: ")
            try:
                shares = int(input("Enter number of shares to buy: "))
                pricePerShare = float(input("Enter price per share: "))
                manager.buyShares(portfolioName, stockName, shares, pricePerShare)
            except ValueError:
                print("Please enter valid numeric values for shares and price per share.")

        elif choice == '4':
            portfolioName = input("Enter portfolio name: ")
            stockName = input("Enter stock name: ")
            try:
                shares = int(input("Enter number of shares to sell: "))
                pricePerShare = float(input("Enter price per share: "))
                manager.sellShares(portfolioName, stockName, shares, pricePerShare)
            except ValueError:
                print("Please enter valid numeric values for shares and price per share.")

        elif choice == '5':
            try:
                amount = float(input("Enter amount to deposit: "))
                manager.depositMoney(amount)
            except ValueError:
                print("Please enter a valid numeric amount.")

        elif choice == '6':
            try:
                amount = float(input("Enter amount to withdraw: "))
                manager.withdrawMoney(amount)
            except ValueError:
                print("Please enter a valid numeric amount.")

        elif choice == '7':
            manager.showAvailBalance()

        elif choice == '8':
            manager.showAllPortfolios()

        elif choice == '9':
            portfolioName = input("Enter portfolio name: ")
            manager.showSpecificPortfolio(portfolioName)

        else:
            print("Invalid choice. Please enter a number from 0 to 9.")
 
    
if __name__ == "__main__":
    main()

