![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Pandas Deep Dive

## Introduction

Now you should already be familar with the workflow of solving and submitting the labs. But in case not, review the guidelines in the `README.md` in the [repo root](../..) and [previous lab](../lab-numpy).

In this lab, again you will be working on [main.py](your-code/main.py). Read the questions in the commentations and provide your answers. Make sure to test your answers in Python.

## Goals

In this lab, you will examine a data file named `apple_store.csv` downloadable from [this link](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/data/apple_store.csv). This file contains information of over 7,000 Apple Store apps such as ID, name, size in bytes, price, number of ratings, user rating, prime genre, and so on. You will use Pandas to import the data source and examine the data in order to answer several questions described next.

### Challenge Questions

1. How many apps are there in the data source?

1. What is the average rating of all apps?

1. How many apps have an average rating no less than 4?

1. How many genres are there in total for all the apps?

1. What are the top 3 genres that have the most number of apps?

1. Which genre is most likely to contain free apps?

1. If a developer tries to make money by developing and selling Apple Store apps, in which genre should s/he develop the apps? Please assume all apps cost the same amount of time and expense to develop.

1. :icecream: Bonus Question: What is the proportion of apps that don't have an English `track_name`?

**:exclamation: In this and future labs, if you feel you are already good at Python/Pandas and you don't need the instructions in `main.py` to walk you through, please feel free to skip `main.py` and create your own solution file. However, if you feel strugling on your own, please still consult those instructions because they guide you to think on the pro's track. As you make more and more progress in this course, the instructions provided in the labs will gradually decrease so that eventually you will think and solve problems by yourself like a real data analyst.**

## Deliverables

- `main.py` with your responses to each of the questions above.

## Submission

Upon completion, add your version of `main.py` to git. Then commit git and push your branch to the remote.

## Resources

[Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/api.html)

[10 Minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/10min.html)

[Google Search](https://www.google.com/search?q=how+to+use+pandas+python)

## Additional Challenges for the Nerds

### [Pandas Tutorial: Data analysis with Python | Part 1](https://www.dataquest.io/blog/pandas-python-tutorial/)

If you have completed the `apple_store` challenge without much difficulty, you will find this tutorial pretty easy. However, it's still a great tutorial to read because it explains a lot of the thinking process behind codes. You can skim through this tutorial quickly to check if there's anything you still don't know.

### [Pandas Tutorial: Data analysis with Python | Part 2](https://www.dataquest.io/blog/pandas-tutorial-python-2/)

This is an advanced tutorial about Pandas that involves [character encoding](http://www.cogsci.nl/blog/a-simple-explanation-of-character-encoding-in-python.html), [Pandas DataFrame `apply` method](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html), [Python `lambda` expression](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions), Python functional programming (you'll learn later this week), data cleaning (you'll learn later this week), and plotting with `matplotlib` (you'll learn in Module 2). There is a lot of new information but if you manage to complete this tutorial you'll be far ahead of your classmates.

The most challenging part of this course is Module 3. In Module 1 and 2 most students should be able to complete with moderate efforts. What will make you truly stand out is how deep you can dive in Module 3, which depends on your level of accomplishment in Module 1 and 2. Therefore, if you have the power to accomplish more (in terms of both the depth and breadth) in the first two modules we will certainly encourage you to.
