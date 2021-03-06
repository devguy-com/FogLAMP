Build Tools
===========

Coverage Report
---------------

 Test coverage report helps you to analyse the code covered by your unit tests.

 FogLAMP uses `pytest-cov <http://pytest-cov.readthedocs.io/en/latest/readme.html>`_ (pytest plugin for coverage reporting) to check the code coverage.

How to run Test Coverage (through make)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``make py-test`` : This installs required dependencies, run python tests and generates coverage report in html format.
- ``make cov-report`` : Opens coverage report htmlcov/index.php in your default browser

How to read coverage report
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- index.html page displays the test coverage of all the files

  .. image:: images/coverage_report.png

- To see the details of file, click on the file hyperlink, this will navigate you to the file details which shows the code covered (in green) and code not covered (in red) by the unit tests

  .. image:: images/coverage_report_file_details.png

How to modify configuration of coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 Default configuration of coverage report is stored in the file ``.coveragerc`` . If you want to include tests in your code coverage, remove ``/*/tests/*`` from the omit option.



Test Report
-----------

 FogLAMP uses `Allure <http://allure.qatools.ru/>`_ to visualise the test reports.

Prerequisite
^^^^^^^^^^^^

 Install allure on your local machine. Use instructions listed `here <http://wiki.qatools.ru/display/AL/Allure+Commandline>`_

 `Note:` Unable to locate package allure-commandline for Ubuntu users. See `link <https://stackoverflow.com/questions/34772906/unable-to-install-allure-cli-on-ubuntu-15-10>`_

How to generate Allure Report (through make)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``make py-test`` : This installs required dependencies, run python tests.
- ``make test-report``: This generates allure reports, Starting web server for report directory <allure-report> and displays the report in your browser.
- To stop the web server and exit, press ``Ctrl+C`` from your terminal.



Documentation
-------------

 FogLAMP uses `Shphinx <http://www.sphinx-doc.org/en/stable/>`_ for documentation. Additionally it uses sphinx.ext.autodoc and sphinx.ext.ifconfig extensions in the project.
 FogLAMP docs has two type of .rst files, one created manually (in /docs) and other (in /docs/api) created automatically for the docstring in foglamp package' python files using sphinx-apidoc tool

Commands
^^^^^^^^

- ``make doc`` - Generates html files from .rst files and places them inside _build/html directory. Open the docs/_build/html/index.html file to see the index page of created docs.
- ``make live-doc`` - Start watchdog on 0.0.0.0:8000 to monitor changes in .rst files, conf.py file and /src/python/foglamp directory and reflects the changes in html format. You can review your docstring changes on fly using this command.
- ``make doc-build-test`` - run docs/check-sphinx tests. Run this command to ensure the .rst files generated are correct and docstrings in your source code are as per PEP8 guidelines.
