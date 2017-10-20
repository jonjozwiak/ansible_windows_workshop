#!/usr/bin/python 
import gitlab
import argparse

# Parse Command Line Arguments 
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--server", help="URL of gitlab host", type=str)
parser.add_argument("-u", "--user", help="User name", type=str)
parser.add_argument("-p", "--pw", help="Password", type=str)
parser.add_argument("-n", "--newuser", help="User to Create", type=str)
parser.add_argument("-w", "--newpw", help="New Users Password", type=str)
parser.add_argument("-e", "--email", help="New Users Email", type=str)

args = parser.parse_args()

print args

server = args.server
user = args.user
password = args.pw
newuser = args.newuser
newpassword = args.newpw
newemail = args.email

git = gitlab.Gitlab(server, verify_ssl=False)
git.login(user, password)

userexists = False
users = git.getusers()
for userlist in users:
    #print userlist['name'], userlist['email']
    if newuser == userlist['name'] and newemail == userlist['email']:
        userexists = True  

if not userexists: 
    print "Creating user"
    git.createuser(name=newuser, username=newuser, password=newpassword, email=newemail)
else: 
    print "User ", newuser, "already Exists"


