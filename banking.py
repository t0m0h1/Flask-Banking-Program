class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            raise ValueError("Account already exists.")
        self.accounts[account_number] = initial_balance


    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.accounts[account_number] += amount


    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.accounts[account_number] < amount:
            raise ValueError("Insufficient funds.")
        self.accounts[account_number] -= amount


    def get_balance(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist.")
        return self.accounts[account_number]
    
    def transfer(self, from_account, to_account, amount):
        if from_account not in self.accounts or to_account not in self.accounts:
            raise ValueError("One or both accounts do not exist.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if self.accounts[from_account] < amount:
            raise ValueError("Insufficient funds for transfer.")
        
        self.withdraw(from_account, amount)
        self.deposit(to_account, amount)


    def get_all_accounts(self):
        return self.accounts.copy()
    
    def delete_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist. Please check the account number.")
        del self.accounts[account_number]