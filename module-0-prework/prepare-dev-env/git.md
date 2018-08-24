![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Challenge: Install Git and Create a GitHub Account

## Introduction

For this course, you will need to install Git and also create an account on Github. We will get into the more intricate details in upcoming lessons, but **Git is the program that runs on your computer and Github is where your work is stored online.**

## Git

![Git](../../images/git.png)

### Install Git

:exclamation: **Windows users: You can skip Git installation because you already have it when you installed [Git for Windows](https://gitforwindows.org/) in the previous lesson Command Line Basics. Scroll down and proceed to Basic Configuration.**

Git is part of the [Xcode](https://developer.apple.com/xcode/) Command Line Tools, so if you have already installed them, you already have git!

If you’re using OSX Maverick or higher, just type `git` into the terminal. If you don’t have the Xcode Command Line Tools already installed, you will be prompted to do so.

Otherwise, there are two ways to install Git:

1. To install Git using Homebrew (recommended), simply run the following command in the terminal:

```
$ brew install git
```

2. You can also download this [Git installer](http://git-scm.com/download/mac) which will guide you through the process.

:bulb: Tip: The benefit of installing Git using Homebrew instead of the installer is you can upgrade Git to the latest version using a simple command:

```
$ brew upgrade git
```

#### Is It Working?

Now, type the following in the terminal:

```
$ git --version
  git version 2.7.4
```

If you can see that, you have git installed!

If you’re still having problems, or if you prefer to install Git from source, here’s more information: [Getting Started Installing Git](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Basic Configuration

The first thing you should do is to set your [identity](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup#Your-Identity) (name and email) for your account. This is important because as git takes snapshots (commits) on our code, it will also store who made the change.

```
$ git config --global user.name "John Doe";`
$ git config --global user.email johndoe@example.com
```

:warning: **Warning: You should replace `"John Doe"` and the `johndoe@example.com` with your own info.**

To learn more about setting up Git configurations, you can read this article on [First-time Git setup](http://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

## Github

### Create an Account

First things first: if you haven’t done so already, go to [Github](https://github.com) and create an account.

![Github](../../images/github.png)

:bangbang: **Alert: Please, save your *username* and *password* in a safe place. Lots of students forget their Github account information :)**

## Summary

In this challenge, we installed Git, a Version Control System (VCS) through the terminal, or directly through the official installer.

We also introduced Github, and how to create an account to, link with Git in the future.

This lesson is purely for configuring and setting up Git and Github. In future lessons, we will cover the logistics of actually working with these two tools.
