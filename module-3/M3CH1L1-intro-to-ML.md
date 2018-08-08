![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Introduction to Machine Learning

## Lesson Goals

In this lesson you will start to learn about Machine Learning, more concretely:

* 1 You will learn what Machine Learning does.
* 2 You will learn about the main types of Machine Learning.
* 3 You will lear what types of problems you can apply Machine Learning to.


## Introduction

Machine Learning is a fundamental part of Data Science, and of Artificial Intelligence as well. It is an important technology for leveraging data to make informed data-driven decisions, and for creating business value from datasets. Machine Learning benefits from contributions from fields like Probability Theory, Statistics, Information Theory, Statistical Learning Theory and Symbolic Reasoning. Currently, there are hundreds of ML algorithms, but don't worry, you don't have to learn them all to be able to use ML effectively. At the beginning it makes the most sense to learn about the basic concepts, the main types of ML algorithms, what you can expect, and to learn a basic methodology to use ML. The good news are that that is enough to leverage ML for solving many real world problems. This lesson is about the "what": what is Machine Learning, what Machine Learning does, what are the types of Machine Learning, what problems you can solve with Machine Learning... But get ready because we are going to discuss the "how" soon, in the coming lessons.


## What is Machine Learning?

Machine Learning (ML) is the capability that a software may have to learn from experience. For instance, the software used to compute the payroll of a small business does not typically have the capability of learning; but the software used by a car insurance company to estimate the cost of premiums, usually has the capability of ML to differentiate cases of high risk from cases of low risk.

Experience is typically provided in the form of a dataset, that contains inherent patterns or regularities hidden in the data. In the car insurance case, that dataset may be contained in a historical database, containing customer profiles, claim history, pricing, policies, a temporal series of risk scores, and others. This database contains inherent patterns that ML can discover, and which provide business value. For instance, ML may be used to find the most prevalent profiles of customers of car insurance, most likely to purchase home insurance from the same provider. This information has business value since it can help to improve the targeting of cross selling campaigns.

ML is a fundamental part of both Data Science, and Artificial Intelligence. You will gain a better understanding of ML by looking at it from both perspectives.

### The Data Science Perspective
The preceding use case of ML in the insurance sector, can be seen as a problem in inferential statistics, where each existing car insurance customer is assigned a score measuring the propensity of acquiring home insurance from the same company. This score is actually the inferred a posteriori probability provided by a model trained on a historical database containing data from both, past customers that purchased home insurance after the having purchased car insurance from the same provider, and from those who didn't.

### The Artificial Intelligence Perspective
There has been an ongoing controversy regarding the definition of Artificial Intelligence, although the following seems to be a good consensus definition:
Artificial Intelligence (AI) is the capability of computer systems to
1. learn knowledge from experience, and
2. use that knowledge to solve problems.
Criterion number 1 is telling us that ML is a requisite ingredient of AI systems.
In our car insurance example, the knowledge learned from the past experience contained in the historical database, will be used to categorize current and future car insurance clients as good or bad targets for the home insurance cross selling campaign.

Both perspectives provide different views of the same reality: ML finds regularities (aka patterns) from datasets that can be incorporated to decision making software to improve the solution given to decision problems by leveraging data-driven criteria.

## Types of Machine Learning.
In your professional practice you will face many different data analytics projects. Different projects may ask for different ML approaches or solutions. It will be very helpful to know the different types of ML available when evaluating the suitability of candidate approaches.

### Types According to Representation Level
So far in this lesson, you have learned that ML analyzes datasets and extracts some knowledge from that process in the form of a model, that will be applied to current and new data, to solve problems like identifying the best cross selling targets. The knowledge that ML extracts from the data may have a low level or high level of representation (aka similarity with how humans represent knowledge). 
Let's illustrate this with our car insurance use case. One of the early decisions in applying ML is deciding what ML algorithm to use. Let's consider two typical decisions applicable in this use case:
1. we use an Artificial Neural Network with error backpropagation. The knowledge this algorithm learns is represented as a sequence of real numbers that encode the (inverse) electrical resistance that an electrical signal would encounter when travelling along the link joining two neurons. This is an example of learning knowledge with a low level of representation. The representation level is so low that it cannot even represent at the symbol level (for instance it cannot perform computations using a concept/variable called risk). There are no variable identifiers available to be used in performing computations, only the real values themselves. This is what is known as **subsymbolic representation level**.
2. another typical decision might be useing as ML algorithm ID3 (Induction of Decision Trees). ID3 will analyze the dataset and extract knowledge that it will represent as a form of decision tree. This decision tree can be read and understood by a person. Moreover, the decision tree can be easily translated into a set of if-then rules, that persons can understand. Since the level of the representation in this case, is very similar to the representation of knowledge that persons use, it is called a **symbolic representation level**.

### Types According to Teaching Signal
ML learns from experience that is typically encoded in a pre-existing dataset. This dataset contains instances (like records in a database) described by sets of attributes (like the attributes of every record). In our running example, every car insurance customer would be an instance, described by a set of attributes, like age, car model category, marital status, gender, type of policy, average cost of residential sq foot in the area of his address, policy expiration date, ... All of these mostly independent attributes are used to determine the value of the target dependent attribute, in our example, the "home insurance cross selling score", measuring the propensity of future acquisition of home insurance from the same provider. If this propensity is provided by a **Teaching Signal** or **Supervisor** we say that this is a problem of **Supervised ML**. One typical practice in examples like our running example, is to consider as instances all existing customers one year ago, and use as value of propensity the fact of whether or not they also are clients of home insurance today. Thus the dataset would be completed with the propensity target value, we would apply supervised ML to the dataset, and obtain a model with one year lookahead.

Now let's imagine a different scenario: there is not teaching signal, nor supervisor, to provide the value of the target attribute. Then, clearly, supervised ML will not be applicable, and thus we will not be able to estimate our target attribute ofr every problem instance. But all is not lost, we can still aplly **Unsupervised ML**, the most typical form of which is **Clustering**. Clustering algorithms analyze all instances (car insurance clients) in the dataset and groups them into different clusters (aka segments). All similar instances are placed on the same cluster, while dissimilar instances are placed on different clusters. Moreover, any cluster contains instances that are more similar to the instances of a nearby cluster than to the instances of a distant cluster.

There is an intermmediate case between supervised and unsupervised ML, it is known as **Criticized ML** and the mostly widespread form is **Reinforcement Learning**. In criticized ML there in no supervisor to provide the correct value of the target attribute required to proceed to supervised ML. But there is a critic that will provide a wek teaching signal, it will not provide the correct solution, but it will provide some kind of evaluation like well done vs bad work, or sugar cube vs whip. In our running example this would mean that every time the production system estimates the value of the home insurance propensity score, the critic would reply with either good, tolerable or bad estimate, expecting that the ML system will then self-adapt in order to perform better in the future.

## Problems Solved by Machine Learning.
After learning some concepts about ML, now you are probably wondering, what problems can I solve with this technology? Here we explain the most common types of problems that you will be solving with ML in the future.
### Classification
In classification problems, ML is used to classify instances into a predetermined set of classes. In our running example about car insurance, a classification task for ML would be to learn a model based on current and former customers, to classify new incoming car insurance customers as high, medium or low value depending on the expected propensity to also acquire home insurance in the future. Note that in this example the classes have symbolic identifiers (e.g. "high") and are disjoint and discrete.
### Regression
In contrast to classification, in regression problems the target attribute has a continuous (real valued) range. In our car insurance example, we might use ML to estimate the cost of a car repairment from a set of photographs of the damaged parts. The output of the model would be the expected dollar cost of repairing the damage. Note that in this case, the output of the model would be a real-valued number instead of a symbol, and thus the range would be continuous as opposed to discrete.
### Prediction
In prediction you are assuming that past history is a valid indication of future events. In our car insurance example, estimating the probability of cross selling home insurance to current car insurance customers is a prediction problem. We are estimating the probability that a certain event will happen in the future, for instance, within the next year. Another typical example is to predict the value of the USD / EUR exchange rate (how many dollars you buy with one euro) tomorrow, given the time series of the last year.


## Summary

ML plays an important role in Data Science and Artificial Intelligence. ML algorithms analyze datasets, looking for regularities and predictive/indicative dependences among sets of variables. This knowledge obtained from the dataset is put into a model that can leverage it by solving new incoming problems based on data-driven criteria. The knowledge that is learned by ML may be completely unintelligible to a person (subsymbolic ML), or it can be easily understood (symbolic ML that outputs a set of if-then rules).
In some ML problems, we can leverage pre-existing datasets containing solved problems, so that ML can learn how to solve problems (that would be supervised ML). But this may not always be the case, we may only have a set of unsolved problems (unsupervised ML), or someone commenting on how satisfactory an intended solution was (criticized ML).
The main three types of ML problems are classification (discrete valued output), regression (real-valued output) and prediction (estimating a future value that may have continuous or discrete range).
