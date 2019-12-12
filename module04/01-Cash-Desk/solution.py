"""Solution of module 4.1 - The Cash Desk problem"""
class Bill:
    """Bill class"""
    def __init__(self, amount):
        if not isinstance(amount, int):
            raise TypeError("The amount should be integer.")
        if amount < 0:
            raise ValueError("The amount should be positive or zero.")
        self.amount = amount

    def __int__(self):
        return self.amount

    def __repr__(self):
        return "A {:d}$ bill".format(self.amount)

    def __dir__(self):
        return self.__repr__()

    def __eq__(self, other):
        return int(self) == int(other)

    def __hash__(self):
        return hash(self.amount)

class BatchBill:
    """Implement list of Bill classes"""
    def __init__(self, bills):
        self.bills = []
        self.bills += bills

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, index):
        return self.bills[index]

    def total(self):
        """Return total amount of money for the batch"""
        summ = 0
        for i in self.bills:
            summ += int(i)
        return summ


class CashDesk:
    """Manage Bill and BatchBill instances"""
    def __init__(self):
        self.money = {}

    def _addmoney(self, key, value):
        if key in self.money:
            self.money[key] += value
        else:
            self.money[key] = value

    def take_money(self, money):
        """Put money in the desk"""
        if isinstance(money, Bill):
            self._addmoney(int(money), 1)
            return
        for bill in money:
            self._addmoney(int(bill), 1)

    def total(self):
        """Return the total money in the desk"""
        summ = 0
        for key, value in self.money.items():
            summ += key * value
        return summ

    def inspect(self):
        """Perform desk inspection"""
        inspection = "We have a total of {:d}$ in the desk\n".format(self.total())
        inspection += "We have the following count of bills, sorted in ascending order:"
        for i in sorted(self.money.keys()):
            inspection += "\n{:d}$ bills - {:d}".format(i, self.money[i])
        return inspection
