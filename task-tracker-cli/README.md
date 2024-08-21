# TASK TRACKER CLI

Task Tracker CLI allows you to track your tasks directly from the terminal. You can add, delete, update, and list tasks.

## Installation

- Clone this repository to your local machine:

```bash
git clone git@github.com:IanDanielM/backend-projects.git
cd task-tracker-cli
```

There are two ways you can run this project:

### 1. Run the Python Script Directly

You can run the script directly using Python:

```bash
python3 main.py --help
```

### 2. Use it as a Command-Line Tool

If you want to run the script as a command-line tool:

1. Open your `.bashrc` (or `.zshrc` for zsh users):

```bash
nano ~/.bashrc
```

2. Add an alias for the command:

```bash
alias tasklist="python3 /path/to/your/script/main.py"
```

3. Save and reload your shell configuration:

```bash
source ~/.bashrc
```

Now, you can run the script by typing `tasklist` in the terminal:

```bash
tasklist --help
```

## Usage

You can use the following commands to interact with the Task Tracker CLI:

- `add`: Add a new task

```bash
tasklist add <description> <status>
# status is not required, default is "todo"
```

- `list`: List all tasks

```bash
tasklist list
```

- `update`: Update a task

```bash
tasklist update <id> <description>
```

- `mark`: change task status

```bash
tasklist mark <id> <status>
```

- `delete`: Delete a task

```bash
tasklist delete <id>
```

## More on Task Tracker CLI
This project has been created as part of the [Backend Projects](https://roadmap.sh/projects/task-tracker) from [roadmap.sh](https://roadmap.sh/). You can find more information on how to build this project by visiting the link.