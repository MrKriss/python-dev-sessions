# Python Development Sessions

# Setup VS Code for Python Development

* Install VS Code
* Install VS Code Python Extension
* Create a new conda environment


# Session 1: Python Packaging

* Python packages vs module
* What happens when Python runs your code
* Imports, namespaces, relative, absolute etc.
  * https://realpython.com/absolute-vs-relative-python-imports/
  * Note that if a module has already been imported in a session it wont be re-imported
* The `setup.py` file
  * Minimal Working example
    * https://setuptools.readthedocs.io/en/latest/setuptools.html#developer-s-guide
  * Note name of overall library of packaged code v!= package names to include.
  * Use `find_packages()` When lots of packages and subpackages
  * Version - Use [Semantic Versioning](https://semver.org/)
  * Use install_requires to specify top level dependencies, their own dependencies will be installed.
  * Reference docs at https://setuptools.readthedocs.io/en/latest/
* Installing with pip
  * pip vs setuptools
    * Pip can uninstall, works better with conda, and provides an editable/develop mode.
  * pip editable mode
    * `pip install -e ./package`
    * Now you can make changes to files locally and they are reflected in the "installed" code

* Packaging
  * To create a source distribution
    * `python setup.py sdist`
  * To create a binary distribution
    * `python setup.py bdist`


# For Future Sessions

* Handling non python files
  * Specifying them in setup.py
    * https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
  * Referring to them in code
    * Using Path in pathlib with __file__
    * or Resource manager API https://setuptools.readthedocs.io/en/latest/pkg_resources.html#resourcemanager-api

* Defining entry points to the code
* Handling Multiple Pythons
* `requirements.txt` files and conda `environment.yaml` files
* pipenv, poetry, flit and all manor of other tooling (that you probably don't need to know!)

# Session 2: Testing with Pytest
