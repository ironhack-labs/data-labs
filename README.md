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

[lab-advanced-mysql](module-1/lab-advanced-mysql)

[lab-advanced-regex](module-1/lab-advanced-regex)

[lab-advanced-web-scraping](module-1/lab-advanced-web-scraping)

[lab-api-scavenger-game](module-1/lab-api-scavenger-game)

[lab-bag-of-words](module-1/lab-bag-of-words)

[lab-code-simplicity-efficiency](module-1/lab-code-simplicity-efficiency)

[lab-data_cleaning](module-1/lab-data_cleaning)

[lab-errhand_listcomp](module-1/lab-errhand_listcomp)

[lab-error-handling](module-1/lab-error-handling)

[lab-functional-programming](module-1/lab-functional-programming)

[lab-import-export](module-1/lab-import-export)

[lab-intro-pandas](module-1/lab-intro-pandas)

[lab-lambda-functions](module-1/lab-lambda-functions)

[lab-list-comprehensions](module-1/lab-list-comprehensions)

[lab-map-reduce-filter](module-1/lab-map-reduce-filter)

[lab-mysql](module-1/lab-mysql)

[lab-mysql-select](module-1/lab-mysql-select)

[lab-numpy](module-1/lab-numpy)

[lab-object-oriented-programming](module-1/lab-object-oriented-programming)

[lab-parallelization](module-1/lab-parallelization)

[lab-resolving-git-conflicts](module-1/lab-resolving-git-conflicts)

[lab-rss](module-1/lab-rss)

[lab-string-operations](module-1/lab-string-operations)

[lab-tuple-set-dict](module-1/lab-tuple-set-dict)

[lab-web-scraping](module-1/lab-web-scraping)

[pandas-project](module-1/pandas-project)

[pipelines-project](module-1/pipelines-project)

[web-project](module-1/web-project)

## Module 2

[lab-advanced-pandas](module-2/lab-advanced-pandas)

[lab-bayesian-statistics](module-2/lab-bayesian-statistics)

[lab-bi-analysis-with-tableau](module-2/lab-bi-analysis-with-tableau)

[lab-correlation-tests-with-scipy](module-2/lab-correlation-tests-with-scipy)

[lab-df-calculation-and-transformation](module-2/lab-df-calculation-and-transformation)

[lab-hypothesis-testing](module-2/lab-hypothesis-testing)

[lab-interactive-visualization](module-2/lab-interactive-visualization)

[lab-intro-to-bi-and-tableau](module-2/lab-intro-to-bi-and-tableau)

[lab-intro-to-scipy](module-2/lab-intro-to-scipy)

[lab-matplotlib-seaborn](module-2/lab-matplotlib-seaborn)

[lab-pandas-deep-dive](module-2/lab-pandas-deep-dive)

[lab-pivot-table-and-correlation](module-2/lab-pivot-table-and-correlation)

[lab-plotting-multiple-data-series](module-2/lab-plotting-multiple-data-series)

[lab-poker-master](module-2/lab-poker-master)

[lab-probability-distribution](module-2/lab-probability-distribution)

[lab-storytelling-data-visualization](module-2/lab-storytelling-data-visualization)

[lab-subsetting-and-descriptive-stats](module-2/lab-subsetting-and-descriptive-stats)

[lab-tableau-data-visualization](module-2/lab-tableau-data-visualization)

[lab-two-sample-hypothesis-tests](module-2/lab-two-sample-hypothesis-tests)

[statistical-analysis-project](module-2/statistical-analysis-project)

[tableau-project](module-2/tableau-project)

[visualizing-real-world-data-project](module-2/visualizing-real-world-data-project)


## Module 3

[Lab | Intro to Machine Learning](module-3/lab-intro-to-ml)

[Lab | Feature Extraction and Introduction to Supervised Learning](module-3/lab-supervised-learning-feature-extraction)

[Lab | Unsupervised Learning with Scikit-Learn](module-3/lab-sklearn-and-unsupervised-learning)

[Lab | Supervised Learning with Scikit-Learn](module-3/lab-supervised-learning-sklearn)

[Project | Supervised Learning](module-3/supervised-learning-project)

[Project | Unsupervised Learning (Clustering)](module-3/clustering-project)

[Lab | Machine Learning Pipelines](module-3/lab-machine-learning-pipelines)

[Lab | Supervised Learning](module-3/lab-supervised-learning)

[Lab | Unsupervised Learning](module-3/lab-unsupervised-learning)

[Project | Machine Learning Pipeline](module-3/machine-learning-pipeline-project)

[Advanced Topics: Network Analysis](module-3/lab-network-analysis)

[Advanced Topics: Topic Modeling](module-3/lab-topic-modeling)

[Advanced Topics: Apache Spark](module-3/lab-apache-spark)

## [Final Project](final-project)
