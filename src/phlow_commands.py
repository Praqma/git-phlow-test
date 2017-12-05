
import logging, os, subprocess, json
import github
from cmd_wrapper import cmd_output, log_cmd_output
from local_git_repo import GitHubRepo

def usecase_workon(repo):
    # Arrange - clone the remote repo
    logging.info("preparing for workon")
    local_clone = repo.create_local_clone()
    issue_number = repo.create_issue("issue_title")
    repo.log_my_issue(issue_number)

    # Act
    log_cmd_output("workon", ["git-phlow", "workon", issue_number], cwd=local_clone.directory)
    
    # Assert
    local_clone.log_branches()
    repo.log_my_issue(issue_number)
    return local_clone, issue_number


def usecase_wrapup(repo, local_clone, issue_number):
    # Arrange - make a commit in the issue branch
    logging.info("preparing for wrapup")
    local_clone.add_local_changes(issue_number, "issue_title")

    # Act
    log_cmd_output("wrapup", ["git-phlow", "wrapup", issue_number], cwd=local_clone.directory)
    
    # Assert
    local_clone.log_branches()
    local_clone.log_last_commit()
    repo.log_my_issue(issue_number)

