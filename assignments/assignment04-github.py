from github import Github
import requests
import json
try:
    from config import config as cfg
except ImportError:
    print("Error: config module not found. Ensure config.py is in the same directory or in the Python path.")
    exit(1)

# Fetch the API key from the configuration file
apikey = cfg["githubkeyassignment4"]

# Initialize the GitHub client using the API key
g = Github(apikey)

# Define repository and file path
repo_name = "ECronin1973/aprivateone"
file_path = "AndrewJacksonStory.txt"  # Specify the file to be edited
output_file = "output.json"
url = f'https://api.github.com/repos/{repo_name}'

try:
    # Access the repository using the GitHub client
    repo = g.get_repo(repo_name)
    
    # Display all files in the root directory of the repository
    print("Repository contents:")
    contents = repo.get_contents("", ref="main")
    for content_file in contents:
        print(content_file.path)
    
    # Fetch the content of the specified file from the repository
    file_content = repo.get_contents(file_path, ref="main")
    content = file_content.decoded_content.decode("utf-8")
    #print(f"\nOriginal content of {file_path}:\n{content}\n")

    # Replace all occurrences of the name "Andrew" with "Edward"
    updated_content = content.replace("Andrew", "Edward")

    # Commit the updated file content back to the repository
    repo.update_file(
        file_path,
        "Replaced 'Andrew' with 'Edward'",
        updated_content,
        file_content.sha,
        branch="main"
    )
    print(f"File '{file_path}' updated and changes committed successfully.")
    
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