# GITHUB USER ACTIVITY

Github User Activity is a command-line tool that allows you to get the activity of a user on Github. You can get the type of different events that a user has performed on Github, such as creating a repository, opening an issue, etc.

## Installation

- Clone this repository to your local machine:

```bash
git clone git@github.com:IanDanielM/backend-projects.git
cd github-user-activity
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
alias github-activity="python3 /path/to/your/script/main.py"
```

3. Save and reload your shell configuration:

```bash
source ~/.bashrc
```

Now, you can run the script by typing `github-activity` in the terminal:

```bash
github-activity --help
```

## Usage

You can use the following command to interact with the github cli:

- `get`: Get the activity of a user on Github

```bash
github-activity get <username>
```

## More on this Project

This project has been created as part of the [Backend Projects](https://roadmap.sh/projects/github-user-activity) from [roadmap.sh](https://roadmap.sh/). You can find more information on how to build this project by visiting the link.
