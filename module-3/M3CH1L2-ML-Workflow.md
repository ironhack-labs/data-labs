![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)


# MACHINE LEARNING WORKFLOW

## Lesson Goals

In this lesson you will learn:

* 1 The procedure to apply ML.
* 2 The inputs and outputs of every stage of the procedure.
* 3 The role of experiments in ML.


## Introduction
At this moment you may be wondering how to apply ML to a problem. This lessons provides the answers by breaking down the process into stages, explaining each stage, including the expected inputs and outputs. The ML workflow is composed of a series of subprocesses, or stages, so that the output of one subprocess is fed as input to the next subprocess. A helpful visual image is a pipeline connecting multiple processing machines. Let's consider as a running example for this lesson an application to eHealth: a project for mining eHRs (electronic Health Records) to improve the quality and effectiveness of health care. More concretely, let's consider the problem of predicting the outcome of a medical treatment prescribed to a patient. Every patient is represented by an instance composed of a set of attributes describing the patient: for instance, age, gender, height, weight, risk factors, medication, daily dosage, amount of intakes per day, dosage per intake, lowest blood pressure value, highest blood presure value, ... You can think of a patient as a vector of values, which are the independent variables. We use ML to learn a model to estimate the value of the dependent variable "efficacy of treatment" that we can model as a real variable in the range [0, 1] with 0 meaning that the treatment is totally ineffective and 1 meaning totally effective. To evaluate the estimation produced by ML, we may compare the estimated value to the actual value, and consider the estimation as accurate anough if the difference is 3% at most. 

## ETL
ETL stands for **Extraction, Transformation and Loading** of data. And it is a preliminary process that has to be completed before proceeding to the application of ML.
In the **Extraction** phase data is imported from data sources to a data storage with a single unified view, like a Data Warehouse. The data sources may be heterogeneous and distributed. For instance, in our eHealth example the medical history of a patient may be distributed across different databases belonging to the same or different health systems.
In the **Transformation** phase the extracted data is homogenized. This includes transforming the data in the following ways:
- Conversion: magnitudes expressed in different units are all converted to a single reference unit. For instance, all volume magnitudes are converted to milliliters (ml).
- Remove outliers: an outlier is a data point that clearly does not belong to the distribution of the rest of the dataset. In our eHealth example we can consider that an age of 121 years is certainly an outlier not belonging to the distribution of a representative sample of the general population. Whatever ML lears from the analysis of this instance is highly likely to not be applicable to the rest of the population. So the outlier is removed. There is another reason to remove the outlier from the data quality perspective. As we will see in the next bullet point, scaling the range of the age variable so that the highest age is mapped to 1, would make the rest of the mapped values to be inadequately compressed.
- Scaling: all variables are scaled so that they take values from the same range, typically this range is [0, 1] (then the transformation is also known as *Normalization*). This is done to avoid bias effects in error metrics. For instance, consider variable A whose range is [0, 1] and variable B whose range is [0, 100]. A 10% error in the measurement of A would cause a "noise" of 0.01, but the same percentage of error in variable B would add a "noise" of 10. Thus the overall error might be dominated by errors in B due to scaling reasons, but not necessarily because of the right reason (possibly B has more influence in estimating the right value). Note that if we use algorithm M to scale the training data, then we will have to scale input data with the same M before inputting it to the model learned by ML.
- Rounding: all real values are rounded to the same amount of decimal figures. For instance 0.333333333333 becomes 0.3333.
- Standardization: transform the data so that it has zero mean (aka mean removal) and unit variance (variance rescaling). For instance, w= (x-mean)/ sigma.
- Shuffling: when working with datasets contained in files (for instance ARFF files, or CSV files) it makes sense to shuffle the instances, otherwise other operations that will happen later in this workflow might be biased. In our eHealth example, if we have the dataset ordered by gender, and train the model on the first half, and test it with the second, we would be applying the knowledge learned from the female population to the male population, which might bias the estimations.
After the dataset has been transformed, the **Loading** phase is executed to store the resulting dataset into a data store, for instance a database.

## SAMPLING
After we have performed ETL on the raw data, we need to split the transformed dataset. At this point you have the option to apply ML in different ways (that will be explained in the following sections). The option that choose is called your "Experimental Design". Depending on this experimental design you will need to split your transformed dataset in different ways. For the time being, it is enough to know about the simplest experimental design, known as train-test split. The train-test split means that the transformed dataset is divided into two disjoint subsets: one subset that will be used for training ML (known as the **Training Set**), and another to test the model learned by ML (known as the **Test Set**).
Note that the sampling used to select the train set and the test set must be random. If the transformed dataset is contained in a text file, it is very helpful to have this file shuffled during ETL (as mentioned in the preceding section).
### HOLDOUT SET
A Holdout Set is a subset that we obtain from the transformed dataset, and that is not available to ML during the training phase (this phase is explained in the next section). In the case of the train-test split, the subset used to test the ML model is a holdout set known as the **Test Set**. And it is very important that this test set not be available to ML during training.

## TRAINING
After the Train Set is available as a result of the completion of the sampling phase, we are ready to put ML to work. Our first step is to select the ML algorithm. You will learn about the ML algorithms available to you in a forthcoming lesson, for the time being it will enough to choose a simple one, like ID3, because the details of how it works and its implementation do not matter at this time.
After you have selected the ML algorithm, you train it on the Training Set. This is usually as simple as configuring/initializing some variables, and making an invocation to a method in a ML toolkit. You will learn how to do this in Python using the Scikit-Learn ML toolkit, and you will see that it is a simple procedure.
### WHAT HAPPENS DURING TRAINING?
During training the ML algorithm looks for regularities that are indicative of the value of the target attribute. In our eHealth example, it might discover that for males over 40 years, suffering diabetes, a dosage over 10ml per intake more than twice a day has a low efficacy of 0.12. After finding this pattern/regularity ML incorporates this piece of discovered knowledge to the model it produces.

The output of the training phase is the ML model, that incorporates the knowledge learned by ML, and can be queried to solve unseen problems (new problems different from those present in the training set).

## TESTING
Now, you might be wondering "how good is the model for solving new problems?". This is the question that the testing phase answers by computing the value of a **quality metric**. Usually you will have a threshold value for this quality metric, meaning that for the model to be usefull the value of its quality metric must be equal or greater to the threshold value. Let's see this with our example eHealth application. Imagine that a medical specialist can predict the efficacy of a treatment for a control cohort with an accuracy of 67%. If the ML model trained to perform the same function only reaches 47% it will not be useful. So in this problem, the treshold value for the accuracy is set to 67%. If the accuracy of the ML model is greater than or equal to 67%, the we can conclude that the ML model may be useful.

Depending on the problem that you are trying to solve by applying ML, you will choose a particular quality metric. In our eHealth example, we might define our quality metric as the percentage of estimations of the ML model that fall within 3% of the real value.

It is important to note that the test set cannot be used for training. The fact that ML is trained with a training set of solved problems (supervised ML), and the fact that it solves those problems well, does not provide any useful information on how well it generalizes (how well it solves *new* problems). 


## EXPERIMENTAL DESIGN
ML is an experimental science. This means that when you approach a new problem, you don't know a priori what ML algorithm will solve the problem satisfactorily. So you have to try different algorithms and analyze what happens. Every time you perform one of these trials you are actually making a ML experiment. That is why it is said that ML is an experimental science.
Before you perform any ML experiment, you have to think about how you will proceed. This is what is called the experimental design. Next, you will learn about the most common expèrimental designs that you can try out in solving ML problems.
### TRAIN-TEST SPLIT
We have already introduced this experimental design in the preceding sections. You proceed by randomly splitting the dataset into disjoint training set and test set. Then you train with the training set and evaluate how good the learned model is by feeding it the test set and comparing the model's estimations to those of the test set.
### CROSS VALIDATION
There is a probability that the train-test split, tests the model on the only subset where it performs well, thus providing an unreliable quality metric. To reduce this probability, you can test on many different test sets and compute an average of the individual quality metrics thus obtained. This is what cross validation does. The procedure is:
1. randomly partition the dataset in n bins.
2. for every bin b
    * train with the remaining n-1 bins
    * test with b and obtain quality metric
3. output the average of the n quality metrics thus obtained.


### TRAIN-VALIDATION-TEST SPLIT
The training of some ML algorithms may be interpreted as learning a set of parameters that minimize the estimation error of the resulting model. How these parameters are learned is controlled by another set of parameters, that are called hyper parameters to avoid the confusion between both sets of parameters. Typical examples of this kind of ML paradigms are SVMs (Support Vector Machines) and Artificial Neural Networks.
The basic procedure is:
```text
    	randomly partition the dataset in 3 disjoint subsets, namely the training, validation and test sets.
	initialize the hyperparameters
	do
		train with the train set
		evaluate on validation set 
		update best performing hyperparameters
		recompute/modify the hyperparameters
	while maximum amt of iterations not reached
	using the best performing hyperparameters, compute the definitive quality metric on the test set 
```
## Summary

In this chapter, you have learned the workflow of ML: ETL, sampling, training and testing. Every time you execute this workflow you have performed one ML experiment, for which you have obtain a quality metric. At this point, you may wish to improve the quality metric, and consequently you may want to perform another experiment changing something, for instance the ML algorithm being used. As you see, this is an iterative process, and ML is an experimental science. 
