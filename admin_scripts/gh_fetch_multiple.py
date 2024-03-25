"""
Experimental automation of local repo actions

Not working on private repos I guess
"""

from git import Repo  #pip install gitpython

repo_list_file = '/home/villares/repos_to_fetch.txt'

with open(repo_list_file) as f:
    repo_list = [line.strip() for line in f
                 if not line.isspace()
                 and not line.strip().startswith('#')]

repos = [Repo(p) for p in repo_list]
for repo in repos:
    try:
        repo.remotes.origin.fetch()
        print(repo.working_dir, ' fetch ', end='')
        repo.remotes.origin.pull()
        print(' pull')
    except Exception as e:
        print(repo.working_dir, ' failed')
        # print(e)
    
