
import json
import requests
import csv
from os import path

def upload_github_issue(title, body=None, labels=None,
                        repo_owner=None, repo_name=None, username=None, password=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (username, password)
    # Create our issue
    issue = {
        "title": title,
        "body": body,
        "labels": [
            labels
        ]
        }
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print(f"Successfully created Issue: {title}")
    else:
        print(f"Could not create Issue: {title}")
        print("Response:", r.content)

def make_github_issue():
    '''Create an issue on github.com from csv file'''
    # csv file with an issue path
    COMPONENTS_PATH = 'components.csv'
    # Authentication for user filing issue (must have read/write access to
    # repository to add issue to)
    USERNAME = 'USERNAME'
    PASSWORD = 'PASSWORD'
    # The repository to add this issue to
    REPO_OWNER = 'REPO_OWNER'
    REPO_NAME = 'REPO_NAME'

    skip = False
    if not path.exists(COMPONENTS_PATH):
        skip = True

    if not skip:
        components_text = open(COMPONENTS_PATH, newline='')
        components_csv = csv.reader(components_text, delimiter=',', quotechar='"')
        components_headers = []
        components_table = []
        count = 0
        for row in components_csv:
            if not count:
                components_headers = row
            else:
                components_table.append(row)
            count += 1
        print(f"Trying to upload {count-1} issues")
        for i in range(count-1):
            upload_github_issue(title=components_table[i][0], body=components_table[i][1], 
                                labels=components_table[i][2], 
                                repo_owner=REPO_OWNER,repo_name=REPO_NAME,
                                username=USERNAME,password=PASSWORD )


if __name__ == '__main__':
    make_github_issue()