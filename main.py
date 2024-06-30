from modules.financial_advisor import FinancialAdvisor

def main():
    print("Welcome to FinOptimize - Personal Finance Advisor")

    # Initialize financial advisor
    advisor = FinancialAdvisor()

    # Example interaction loop (can be expanded)
    while True:
        print("\nOptions:")
        print("1. Update Budget")
        print("2. Add Expense")
        print("3. Evaluate Investment")
        print("4. View Current Budget")
        print("5. View Total Expenses")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            amount = float(input("Enter amount to update budget: "))
            advisor.handle_budget_update(amount)
            print(f"Budget updated. Current budget: ${advisor.get_current_budget()}")

        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            advisor.add_expense(amount)
            print(f"Expense added. Total expenses: ${advisor.get_total_expenses()}")

        elif choice == "3":
            investment = float(input("Enter investment amount: "))
            evaluated_amount = advisor.evaluate_investment(investment)
            print(f"Investment evaluated. Expected return: ${evaluated_amount}")

        elif choice == "4":
            print(f"Current budget: ${advisor.get_current_budget()}")

        elif choice == "5":
            print(f"Total expenses: ${advisor.get_total_expenses()}")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
