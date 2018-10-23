![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Ironhack Data Analytics Labs

## Getting Started

1. Install [grip](https://github.com/joeyespo/grip) with `brew install grip` (Mac) or `pip install grip` (Windows).

2. Start local Markdown server:

```
$ grip -b README.md 8080 --user <your-github-username> --pass <your-github-password>
```

:bulb: `grip` uses the GitHub Markdown API to render the files in localhost so that you'll see exactly how GitHub would render the Markdown files. Running `grip` with your Github username and password will allow you to make unrestricted requests to GitHub. If you see error when you run the problem that says `GitHub Rate Limit Reached`, it's because you didn't run grip with your GitHub credentials or the provided credentials are incorrect.

## Working on the Assignments

**To work on your first assignment**, create a branch of your own with your name (change the branch name unless your name is John Doe):

```
$ git checkout -b john-doe
```

Each project/lab has its own directory in which you'll find a `README.md` file and a sub-directory named `your-code`. The descriptions and requirements of the assignment can be found in the README file. When you work on the assignment, create your code files in the `your-code` directory and save regularly while you work.

After you finish, add those files to git, commit, and push your branch to GitHub. In the commit message, specify which lab/project you are submitting. For example:

```
$ git add <files-to-add>
$ git commit -m "Module 1 MySQL project"
$ git push origin john-doe
```

The instructional team will review your branch and provide feedback.

**To work on the subsequent assignments**, keep using the same branch you created and push your new codes to GitHub.

:exclamation: Update your branch regularly because the curriculum development team is developing new assignments for you as the course proceeds. Make sure you have committed all your codes then exectue `git pull origin master` to obtain the latest code from the `master` branch.

### Happy coding!

# Lab Index

## Module 1

[Project | Merge Resolving Conflicts](module-1/resolving-merge-conflicts)

[Lab | Entity Relationship Diagram](module-1/lab-erd)

[Project | MySQL](module-1/mysql-project)

[Lab | Numpy Deep Dive](module-1/lab-numpy)

[Lab | Pandas Deep Dive](module-1/lab-pandas)

Lab | Data Cleaning

[Project | Pandas Project](module-1/pandas-project)

Lab | Python List Comprehension & Error Handling

Lab | Python String Operations & Functional Programming

[Project | Web Data Pipeline](module-1/pipelines-project)

Lab | Working with APIs

Lab | Web Scraping

[Project | API and Web Data Scraping](module-1/web-project)

## Module 2

Lab | Statistical Analysis with Pandas

Lab | Pandas DataFrame, Aggregations, & Summarization

Lab | Pivot Tables, Field Relations & Correlations

[Project | Data Analysis with Pandas](module-2/data-analysis-with-pandas)

Lab | DataViz with Seaborn & Matplotlib

[Project | Visualizing Real World Data](module-2/visualizing-real-world-data)

[Project | Storytelling with Data Visualizations](module-2/storytelling-with-data-visualizations)

Lab | Probability

Lab | Hypothesis Testing & Statistical Significance

[Project | Calculating Game of Chances](module-2/calculating-games-of-chance)

Lab | Tableau Deep Dive

Lab | DataViz with Tableau

Lab | BI with Tableau

[Project | BI with Tableau](module-2/tableau-project)

## Module 3

Lab | Machine Learning Workflow

Lab Feature Extraction & Engineering + Scikit-Learn

Lab | Building & Saving Models

Lab | Supervised Learning with Scikit-Learn

[Project | Supervised Learning](module-3/supervised-learning-project)

Lab | Unsupervised Learning with Scikit-Learn

[Project | Unsupervised Learning (Clustering)](module-3/clustering-project)

Lab | Machine Learning Pipelines

[Project | Machine Learning Pipeline](module-3/machine-learning-pipeline-project)

## [Final Project](final-project/final-project.md)