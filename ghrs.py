# Python 3.5.2
# http://stackoverflow.com/questions/8646517/see-the-size-of-a-github-repo-before-cloning-it
# https://developer.github.com/v3/repos/#get
# http://www.python-requests.org/en/master/
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm

import sys, getopt
import requests

opts, args = getopt.getopt(sys.argv[1:], "o:r:")
owner = ""
repo = ""

for op, value in opts:
    if op == "-o":
        owner = value
    elif op == "-r":
        repo = value

r = requests.get('https://api.github.com/repos/' + owner + '/' + repo)
if r.status_code == 200:
    print(r.json()['size'])
