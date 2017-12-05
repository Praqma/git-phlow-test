#!/usr/bin/env python3
"""Perform a use case with git-phlow

Usage:
    usecase.py <repo-url>


"""
import logging, sys, docopt

from local_git_repo import GitHubRepo
from phlow_commands import usecase_workon, usecase_wrapup

def perform_usecase(local_repo):
    logging.info(f"usecase with repo {local_repo.repo_name}")
    clone_directory, issue_number = usecase_workon(local_repo)
    usecase_wrapup(local_repo, clone_directory, issue_number)


def setup_repos(repo_url):
    if 'jira' in repo_url:
        raise ValueError("not supported yet")
    elif 'github' in repo_url:
        local_repo = GitHubRepo(repo_url)
    else:
        raise ValueError(f"unknown remote type in url: {repo_url}")
    return local_repo


def main():
    FORMAT = 't=%(relativeCreated)d %(name)s %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT, filename="usecase.log", level=logging.INFO)

    flags = docopt.docopt(__doc__)
    repo_url = flags['<repo-url>']
    
    local_repo = setup_repos(repo_url)
    perform_usecase(local_repo)

    logging.shutdown()  


if __name__ == "__main__":
    main()
