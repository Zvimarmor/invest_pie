# Investment Portfolio Visualization Tool

## Overview

This program allows users to visualize their investment portfolios as pie charts based on predefined or custom investment policies. Users can input their name, select an investment policy from a list of predefined policies or create a custom one, and input their current investment amounts. The program then generates a pie chart displaying the distribution of investments in the portfolio according to the selected policy. Additionally, it suggests adjustments needed to align the portfolio with the selected policy.

## Features

- **Predefined Investment Policies**: The program offers a set of predefined investment policies, such as Conservative, Moderate, Aggressive, Income, Growth, and more.

- **Custom Investment Policies**: Users can create custom investment policies by specifying the percentage allocation for various investment types, including Bonds, Stocks, Real Estate, Cash, and others.

- **Investment Portfolio Management**: Users can input their current investments and receive suggestions for adjustments to match their selected policy.

- **Pie Chart Visualization**: The program generates a pie chart visualization that illustrates the distribution of investments in the portfolio according to the selected investment policy.

## Usage

### 1. Installation

- Ensure that Python is installed on your system. You can download Python from the official [Python website](https://www.python.org/).

- Clone or download the project repository to your local machine.

### 2. Running the Program

- Open a terminal or command prompt.

- Navigate to the directory where the program files are located.

- Run the `invest_user.py` file using the following command:
  
  ```
  python invest_user.py
  ```

### 3. Input Investor Details and Policy Selection

- Enter your name when prompted.

- Choose whether you want to view the available investment policies by typing 'yes' or 'no'.

- If you choose to view the available policies, a list of predefined investment policies will be displayed. Select one of the policies or enter 'Other' to create a custom policy.

- If you create a custom policy, you will be prompted to specify the percentage allocation for each investment type.

### 4. Input Current Investments

- For each investment type in the selected policy, you will be prompted to enter the amount you currently have invested in that type.

### 5. Viewing the Pie Chart

- After entering your current investments, you will be prompted to choose whether to display a pie chart of your portfolio. Type 'yes' to view the chart.

- The pie chart title will include your name and account number, along with the selected investment policy.

- The slices of the pie chart represent different investment types, and the percentage allocation for each type is displayed on the chart.

### 6. Portfolio Adjustment Suggestions

- After displaying the pie chart, the program will suggest changes needed to align your portfolio with the selected investment policy.

- If adjustments are needed, the program will list the investment types and the amounts to change.

### 7. Creating Additional Users

- You will be prompted whether to create another user. Type 'yes' to create another user or 'no' to exit the program.

- The program keeps track of the number of users created during the session.

### Example Run

1. Start the program.
2. Enter your name.
3. Choose to view available investment policies.
4. Select a predefined policy or create a custom one.
5. Enter your current investment amounts.
6. View the pie chart of your portfolio.
7. Review and apply the suggested adjustments.
8. Create additional users if needed.
9. Exit the program when done.

## Dependencies

- This program relies on the `matplotlib` library for generating pie chart visualizations. Ensure that `matplotlib` is installed on your system. You can install it using pip:

  ```
  pip install matplotlib
  ```

## File Structure

- `invest_user.py`: Main program file to run the user input and portfolio visualization process.
- `investment_policies.py`: Contains definitions of various investment policies.
- `invest_showing.py`: Contains classes and functions related to investment portfolios and their visualization.