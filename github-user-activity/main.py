import argparse as ar

from api.git_api_request import get_user_activity, parse_user_activity


def main():
    parser = ar.ArgumentParser(description="GitHub User Activity CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    get_user = subparsers.add_parser("get", help="Get user activity")
    get_user.add_argument("user", help="GitHub username")

    args = parser.parse_args()

    # Get user activity
    if args.command in ["get"]:
        activities = get_user_activity(args.user)
        if not activities:
            return
        user_activities = parse_user_activity(activities)
        print("output:")
        print("\n".join(user_activities))


if __name__ == "__main__":
    main()
