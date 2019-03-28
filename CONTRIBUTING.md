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

Before you make a Pull Request, make sure of the following: 

1. Make sure your tests pass. Run `tox` beforehand.
2. Update documentation where necessary.
3. Note changes to `CHANGELOG.md`.
4. Add yourself to `AUTHORS.md`.

## Improvements

This library could always use more documentation, whether as part of the official docs, in docstrings, or even in blog posts and articles. We look forward to add them to our RESOURCES file.

