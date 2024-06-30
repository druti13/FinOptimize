from .budgeting import BudgetManager
from .expense_monitoring import ExpenseMonitor
from .investment_evaluation import InvestmentEvaluator

class FinancialAdvisor:
    def __init__(self):
        self.budget_manager = BudgetManager(10000)  # Initial budget of $10,000
        self.expense_monitor = ExpenseMonitor()
        self.investment_evaluator = InvestmentEvaluator()

    def handle_budget_update(self, amount):
        self.budget_manager.update_budget(amount)

    def add_expense(self, amount):
        self.expense_monitor.add_expense(amount)

    def evaluate_investment(self, investment):
        return self.investment_evaluator.evaluate_investment(investment)

    def get_current_budget(self):
        return self.budget_manager.get_budget()

    def get_total_expenses(self):
        return self.expense_monitor.get_total_expenses()
