import argparse as ar

from expenses import expense_funcs


def main():
    parser = ar.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Get all expenses
    get_expenses_parser = subparsers.add_parser("list", help="List all expenses")

    # Get expenses by category
    get_expenses_by_category_parser = subparsers.add_parser("list_category", help="List all expenses by category")
    get_expenses_by_category_parser.add_argument("category", help="Category name")

    # add expenses
    add_expense_parser = subparsers.add_parser("add", help="Add a new expense")
    add_expense_parser.add_argument("--description", help="Expense description")
    add_expense_parser.add_argument("--amount", type=float, help="Expense amount")
    add_expense_parser.add_argument("--category", help="Expense category")

    # update expenses
    update_expense_parser = subparsers.add_parser(
        "update", help="Update an expense")
    update_expense_parser.add_argument("--id", type=int, help="Expense ID")
    update_expense_parser.add_argument("--description", help="Expense description")
    update_expense_parser.add_argument("--amount", type=float, help="Expense amount")

    # delete expenses
    delete_expense_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_expense_parser.add_argument("--id", type=int, help="Expense ID")

    # total_summary_expenses
    total_summary_parser = subparsers.add_parser("total_summary", help="Total summary of expenses")

    # total_summary_expenses_per_month
    total_summary_per_month_parser = subparsers.add_parser("summary_per_month", help="Total summary of expenses per month")
    total_summary_per_month_parser.add_argument("--month", type=int, help="Month number")

    # set_monthly_cap
    set_monthly_cap_parser = subparsers.add_parser("set_monthly_cap", help="Set monthly budget cap")
    set_monthly_cap_parser.add_argument("--amount", type=float, help="Monthly budget cap")

    args = parser.parse_args()

    if args.command == "list":
        expenses = expense_funcs.read_all_expenses()
        id = 0
        for expense in expenses:
            id += 1
            print(f"ID: {id}, Description: {expense['description']}, Amount: {expense['amount']}, Category: {expense['category']}")
    elif args.command == "list_category":
        expenses = expense_funcs.read_expense_by_category(args.category)
        id = 0
        for expense in expenses:
            id += 1
            print(f"ID: {id}, Description: {expense['description']}, Amount: {expense['amount']}, Category: {expense['category']}")
    elif args.command == "add":
        message = expense_funcs.create_expense(args.description, args.amount, args.category)
        print(message)
    elif args.command == "update":
        message = expense_funcs.update_expense(
            args.id, args.description, args.amount)
        print(message)
    elif args.command == "delete":
        message = expense_funcs.delete_rows(args.id)
        print(message)
    elif args.command == "total_summary":
        message = expense_funcs.expenses_summary()
        print(message)
    elif args.command == "summary_per_month":
        message = expense_funcs.expenses_summary_per_month(args.month)
        print(message)
    elif args.command == "set_monthly_cap":
        message = expense_funcs.set_monthly_cap(args.amount)
        print(message)
    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
