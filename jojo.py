import requests

username = "oscarmmv"
repo = "hello"

# Make a GET request to the GitHub API to fetch the pull requests
response = requests.get(f"https://api.github.com/repos/{username}/{repo}/pulls")

# Check if the request was successful
if response.status_code == 200:
    pull_requests = response.json()
    num_pull_requests = len(pull_requests)
    print(f"{username} made {num_pull_requests} pull requests on GitHub.")
else:
    print("Failed to fetch pull requests from GitHub API.")
