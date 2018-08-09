![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)


# TITLE

## LOADING DATASETS INTO SCIKIT-LEARN

In this lesson you learn how to:

* Load Scikit-learn's bundled datasets.
* Load other external datasets of the most relevant formats.
* Visualize your dataset.


## Introduction
In your Machine Learning workflow, loading your dataset is your first stage. You will load the dataset into a data object typically a dataframe, an ndarray, a dictionary or a list. The process of loading a dataset with scikit-learn depends on the type of dataset: whether it is a dataset bundled with scikit-learn or not, and if not, depending on the format of the dataset. We will cover the cases separately, providing you with code snippets for your to reuse in the implementations of your Machine Learning workflow.


## LOAD BUNDLED DATASET

As mentioned in the lesson introducing Scikit-learn, it comes with several datasets bundled that you can load quickly from your python application. There are three datasets representing regression problems:
1. Boston house prices.
2. Diabetes.
3. Linnerud.
And four datasets representing classification problems:
1. Iris.
2. Digits.
3. Wine.
4. Breast cancer.
All of them are public open datasets, that you can use to test your Machine Learning workflows.
You can download one of these datasets and have a look at the structure using the following python code:
```python
from sklearn import datasets

# dictionary-like object
diabetesDataset= datasets.load_diabetes()
# get the data type
print(type(diabetesDataset))
# get the list of attributes of the object
print(dir(diabetesDataset))
```
If you execute the code you will get an output like this one:
```python
<class 'sklearn.utils.Bunch'>
['DESCR', 'data', 'feature_names', 'target']
```
By printing the DESCR attribute of the dataset you get its documentation informing you about what the dataset describes, amount of instances, amount of attributes, target attribute, any preprocessing already performed on the dataset, and a citation of its original source. But note that this only works for the bundled datasets.
## LOAD EXTERNAL DATASET
The datasets that come bundled with Scikit-learn are very convenient to get you started quickly with building Machine Learning workflows, and testing your code. But most of the time you will be working with external datasets that you will first download from the web, and the load from your computer storage device (e.g. your hard disk) into your python program.
### CSV FORMAT
CSV stands for "Comma Separated Values". In a csv file you have one instance per line, and attribute values are separated by commas as the name implies. The target attribute is usually the last one of the line.
In your python application, you can read a python csv dataset like this:
```python
import csv

with open(PATHTOCSV, "r") as csvfile:
    data = list(csv.reader(csvfile))
print("%d instances were read."% len(data))
```
This code reads the csv dataset into a list. If you want to read the csv dataset into a pandas DataFrame, which is often a good idea due to its flexibility and versatility, you can do:
```python
import pandas.io
theDataFrame= pandas.read_csv(path)
```
It is often a good idea to check the size and the shape of the resulting DataFrame:
```python
print("size is %s" % theDataFrame.size)
print("shape is ", end="")
print(theDataFrame.shape)
```
CSV datasets may contain a first row to be used as column or feature names. You can visualize those names by printing the value of DataFrame.columns, or DataFrame.axes.
### LIBSVM FORMAT
Libsvm is a Machine Learning library for SVMs (Support Vector Machines) developed by Chih-Chung Chang and Chih-Jen Li at NTU (National Taiwan University). Libsvm uses its own dataset format, that has grown in adoption with the popularization of Libsvm as the reference implementation of SVMs. The format of the datasets is:
[targetValue] 1:value-1 2:value-2 ... n:value-n
where value-n is the value of the nth feature. This format is specially convenient for large sparse datasets, since only the nonzero entries need to be presented, and they are preceded by their ordinal value, which makes parsing easy.
Use the load_svMachine Learningight_file() method to load a libsvm dataset:
```python
from sklearn.datasets import load_svMachine Learningight_file
X_train, y_train = load_svMachine Learningight_file(path)
```
the first return type is scipy.sparse.csr.csr_matrix and the second is numpy.ndarray.
### JSON FORMAT
JSON is a popular data format. JSON stands for (JavaScript Object Notation) and it is documented at www.json.org. A JSON object is a sequence of label:value pairs, conceptually similar to a python dictionary or database record. To read a JSON dataset into a pandas DataFrame you can use this code:
```python
import pandas.io
data_df = pandas.read_json(path)
```

## DATASET GENERATOR
Instead of looking for the appropriate dataset, downloading it, and reading it, to test your workflow, you can also create a synthetic dataset according to your needs, using Scikit-learn. For instance, you can use sklearn.datasets.make_classification() to generate a synthetic dataset to test your classification workflow:
```python
from sklearn import datasets
featureVectors, targets= datasets.make_classification(amt_instances, amt_features, amt_classes)
```

## PLOT THE DATASET
After loading your dataset into a python data object, and inspecting the shape of the data object, you will usually need to visualize the dataset to determine whether any correlations, symmetries or regularities are present. You can use matplotlib for this. First you need to import the appropriate modules:
```python
import matplotlib
import matplotlib.pyplot as pyplot
```
You will need to read your dataset, for instance:
```python
with open(PATHTOCSV, "r") as csvfile:
    data = list(csv.reader(csvfile))
print("%d instances were read."% len(data))
```
One informative visualization is the scatter plot, where the projections of the datapoints to any given two axes are shown, with different coloring of the projected point depending on the class value. Assuming that the class values 0 and 1 are at the beginning of the CSV line, we can segment our dataset separating the instances of class 0 from the instances of class 1:

```python
# separate vectors into segments according to their class value
segment0= list(filter(lambda e: e[0].startswith("0"), data))
segment1= list(filter(lambda e: e[0].startswith("1"), data))
```
Then, assuming that attribute 1 has index equal to INDEX1 in the CSV line, and attribute 2 has index INDEX2, we can create lists with their values for the case of class 0, and for the case of class 1:
```python
att1Segment0List= list(map(lambda e: strToFloat(e[INDEX1]), segment0))
att2Segment0List= list(map(lambda e: strToFloat(e[INDEX2]), segment0))
att1Segment1List= list(map(lambda e: strToFloat(e[INDEX1]), segment1))
att2Segment1List= list(map(lambda e: strToFloat(e[INDEX2]), segment1))
```
Then we use matplotlib to scatter plot attribute 1 versus attribute 2, using a differentiating color according to class value:
```python
pyplot.scatter(att1Segment0List, att2Segment0List, c="red", alpha=0.1)
# alpha's range: 0 (transparent) ... 1 (opaque).
pyplot.scatter(att1Segment1List, att2Segment1List, c='blue', marker="x", alpha=0.05)
xLabel= "att%d" % INDEX1
yLabel= "att%d" % INDEX2
pyplot.xlabel(xLabel)
pyplot.ylabel(yLabel)
pyplot.show()
```
You can adapt the above code snippets to your own project and class values, and visualize your dataset from different perspectives/projections before moving on with the Machine Learning workflow.



## Summary

In this chapter, you have learned about the most popular dataset formats in Machine Learning, and how to load those datasets to a data object in your python program using Scikit-learn. The methods you will use for reading the dataset depend on the dataset format: CSV, libsvm, JSON have been presented in this lesson. They will cover your most usual needs. Inspecting the data object where the dataset was loaded is usually a good idea. You have learned several ways to do it that you can reuse in your projects. Plotting the dataset before proceeding to training is usually a good idea also. You have learned from several code snippets, how to load, segment and plot a 2 dimensional projection of a possibly higher dimension dataset.
