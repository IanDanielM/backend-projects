import argparse as ar

from logic.guessing_logic import play_game


def main():
    parser = ar.ArgumentParser(description="Number Guessing Game CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("play", help="Play Game")
    args = parser.parse_args()

    if args.command == "play":
        play_game()


if __name__ == "__main__":
    main()
