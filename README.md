Welcome to My Portfolio Manager Application! 

As a 2nd-year robotics student, I created this Python application to help manage multiple stock portfolios for my college assignment which I recieved full marks for.

This tool allows users to add and manage multiple portfolios, track stock options within each portfolio, and handle financial transactions efficiently. 
Below is an overview of the application features and their descriptions.

Features:
This application includes a class with methods to handle the following tasks:

Add New Portfolio: Adds a new portfolio to the catalogue. If the name already exists, the user will be asked for a different one.

Add Stock to Portfolio: Adds a new stock to the specified portfolio. An error message will appear when the portfolio isn't found.

Buy Shares: Adds shares to an existing stock option and displays an error message if the stock/portfolio isn't found. Ensures sufficient funds before purchase.

Sell Shares: Enables users to sell shares from an existing option. Appropriate error messages will pop up to guide the user.

Deposit Money: Allows the user to deposit money and add to their available balance.

Withdraw Money: Allows the user to withdraw from their available balance. Ensures sufficient balance before withdrawal.

Display Available Balance: Allows the user to view their balance.

Display All Portfolios: Allows the user to view all their existing portfolios. An error message appears if no portfolios are found.

Display Specific Portfolio: Allows the user to view their specified portfolio, if it exists.

The class constructor initializes the collection of portfolios and sets the available balance to R10,000.

User Interaction:
A user-friendly menu helps navigate the application, and a sentinel loop ensures the menu is displayed until the user decides to close the program.