import json

def test_parse_issue_number():
    resp = """{
    "url": "https://api.github.com/repos/praqma-test/git-phlow-systest-workon_repo/issues/7",
    "repository_url": "https://api.github.com/repos/praqma-test/git-phlow-systest-workon_repo",
    "labels_url": "https://api.github.com/repos/praqma-test/git-phlow-systest-workon_repo/issues/7/labels{/name}",
    "comments_url": "https://api.github.com/repos/praqma-test/git-phlow-systest-workon_repo/issues/7/comments",
    "events_url": "https://api.github.com/repos/praqma-test/git-phlow-systest-workon_repo/issues/7/events",
    "html_url": "https://github.com/praqma-test/git-phlow-systest-workon_repo/issues/7",
    "id": 279288607,
    "number": 7,
    "title": "foobar",
    "user": {
        "login": "emilybache",
        "id": 48844,
        "avatar_url": "https://avatars2.githubusercontent.com/u/48844?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/emilybache",
        "html_url": "https://github.com/emilybache",
        "followers_url": "https://api.github.com/users/emilybache/followers",
        "following_url": "https://api.github.com/users/emilybache/following{/other_user}",
        "gists_url": "https://api.github.com/users/emilybache/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/emilybache/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/emilybache/subscriptions",
        "organizations_url": "https://api.github.com/users/emilybache/orgs",
        "repos_url": "https://api.github.com/users/emilybache/repos",
        "events_url": "https://api.github.com/users/emilybache/events{/privacy}",
        "received_events_url": "https://api.github.com/users/emilybache/received_events",
        "type": "User",
        "site_admin": false
    },
    "labels": [],
    "state": "open",
    "locked": false,
    "assignee": null,
    "assignees": [],
    "milestone": null,
    "comments": 0,
    "created_at": "2017-12-05T08:36:19Z",
    "updated_at": "2017-12-05T08:36:19Z",
    "closed_at": null,
    "author_association": "OWNER",
    "body": null,
    "closed_by": null
}
"""
    issue_number = json.loads(resp)["number"]
    assert issue_number == 7
