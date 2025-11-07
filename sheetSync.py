#! python3
"""sheetSync.py - A command line program that lets the user sync data between a Google
Sheet and a local SQLite database"""

import sys, ezsheets, sqlite3, os, bext
from datetime import datetime

spreadsheetID = '1Dzel5arVld2v7jCNCUoXWKkG9LyBGGEG4lKOVyB3LKo'
databaseName = 'data.db'

def inexistentDB():
    """This helper function is called if the database hasn't been created yet to show the
user how to initialize the database and terminate the program"""
    print('The Database hasn\'t been created yet.')
    print('Usage: python sheetSync.py [init-db]')
    sys.exit()    

def init_db():
    """This function initializes the database with both the items and sync_log tables"""
    conn = sqlite3.connect(databaseName, isolation_level=None)
    conn.execute('CREATE TABLE IF NOT EXISTS items (item_Name TEXT, quantity INTEGER,' +
                 ' price_€ REAL, in_stock TEXT, last_updated TEXT) STRICT')
    conn.execute('CREATE TABLE sync_log (timestamp TEXT, direction TEXT, row_count' +
                 ' INTEGER) STRICT')

def pull_db():
    """This function updates the database items table with the contents of the spreadsheet
and adds a line to the sync_log table"""
    if os.path.exists(databaseName):
        ss = ezsheets.Spreadsheet(spreadsheetID)      
        sheet = ss.sheets[0]
        conn = sqlite3.connect(databaseName, isolation_level=None)
        conn.execute('DELETE FROM items')
        rowCounter = 0
        sheetRows = sheet.getRows()
        for row in range(1, len(sheetRows)):
            conn.execute('INSERT INTO items VALUES (?, ?, ?, ?, ?)', sheetRows[row][1:])
            rowCounter += 1
        syncList = [str(datetime.now()), 'pull', rowCounter]
        conn.execute(f'INSERT INTO sync_log VALUES (?, ?, ?)', syncList)     
    else:
        inexistentDB()      

def push_db():
    """This function updates the spreadsheet with the contents of the database items table
and adds a line to the sync_log table"""
    if os.path.exists(databaseName):
        ss = ezsheets.Spreadsheet(spreadsheetID)
        ss.sheets[0].clear()
        sheet = ss.sheets[0]
        sheet.updateRow(1, ['ID', 'Item Name', 'Quantity', 'Price (€)', 'In Stock',
                            'Last Updated'])
        conn = sqlite3.connect(databaseName, isolation_level=None)
        rowCounter = 0
        itemsRows = conn.execute('SELECT rowid, * FROM items').fetchall()
        for row in range(len(itemsRows)):
            sheet.updateRow(row + 2, itemsRows[row])
            rowCounter += 1            
        syncList = [str(datetime.now()), 'push', rowCounter]
        conn.execute(f'INSERT INTO sync_log VALUES (?, ?, ?)', syncList)     
    else:
        inexistentDB()       

def summary():
    """This function prints to the console a summary of how many records the database items
table has and the timestamp and direction of the last sync"""
    if os.path.exists(databaseName):
        conn = sqlite3.connect(databaseName, isolation_level=None)
        sync_logRows = conn.execute('SELECT * FROM sync_log').fetchall()
        if sync_logRows != []:
            rowCount = len(conn.execute('SELECT * FROM items').fetchall())
            syncCount = len(sync_logRows)
            pulls = conn.execute('SELECT * FROM sync_log WHERE direction' +
                                 ' = "pull"').fetchall()
            pushes = conn.execute('SELECT * FROM sync_log WHERE direction' +
                                 ' = "push"').fetchall()       
            bext.fg('red')
            bext.bg('yellow')
            print(f'Database: {rowCount} records in table items')
            print(f'Total number of syncs: {syncCount}')
            if pulls != []:
                lastPullTime = pulls[-1][0]
                print(f'Last pull time: {lastPullTime}')
            else:
                print('There haven\'t been any pulls yet')
            if pushes != []:
                lastPushTime = pushes[-1][0]
                print(f'Last push time: {lastPushTime}')
            else:
                print('There haven\'t been any pushs yet')
            bext.fg('reset')
            bext.bg('reset')
        else:
            print('No sync has been performed yet.')
            sys.exit()
    else:
        inexistentDB()

def helper():
    """This function prints to the console a description of what each command does"""
    print('init-db - Initializes the database')
    print('pull - Updates the database with the contents of the spreadsheet')
    print('push - Updates the spreadsheet with the contents of the database')
    print('summary - Prints a summary of the last sync to the console')
    
def main():
    """This function is the main function of the program and calls the other fucntions based
on what the user types in the command line"""
    if len(sys.argv) == 2:
        if sys.argv[1].lower() == 'init-db':
            init_db()
            sys.exit()
        elif sys.argv[1].lower() == 'pull':
            pull_db()
            sys.exit()
        elif sys.argv[1].lower() == 'push':
            push_db()
            sys.exit()
        elif sys.argv[1].lower() == 'summary':
            summary()
            sys.exit()
        elif sys.argv[1].lower() == 'help':
            helper()
            sys.exit()            
    print('Usage: python sheetSync.py [init-db|pull|push|summary|help]')
    sys.exit()
        
main()
