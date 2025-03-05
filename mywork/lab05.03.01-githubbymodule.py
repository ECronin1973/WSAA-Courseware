from github import Github
import requests
import json
from config import config as cfg

# Fetch the API key from the config file
apikey = cfg["githubkey"]

# Initialize the GitHub client
g = Github(apikey)

# Define repository and file path
repo_name = "ECronin1973/aprivateone"
output_file = "output.json"
url = f'https://api.github.com/repos/{repo_name}'

try:
    # Access the repository
    repo = g.get_repo(repo_name)

    # Get the list of all contents in the repository
    contents = repo.get_contents("", ref="main")

    # List the contents of the repository
    print("Repository contents:")
    for content_file in contents:
        print(content_file.path)

    # Make the GET request to GitHub API with authentication
    response = requests.get(url, auth=("token", apikey))
    if response.status_code == 401:  # Unauthorized
        print("Bad credentials: Please check your API key.")
    elif response.status_code == 200:  # Success
        repoJSON = response.json()
        
        # Write repository data to the JSON file
        with open(output_file, "w") as fp:
            json.dump(repoJSON, fp, indent=4)
        print(f"Repository information written to {output_file} successfully.")
    else:
        print(f"An error occurred: {response.status_code} - {response.reason}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")