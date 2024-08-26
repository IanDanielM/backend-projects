# expense Tracker

# Users can add an expense with a description and amount.
# Users can update an expense.
# Users can delete an expense.
# Users can view all expenses.
# Users can view a summary of all expenses.
# Users can view a summary of expenses for a specific month (of current year).

import csv
import os

CSV_FILE = 'expenses.csv'


# create  function to help with csv operations
def csv_handler(operation, data=None):
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, operation, newline='') as csvfile:
            writer = csv.writer(csvfile)
            if operation == 'r':
                return list(csv.reader(csvfile))
            elif operation == 'a':
                writer.writerow(data)
    else:
        with open(CSV_FILE, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Description', 'Amount', 'Date'])


def read_expenses():
    return csv_handler('r')


def add_expense(description, amount, date):
    expenses = read_expenses()
    if expenses:
        id = int(expenses[-1][0]) + 1
    else:
        id = 1
    csv_handler('a', [id, description, amount, date])
    return f'Expense added successfully with ID: {id}'

def update_expense(id, description, amount, date):
    expenses = read_expenses()
    for expense in expenses:
        if expense[0] == id:
