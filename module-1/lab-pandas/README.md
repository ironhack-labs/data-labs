![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Pandas Deep Dive

## Introduction

Now you should already be familar with the workflow of solving and submitting the labs. But in case not, review the guidelines in the `README.md` in the [repo root](../../..) and [previous lab](../lab-numpy).

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

**What is the proportion of the apps that don't have an English `track_name`?**

:bulb: Tip: You can install [langdetect](https://pypi.org/project/langdetect/) with `pip`, then use `langdetect.detect()` to detect the language of a string. Also, you may need to decode the string with `utf8` if the string is not based on the [ASCII encoding](https://en.wikipedia.org/wiki/ASCII). Otherwise `langdetect.detect()` may throw errors.
