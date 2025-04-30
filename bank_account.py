import sqlite3


class BankAccount:
    def __init__(self, user_id):
        self.user_id = user_id
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS UserAccounts (
                user_id TEXT PRIMARY KEY,
                balance REAL DEFAULT 0.0
            )
            ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                transaction_type TEXT,
                amount REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            ''')
        self.conn.commit()

    def create_account(self):
        self.cursor.execute('''INSERT OR IGNORE INTO UserAccounts (user_id, balance) VALUES (?, ?)''', (self.user_id, 0.0))
        self.conn.commit()

    def get_balance(self):
        self.cursor.execute('''SELECT user_id, balance FROM UserAccounts WHERE user_id = ?''', (self.user_id,))
        result = self.cursor.fetchone()
        if result[1] is None:
            print ('Balance not found. Account is empty.')
            return
        print (f'\nAccount Balance: ${result[1]:.2f}')

    def take_deposit(self, amount):
        self.cursor.execute('''INSERT INTO Transactions (user_id, transaction_type, amount) VALUES (?, "Deposit", ?)''', (self.user_id, amount,))
        self.cursor.execute('''SELECT user_id, balance FROM UserAccounts WHERE user_id = ?''', (self.user_id,))
        result = self.cursor.fetchone()
        if result[0] is None:
            print ('Account error. Please contact customer service for further inspection')
            return
        current_balance = result[1]
        new_balance = current_balance + amount
        self.cursor.execute('''UPDATE UserAccounts SET balance = ? WHERE user_id = ?''', (new_balance, self.user_id,))
        self.conn.commit()
        print (f'\nDeposit Succesful. New Balance: ${new_balance:.2f}')    


    def pull_withdrawl(self, amount):
        self.cursor.execute('''INSERT INTO Transactions (user_id, transaction_type, amount) VALUES (?, "Withdrawl", ?)''', (self.user_id, amount,))
        self.cursor.execute('''SELECT user_id, balance FROM UserAccounts WHERE user_id = ?''', (self.user_id,))
        result = self.cursor.fetchone()
        if amount > result[1]:
            print (f'\nInsuffecient funds. Account Balance: ${result[1]} ')
            return
        else:
            current_balance = result[1]
            new_balance = current_balance - amount
            self.cursor.execute('''UPDATE UserAccounts SET balance = ? WHERE user_id = ?''', (new_balance, self.user_id,))
            self.conn.commit()
            print (f'\nWithdrawl Succesful. New Balance: ${new_balance:.2f}')    


    def del_account(self):
        self.cursor.execute('''DELETE FROM UserAccounts WHERE user_id = ?''',(self.user_id,))
        self.conn.commit()