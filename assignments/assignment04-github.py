from github import Github
import requests
import json
try:
    from config import config as cfg

except ImportError:
    print("Error: config module not found. Ensure config.py is in the same directory or in the Python path.")
    exit(1)

# Fetch the API key from the configuration file
# The 'apikey' provides authorization to interact with the GitHub API
apikey = cfg["githubkeyassignment4"]

# Initialize the GitHub client using the API key
g = Github(apikey)

# Target repository name defined
repo_name = "ECronin1973/aprivateone"

# Define the path to the file you want to modify within the repository
file_path = "AndrewJacksonStory.txt"  # Specify the file to be edited

try:
    # Access the repository using the GitHub client
    # 'get_repo' fetches the repository object for the given repository name
    repo = g.get_repo(repo_name)

    # Fetch the content of the specified file from the repository
    # 'get_contents' retrieves the file content at the provided path and branch (default: main)
    file_content = repo.get_contents(file_path, ref="main")
    
    # Decode the file content (bytes) into a string format (UTF-8)
    content = file_content.decoded_content.decode("utf-8")

    # Replace all occurrences of the name "Andrew" with "Edward"
    # The updated content is stored in the 'updated_content' variable
    updated_content = content.replace("Andrew", "Edward")

    # Commit the updated file content back to the repository
    # 'update_file' updates the file with the new content, including a commit message
    repo.update_file(
        file_path,  # Path to the file being updated
        "Replaced 'Andrew' with 'Edward'",  # Commit message describing the change
        updated_content,  # New content to replace the old content
        file_content.sha,  # SHA value of the current file version (for consistency)
        branch="main"  # Specify the branch to push the changes (default: main)
    )
    
    # Print a success message upon completion
    print(f"File '{file_path}' updated and changes committed successfully.")

except Exception as e:
    # Catch any exception that occurs during execution
    # Print a descriptive error message to aid debugging
    print(f"An unexpected error occurred: {e}")