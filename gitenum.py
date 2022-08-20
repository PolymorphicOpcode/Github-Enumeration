#!/usr/bin/env python3

import requests
import argparse
import json

msg = "A quick and dirty enumeration script for pulling GitHub users' past emails through their previous commits."
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', help = "User to enumerate")
args = parser.parse_args()

name_db = set()
email_db = set()

if args.user:

    # Pull the list of different repositories
    repos = f'https://api.github.com/users/{args.user}/repos'
    r = json.loads(requests.get(repos).text)

    #Pull the commit list for each repository
    for repo in r:
        json_list = json.loads(requests.get(repo['commits_url'][:-6]).text)
        for commit in json_list:
            #TODO: Implement rate limit handling
            print(commit)
            print(commit['commit']['author']['name'])
            print(commit['commit']['author']['email'])

    print(name_db)
    print(email_db)
