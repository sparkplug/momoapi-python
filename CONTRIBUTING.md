Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

Bug reports
===========

To report a bug, Open an issue in [ python-momoapi issues](https://github.com/mossplix/python-momoapi/issues) and please include:

    * Your operating system name and version.
    * Any details about your local setup that might be helpful in troubleshooting.
    * Detailed steps to reproduce the bug.

Documentation improvements
==========================

momoapi-python could always use more documentation, whether as part of the
official momoapi-python docs, in docstrings, or even on the web in blog posts,
articles, and such.

Feature requests and feedback
=============================

The best way to send feedback is to file an issue at https://github.com/mossplix/python-momoapi/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that code contributions are welcome :)

Development
===========

To set up `python-momoapi` for local development:

1. Fork [python-momoapi](https://github.com/mossplix/python-momoapi) (look for the "Fork" button). Forking will create a copy of this repo on your own github account.

2. Clone your fork locally. Example:
```bash
  $ git clone git@github.com:your_name_here/python-momoapi.git
```

3. Create a branch for local development:

```bash
  $ git checkout -b name-of-your-bugfix-or-feature
```

  You can now make your changes locally.

4. When you're done making changes, run all the checks, doc builder and spell checker with `tox`, [Learn about tox](http://tox.readthedocs.io/en/latest/install.html) :

```bash
  $ tox
```

5. Commit your changes and push your branch to GitHub:
```bash
  $ git add .
  $ git commit -m "A detailed description of your changes."
  $ git push origin name-of-your-bugfix-or-feature
```

6. Submit a pull request through the GitHub website.


Pull Request Guidelines
-----------------------

If you need some code review or feedback while you're developing the code just make the pull request.

For merging, you should:

1. Include passing tests (run ``tox``) [1].
2. Update documentation when there's new API, functionality etc.
3. Add a note to ``CHANGELOG.rst`` about the changes.
4. Add yourself to ``AUTHORS.rst``.

.. [1] If you don't have all the necessary python versions available locally you can rely on Travis - it will
       `run the tests <https://travis-ci.org/mossplix/python-momoapi/pull_requests>`_ for each change you add in the pull request.

       WARNING: It will be slower though ...

Tips
----

To run a subset of tests::

    tox -e envname -- pytest -k test_myfeature

To run all the test environments in *parallel* (you need to ``pip install detox``)::

    detox
