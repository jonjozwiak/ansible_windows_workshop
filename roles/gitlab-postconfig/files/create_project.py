#!/usr/bin/python 
import gitlab
import argparse

# Parse Command Line Arguments 
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--server", help="URL of gitlab host", type=str)
parser.add_argument("-u", "--user", help="User name", type=str)
parser.add_argument("-p", "--pw", help="Password", type=str)
parser.add_argument("-r", "--repo", help="Git Repo to Create", type=str)
args = parser.parse_args()

print args

server = args.server
user = args.user
repo = args.repo
password = args.pw

git = gitlab.Gitlab(server, verify_ssl=False)
git.login(user, password)

projectexists = False
projects = git.getprojects()
for project in projects:
    #print project['owner']['username'], project['name']
    if user == project['owner']['username'] and repo == project['name']:
        projectexists = True  

if not projectexists: 
    print "creating repo"
    git.createproject(name=repo, description="Ansible Repo", issues_enabled=1, merge_requests_enabled=1, wiki_enabled=0, snippets_enabled=0, visibility_level=10)
else: 
    print "Repo", user, repo, "already Exists"

