![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Final Project Demo

## Overview

This demo is meant to serve as a simplified version of the type of analysis expected from you for your final project. In the sections below, we will go through each step of the data analysis workflow applying the appropriate operations at each step. You can use the code snippets and examples below as a guide for your own final project, but also feel free to go beyond what we have done and apply whichever methods are applicable to the data set you have chosen.

## The Data

The data set we will be using for this demo will be a housing price data set. The data set contains a variety of features for each property listed for sale in a geographic area as well as the sale price at which each property was ultimately sold.

## Data Ingestion

In order to work with this data set, we must first ingest it. The file containing the data was in CSV format, so after downloading it, we used the `read_csv` method to read the data into a Pandas data frame.

```python
import pandas as pd

data = pd.read_csv('housing_prices.csv')
```

Next, we checked that the data set loaded correctly by checking the shape of the data frame, looking at the first few rows of the data, and evaluating the column names to ensure that they look as we would expect.

```python
data.shape

(1460, 81)
```

```python
data.head(10)
```

![Housing Data](./images/housing-data.png)

```python
print(list(data.columns))

['Id', 'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1', 'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating', 'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual', 'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC', 'Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold', 'SaleType', 'SaleCondition', 'SalePrice']
```

From this initial assessment, it looks like we have successfully ingested the data set. We can now move on to evaluating the quality of the data, cleaning it, and wrangling it so that it is ready to be analyzed and modeled.

## Data Wrangling and Cleaning

One of the first things we do in the wrangling and cleaning phase of the workflow is ensure that each column is of the correct data type. Below, we produce a data frame of numeric fields (including various descriptives statistics about them) using the `describe` method and then transposing the results since so that we can see all the resulting fields. We will also add a unique column to the results that returns the number of unique values in each column and a null column that calculates the number of missing values.

```python
stats = data.describe().T
stats['unique'] = [len(data[column].unique()) for column in stats.index]
stats['null'] = [data[column].isnull().sum() for column in stats.index]
stats
```

![Describe Data](./images/housing-data-describe.png)

We call the `describe` method for categorical fields by setting the `include` parameter to contain only object and category data types.

```python
cat_stats = data.describe(include=['object','category']).T
cat_stats['null'] = [data[column].isnull().sum() for column in cat_stats.index]
cat_stats
```

![Describe Data Categorical](./images/housing-data-describe-cat.png)

Below are a few insights we derived from this brief look at the data that can help guide our data wrangling and cleaning efforts.

* There are several fields that are currently numeric that should be categorical. We can identify these via a combination of their column name and their low number of unique values.

* There are several fields in the data that contain null values. We will need to figure out how to address those.

To fix the incorrect data types, we will simply identify the columns that are incorrectly typed and use the `astype` method to change the data type of each field to object.

```python
categorical = ['MSSubClass', 'OverallQual', 'OverallCond', 'MoSold', 'YrSold']

for i in categorical:
    data[i] = data[i].astype('object')
```

In order to address null values in the data, we looked at which fields contained them and decided whether we would like to leave them as is or replace them with an appropriate value.

```python
fill_zeros = ['LotFrontage', 'MasVnrArea']

for column in fill_zeros:
    data[column] = data[column].fillna(0)
```

## Data Storage

Once the data had been ingested and cleaned, we stored it in a MySQL database. To do this we first created a *housing* database using the `CREATE DATABASE` command.

```sql
CREATE DATABASE housing;
```

We then used `pymsql` and `sqlalchemy` to write the data to the database.

```python
import pymysql
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://user:password@localhost/housing')
data.to_sql('housing', engine, if_exists='replace', index=False)
```

To read the stored data back into Pandas at a later date, we used the `read_sql_query` method.

```python
data = pd.read_sql_query('SELECT * FROM housing.housing', engine)
```

## Data Exploration and Analysis

After cleaning and storing the data, the next steps we took were exploring and analyzing the data. Each row in the data set represents a property and each column represents attributes belonging to those properties. We looked through these attributes to determine 

## Feature Selection

## Model Training and Evaluation

## Reporting of Insights

## Conclusion
