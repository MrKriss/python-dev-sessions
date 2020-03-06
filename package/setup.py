from setuptools import setup, find_packages

setup(
    # The name that pip will use to identify the packaged code.
    name="mpg",
    # The list of python packages, relative to setup.py to include.
    # Note that find_packages is useful here when you have lots of sub packages
    # https://setuptools.readthedocs.io/en/latest/setuptools.html#using-find-packages
    packages=["mpg"],
    # Version String, please use semantic versioning https://semver.org/
    version="0.1.0",
    # Dependencies that will be installed by pip before this package.
    install_requires=["pandas", "matplotlib"],
)
