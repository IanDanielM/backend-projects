# expense Tracker

import datetime
from typing import Any, Dict, List, Optional

from expenses.csv_helper import CSVHelper

CSV_FILE = 'expenses.csv'
CAP_FILE = 'monthly_cap.csv'
FIELDNAMES = ['description', 'amount', 'category', 'creation_date']


def parse_date(date_string: str) -> datetime.date:
    return datetime.datetime.strptime(date_string, '%Y-%m-%d').date()


def read_all_expenses() -> List[Dict[str, Any]]:
    with CSVHelper(CSV_FILE, 'r', FIELDNAMES) as csv_file:
        return csv_file.read_all()


def read_expense_by_category(category) -> List[Dict[str, Any]]:
    expenses = []
    with CSVHelper(CSV_FILE, 'r', FIELDNAMES) as csv_file:
        for row in csv_file.read_all():
            if row['category'] == category:
                expenses.append(row)

    return expenses


def get_total_monthly_expense() -> float:
    total = 0
    current_month = datetime.date.today()
    with CSVHelper(CSV_FILE, 'r', FIELDNAMES) as csv_file:
        for row in csv_file.read_all():
            expense_date = parse_date(row['creation_date'])
            if expense_date >= current_month:
                total += float(row['amount'])

    return total


def get_monthly_cap() -> Optional[float]:
    with CSVHelper(CAP_FILE, 'r', headers=['monthly_cap', 'update_date']) as csv_file:
        cap = csv_file.read_all()
        if cap:
            return cap[-1].get('monthly_cap', 0)


def set_monthly_cap(cap: float) -> str:
    with CSVHelper(CAP_FILE, 'w', headers=['monthly_cap', 'update_date']) as csv_file:
        csv_file.write_row({
            "monthly_cap": cap,
            "update_date": datetime.date.today()
        })

    return f"Monthly Budget Cap set to {cap}"


def create_expense(description: str, amount: float, category: str) -> str:
    if amount < 0:
        return "Error: Expense amount cannot be negative."
    current_total = get_total_monthly_expense()
    total = current_total + amount
    with CSVHelper(CSV_FILE, 'a', headers=FIELDNAMES) as csv_file:
        csv_file.write_row({
            "description": description,
            "amount": amount,
            "category": category,
            "creation_date": datetime.date.today()
        })
    message = f"Expense {description} added succesfully"

    monthly_cap = get_monthly_cap()
    if monthly_cap is not None:
        if total > float(monthly_cap):
            message += f"\nYou have exceeded your monthy budget cap. Current Total is: {total}"

    return message


def update_expense(row_number, description: str = None, amount: float = None) -> str:
    if amount is not None and amount < 0:
        return "Error: Expense amount cannot be negative."
    with CSVHelper(CSV_FILE, 'r+', headers=FIELDNAMES) as csv_file:
        rows = csv_file.read_all()
        if not (1 <= row_number <= len(rows)):
            return f"Error: Expense ID {row_number} does not exist."
        updated_row = {}
        if description:
            updated_row["description"] = description
        if amount:
            updated_row["amount"] = amount

        csv_file.update_row(row_number, updated_row)
    message = f"Expense Row {row_number} updated successfuly"
    if amount:
        current_total = get_total_monthly_expense()
        monthly_cap = get_monthly_cap()
        if monthly_cap is not None:
            if current_total > float(monthly_cap):
                message += f"\nYou have exceeded your monthy budget cap. Current Total is: {current_total}"

    return message


def delete_rows(row_number) -> str:
    with CSVHelper(CSV_FILE, 'r+') as csv_file:
        rows = csv_file.read_all()
        if not (1 <= row_number <= len(rows)):
            return f"Error: Expense ID {row_number} does not exist."
        csv_file.delete_row(row_number)

    return "{} deleted successfully".format(row_number)


def expenses_summary() -> str:
    expenses = read_all_expenses()
    summary = {
        "total": sum(float(expense['amount']) for expense in expenses),
        "count": len(expenses)
    }
    return "Total Expenses: {total}, Count: {count}".format(**summary)


def expenses_summary_per_month(month: int) -> str:
    total = 0
    count = 0
    with CSVHelper(CSV_FILE, 'r', FIELDNAMES) as csv_file:
        for row in csv_file.read_all():
            if parse_date(row['creation_date']).month == month:
                total += float(row['amount'])
                count += 1
    if count == 0:
        return "No expenses for the month"
    return f"Total Expenses: {total}, Count: {count}"
