class BudgetManager:
    def __init__(self, initial_budget):
        self.budget = initial_budget

    def update_budget(self, amount):
        self.budget += amount

    def get_budget(self):
        return self.budget
