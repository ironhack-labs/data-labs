![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)


# FEATURE EXTRACTION AND ENGINEERING

## Lesson Goals

In this lesson you are going to learn:

* 1 What feature selection is.
* 2 Why you need to select features.
* 3 How to select features.


## Introduction

From the Machine Learning perspective, a dataset represents a set of problem instances. Every **instance** represents an individual case described by a set of independent variables known as attributes of the instance, or **features** of the instance. For example, in an application of financial credit assignment, every consumer applying for a loan would be represented by an instance, and each instance would be described by features such as age, marital status, amount of dependent persons, employment status, yearly income, etc. The target feature that we wish to estimate with the Machine Learning model would then be "approval" with possible values "yes" or "no".


## FEATURE SELECTION
In Machine Learning **Data Modeling** is the task of deciding how to represent an instance. There may be many features available to represent an instance, but all of them may not be necessarily useful. For instance, in our example credit application, the favorite refrigerator color of the consumer would not be relevant, and thus we would not include it in the instance representation.
Another issue that we will have to decide is the range of the attributes, it may be continuous, discrete, numeric or symbolic, and this decision may have further repercusions down the road. To illustrate this, consider our example credit application. If we model yearly income as a real valued feature, then applicant A earning $80.000 would have a different feature value from applicant B earning $80.001. But if a symbolic discrete range is used:
- low if less than $40.000
- medium if between $40.000 and $70.000
- high if above $70.000
then many instances, like A and B, that where different from the perspective of the yearly income feature, are now considered equal or equivalent.
In performing feature selection, we will also want to avoid highly correlated features, and dependent features. The reason is that adding one new highly correlated or dependent feature to the instance representation does not provide new information the Machine Learning can leverage, and it has the disadvantage of unnecessarily complicating the learning process and the resulting model. In our example, if we already have a yearly income feature, it may be redundant to include a monthly income feature.
As a general rule, a low amount of features is preferred over a high amount of features. The main reason for this to facilitate generalization: it is known that models with low complexity tend to generalize better than models with a high complexity. Using a small amount of features is one of the ways in which you can reduce model complexity.

## DISCERNMENT POWER
Machine Learning tries to learn a set of criteria that separates one class of instances from the others. So it has to learn to discern instances of one class, from instances of other classes. Features are not equally effective in separating classes, so we need a quantitave measure of the discernment power, also known as separating power, indicative power or predictive power. 

### MEASURES OF DISCERNMENT POWER
The measure of the discernement power of a feature is directly proportional to the capacity of the feature to separate classes when the dataset is partitioned according to the values of the feature.
Datasets without any partitioning may have varying levels of disorder. This disorder can be measured by the **entropy of the dataset**:
- if all instances belong to the same class (for instance, a class labeled as positive), the certainty of choosing an instance at random and that instance being positive is maximum. We interpret that the uncertainty is 0 and that this situation resembles our idea of maximum order. The entropy (i.e. disorder) in this case is equal to zero.
- if the classes are equally distributed in the dataset, then the certainty of choosing an instance at random, and that instance being of the positive class is minimum (0.5 probability in the case of 2 classes). This situation of maximum uncertainty resembles our intuitive notion of maximum disorder, so the entropy is maximum.
Given a dataset with two classes (yes / no), like the dataset of our example credit application, the entropy of the dataset D is computed as follows:
```text
entropy(D)= -p(yes)*log p(yes) - p(no) * log p(no)
```
where p(yes) is the proportion of instances of class "yes" in the dataset D, and p(no) the same for class "no". And the log is computed with base 2.

#### INFORMATION GAIN
Information Gain G(D, F) measures the discernment power of a feature F: how much the existing classes are separated when the dataset D is partitioned into subsets according to the values of the feature F. This is measured by subtracting the entropies of the subsets of the partition from the entropy of the whole dataset (intuitively, subtracting the order induced by partitioning according to F, from the pre-existing disorder of the dataset).
```text
Gain(D, F)= entropy(D)- SIGMA for v belonging to R(F) |S(v)|*entropy(S(v))/|S|
```
where S(v) is the subset of D for which all instances have v as the value of feature F.

#### THE SINGLE FEATURE ESTIMATOR
The simplest feature selection algorithm is to select the best performing k features out of a total of n>k available features, by ranking them according to the quality metrics of the single feature estimators. The procedure is
```text
	for every feature f
		train model m using only f (m is the single feature estimator)
		test m	
		keep a ranking of the k top performing features in descending quality metric order
```

### FORWARD GREEDY FEATURE SELECTION
Again, let's consider that we have to select the best performing k features out of a total of n available features. We will start considering single feature estimators, and we will extend the best single feature estimator with the best performing second feature, iterating the process until we have k features in all. Given that we have the best estimator with only q features, we would proceed as follows to obtain the best performing q+1 features:
```text
	for every remaining feature f
		m is the model resulting from adding f to the best estimator with q features
		test m
		update b which is the best feature to add so far
	the best performing q+1 features are the original q features plus feature b
```

### BACKWARD ELIMINATION
This feature selection algorithm starts with all the available features n. Then it removes the feature that produces the greatest improvement in the resulting model. And continues the process until no gain in the value of the quality metric is obtained by further elimination of a feature.

## DERIVED FEATURES
A derived feature is a new feature that you create by combining two preexisting raw features. In the example of our credit application, given the original features marital status, employment status and yearly income we might invent and test the derived boolean feature: 
```text
	marital status== married AND emplyment status== unemployed OR rearly income== low
```
How do we know whether Machine Learning will improve with our new derived feature? As mentioned previously on this chapter, Machine Learning is an experimental science, so you make the experiment of adding the new derived feature and compare the resulting quality metric with that of the original model. 


## WRAPPERS
A wrapper is a program that performs feature selection and provides the resulting feature set to the Machine Learning workflow. In our example credit application, if every applicant is described by a set of 20 features, but we suspect that not all of them are independent and informative, we may use a backward elimination wrapper, that will find the smallest best performing subset of features, let's assume that it has only 8 features, then the Machine Learning workflow would proceed from the sampling phase considering for the rest of the workflow only those 8 features.



## Summary

Data Modeling in Machine Learning includes selecting the features to be given to the Machine Learning pipeline. Usually there will be some irrelevant or dependent features that will hinder Machine Learning. The recommended practice is to perform feature selection to extract from the available features only those that are potentially useful for Machine Learning. You can perform feature selection by building a ranking in descending discernment power order, and then selecting the top k features. There are multiple options to measure the discernement power of a feature. One option that does not require training a model is computing its information gain. Options requiring training models include the method of the single method estimator, forward greedy feature selection and backward elimination. You can invent your own derived features by combining preexisting raw features. You can test whether your newly derived feature produces any imporvement by performing A/B testing (i.e. comparing the performance with and without the new feature). A wrapper is a feature selection software that provides the Machine Learning workflow with the resulting best set of features.
