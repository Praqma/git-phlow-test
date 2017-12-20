Git Phlow System Tests
======================

This repo contains system tests for the [git-phlow tool](https://github.com/Praqma/git-phlow) It's a proof-of-concept. If the approach to testing is successful, I expect this repo will be merged into the normal git-phlow repo.

Running the tests
-----------------

You need to install [texttest](http://texttest.org). Then you can start the TextTest GUI like this:

	$> cd git-phlow-test
	$> texttest -d $PWD/tests -c $PWD

Before you will be able to run the tests you will need to get an api token. The easiest way to do this is using git-phlow itself:

	$> git-phlow auth

You also need full access to the test repositories we have set up on github: 

	- https://github.com/praqma-test/git-phlow-systest-workon_repo	

Then you can select and run test cases in the GUI. If you prefer to run using the command line, use this command:

	$> texttest -d $PWD/tests -c $PWD -b default

This will produce a report under target/default.xxxxxx/junitreport that Jenkins will understand. If the test fails and you want to inspect what happened, you will find TextTest's sandbox directory under target/default.xxxx/phl, containing the files produced during the test run.

