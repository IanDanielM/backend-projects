import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def get_user_activity(user):
    try:
        url = f"https://api.github.com/users/{user}/events"
        request = Request(url)
        with urlopen(request) as response:
            return json.loads(response.read().decode())
    except HTTPError as error:
        if error.code == 404:

            print("User not found.")
        else:
            print(f"HTTP Error {error.code}: {error.reason}")
    except URLError as error:
        print(f"URL Error: {error.reason}")
    except Exception as error:
        print(f"Error: {error}")
    return None


def parse_user_activity(activities):
    if not activities:
        return "No activities found."
    user_activities = []
    for activity in activities:
        user = activity['actor']['login']
        repo = activity['repo']['name']

        if activity['type'] == 'CreateEvent':
            user_activities.append(f"- {user} created repository {repo}")
        elif activity['type'] == 'PushEvent':
            user_activities.append(
                f"- {user} pushed {len(activity['payload']['commits'])} commits to {repo}")
        elif activity['type'] == 'WatchEvent':
            user_activities.append(f"- {user} starred {repo}")
        elif activity['type'] == 'IssuesEvent':
            user_activities.append(f"- {user} opened issue on {repo}")
        elif activity['type'] == 'IssueCommentEvent':
            user_activities.append(f"- {user} commented on issue on {repo}")
        elif activity['type'] == 'ForkEvent':
            user_activities.append(f"- {user} forked {repo}")
        elif activity['type'] == 'PublicEvent':
            user_activities.append(f"- {user} made repository {repo} public")
        elif activity['type'] == 'PullRequestEvent':
            user_activities.append(f"- {user} opened pull request on {repo}")
        else:
            user_activities.append(f"- {user} did something on {repo}")
    return user_activities
