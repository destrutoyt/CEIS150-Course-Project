# Summary: This module contains helper functions used by the stock manager program.
# Author: 
# Date: 

import matplotlib.pyplot as plt

from os import system, name

# Function to Clear the Screen
def clear_screen():
    if name == "nt": # User is running Windows
        _ = system('cls')
    else: # User is running Linux or Mac
        _ = system('clear')

# Function to sort the stock list (alphabetical)
def sortStocks(stock_list):
    stock_list.sort(key=lambda s: s.symbol)


# Function to sort the daily stock data (oldest to newest) for all stocks
def sortDailyData(stock_list):
    for stock in stock_list:
        stock.DataList.sort(key=lambda s: s.date)

# Function to create stock chart
def display_stock_chart(stock_list,symbol):
    clear_screen()
    print("*** This Module Under Construction ***")
    _ = input("*** Press Enter to Continue ***")
