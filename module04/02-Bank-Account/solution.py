"""Solution of module 4.1 - A Bank Account"""
class BankAccount:
    """Bank account class"""
    def __init__(self, name, balance, currency):
        if balance < 0:
            raise ValueError("The balance should be positive.")
        if currency == "":
            raise ValueError("The currency may not be ambiguous.")
        self.name = name
        self.bal = balance
        self.currency = currency
        self.hist = ['Account was created']

    def __int__(self):
        self.hist.append('__int__ check -> {}{}'.format(self.bal, self.currency))
        return int(self.bal)

    def __str__(self):
        return "Bank account for {0} with balance of {1:d}{2}"\
            .format(self.name, self.bal, self.currency)

    def deposit(self, amount, log=True):
        """Make a deposit"""
        if amount < 0:
            raise ValueError("The deposit should be positive.")
        self.bal += amount
        if log:
            self.hist.append('Deposited {}{}'.format(amount, self.currency))

    def balance(self):
        """Return account balance"""
        self.hist.append('Balance check -> {}{}'.format(self.bal, self.currency))
        return self.bal

    def withdraw(self, amount, log=True):
        """Withdraw money from the account"""
        if self.bal - amount < 0:
            self.hist.append('Withdraw for {}{} failed'.format(amount, self.currency))
            return False
        self.bal -= amount
        if log:
            self.hist.append('{}{} was withdrawn'.format(amount, self.currency))
        return True

    def history(self):
        """Return account history"""
        return self.hist

    def transfer_to(self, account, amount):
        """Transfer money to another account"""
        if amount < 0:
            raise ValueError("The amount should be positive.")
        if self.currency != account.currency:
            raise TypeError("The currency should match.")
        if not self.withdraw(amount, False):
            raise ValueError("Insufficient funds.")
        account.deposit(amount, False)
        self.hist.append('Transfer to {} for {}{}'.format(account.name, amount, self.currency))
        account.hist.append('Transfer from {} for {}{}'.format(self.name, amount, self.currency))
        return True
