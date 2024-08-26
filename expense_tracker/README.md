# EXPENSE TRACKER CLI

This is a simple CLI application that allows you to track your expenses. You can add, list, update, and delete expenses using this tool.

## Installation

- Clone this repository to your local machine:

```bash
git clone git@github.com:IanDanielM/backend-projects.git
cd expense_tracker
```

There are two ways you can run this project:

### 1. Run the Python Script Directly

You can run the script directly using Python:

```bash
python3 main.py --help
```

### 2. Use it as a Command-Line Tool

If you want to run the script as a command-line tool:

1. Open your `.bashrc`:

```bash
nano ~/.bashrc
```

2. Add an alias for the command:

```bash
alias expense-tracker="python3 /path/to/your/script/main.py"
```

3. Save and reload your shell configuration:

```bash
source ~/.bashrc
```

Now, you can run the script by typing `expense-tracker` in the terminal:

```bash
expense-tracker --help
```

## Usage

You can use the following commands to interact with the Expense Tracker CLI:

- `add`: Add a new expense

```bash
expense-tracker add --description "Rent" --amount 30 --category "essentials"
```

- `list`: List all expenses

```bash
expense-tracker list
```

- `update`: Update an expense

```bash
expense-tracker update --id 1 --description "Groceries" --amount 20
```

- `expenses summary`: Get a summary of all expenses

```bash
expense-tracker total_summary
```

- `expenses summary by month`: Get a summary of all expenses by month

```bash
expense-tracker summary_per_month --month 8
```

- `Set Budget`: Set a budget for a month

```bash
expense-tracker set_monthly_cap --amount 10000
```

- `delete`: Delete an expense

```bash
expense-tracker delete 1
```

## More on Expense Tracker CLI
This project has been created as part of the [Backend Projects](https://roadmap.sh/projects/expense-tracker) from [roadmap.sh](https://roadmap.sh/). You can find more information on how to build this project by visiting the link.
