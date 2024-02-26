import requests

def get_user_repositories(username, token):
    # Set the GitHub API endpoint for user repositories
    api_url = f"https://api.github.com/users/{username}/repos"

    # Set headers with authorization and accept header
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Send GET request to retrieve user repositories
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        repositories = response.json()
        print("User Repositories:")
        for repo in repositories:
            print(repo["name"])
    else:
        print("Failed to fetch user repositories.")
        print("Status Code:", response.status_code)
        print("Response:", response.json())

if __name__ == "__main__":
    # Replace these values with your GitHub username and personal access token
    github_username = "<your_github_username>"
    github_token = "<your_personal_access_token>"

    get_user_repositories(github_username, github_token)
