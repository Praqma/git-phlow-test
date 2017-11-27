
import logging, os, subprocess
import github

def usecase_workon(repo_name):
    # Arrange
    logging.info("workon usecase")
    repo = GitHubRepo("praqma-test", repo_name)
    clone_directory = repo.create_local_clone()
    issue_number = repo.create_issue("foobar")
    repo.log_my_issue(issue_number)

    # Act
    output = _cmd_output(["git-phlow", "workon", issue_number], cwd=clone_directory)
    
    # Assert
    print(output)
    logging.info("branches: %s", _cmd_output(["git", "branch"], cwd=clone_directory))
    my_issues = repo.log_my_issue(issue_number)


class GitHubRepo:
    def __init__(self, repo_owner, repo_name):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.gh = _github()

    def _remote_name(self):
        return f"https://github.com/{self.repo_owner}/{self.repo_name}"

    def create_local_clone(self):
        cmd = ["git", "clone", self._remote_name()]
        logging.info(_cmd_output(cmd))

        logging.info("created local clone of %s", self.repo_name)
        return os.path.join(os.getcwd(), self.repo_name)


    def create_issue(self, title, body=None):
        # having trouble using the api to create issues, hard-coding issue number for now
        issue_number = "3"
        #self.gh.repos('praqma-test')(self.repo_name).issues().post(title=title, body=body)
        return issue_number

    def list_issues(self, **kwargs): 
        return self.gh.repos(self.repo_owner)(self.repo_name).issues().get(**kwargs)

    def log_my_issue(self, issue_number):
        my_issue = self.list_issues(number=issue_number)
        if my_issue:
            assignee = my_issue[0].assignee
            if assignee:
                assignee = assignee.login
            logging.info("assignee for issue %s: %s", issue_number, assignee)
        else:
            logging.warn("no issue found with number %s", issue_number)



def _github():
    cmd = ["git", "config", "--global", "--get"]
    username = _cmd_output(cmd + ["phlow.user"])
    token = _cmd_output(cmd + ["phlow.token"])
    gh = github.GitHub(username=username, password=token)
    gh.username = username
    return gh



def create_local_repo(repo_name):
    os.mkdir(repo_name)
    logging.info(subprocess.check_output(["git", "init"], cwd=repo_name))

def _cmd_output(cmd, cwd=None):
    if cwd is None:
        cwd = os.getcwd()
    return subprocess.check_output(cmd, cwd=cwd).strip().decode("UTF-8")

