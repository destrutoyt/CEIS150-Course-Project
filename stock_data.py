# Summary: This module contains the functions used by both console and GUI programs to manage stock data.
# Author: 
# Date: 

import sqlite3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import csv
import time
from datetime import datetime
from utilities import clear_screen
from utilities import sortDailyData
from stock_class import Stock, DailyData

# Create the SQLite database
def create_database():
    pass #Replace with code to create database

# Save stocks and daily data into database
def save_stock_data(stock_list):
    clear_screen()
    print("*** This Module Under Construction ***")
    _ = input("*** Press Enter to Continue ***")
    
# Load stocks and daily data from database
def load_stock_data(stock_list):
    clear_screen()
    print("*** This Module Under Construction ***")
    _ = input("*** Press Enter to Continue ***")

# Get stock price history from web using Web Scraping
def retrieve_stock_web(dateStart,dateEnd,stock_list):
    clear_screen()
    print("*** This Module Under Construction ***")
    _ = input("*** Press Enter to Continue ***")

# Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_web_csv(stock_list,symbol,filename):
    clear_screen()
    print("*** This Module Under Construction ***")
    _ = input("*** Press Enter to Continue ***")

def main():
    clear_screen()
    print("This module will handle data storage and retrieval.")

if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()
