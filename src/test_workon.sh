#!/bin/sh

set -e

REPO_NAME="$1"

# Arrange
./src/create_repo.py $REPO_NAME
ISSUE_NUMBER=$(./src/create_issue.py $REPO_NAME 'title')


# Act
(
	cd $REPO_NAME

	git-phlow workon $ISSUE_NUMBER

# Assert
	# should have a new local branch '$ISSUE_NUMBER-title'
	git branch
)

# issue should have label 'status-inprogress'
./src/list_issue.py $REPO_NAME $ISSUE_NUMBER

# Cleanup
./src/delete_repo.py $REPO_NAME