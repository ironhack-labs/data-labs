![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Challenge: Install Python and PyCharm

## Introduction

This course will be taught using the Python Programming Language. Therefore, in this challenge we will install Python as well as PyCharm, an Integrated Development Environment (IDE) for Python.

## Python

![Python](../../images/python.png)

Python is a general-purpose programming language that is gaining popularity in data analytics and data science.

### Install Python

#### Install on Mac

Python has come pre-installed on Mac for many years. However, we are going to install Python ourselves for a few reasons:

* Currently MacOS High Sierra or older versions have Python 2.7 pre-installed. However, this course will use Python 3 because Python 2.7 will be deprecated in the near future and some packages already only support Python 3.
* Using the pre-installed Python version means that updating your MacOS will wipe out your Python packages, forcing you to re-install them.
* The pre-installed version might not be the most up-to-date.

To install the latest version of Python 3, enter in the terminal:

```
$ brew install python3
```

#### Install on Windows

To install Python on Windows, first download the latest release of Python 3 (at the time this lesson was written, v3.7.0 was the latest release) from [python.org](https://www.python.org/downloads/). Click the EXE file to install. When the installation dialogue is open, make sure to check "Add Python 3.7 to PATH". Adding the Python 3.7 excutable to the Windows path will allow other applications such as Git Bash to know where the Python program is. Then follow the installation dialogue to finish installing Python.

![Install Python](../../images/install-python.png)

#### Is it Working?

To check if the installation was successful, type the following in the terminal:

```
$ python3 --version
Python 3.7.0
```

If you see that, then you have correctly installed Python!


## PyCharm

![PyCharm](../../images/pycharm.png)

PyCharm is an Integrated Development Environment (IDE) made primarily for Python. An IDE is essentially like a word processor for code. PyCharm allows us to write code more effectively with features like auto-completion and debugging. We can also easily integrate PyCharm with Git.

### Install PyCharm

#### Install with Brew Cask (Mac)

To install PyCharm using Brew Cask, simply run the following command in the terminal:

```
$ brew cask install pycharm
```

#### Install with Official Installer (Mac & Windows)

For this course, you can download PyCharm Edu installer from the [following webpage](https://www.jetbrains.com/pycharm-edu/download/). Alternatively, you can also download the non-education PyCharm installer from the [following webpage](https://www.jetbrains.com/pycharm/download/). If you choose to download the non-education version, make sure to download the community edition rather than the professional edition.

In the PyCharm installation dialogue, make sure to check Python 3.7 instead of 2.7.

![Install PyCharm](../../images/install-pycharm.png)

:bulb: Tip: Many of the current software vendors offer the Community Edition of their software for free. Often times, the Community Edition is open-source, has a restrictive license, or has a limited feature set in comparison with the paid editions such as the Professional Edition, Enterprise Edition, etc.

## Summary

In this challenge we installed Python, a programming language commonly used for data analysis.

We also installed PyCharm, an IDE used for developing with Python.

Using these tools, we can finally start writing code to perform data analysis!
