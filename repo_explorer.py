import requests
import sys


def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: could not find user '{username}' (status {response.status_code})")
        return

    repos = response.json()

    if not repos:
        print(f"{username} has no public repositories.")
        return

    print(f"\nPublic repositories for {username}:\n")
    for repo in repos:
        name = repo.get("name")
        stars = repo.get("stargazers_count")
        language = repo.get("language") or "Not specified"
        updated = repo.get("updated_at", "")[:10]

        print(f"- {name}")
        print(f"  Language: {language} | Stars: {stars} | Last updated: {updated}\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python repo_explorer.py <github-username>")
        sys.exit(1)

    get_repos(sys.argv[1])
