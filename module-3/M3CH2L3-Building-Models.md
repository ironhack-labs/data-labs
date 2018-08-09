![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)


# BUILDING AND SAVING MODELS

## Lesson Goals

In this lesson you are going to learn the concrete details of:

* How to perform grid search.
* How to train a Machine Learning model.
* How to save the model and read it later.


## Introduction

As introduced in the Machine Learning Workflow lesson, training Machine Learning models and testing them are two core activities. Fortunately, Scikit-learn makes those activities pain-free for us. We will show you how to do them with Scikit-learn, providing an example, and code snippets for you to reuse as templates. So let's get started!


## SOLVING A SIMPLE MACHINE LEARNING PROBLEM
In this lesson we will solve a simple Machine Learning problem using Scikit-learn. The problem we will use as example is the iris plant classification problem. Depending on length and width of petals and sepals, iris plants can be classified into three classes:
1. Iris Setosa
2. Iris Versicolour
3. Iris Virginica
We are given a dataset with 150 instances of plants and their correct classification. Every instance is represented by four attributes:
1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
The Machine Learning problem is to make a Machine Learning algorithm learn to classify iris plants correctly using knowledge learned from the dataset. To determine how good the Machine Learning model is, we will test it using cross validation.


## LOAD THE DATASET
We start by loading the iris dataset bundled with Scikit-learn using the following function:
```python
def loadBundledDataset():
    # dictionary-like object
    iris_dataset = datasets.load_iris()
     # get the data type
    print(type(iris_dataset))
    # get the list of attributes of the object
    print(dir(iris_dataset))
    return iris_dataset
```
The function also prints to the console some valuable information, like the class of the object and its structure:
```python
<class 'sklearn.utils.Bunch'>
['DESCR', 'data', 'feature_names', 'target', 'target_names']
```

## TRAIN AND TEST A MODEL
For training our model with the Iris dataset we will use a Machine Learning algorithm known as Ridge Regression, which is a regularized version of Least Squares. For the time being, you do not need to know all the internals of Ridge Regression to be able to use it effectively in this lesson. You only need to know that Ridge Regression has a regularization parameter known as alpha. This parameter regulates how the algorithm learns from the data, and as you may remember from previous lessons, is called a hyper parameter. So now, we have to fix the value of this hyper parameter before execution the Ridge Regression. Since we don't know which value might perform well (remember that Machine Learning is an experimental science), we are going to do a **grid search**. In our grid search for the right value of alpha, we will train Ridge Regression models using different values of alpha, and we will take note of what value of alpha provides the best performance. We generate all real values from 0.1 to 10 using a 0.01 interval:
```python
# alpha is the regularization parameter
# numpy.arange creates an array given start, end and step values
alphaValuesArr= numpy.arange(0.1, 10, 0.01)
```
then, for every value of alpha, we create a Ridge Regression model and evaluate it with 5-fold cross validation:
```python
model = linear_model.RidgeCV(alphas = alphaValuesArr, cv=5)
model.fit(vectors, targetvalues)

print("best alpha is %f" % model.alpha_)
```
This is the best value for alpha obtained by executing our grid search:
```python
best alpha is 0.100000
```
we use the best value for alpha to obtain the cross validation accuracy:
```python
# now train with the best alpha
ridge_reg_model = linear_model.Ridge (alpha = model.alpha_)
# return value is array of scores
scores = cross_val_score(ridge_reg_model, vectors, targetvalues, cv=5)
# use as quality metric the average CV score
meanCvAccuracy= scores.mean()
print("Mean CV accuracy= %f" % meanCvAccuracy)
```
and this is what we get:
```python
Mean CV accuracy= 0.322745
```
The result is not very good... it means that the model learned by Machine Learning is expected to be correct approximately one third of the times. What went wrong?
Let's look at our dataset and print the distribution of class values:
```python
print(targetvalues)
```
we get an output like this one:
```text
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
 2 2]
```
the instances of the dataset are perfectly sorted according to class values. Let's illustrate with an example why this is detrimental to the performance: if we trained with the first half of instances and tested with the seconf half of instances, we would not be training with class 2 instance at all, and yet we would be testing with ALL class 2 instances.
A good practice to avoid this undesired side effects is to shuffle the dataset before any training takes place:
```python
# without this shuffling results are much worse!
vectors, targetvalues= utils.shuffle(dataset.data, dataset.target)
print(targetvalues)
```
utils.shuffle() carefully shuffles the two parallel arrays dataset.data and dataset.target, so that after the shuffling, vectors and targetvalues are still parallel arrays. This means that the third vector and third target values of the original arrays are both shuffled to another ordinal position n, which is the same for both, so that parallellism is maintained. When the targetvalues array is printed we obtain this:
```text
[2 2 0 2 1 0 0 2 2 1 1 2 1 1 1 0 1 1 0 2 2 1 1 2 0 0 2 0 1 2 0 1 1 1 1 0 0
 2 0 0 2 2 2 2 2 0 2 0 2 1 1 1 0 1 2 1 2 1 2 2 0 2 1 2 2 2 1 0 2 0 1 0 2 1
 0 1 1 2 2 1 1 1 0 2 1 2 0 0 2 2 0 0 1 0 0 1 1 0 0 2 0 2 1 2 1 0 2 0 0 1 1
 0 1 0 1 1 1 2 0 2 0 1 0 1 0 2 1 2 0 0 2 0 0 0 0 1 2 1 0 2 2 2 0 2 0 1 1 2
 1 0]
```
which is indicative that instances are no longer sorted according to target class value. If we proceed to grid search again, now we get a slightly different best value for alpha:
```python
best alpha is 0.950000
```
with this alpha value, we perform cross validation again getting a new and much improved accuracy:
```text
Mean CV accuracy= 0.922372
```
which is a good result indeed.

Finally, we use the best value for alpha for training our model on the whole dataset:
```python
# train with the whole dataset
ridge_reg_model.fit(dataset.data, dataset.target)
```

## SAVE THE MODEL
For saving the model, which is an object, we will serialize it and then save it as a text string:
```python
import pickle
# serialize and save the model
pickle.dump(ridge_reg_model, open(MODELPATH, "wb"))
```
where MODELPATH is a string containing the path to the file containing the model.

## USE A SAVED MODEL
To close the loop, we now show you how to deserialize the model and use it to predict the class value of an instance:
```python
# read the file and deserialize the model
retrieved_model= pickle.load( open( MODELPATH, "rb" ) )
result= retrieved_model.predict([[1, 0.4, 0.5, 0.6]])
print(result)
```



## Summary

In this chapter, you have learned how to load a dataset, shuffle it, perform grid search, train a model, save it to file, read the model from file, and use it to classify instances. Congratulations: that is a lot and it will take you far. By reusing the code snippets provided you will be able to complete quickly many Machine Learning assignments.
