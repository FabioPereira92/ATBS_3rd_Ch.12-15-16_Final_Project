# Sheet Sync
A command line program that lets the user sync data between a Google Sheet and a local SQLite database.

## Features
- init-db - Initializes the database.
- pull - Updates the database with the contents of the spreadsheet.
- push - Updates the spreadsheet with the contents of the database.
- summary - Prints a summary to the console.
- help - Prints a description of what each command does.
  
## How to run
1. Clone this repository or download the file `sheetSync.py`.
2. Run in terminal.

## Example Usage
### Example text file
![example text file](https://github.com/user-attachments/assets/f3da1ce2-baff-4509-b215-aa665d01a0c3)
### Content of one of the scanned URLs 
![content of one of the scanned URLs](https://github.com/user-attachments/assets/893c6af2-e7f1-4063-8c25-00467a5c924b)
### Content of the generated priceTrackerFolder
![content of the generated priceTrackerFolder](https://github.com/user-attachments/assets/a2fff273-ecb5-4022-9781-851f8373eb47)
### Content of one of the sheets of the generated excel file
![content of one of the sheets of the generated excel file](https://github.com/user-attachments/assets/41f180ef-add3-4eef-a398-5e2e0a893da4)
### Content of the generated logsTracker1 file
![content of the generated logsTracker1 file](https://github.com/user-attachments/assets/641cae06-de29-475c-9cdd-0d2a0ae4db3b)
### Final summary in the console
![final summary in the console](https://github.com/user-attachments/assets/6de2bcfb-6015-4377-bf07-02e2145a4ebe)

## Tech Stack
- Python 3.13
- Standard library only (sys, ezsheets, sqlite3, os, bext, datetime)

## License
MIT
