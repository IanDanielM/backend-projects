# Number Guessing Game

Number Guessing Game is a command-line tool that allows you to play a number guessing game. The game generates a random number between 1 and 100, and you have to guess the number. The game will tell you if your guess is too high or too low.

## Installation

- Clone this repository to your local machine:

```bash
git clone git@github.com:IanDanielM/backend-projects.git
cd number-guessing-game
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
alias play-game="python3 /path/to/your/script/main.py"
```

3. Save and reload your shell configuration:

```bash
source ~/.bashrc
```

Now, you can run the script by typing `play-game` in the terminal:

```bash
play-game --help
```

## Usage

You can use the following command to interact with the game cli:

- `play`: Start the game.

```bash
play-game play
```

## More on this Project

This project has been created as part of the [Backend Projects](https://roadmap.sh/projects/number-guessing-game) from [roadmap.sh](https://roadmap.sh/). You can find more information on how to build this project by visiting the [link](https://roadmap.sh/projects/number-guessing-game).
https://roadmap.sh/projects/number-guessing-game