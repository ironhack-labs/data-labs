![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Data Analysis with Pandas

## Introduction

Pandas can be an incredible tool for making data analysis accessible. We are able to use this Python library to perform exploratory data analysis and find relationships in our data. In this guided project we will explore a dataset describing the performance in math of a sample of students from two school districts in Portugal. 

## Loading the Data

In this example we will be using Jupyter notebooks to analyze the data.

First we load the dataset

```
import numpy as np
import pandas as pd

student = pd.read_csv('./data/student-mat.csv')
```
Let's see how many columns this dataset has and what they contain:

```
student.dtypes()
school        object
sex           object
age            int64
address       object
famsize       object
Pstatus       object
Medu           int64
Fedu           int64
Mjob          object
Fjob          object
reason        object
guardian      object
traveltime     int64
studytime      int64
failures       int64
schoolsup     object
famsup        object
paid          object
activities    object
nursery       object
higher        object
internet      object
romantic      object
famrel         int64
freetime       int64
goout          int64
Dalc           int64
Walc           int64
health         int64
absences       int64
G1             int64
G2             int64
G3             int64
dtype: object
```

We can see that there are 17 object columns (columns that contain strings) and 16 integer columns. We can learn more about the data from the data dictionary. In general, we should examine the data dictionary when examining a new dataset.

```
1 school - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)
2 sex - student's sex (binary: 'F' - female or 'M' - male)
3 age - student's age (numeric: from 15 to 22)
4 address - student's home address type (binary: 'U' - urban or 'R' - rural)
5 famsize - family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)
6 Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)
7 Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
8 Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
9 Mjob - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
10 Fjob - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
11 reason - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')
12 guardian - student's guardian (nominal: 'mother', 'father' or 'other')
13 traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
14 studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
15 failures - number of past class failures (numeric: n if 1<=n<3, else 4)
16 schoolsup - extra educational support (binary: yes or no)
17 famsup - family educational support (binary: yes or no)
18 paid - extra paid classes within the course subject (binary: yes or no)
19 activities - extra-curricular activities (binary: yes or no)
20 nursery - attended nursery school (binary: yes or no)
21 higher - wants to take higher education (binary: yes or no)
22 internet - Internet access at home (binary: yes or no)
23 romantic - with a romantic relationship (binary: yes or no)
24 famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
25 freetime - free time after school (numeric: from 1 - very low to 5 - very high)
26 goout - going out with friends (numeric: from 1 - very low to 5 - very high)
27 Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
28 Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
29 health - current health status (numeric: from 1 - very bad to 5 - very good)
30 absences - number of school absences (numeric: from 0 to 93)
31 G1 - first period grade (numeric: from 0 to 20)
31 G2 - second period grade (numeric: from 0 to 20)
32 G3 - final grade (numeric: from 0 to 20, output target)
```

## Describing the Data

Let's look at the numeric columns in the dataset using the `describe` function:

```
student.describe()
 	    age 	Medu 	        Fedu 	    traveltime 	        studytime 	failures 	famrel 	        freetime 	goout 	        Dalc 	        Walc 	        health 	        absences 	G1 	        G2 	        G3
count 	395.000000 	395.000000 	395.000000 	395.000000 	395.000000 	395.000000 	395.000000 	395.000000 	395.000000 	395.000000 	395.000000 	395.000000 	395.000000 	395.000000 	395.000000 	395.000000
mean 	16.696203 	2.749367 	2.521519 	1.448101 	2.035443 	0.334177 	3.944304 	3.235443 	3.108861 	1.481013 	2.291139 	3.554430 	5.708861 	10.908861 	10.713924 	10.415190
std 	1.276043 	1.094735 	1.088201 	0.697505 	0.839240 	0.743651 	0.896659 	0.998862 	1.113278 	0.890741 	1.287897 	1.390303 	8.003096 	3.319195 	3.761505 	4.581443
min 	15.000000 	0.000000 	0.000000 	1.000000 	1.000000 	0.000000 	1.000000 	1.000000 	1.000000 	1.000000 	1.000000 	1.000000 	0.000000 	3.000000 	0.000000 	0.000000
25% 	16.000000 	2.000000 	2.000000 	1.000000 	1.000000 	0.000000 	4.000000 	3.000000 	2.000000 	1.000000 	1.000000 	3.000000 	0.000000 	8.000000 	9.000000 	8.000000
50% 	17.000000 	3.000000 	2.000000 	1.000000 	2.000000 	0.000000 	4.000000 	3.000000 	3.000000 	1.000000 	2.000000 	4.000000 	4.000000 	11.000000 	11.000000 	11.000000
75% 	18.000000 	4.000000 	3.000000 	2.000000 	2.000000 	0.000000 	5.000000 	4.000000 	4.000000 	2.000000 	3.000000 	5.000000 	8.000000 	13.000000 	13.000000 	14.000000
max 	22.000000 	4.000000 	4.000000 	4.000000 	4.000000 	3.000000 	5.000000 	5.000000 	5.000000 	5.000000 	5.000000 	5.000000 	75.000000 	19.000000 	19.000000 	20.000000
```

Some observations regarding the data:

- The median age in this group is 17 (with a mean of 16.696).
- The median travel time is under 15 minutes.
- With one student having 75 absences and the mean being slightly larger than the median, we can assume the data is skewed and this student with 75 absences is an outlier
- The mean and median grade stayed pretty similar throughout the year with the mean fluctuating between 10 and 11 and the median fluctuating between 13 and 14.

We can also try to make some inferences regarding the variables that contain characters.

We can do this using the `crosstab` function. Using this function we can find the count of each value in the variable. We can also find the counts for multiple variables at once.

For example, we would like to know how many males and how many females are in this survey

```
pd.crosstab(index=student.sex, columns="count")
col_0 	count
sex 	
F 	208
M 	187
```

So here we see that there are slightly more males than females in the survey.

We can also look at the breakdown of students who participate in extracurricular activities by sex.

```
pd.crosstab(index=student.sex, columns=student.activities)
activities 	no 	yes
sex 		
F 	        112 	96
M 	        82 	105
```

It seems like the proportion of males participating in extracurricular activities is larger.

We can also look at type of address vs. family size:

```
pd.crosstab(index=student.address, columns=student.famsize)
famsize 	GT3 	LE3
address 		
R 	        68 	20
U 	        213 	94
```

There are a lot less students living in rural areas and the proportion of them living in families larger than 3 is greater.

## Calculated Columns

We can add more to our inference by computing new columns using the existing data. For example, we would like to know how many students improved their grade between the first and second period. We create a calculated column and then count the number of students that improved and did not improve in each district.

```
student['improvement'] = np.where(student.G2 > student.G1, "improved", "did not improve")
pd.crosstab(index=student.school, columns=student.improvement)
improvement 	did not improve 	improved
school 		
GP 	228 	121
MS 	39 	7
```

The data shows that almost a third of students in Gabriel Periera improved.

## Pivot Tables

We can generate a pivot table of this data to provide us with a concise summary that will contain a large amount of insight.

Let's generate a pivot table that shows us the mean final grade by school, sex and weekly study time:

```
student.pivot_table(index=["school"], columns=["sex", "studytime"], values=["G3"], fill_value=0)
        	G3
sex 	        F 	                                         M
studytime 	1 	2 	        3 	        4 	 1 	        2 	        3 	        4
school 								
GP 	10.652174 	9.363636 	10.590909 	11 	10.363636 	11.090909 	13.923077 	11.7
MS 	5.250000 	10.428571 	11.571429 	0 	8.750000 	10.875000 	13.000000 	0.0
```

We can see that at Mousinho da Silveira there are no students studying the maximum amount of time.

Also, the fact that students who study 5-10 hours a week are more successful than students who study more than 10 hours per week could be attributed to the small sample size in this group.

We can examine this by looking at a pivot table of counts instead of means.

```
student.pivot_table(index=["school"], columns=["sex", "studytime"], values=["G3"], fill_value=0, aggfunc='count') 
 	G3
sex 	        F 	                        M
studytime 	1 	2 	3 	4 	1 	2 	3 	4
school 								
GP 	        23 	99 	44 	17 	66 	77 	13 	10
MS 	        4 	14 	7 	0 	12 	8 	1 	0
```

As we can see, the count of students in group 4 is the smallest in both schools.

## Conclusion

In this lesson we have learned how to look at descriptive statistics to discover information about our data. We have done this by looking at counts and averages using crosstabs and pivot tables.

We are also able to learn information about our data by comparing the mean and the median of a column.
