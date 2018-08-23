![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Challenge: Install Homebrew and Brew Cask

:exclamation: **This challenge is for Mac users only. Skip this challenge if you are a Windows user.**

## Introduction

[Homebrew](https://brew.sh/), "the missing package manager for OS X", is a convenient utility for Mac OS X that allows you to easily install and upgrade hundreds of open-source tools via simple commands. Brew Cask is an extension of Homebrew that allows you to install OS X apps, fonts and plugins and other non-open source software.

## Homebrew

![Homebrew](../../images/homebrew.png)

### Install Homebrew

To install Homebrew, you can follow the full instructions on the [Homebrew Installation Doc](https://docs.brew.sh/Installation). However, typically all you need to do is to simply run the following command in the terminal as seen at the Homebrew site:

```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

#### Is it Working?

Now, type the following in the terminal:

```
$ brew -v
  Homebrew 1.6.9
  Homebrew/homebrew-core (git revision 95e6; last commit 2018-07-08)
```

If you can see that, you have Homebrew installed! Otherwise, refer to the full instructions on the [Homebrew Installation Doc](https://docs.brew.sh/Installation).

#### Search for Homebrew packages

To search for open-source software packages, use the following command line:

```
$ brew search python
==> Searching local taps...
python@2 ✔            boost-python          boost-python@1.59     ipython               micropython           python-markdown       zpython
app-engine-python     boost-python3         gst-python            ipython@5             python                wxpython
==> Searching taps on GitHub...
homebrew/cask/awips-python                           homebrew/cask/kk7ds-python-runtime                   homebrew/cask/mysql-connector-python
```

## Brew Cask

You should already have Brew Cask after installing the latest Homebrew. To test, try to install Google Chrome with Brew Cask:

```
$ brew cask install google-chrome
```

You may be prompted to enter the admin password in a pop-up window. Enter the admin password and click "Always Allow" to continue installation.

If you don't have Google Chrome yet, Brew Cask will install it for you:

```
==> Satisfying dependencies
==> Downloading https://dl.google.com/chrome/mac/stable/GGRO/googlechrome.dmg
==> Verifying checksum for Cask google-chrome
==> Installing Cask google-chrome
==> Moving App 'Google Chrome.app' to '/Applications/Google Chrome.app'.
🍺  google-chrome was successfully installed!
```

If you already have Google Chrome, you will see an error message which you can safely ignore:

```
Error: It seems there is already an App at '/Applications/Google Chrome.app'.
```

## Summary

In this challenge we installed Homebrew and Brew Cask, which can be used to install hundreds of open source software packages (e.g. Git, Python, and MySQL) and non-open source packages (e.g. PyCharm and Sequel Pro). In the following challenges you will use them to install the software packages required for this course.
