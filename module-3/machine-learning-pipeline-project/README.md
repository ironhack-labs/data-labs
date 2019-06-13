![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Machine Learning Pipeline

## Overview

In the past lesson, you learned about Machine Learning pipelines and how to implement a typical Machine Learning pipeline in Scikit-learn. The current lesson does not present any new content, it is only intended to put to work the knowledge you acquired in the previous lessons, while constructing a solution to a real world problem based on Machine Learning pipelines implemented with Scikit-learn.

We recommend you follow the process exemplified in the previous lesson "Machine Learning Pipelines", which consists of 8 clearly defined phases. If you get stuck at any point, you can always go back to the lesson "Machine Learning Pipelines" and re-read the material presented there on the particular phase where you got stuck. Everything you need to know to succeed in this project has already been presented on the previous lesson, so going back to review the material presented there is always a good idea.

In the previous lessons you "learned by being told", the current project is a great complement to that because now you "learn by doing." In this project, you are asked to choose a challenging Machine Learning problem that motivates you, to devise a Machine Learning solution following the phases presented in the previous lesson "Machine Learning Pipelines," and to implement the solution in Python using the Scikit-learn libraries. Next, we present the requirements your application must comply with.

## External Interface Requirements

1. Input requirement: capacity to read a dataset stored on disk.
2. Output requirement: capacity to save a Machine Learning pipeline to a file.
3. Output requirement: capacity to output the estimations of a Machine Learning pipeline for a variety of problem instances.

## Functional Requirements

1. Reading external dataset from file.
2. Creation of a Machine Learning pipeline containing a minimum of 2 steps.
3. Training of Machine Learning pipeline.
4. Evaluation of Machine Learning pipeline using cross validation.
5. Saving the Machine Learning pipeline to a file on disk.
6. Loading a Machine Learning pipeline from a file on disk.
7. Classiying new problem instances with the Machine Learning pipeline read from file.

## Technical Requirements

1. Use Python as programming language.
2. Use Pandas for reading the dataset into a dataframe.
3. Use Scikit-learn for creating, training and evaluating the Machine Learning pipeline.
4. Use a Scikit-learn pipeline for classifying new problem instances.
5. Use the class sklearn.externals.joblib for saving and reading serialized pipelines.

## Necessary Deliverables

1. Software application implemented in one or several Python modules.
2. Report explaining the problem, the dataset, the design of the solution, and the evaluation.

## Suggestions to Get Started

1. Find an interesting dataset! Look in the Useful Resources section for sources of ideas.
2. If you do not find a pre-existing dataset on the problem domain that you like, be creative: consider building the dataset yourself and donating the dataset to one of the public Machine Learning repositories.
3. Break down the project into smaller tasks: the 8 phases presented in the previous lesson.
4. Decide whether you will implement the software in a single Python module, or in several Python modules.
5. If you feel completely lost and do not know where to start, start by executing the program presented in the previous lesson. Then follow the next suggestion in this list.
6. Use an iterative approach: implement one phase per iteration.
7. Reuse: adapt the code snippets of each phase, presented in the previous lesson, to your current problem.

## Potential Project Ideas

Find some problem domain that motivates you, and ideally has a remarkable social and/or economic impact as well.These are a few ideas that you might want to consider:

1. Malicious web site detection.
2. Detection of spam.
3. Diagnosis of Parkinson's disease.

## Useful Resources

* University of California at Irvine's [Machine Learning Repository](https://archive.ics.uci.edu/ml)
* OpenML [datasets](https://www.openml.org)
* Kaggle [datasets](https://www.kaggle.com/datasets)

## Rubric

* Read dataset into Pandas dataframe and select the training set from it: 1 point.
* Pipeline formed, trained and evaluated: 3 points.
* Pipeline saved, read from disk and used for estimation of new instances: 2 point.
* Different experiments performed using different pipelines, to determine best choice: up to 2 points.
