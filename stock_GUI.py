# Summary: This module contains the user interface and logic for a graphical user interface version of the stock manager program.
# Author: 
# Date: 

from datetime import datetime
from os import path
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, simpledialog, filedialog
import csv
import stock_data
from stock_class import Stock, DailyData
from utilities import clear_screen, display_stock_chart, sortStocks, sortDailyData

class StockApp:
    def __init__(self):
        self.stock_list = []
        #check for database, create if not exists
        if path.exists("stocks.db") == False:
            stock_data.create_database()

 # This section creates the user interface

        # Create Window
        self.root = Tk()
        self.root.title("(myname) Stock Manager") #Replace with a suitable name for your program


        # Add Menubar
        self.menubar = Menu(self.root)

        # Add File Menu
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label = "Load Data",command = self.load)
        self.filemenu.add_command(label = "Save Data",command = self.save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command = self.root.quit)
        self.menubar.add_cascade(label="File",menu=self.filemenu)

        # Add Web Menu 
        self.webmenu = Menu(self.menubar, tearoff=0)
        self.webmenu.add_command(label = "Scrape Data from Yahoo! Finance...", command=self.scrape_web_data)
        self.webmenu.add_command(label = "Import CSV from Yahoo! Finance...", command=self.importCSV_web_data)
        self.menubar.add_cascade(label="Web",menu=self.webmenu)

        # Add Chart Menu
        self.chartmenu = Menu(self.menubar,tearoff=0)
        self.chartmenu.add_command(label="Display Stock Chart", command=self.display_chart)
        self.menubar.add_cascade(label="Chart",menu=self.chartmenu)

        # Add menus to window       
        self.root.config(menu=self.menubar)

        # Add heading information
        self.headingLabel = Label(self.root,text="No Stock Selected")
        self.headingLabel.grid(column=0,row=0,columnspan=3,padx = 5, pady = 10)
        

        # Add stock list
        self.stockLabel = Label(self.root,text="Stocks")
        self.stockLabel.grid(column=0,row=1,padx = 5, pady = 10,sticky=(N))

        self.stockList = Listbox(self.root)
        self.stockList.grid(column=0,row=2,padx = 5, pady = 5,sticky=(N,S))
        self.stockList.bind('<<ListboxSelect>>',self.update_data)
        
        
        # Add Tabs
        self.notebook = ttk.Notebook(self.root,padding="5 5 5 5")
        self.notebook.grid(column=2,row=2,sticky=(N,W,E,S))
        self.mainFrame = ttk.Frame(self.notebook)
        self.stockDataFrame = ttk.Frame(self.notebook)
        self.reportFrame = ttk.Frame(self.notebook)
        self.notebook.add(self.mainFrame,text='Manage')
        self.notebook.add(self.stockDataFrame,text='History')
        self.notebook.add(self.reportFrame,text = 'Report')
        

        # Set Up Main Tab
        self.addStockGroup = LabelFrame(self.mainFrame,text="Add Stock",padx=5,pady=5)
        self.addStockGroup.grid(column=0,row=0,padx=5,pady=5,sticky=(W,E))

        self.addSymbolLabel = Label(self.addStockGroup,text = "Symbol")
        self.addSymbolLabel.grid(column=0,row=0,padx = 5, pady = 5,sticky=(W))
        self.addSymbolEntry = Entry(self.addStockGroup)
        self.addSymbolEntry.grid(column=1,row=0,padx=5,pady=5)

        self.addNameLabel = Label(self.addStockGroup,text = "Name")
        self.addNameLabel.grid(column=0,row=1,padx = 5, pady = 5,sticky=(W))
        self.addNameEntry = Entry(self.addStockGroup)
        self.addNameEntry.grid(column=1,row=1,padx=5,pady=5)

        self.addSharesLabel = Label(self.addStockGroup,text = "Shares")
        self.addSharesLabel.grid(column=0,row=2,padx = 5, pady = 5,sticky=(W))
        self.addSharesEntry = Entry(self.addStockGroup)
        self.addSharesEntry.grid(column=1,row=2,padx=5,pady=5)

        self.addStockButton = Button(self.addStockGroup,text = "New Stock",command=self.add_stock)
        self.addStockButton.grid(column=0,row=3,columnspan = 2, padx = 5, pady = 5)

        self.transactionGroup = LabelFrame(self.mainFrame,text="Update Shares",padx=5,pady=5)
        self.transactionGroup.grid(column=0,row=1,padx=5,pady=5,sticky=(W,E))
        self.updateSharesLabel = Label(self.transactionGroup,text = "Shares")
        self.updateSharesLabel.grid(column=0,row=0,padx = 5, pady = 5,sticky=(W))
        self.updateSharesEntry = Entry(self.transactionGroup)
        self.updateSharesEntry.grid(column=1,row=0,columnspan=2, padx=5,pady=5)

        self.buyStockButton = Button(self.transactionGroup,text = "Buy Selected Stock",command=self.buy_shares)
        self.buyStockButton.grid(column=1,row=1, padx = 5, pady = 5)
        self.sellStockButton = Button(self.transactionGroup,text = "Sell Selected Stock",command=self.sell_shares)
        self.sellStockButton.grid(column=2,row=1, padx = 5, pady = 5)

        self.deleteGroup = LabelFrame(self.mainFrame,text="Delete Stock",padx=5,pady=5)
        self.deleteGroup.grid(column=0,row=2,padx=5,pady=5,sticky=(W,E))

        self.deleteStockButton = Button(self.deleteGroup,text="Delete Selected Stock",command=self.delete_stock)
        self.deleteStockButton.grid(column=0,row=0,padx=5,pady=5)


        # Setup History Tab
        self.dailyDataList = Text(self.stockDataFrame,width=40)
        self.dailyDataList.grid(column=0,row=0,padx = 5, pady = 5)
        
        
        # Setup Report Tab
        self.stockReport = Text(self.reportFrame,width=40)
        self.stockReport.grid(column=0,row=0,padx=5,pady=5)

        self.root.mainloop()

# This section provides the functionality
       
    # Load stocks and history from database.
    def load(self):
        messagebox.showinfo("Under Construction","This Module Not Yet Implemented")

    # Save stocks and history to database.
    def save(self):
        messagebox.showinfo("Under Construction","This Module Not Yet Implemented")

    # Refresh history and report tabs
    def update_data(self, evt):
        self.display_stock_data()

    # Display stock price and volume history.
    def display_stock_data(self):
        messagebox.showinfo("Under Construction","This Module Not Yet Implemented")
    
    # Add new stock to track.
    def add_stock(self):
        messagebox.showinfo("Under Construction","This Module Not Yet Implemented")

    # Buy shares of stock.
    def buy_shares(self):
        messagebox.showinfo("Under Construction","This Module Not Yet Implemented")

    # Sell shares of stock.
    def sell_shares(self):
        messagebox.showinfo("Under Construction","This Module Not Yet Implemented")

    # Remove stock and all history from being tracked.
    def delete_stock(self):
        messagebox.showinfo("Under Construction","This Module Not Yet Implemented")

    # Get data from web scraping.
    def scrape_web_data(self):
        messagebox.showinfo("Under Construction","This Module Not Yet Implemented")

    # Import CSV stock history file.
    def importCSV_web_data(self):
        messagebox.showinfo("Under Construction","This Module Not Yet Implemented")  
    
    # Display stock price chart.
    def display_chart(self):
        messagebox.showinfo("Under Construction","This Module Not Yet Implemented")


def main():
        app = StockApp()
        

if __name__ == "__main__":
    # execute only if run as a script
    main()
