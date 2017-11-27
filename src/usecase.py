#!/usr/bin/env python3
"""Perform a use case with git-phlow

Usage:
    usecase.py <repo-name> <git-phlow-command>


"""
import logging, sys, docopt

from phlow_commands import usecase_workon

USECASE_FUNCTIONS = {'workon': usecase_workon}

def perform_usecase(repo_name, phlow_command):
    logging.info(f"usecase with repo {repo_name} and {phlow_command}")
    usecase_function = USECASE_FUNCTIONS[phlow_command]
    usecase_function(repo_name)


def main():
    FORMAT = 't=%(relativeCreated)d %(name)s %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT, filename="usecase.log", level=logging.INFO)

    flags = docopt.docopt(__doc__)
    repo_name = flags['<repo-name>']
    phlow_command = flags['<git-phlow-command>']
        
    perform_usecase(repo_name, phlow_command)

    logging.shutdown()  


if __name__ == "__main__":
    main()
