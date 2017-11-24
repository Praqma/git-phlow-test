#!/usr/bin/env python3
print("creating repo")

import os, sys, subprocess

repo_name = os.path.abspath(sys.argv[1])

os.mkdir(repo_name)

print(subprocess.check_output(["git", "init"], cwd=repo_name))

cmd = ["git", "remote", "add", "origin", "https://github.com/praqma-test/git-phlow-systest-workon_repo"]
print(subprocess.check_output(cmd, cwd=repo_name))

print("created repo")
