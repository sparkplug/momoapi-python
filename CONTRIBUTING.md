# Contributing

First off, thank you for considering contributing to this Python MTN MoMo Library. It's people like you that make it such a great tool. Contributions are welcome, and they are greatly appreciated!

## Where do I go from here?

If you've noticed a bug or have a question that doesn't belong on the
[Spectrum](https://spectrum.chat/momo-api-developers/) or [Stack Overflow](https://stackoverflow.com/), [search the issue tracker](https://github.com/sparkplug/momoapi-python/issues) to see if
someone else in the community has already created a ticket. If not, go ahead and
[make one](https://github.com/sparkplug/momoapi-python/issues/new/choose)! 



## Fork & create a branch

If there is something you think you can fix, then fork the [repo](https://github.com/sparkplug/momoapi-python) and create a branch with a descriptive name.

A good branch name would be (where issue #32 is the ticket you're working on):

```sh
git checkout -b 32-add-swahili-translations
```

## Get the test suite running

This library has a comprehensive test suite, which can be run using the `tox` command:

To view all test environments

```sh
$ tox -l  
``` 
To run the tests for Python 2.7  

```sh
$ tox -e py27-cover 
```

To run the tests for Python 3.4

```sh
$ tox -e py34-cover 
``` 

To run a subset of tests::

```sh
tox -e envname -- pytest -k test_myfeature
```

To run all the test environments in *parallel*, you need to `pip install detox`:

```sh
detox
```

## Bugs and Fixes

### Did you find a bug?

* **Ensure the bug was not already reported** by [searching all issues](https://github.com/sparkplug/momoapi-python/issues).

* If you're unable to find an open issue addressing the problem,
  [open a new one](https://github.com/sparkplug/momoapi-python/issues/new/choose). Be sure to include a **title and clear
  description**, as much relevant information as possible, and a **code sample**
  or an **executable test case** demonstrating the expected behavior that is not
  occurring.

* If possible, use the relevant bug report templates to create the issue.
  Make the necessary changes to demonstrate the issue, and **paste the content into the
  issue description**

### Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help;
everyone is a beginner at first :smile_cat:

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that code contributions are welcome :)

If you would like to send us feedback, simply [file an issue](https://github.com/sparkplug/momoapi-python/issues/new/choose).

## Local Development

To set up `python-momoapi` for local development:

1. Fork the repo. Look for the "Fork" button in the Github UI.
2. Clone your fork locally:

```sh
git clone https://github.com/your_name_here/momoapi-python.git
```

3. Create a branch for local development:
```sh
git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

4. When you're done making changes, run all the checks, doc builder and spell checker with `tox`. 
```sh
tox
```
Make sure Tox is installed by following the instructions [here](http://tox.readthedocs.io/en/latest/install.html)

5. Commit your changes and push your branch to GitHub::

```sh
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

6. Submit a pull request through the GitHub website.

## Pull Request Guidelines

### Make a Pull Request

At this point, you should switch back to your master branch and make sure it's
up to date with `momoapi-python`'s master branch:

```sh
git remote add upstream https://github.com/sparkplug/momoapi-python.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy of master, and push it!

```sh
git checkout 32-add-swahili-translations
git rebase master
git push --set-upstream origin 32-add-swahili-translations
```

Finally, go to GitHub and make a Pull Request :D

TravisCI will run our test suite against all supported Python versions. We care
about quality, so your PR won't be merged until all tests pass. It's unlikely,
but it's possible that your changes pass tests in one Python version but fail in
another. In that case, you'll have to setup your development environment to use your Python version, and investigate what's going on!

### Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

To learn more about rebasing in Git, there are a lot of [good](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase) [resources](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) but here's the suggested workflow:

```sh
git checkout 32-add-swahili-translations
git pull --rebase upstream master
git push --force-with-lease 32-add-swahili-translations
```

### Merging a PR (maintainers only)

A PR can only be merged into master by a maintainer if:

* It is passing CI.
* It has been approved by at least one maintainers. If it was a maintainer who opened the PR, only one extra approval is needed.
* It has no requested changes.
* It is up to date with current master.

Any maintainer is allowed to merge a PR if all of these conditions are met.

### Shipping a release (maintainers only)

Maintainers need to do the following to push out a release:

* Make sure all pull requests are in and that changelog is current
* Update version and changelog with new version number using semver
* If it's not a patch level release, create a stable branch for that release,
  otherwise switch to the stable branch corresponding to the patch release you
  want to ship:

  ```sh
  git checkout master
  git fetch momoapi-python
  git rebase momoapi-python/master
  # If the release is 2.1.x then this should be: 2-1-stable
  git checkout -b N-N-stable
  git push momoapi-python N-N-stable:N-N-stable
  ```

Before you make a Pull Request, make sure of the following: 

1. Make sure your tests pass. Run `tox` beforehand.
2. Update documentation where necessary.
3. Note changes to `CHANGELOG.md`.
4. Add yourself to `AUTHORS.md`.

## Improvements

This library could always use more documentation, whether as part of the official docs, in docstrings, or even in blog posts and articles. We look forward to add them to our RESOURCES file.

