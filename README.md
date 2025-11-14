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
### Example spreadsheet
![example spreadsheet](https://github.com/user-attachments/assets/b2a595a7-a3a7-49bc-80f4-181b190e7986)

### Example of run dialog box usage 
![example of command line usage](https://github.com/user-attachments/assets/8a89868f-38d3-46d8-a38a-1b6e487b6ffa)

### Content of the terminal after choosing "help"
![content of the terminal after choosing "help"](https://github.com/user-attachments/assets/289c4daa-836b-450d-9be9-1a4f1e220cfc)

### Content of the table "items" in the database
![content of the table "items" in the database](https://github.com/user-attachments/assets/a28cff80-f8ec-4ab7-b2b0-81254cd06ec3)

### Content of the table "sync_log" in the database
![content of the table "sync_log" in the database](https://github.com/user-attachments/assets/33ba3316-3136-4280-b989-9af6a9a3bdfa)

### Content of the terminal after choosing "summary"
![content of the terminal after choosing summary](https://github.com/user-attachments/assets/937a69b6-e4cd-45a1-a811-1430aa47e8ad)

## Tech Stack
- Python 3.13
- Standard library: sys, sqlite3, os, datetime
- Third-party libraries: ezsheets, bext

## License
MIT
