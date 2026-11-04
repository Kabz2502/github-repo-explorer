# github-repo-explorer
Python CLI to fetch and display a GitHub user's public repos.
## What it does

Given a GitHub username, the script returns each public repository along with:
- Primary language
- Star count
- Last updated date

## Requirements

- Python 3
- `requests` library

## Installation

```bash
pip install requests
```

## Usage

```bash
python repo_explorer.py <github-username>
```

**Example:**

```bash
python repo_explorer.py Kabz2502
```

**Sample output:**

## Run with Docker

Build the image:

    docker build -t github-repo-explorer .

Run it (replace `octocat` with any GitHub username):

    docker run --rm github-repo-explorer octocat

The image is based on `python:3.12-slim`, installs dependencies from
`requirements.txt`, and runs as a non-root user.
