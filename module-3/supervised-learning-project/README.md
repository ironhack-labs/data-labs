![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Supervised Learning

## Overview

There are many interesting use cases for Supervised Machine Learning. To name a few: prediction of the effectiveness of medical treatments, prediction of the exchange rates of foreign currencies, diagnosing Parkinson's disease just by listening to the voice of a patient, face recognition, recommendation of the news that are expected to be most interesting to a given user, etc. Choose one that motivates you and implement a solution using a Supervised Machine Learning algorithm of your choice. You don't have to start from zero: in the previous lessons you have read Python code snippets that you can adapt and reuse for you project, just make sure you understand what they do. This lesson does not present any new material at all, it is only intended as an opportunity to put into practice the knolwedge you learned in the previous lessons.

## External Interface Requirements

1. Input requirement: capacity to read a dataset stored on disk.
2. Output requirement: report quality metrics of the Machine Learning model.
3. Output requirement: output estimations corresponding to test instances.

## Functional Requirements

1. The software must be able to learn a model from a supervised dataset.
2. The software must be able to use the learned model to estimate the target value of problem instances.
3. The software must be able to compute a quality metric of the learned model.

## Technical Requirements

1. Use Python as programming language.
2. Use Pandas for reading the dataset into a pandas dataframe.
3. Use Scikit-learn for training and testing the Machine Learning model.

## Necessary Deliverables

1. Python application, or applications, that perform ETL, training and testing.
2. Report containing quality metrics, and explanation of the dataset, and the experimental procedure (whether a single split was performed, or cross-validation, etc.).

## Suggestions to Get Started
1. Find an interesting dataset! Look in the Useful Resources section for sources of ideas.
2. Break down the project into smaller tasks, for instance: importing the dataset, training, etc.
3. Decide whether you will create a single Python application or several Python applications.

## What to Do When Feeling Stuck
If you get stuck at some stage of the project, and you cannot find a way out, you can try this:
1. Nothing you are asked to do in this project is new, you have examples of all the ingredients you need in the previous lessons. Go back to the previous lessons and review the procedure used there to move on.
2. Think at a level higher than the details of the problem, at the methodology level, and identify on what stage of the methodology you are stuck, and rephrase for yourself the reason why you are stuck, and why the solutions presented in the examples of the previous lessons are not helping you to find a solution.
3. Check with your peers whether they got stuck at the same point, and what they did to move on.
4. Consult with your instructor.

## Useful Resources
* University of California at Irvine's [Machine Learning Repository](https://archive.ics.uci.edu/ml)
* OpenML [datasets](https://www.openml.org)
* Kaggle [datasets](https://www.kaggle.com/datasets)

## Rubric
* Separate dataframes for attribute values, and target values: 1 point.
* Model trained and evaluated: 2 points.
* Model used for estimation of new instances: 1 point.
* Different experiments performed using different models, to determine best choice: up to 2 points.
