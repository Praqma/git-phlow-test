import json, logging, os
import github
from cmd_wrapper import cmd_output, log_cmd_output

class LocalClone:

    def __init__(self, repo_dir, repo_url):
        self.directory = repo_dir
        self.repo_url = repo_url
        log_cmd_output("creating local clone", ["git", "clone", self.repo_url])


    def add_local_changes(self, issue_number, issue_title):
        log_cmd_output("creating local changes", ["touch", f"{issue_number}-{issue_title}.txt"], cwd=self.directory)
        log_cmd_output("adding local changes", ["git", "add", "."], cwd=self.directory)

    def log_branches(self):
        log_cmd_output("listing branches", ["git", "branch"], cwd=self.directory)
    
    def log_last_commit(self):
        log_cmd_output("log last commit", ["git", "log", "--oneline", "--name-only", "-1"], cwd=self.directory)
    


class GitHubRepo:
    def __init__(self, repo_url):
        self.repo_url = repo_url
        self.repo_name = self.repo_url.split("/")[-1]
        self.repo_owner = self.repo_url.split("/")[-2]
        self.local_clone = None
        self.gh = _github()
        self.logger = logging.getLogger("GitHubRepo")

    def create_local_clone(self):        
        self.local_clone = LocalClone(os.path.join(os.getcwd(), self.repo_name), self.repo_url)
        return self.local_clone


    def create_issue(self, title, body=None):
        issue = self.gh.repos(self.repo_owner)(self.repo_name).issues().post(title=title, body=body)
        issue_number = issue["number"]
        return str(issue_number)

    def list_issues(self, **kwargs): 
        return self.gh.repos(self.repo_owner)(self.repo_name).issues().get(**kwargs)

    def log_my_issue(self, issue_number):
        my_issue = self.list_issues(number=issue_number)
        if my_issue:
            assignee = my_issue[0].assignee
            if assignee:
                assignee = assignee.login
            self.logger.info("assignee for issue %s: %s", issue_number, assignee)
        else:
            self.logger.warn("no issue found with number %s", issue_number)



def _github():
    cmd = ["git", "config", "--global", "--get"]
    username = cmd_output(cmd + ["phlow.user"])
    token = cmd_output(cmd + ["phlow.token"])
    gh = github.GitHub(username=username, password=token)
    gh.username = username
    return gh
