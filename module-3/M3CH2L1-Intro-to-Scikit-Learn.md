![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)


# INTRODUCTION TO SCIKIT-LEARN

## Lesson Goals

In this lesson we focus on explaining the Scikit-learn Machine Learning Toolkit:

* You will learn how to install Scikit-learn and its dependencies.
* You will learn about the functionalities of Scikit-learn that will help you in the implementation of the Machine Learning workflow in your Machine Learning projects.
* You will learn the programming model for programming Machine Learning workflows with Scikit-learn.


## Introduction
So far in this course, you have learned basic concepts and procedures required in a Machine Learning project. A summary of those is the Machine Learning workflow introduced in previous lessons. The good news now are that you do not need to program everything from bottom up, to implement a Machine Learning workflow. We are presenting you in this lesson with a Machine Learning toolkit that comes with the most relevant Machine Learning functionalities available through an API. So implementing a Machine Learning workflow is great simplified. In a nutshell, you will implement the Machine Learning workflow a series of API calls from your python program, and you will connect the output of one stage of the workflow to the input of the next in your program.



## INSTALLATION
In this section we will guide you through the process of installing scikit-learn as a python package. Scikit-learn depends on other packages, so first we have to check that those dependecies are installed.
### PYTHON PREINSTALLED
Before proceeding, let's check that python is installed and available in your computer. You can check by typing this command on a terminal window:
```text
python --version
```
If the python interpreter is installed and accessible, it will reply with a line of text like the following:
```text
Python x.y.z
```
where x.y.z is the version of the python interpreter.
### DEPENDENCIES
Scikit-learn depends on NumPy and SciPy, so before proceeding to install the scikit-learn package, we will check the availability of the numpy and scipy packages. Since at this point, we have already checked that the python interpreter is installed and accessible, we can invoke the python interpreter asking it to load numpy, and it will reply with an error if numpy is unavailable. It can be done on a single line, at the command prompt in a terminal, just write:
```text
python -c "import numpy"
```
The -c command line option, tells python to executed the parameter string as a python program. The python interpreter will try load the numpy package. If the numpy package is not installed, the python interpreter will print a message similar to "ImportError: No module named 'numpy'".

Now we will check the installation of the scipy package in a similar way. Just type at the command prompt:
```text
python -c "import scipy"
```
if no error is reported, then it means that the scipy package is installed and accessible to the python interpreter.
If either of the packages is not installed, you can install it with the following command written at the terminal prompt:
```text
pip install thePackage
```
where you should replace thePackage with the name of the package to be installed.

### INSTALLATION OF THE SCIKIT-LEARN PACKAGE
So far you have checked that the required dependencies of the scikit-learn package are in place, so now you are ready to proceed to install the scikit-learn package.
The quickest and easiest way is to install the scikit-learn package using pip. At the terminal's command line, you should write:
```text
pip install -U scikit-learn
```

Check the proper installation by asking the python interpreter to import scikit-learn and print the package's version number. At the terminal command prompt, write:
```text
python3 -c "import sklearn; print(sklearn.__version__)"
```
If everything is alright, the version number in the x.y.z will be output.
Now, you are ready to go!


## MAIN FUNCTIONALITIES
At this point, you may be wondering exactly what functionalities scikit-learn can provide, and how you will  use them. These topics will be explained in two stages. First, and for the remaining of this lessons you will learn what scikit-learn can do for you. We will review the functionalities most relevant to you, so that you can establish a parallelism with the Machine Learning workflow explained in an earlier lesson of this module. Scikit-learn provides all the functionalities required to implement the Machine Learning workflow that you learned. Let's review them. 
### LOAD DATASET
Scikit-learn comes bundled with several well known public datasets, to take you up to speed quickly, avoiding the hassle of finding and downloading datasets from the web. These bundled datasets can be loaded by name without even providing a path to the dataset file. This is an example:
```python
from sklearn import datasets
diabetesDataset= datasets.load_diabetes()
```
Surely, scikit-learn is also prepared for loading other datasets from your storage devices, like a hard disk, given a path to the file. 
### PREPROCESS DATASET
Once the dataset is loaded, we will have to perform transformations on the data to make it operational for Machine Learning, as discussed on the lesson "Machine Learning Workflow". Scikit-Learn provides multiple functionalities to help you with these transformations. One typical tranformation is to express a symbolic feature using a numeric valued range. For instance, let's consider feature A that can take values from a set of symbols {a, b, c, d}. This might applicable to a feature employment_status taking values from the discrete set of symbols {unemployed,  employed, under_age, retired}. One option might be transforming the discrete valued feature A into a an integer valued feature A' taking values from the set of integers {1, 2, 3, 4} where "unemployed" has been mapped to the integer 1, "employed" to integer 2, "under_age" to the integer 3 and "retired" to the integer 4. This first solution to the problem of mapping a symbolic attribute to a numeric valued attribute may cause trouble down the road. Indirectly we have imposed a metric in instance space that was not present originally. In the case of the original symbolic feature A, datapoints with all features equal, except for the value of A, were equally distant, "meaning" that unmeployed was as different from "employed" as it was from "retired". But after the mapping to numeric values, if feature A' is considered, now we have inadvertently imposed that "unemployed" is more similar to "employed" that to "retired", because integer 1 is closer to integer 2, than it is to integer 4.
To solve this unwanted problem, the one out of n representations is used. This means that every symbols is mapped to a vector where all the entries are 0 except for one that has value 1. In our example:
- "unemployed" is mapped to [1, 0, 0, 0]
- "employed" is mapped to [0, 1, 0, 0]
- "under-age" is mapped to [0, 0, 1, 0]
- "retired" is mapped to [0, 0, 0, 1]
This mapping is performed by Scikit-Learn using the class DictVectorizer. And it preserves the original metric: the original symbolic are equally distant after the mapping as they were before.
### FEATURE SELECTION
This is another stage of our Machine Learning workflow for which Scikit-Learn provides support. As mentioned previously on this course, it pays off to study the original features describing the instances on the raw data and to choos only those features that provide greatest class discernment power. This task is also known as dimentsionality reduction, since initially instances are represented by a vector of n features, and after feature selection, we have only kept a subset of the original features, so that an instance is now represented by a vector of only k features, where k<n.
One typical feature selection method that Scikit-Learn provides is to perform the chi-square test on the symbolic features and return the best k symbolic features. The chi-square test measures the independency of two variables. In Machine Learning we hypothesize that the target feature (dependent variable) that we want to estimate, is dependent on the rest of features (the independent variables/features). So if we discover that the target feature that provides the class label, is independent from another feature F, then we can discard F to attain dimensionality reduction. This functionality is provided by the SelectKBest class in the feature_selection module of Scikit-Learn.
### TRAIN A MODEL
This is the core functionality of Scikit-Learn. It provides a variety of Machine Learning algorithms grouped according to the availability of teaching signal criterion. In previous lessons the interpretation of a training set as a set of problems was introduced. If a supervisor provided the solutions, then we can perform supervised Machine Learning. If no solutions are available then we are restricted to unsupervised Machine Learning. According to this division between supervised and unsupervised Machine Learning, Scikit-Learn provides the most popular, or widely used, Machine Learning algorithms:
* Supervised Machine Learning
	* Ordinary Least Squares
	* Logistic Regression
	* Support Vector Machines
	* Stochastic Gradient Descent
	* K-Nearest Neighbors
	* Naive Bayes
	* ID3
	* Artificial Neural Networks
* Unsupervised Machine Learning
	* K-Means
	* Spectral Clustering
	* Hierarchical Clustering
	

### MODEL SELECTION AND EVALUATION
Scikit-Learn test and tuning functionalities include the functionalities that were introduced in the previous lessons. The main test functionalities you will need are:
* Cross-Validation
* Kappa statistic
* Accuracy
* Precision, recall, F1
* Mean squared error
these functionalities are available as functions from the sklearn.metrics package.
For model selection, you will be able to perform hyper-parameter tuning using the GridSearchCV class in sklearn.model_selection
### VISUALIZATION
Matplotlib is a visualization python library independent of Scikit-Learn but that is very convenient to use together with Scikit-Learn. The basic procedure for using the matplotlib library to visualize a scikit-learn dataset is:
1. import the library
2. create a subplot (this will return an axes object)
3. use a method of the axes object to specify the type of plot (for instance "scatter")
4. use the plot method of the axes object to generate the plot
5. display the plot with the method show()
You will see examples of this in the following lessons that you will be able to reuse as templates for your own projects.
## PROGRAMMING MODEL
In the preceding sections we have reviewed the functionalities that Scikit-learn provides that are helpful for the implementation of our Machine Learning workflow. Now you need to learn how to use those functionalities effectively. The programming model tells you the basic method to follow:
1. import the appropriate libraries
2. use the sklearn API to invoke methods performing the desired functionality (like reading a dataset from a file, or training a Machine Learning model on a preexisting dataset).
3. the invocation will return an object with its attributes documented by the sklearn API
4. iterate from step 2 with the next functionality of the Machine Learning workflow
So, the main idea is to implement the abstract idea of our Machine Learning workflow as a series of invocations to the sklearn API, where in general the return values of one call are all or some of them only, used as parameters to the next call.





## Summary

In this chapter, you have learned what Scikit.learn can do for you: its functionalities, accessible by means of API calls, help you implement the Machine Learning workflow explained in previous lessons. You have also learned how to install Scikit.learn and its dependencies. At this moment, you don't need to know about all the extensive functionalities that Scikit-learn provides. We have outlined the most relevant to you for each stage of the Machine Learning workflow. And we have introduced some concepts and techniques that will be useful to you in developing projects, and that you can implement inkoking the Scikit-learn API. Now that you know what Scikit-learn can do for you, in the following lessons, you will be presented with programming examples of the key functionalities, so that you can reuse them as a template in your projects.
