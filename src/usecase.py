#!/usr/bin/env python3
"""Perform a use case with git-phlow

Usage:
    usecase.py <repo-url>


"""
import logging, sys, docopt

from local_git_repo import GitHubRepo
from phlow_commands import usecase_workon, usecase_wrapup, usecase_deliver

def perform_usecase(repo):
    logging.info(f"usecase with repo {repo.repo_name}")
    clone_directory, issue_number = usecase_workon(repo)
    usecase_wrapup(repo, clone_directory, issue_number)
    usecase_deliver(repo, clone_directory, issue_number)


def setup_repos(repo_url):
    if 'jira' in repo_url:
        raise ValueError("not supported yet")
    elif 'github' in repo_url:
        repo = GitHubRepo(repo_url)
    else:
        raise ValueError(f"unknown remote type in url: {repo_url}")
    return repo


def main():
    FORMAT = 't=%(relativeCreated)d %(name)s %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT, filename="usecase.log", level=logging.INFO)

    flags = docopt.docopt(__doc__)
    repo_url = flags['<repo-url>']
    
    repo = setup_repos(repo_url)
    perform_usecase(repo)

    logging.shutdown()  


if __name__ == "__main__":
    main()
