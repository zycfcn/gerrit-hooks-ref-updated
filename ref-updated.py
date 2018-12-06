#!/usr/bin/env python

import urllib
import urllib2
import optparse
import time
import json
import logging
# hudson_config keys:
# logging.basicConfig(level=logging.DEBUG,
#                     filename='new.log',
#                     filemode='a',
#                     format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
#                     )
#don't have http example: gerrit.example.com:8080
GERRIT_SERVER = "gerrit.example.com"
GERRIT_PORT="24918"
GERRIT_NAME = "Gerrit Code Review"
WEBHOOKS_URL = ["http://webhooks.com/gitupdate/",]




def webhook(before, after, refname, projectname, name, username, timestamp):
    data = {
        "before": before,
        "after": after,
        "ref": refname,
        "repository": {
            "homepage": "http://" + GERRIT_SERVER + "/admin/repos/" + projectname,
            "url": "ssh://" + username + "@" + GERRIT_SERVER + ":" + GERRIT_PORT + "/" + projectname + ".git" ,
            "git_ssh_url": "ssh://" + username + "@" + GERRIT_SERVER + ":" + GERRIT_PORT + "/" + projectname + ".git" ,
            "name": projectname,
            "description": "",
            "owner": {
                "name": username,
                "email": ""}},
        "commits": [{"id": after,
                 "author": {"name": name, "email": ""},
                 "url": "",
                 "message": "",
                 "timestamp": timestamp}],
        "username": name,
        "message": "",

    }
    headers = {
        "User-Agent": GERRIT_NAME,
        "Content-Type": "application/json",
    }
    for url in WEBHOOKS_URL:
        if url:
            req = urllib2.Request(WEBHOOKS_URL, headers = headers, data= json.dumps(data))
            urllib2.urlopen(req
                            ).read()

def main():
    parser = optparse.OptionParser()
    parser.add_option("", "--oldrev")
    parser.add_option("", "--newrev")
    parser.add_option("", "--refname")
    parser.add_option("", "--project")
    parser.add_option("", "--submitter")
    parser.add_option("", "--submitter-username")

    (options, args) = parser.parse_args()
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())
    # logging.debug(options)
    try:
        webhook(options.before, options.newrev, options.refname, options.project, options.submitter,
                options.submitter_username, timestamp)
    except KeyError as  e:
        # no op if this project/refname aren't set up
        return

if __name__ == "__main__":
    main()
