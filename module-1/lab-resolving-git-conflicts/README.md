![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Resolving Git Conflicts

## Introduction

Resolving Git conflicts and merging branches is an import skill every software/data engineer must possess because code conflicts occur on daily basis in collaborative projects. This lab will help you learn the whole process process and become prepared to solve Git conflicts next time you encounter them.

The general steps for this lab are as follows:

1. Commit changes on local branch and sync with remote.
1. Create a new git branch.
1. Create a conflict with the master branch.
1. Resolve the conflict.
1. Merge your branch.
1. Push to remote.

**Note: The above is also the general procedure for you to submit your assignments in this course. However, you will not be required to fix conflicts every time when you push codes.**

## Deliverables

* Your branch where conflicts are resolved and merged

* `your-code/about-me.md` updated with introductions about yourself

## Steps

### Step 1 - Check Local Branch Status

If you work in a team, every time before you start working on the code you should check if there is any unstaged or uncommited changes in your local branch by executing `git status` within the project directory in Terminal.

In the git status output, check whether there is any **file with unstaged changes** or **untracked files**. Sometimes you may also find **files with changes to be committed**. If you see any of those, you need to stage and commit the changes in Step 2. If you don't see any of those, jump to Step 3.

### Step 2 - [OPTIONAL] Stage and Commit Changes

If you identified unstaged or uncommitted changes in the previous step, you need to stage and commit the changes. Git will not allow you to sync your local branch with the remote if you have unstaged/uncommitted changes in case they conflict with the remote branch.

So if you need to execute this step, do `git add` for the unstaged changes and untracked files. Then commit the changes with `git commit`.

After committing, if you do `git status` again you should see something like:

```
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

### Step 3 - Pull Latest Changes From the Remote Branch

Now that you have staged and committed all changes, you can obtain the latest changes from the remote branch. This step is not required but it's a good practice because it can reduce the chance of conflicts when you push your code to remote. Git conflicts occur when more than one developers have changed the same regions of the same files and subsequently merge their respective branches. If you don't pull the latest changes from remote at this time and you will be working on some files that have been recently changed, you will likely have conflicts when you push your code back to remote. So a better idea is to obtain the latest changes from remote and start working from there.

To pull the latest changes from the remote (assuming you are working on the master branch), execute:

```bash
git pull origin master
```

If your local branch is lagged behind, git will update the codes in your local branch. If the latest code in the remote branch has conflicts with your local branch, you will see warnings and you will need to resolve the conflicts in the next step. However, if there is no conflict or auto merging is successful, you can skip to Step 5.

### Step 4 - [OPTIONAL] Resolve Conflicts

If you encounter conflicts when you sync your branch with the remote, fix the conflicts as the lesson showed you. After resolving the conflict, commit your changes and push your code back to remote.

### Step 5 - Create Conflicting Changes

In your real work you don't create conflicting changes on purpose. But for the sake of practicing in this lab, let's create a conflicting change. Here's how:

#### TBD

```
# Who am I

* Where are you from?
* What do you do?
* Do you have previous experience with technology/data?

# Why am I here

* What has brought you to Ironhack?
* What knowledge/skills do you expect to learn in this bootcamp?

# What will I do after the bootcamp?

* Which industry will you seek employment in?
* What will your future role look like?
* What is your career goal?
```

### Step 6 - Resolve Conflicts

Resolve the conflicts in the affected files. You can see which files have conflicts by executing `git status`. You will need to examine each of the files with conflicts and fix the conflicts manually. After you are done fixing conflicts, make sure to double check / test the files to make sure you haven't missed anything.

### Step 7 - Commit and push Changes

After resolving the conflicts, add the files with unstaged changes and commit. Then push your local branch to remote.

### Step 8 - Make Pull Request

Make a pull request of your branch to the master branch. Check the pull request and make sure there are no conflicts.