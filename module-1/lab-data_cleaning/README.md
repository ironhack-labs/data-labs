![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Data Cleaning

## Introduction

We keep seeing a common phrase that 80% of the work of a Data Scientist is data cleansing. We are not sure whether this number is a true reflection or not, but a data scientist spends lots of time and effort in collecting, cleaning and preparing the data for analysis because datasets come in various sizes and are different in nature. It is a very important ability for a data scientist to reshape and refine the datasets into usable datasets, which can be leveraged for further steps of the data science process.

In the exercise, you will both practice the Data Cleaning features we discussed in the lesson and learn new features by looking up documentations and references. You will work on your own but remember the teaching staff is at your service whenever you encounter problems.

## Getting Started

Now you should already be familar with the workflow of solving and submitting the labs. But in case not, review the guidelines in the `README.md` in the [repo root](../..) and [previous lab](../lab-pandas).

In this lab, you will be working on [main.ipynb](your-code/main.ipynb). Read the questions in the commentations and provide your answers. Make sure to test your answers of your Python Notebook.

## Goals

Do you remember your mysql project? In this lab, you will examine some tables from [here] (https://relational.fit.cvut.cz/dataset/Stats). This database contains an anonymized dump of all user-contributed content on the Stats Stack Exchange network.

You will need to import the `pymysql` library and the `create_engine` function from the `sqlalchemy` library.

```python
import pymysql
from sqlalchemy import create_engine
```
Once you make the connection yoo will use some basic SELECT queries to retrieve the data in order to answer the questions described next.

### Challenge Questions

1. Connect to the server and collect all the data from users and posts tables.

1. Create a merged dataframe with users and post tables. **Take into account that you will need to do some stuff before merging**

1. Identify missing values in the merged dataframe and apply some of the methods 

1. Change the data types of your merged dataset accordingly

1. Bonus Question: Create a dataframe with the outliers you have identified in the dataframe and export it to a csv file in your-code folder. 


**:exclamation: In this and future labs, if you feel you are already good at Python/Pandas and you don't need the instructions in `main.ipynb` or `main.py` to walk you through, please feel free to skip `main.ipynb` or `main.py` and create your own solution file. However, if you feel strugling on your own, please still consult those instructions because they guide you to think on the pro's track. As you make more and more progress in this course, the instructions provided in the labs will gradually decrease so that eventually you will think and solve problems by yourself like a real data analyst.**

## Deliverables

- `main.ipynb` with your responses to each of the questions above.
- `outliers.csv` containing the outliers of the dataset.
- `climate.ipynb` containing the additional challenge code and results.


## Submission

Upon completion, add your version of the deliverables to git. Then commit git, push to your forked repo and create the pull request as in the previous labs. **REMEMBER

- Upon completion, commit your code and submit to github. **REMEMBER YOU HAVE ALREADY FORKED THE REPO BEFORE**!!

  ```
  git add .
  git commit -m "<lab or project name>"
  git push origin master
  ```

- Navigate to your repo and [create a Pull Request](https://help.github.com/articles/creating-a-pull-request/).
- Create a pull request with title following this format: **"[<your_campus>][<bootcamp_code>] [<lab/project_name>]<your_name>"**
  If you are doing data bootcamp in Madrid, your name is Marc and the lab you are working on is `lab-numpy` it should be like this: "[MAD][datamad10108] [lab-numpy] Marc Pomar"
- If you have successfully created the pull request you are done!  CONGRATS :)

## Resources

[Data Cleaning Tutorial](https://www.tutorialspoint.com/python/python_data_cleansing.html)

[Data Cleaning with Numpy and Pandas](https://realpython.com/python-data-cleaning-numpy-pandas/#python-data-cleaning-recap-and-resources)

[Data Cleaning Video](https://www.youtube.com/watch?v=ZOX18HfLHGQ)

[Data Preparation](https://www.kdnuggets.com/2017/06/7-steps-mastering-data-preparation-python.html)

[Google Search](https://www.google.es/search?q=how+to+clean+data+with+python)

## Additional Challenges for the Nerds

If you have completed the `Stats` challenge without much difficulty, you can try to tidy the data you will find in thie lab folder [weather](../weather-raw.csv). This dataset is a subset of a global historical climatology network dataset. The data represents the daily weather records for a weather station (MX17004) in Mexico for five months in 2010. The goal of this additional challenge is to get the most tidy dataset you are able to produce. **Hint:Variables are stored in both rows and columns.**
To face this challenge, you will need to do a little research on tidying and melt&pivot. Feel free to use the sources you consider most appropiate.
