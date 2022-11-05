class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        title = "{:*^30s}".format(self.name) + '\n'
        item = ""

        total_balance = 0
        for i in self.ledger:
            total_balance += i['amount']

        for i in self.ledger:
            item += '{0:23}'.format(i['description'][:23]) + '{:>7}'.format('{:.2f}'.format(float(i['amount']))) + '\n'

        return title + item + "Total: " + str(total_balance)

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        total_balance = 0
        for i in self.ledger:
            total_balance += i['amount']
        return total_balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def cat_with(self):
        cat_with = 0
        for i in self.ledger:
            if i['amount'] < 0:
                cat_with += i['amount']
        return -cat_with


def create_spend_chart(categories):
    spending = 0
    total = 0
    percentage = []
    for c in categories:
        spending = c.cat_with()
        total += spending
    maxlen = 0
    cat_names = []
    for c in categories:
        spending = c.cat_with()
        percentage.append(spending * 100 / total)
        cat_names.append(c.name)

    graph = ""

    for count in range(100, -10, -10):
        s = '{:>5}'.format(str(count) + "|" + " ")
        for i in percentage:
            if i >= count:
                s += "o  "
            else:
                s += "   "
        graph += s + '\n'

    lines = '{:>14}'.format("-" * (len(categories) * 3 + 1))
    names = "     "
    maxlen = max([len(w) for w in cat_names])

    for x in range(maxlen):
        for w in categories:
            try:
                names += w.name[x] + "  "
            except IndexError:
                names += " " + "  "
        names += "\n" + "     "

    names = names.rstrip()
  

    return "Percentage spent by category"'\n' + graph + lines + '\n' + names + "  "