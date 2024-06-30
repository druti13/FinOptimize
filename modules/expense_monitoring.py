class ExpenseMonitor:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount):
        self.expenses.append(amount)

    def get_total_expenses(self):
        return sum(self.expenses)
