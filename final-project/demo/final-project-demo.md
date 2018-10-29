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

* There is an opportunity to create a couple of additional informative fields by performing calculations on existing fields.

To fix the incorrect data types, we will simply identify the columns that are incorrectly typed and use the `astype` method to change the data type of each field to object.

```python
categorical = categorical = ['MSSubClass', 'OverallQual', 'OverallCond', 
                             'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 
                             'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 
                             'TotRmsAbvGrd', 'Fireplaces', 'GarageCars', 
                             'PoolArea', 'MoSold', 'YrSold']

for i in categorical:
    data[i] = data[i].astype('object')
```

In order to address null values in the data, we looked at which fields contained them and decided whether we would like to leave them as is or replace them with an appropriate value.

```python
fill_zeros = ['LotFrontage', 'MasVnrArea']

for column in fill_zeros:
    data[column] = data[column].fillna(0)
```

As far as creating additional informative fields, we could add together the 1st floor, 2nd floor, and basement square footage to get the total square footage of the property. Once we have total square footage, we could divide the sale price by it to arrive at a price per square foot metric.

```python
data['Total Sqft'] = data['1stFlrSF'] + data['2ndFlrSF'] + data['TotalBsmtSF']
data['Price Per Sqft'] = data['SalePrice'] / data['Total Sqft']
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

We also exported the cleaned data set as a CSV file that could be imported into Tableau for exploration and reporting.

```python
data.to_csv('housing_clean', index=False)
```

## Data Exploration and Analysis

After cleaning and storing the data, the next steps we took were exploring and analyzing the data. Each row in the data set represents a property and each column represents attributes belonging to those properties. We looked through these attributes to determine which ones would potentially yield the most informative insights. Below are a list of those fields followed by a series of data visualizations conveying insights discovered.

* Type of Sale
* Sale condition
* Neighborhood
* Total square footage of the property
* Numbers of bedrooms and bathrooms
* Overall quality
* Overall condition
* Month and year of sale
* Sale Price
* Price per square foot

The first thing we wanted to look at was the number of sales and average sale prices by type of sale and sale condition.

![Price by Sales Type](./images/sales-avg-price-by-sale-type.png)

![Price by Sales Condition](./images/price-by-sale-condition.png)

Most of the property sales in this data set were of the *Warranty Deed - Conventional* type and under *Normal* conditions and the average price for those was in the low-to-mid $170,000's. The next most common were new construction sales, which were priced about $100,000 higher on average.

One of the most obvious drivers of sales price for a property its size, typically represented by the total number of square feet. Below is a scatter plot showing the relationship between *Total Sqft* and *Sale Price* with regression line fit to the data.

![Sqft vs. Price](./images/sqft-vs-price.png)

The R-squared for the trend line is 0.65 and the equation for the line is as follows, which can be used to set a base price for a given property given its square footage.

```text
ln(Total SQFT) = 0.63358*ln(Sale Price) + 0.184256
```

Another important factor in the value of a property is its location. Because of this, we wanted to examine how the neighborhood the property was located in impacted the value of the property. We evaluated this from three perspectives - average price by number of bedrooms, how price per square foot changes based on size of the property, and price per square foot by the number of bedrooms.

![Price by Neighborhood](./images/price-by-neighborhood.png)

![Price Per Sqft by Neighborhood and Total Sqft](./images/price-per-sqft-neighborhood-total-sqft.png)

![Price Per Sqft by Neighborhood and Bedrooms](./images/price-per-sqft-neighborhood-bedrooms.png)

From the visualizations above, we can see that there are some neighborhoods where the properties are valued higher (e.g. StoneBr, NoRidge, NridgHt, etc.) and other neighborhoods where the location hurts the value of the property (BrDale, MeadowV, Edwards, SWISU, etc.). This also lets you see the neighborhoods where someone may be able to get the most property for their money. For example, larger (6-8 bedroom) properties in the NAmes, Sawyer, and SWISU neighborhoods have significantly lower value per square foot than smaller properties in those areas.

There were a few other perspectives we wanted to look at the data from as well. We noticed that there were fields representing overall condition and overall quality and wanted to take a closer look at the differences between them and the impact they had on sales price.

![Condition vs. Quality](./images/condition-vs-quality.png)

It looks like most properties were rated a 5 for condition and were rated somewhere in the 5-8 range for quality. It looks like the quality rating for these properties is especially important as we see an typical increase of between 20% and 35% in average sales price for every point on the scale a property earns.

We also wanted to take a look at how price varies based on the number of bedrooms and bathrooms a property has. From the visualization below, it looks as though half bathrooms are valued pretty highly - especially in 4 bedroom properties (between 45% and 72% increase in price).

![Bedroom vs. Bathroom](./images/bedroom-vs-bathroom.png)

Finally, we also wanted to look at how average prices have typically changed through out the year and from one year to the next. The visualization below shows an area chart for average price by month, stacked by year.

![Avg Price by Month and Year](./images/month-year.png)

From this, we can see that average sale prices are relatively consistent throughout the year, aside from a small bump in September. Additionally, it looks as though prices took a slight downturn over the last couple years (2008 and 2009) - down about 6% from the previous two years.

## Feature Selection

## Model Training and Evaluation

## Reporting of Insights

## Conclusion
