![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | BI Analysis with Tableau

## Introduction

In this lab, we will practice performing business intelligence analysis on a company's customer data. The data set we will be working with contains information about customers of a telecommunications company such as demographic information, information about what services the customer uses, and billing information as well as whether or not the customer has churned (cancelled their service).

As in previous labs, if you get stuck on any of the tasks in this lab, you can reference the excellent training video resources provided on the [Tableau website](https://www.tableau.com/learn/training).

## Getting Started

To complete this lab, follow each of the steps below.

1. Open Tableau and import the `churn.csv` file.
2. Let's start out by exploring the company's customers from a demographics perspective.
    - Create a new worksheet and drop the Number of Records measure into the center. You should see that the total customer count is 7,043.
    - Drag and drop the Gender dimension into the Rows area and the Partners dimension into the Columns area.
    - Click on the Show Me menu at the top right of the screen and select the highlight table visualization so that we can see the density of records as we continue to build our view.
    - Add the Dependents dimension to the Columns area (next to Partners).
    - Convert the Senior Citizen measure to a dimension by right clicking on it and selecting *Convert to Dimension*. This is a binary categorical field, so it is beneficial to convert it to a dimension if we want to be able to group by it.
    - Drag and drop the new Senior Citizen dimension into the Rows area (right next to Gender).
    - From the Analysis menu, select *Totals > Show Row Grand Totals* and then *Totals > Show Column Grand Totals*.
    - We should clearly be able to see that the majority of the company's customers tend to be non-senior individuals (no partners and no dependents) and that there is a fairly even split between male and female customers.
3. Another perspective from which we can view the customer data is the core services (phone and internet) they signed up for.
    - Create a new worksheet containing another highlighted table visualization with the Phone Service and Multiple Lines dimensions as rows and the Internet Service dimension as columns.
    - Add row and column grand totals to this visualization as well.
    - There are a few insights that we should be able to derive from this visualization.
        - Most of the company's customers have both phone and internet service with the company.
        - Fiber optic is the most popular type of internet service, especially among customers that have phone service with multiple lines.
        - DSL is the only type of internet service provided to customers that do not have phone service.
4. We can also look at what billing options are most popular among customers.
    - Create a new worksheet containing a stacked bar chart showing the number of records by Paperless Billing and Payment Method (columns).
    - Add the Number of Records measure to the Label box in the Marks section so that we can easily see it next to each bar in the visualization.
    - From this visualization, we can see that most customers who have paperless billing also pay via electronic payment methods (with electronic check being the most popular), while payment via mailed check is the most popular payment option for customers who do not have paperless billing.
    - Bonus: You can also drop the Contract dimension into the Rows section to get a more granular view of which billing options are most popular among customers on month-to-month, one year, and two year service contracts.
5. Now that we have looked at customer distribution from a variety of perspectives, let's shift our focus to some of the other measures in our data set. Specifically, let's take a look at how pricing (Monthly Charge) changes with longevity (Tenure).
    - In order to be able to visualize monthly charges over Tenure, we need to convert the Tenure from a measure to a dimension. Right click on the Tenure measure and select *Convert to Dimension*.
    - Drag and drop the Monthly Charges measure into the Rows section. Click the drop-down arrow next to it and change the dimension from sum to average.
    - Drag and drop the newly-converted Tenure dimension into the Columns section. This should produce a line chart showing the average monthly charge for customers as they stay with the company longer.
    - We can see that the average monthly charge across all customers starts out at $41.42, increases sharply in the first three months to $57.21, and then continues to increase gradually to eventually reach the $80 price range.
6. We can observe the relationship between Monthly Charges and Tenure from a variety of perspectives to gain insight into how pricing changes for different subsets of customers.
    - Create a duplicate of the previous Monthly Charge by Tenure visualization by right clicking on the tab for the visualization and selecting *Duplicate*.
    - Drag and drop the Gender dimension into the Color box in the Marks section. The chart breaks into two lines (one for each gender). One of the interesting insights we can see from this perspective is that the company charges new women customers twice as much on average than new male customers. However, we see that by the third month, the price level for men is back up to where it is for women. One thing we can infer from this is that perhaps the company regularly runs low-cost introductory promotions aimed at men to try their services.
    - Create another duplicate of the original Monthly Charge by Tenure visualization by right clicking on the tab for the visualization and selecting *Duplicate*.
    - Drag and drop the Senior Citizen dimension into the Color box in the Marks section. From this perspective, it looks as though the company charges senior citizens more on average across the board than they charge non-seniors.
7. The pricing charts we have looked at thus far makes it seem like the company is providing cheaper services to some customers based on demographics. However, we should also take into consideration that pricing is typically heavily dependent on services purchased, and it may just be that seniors purchase more expensive services on average than younger customers. Let's look at how pricing varies across services.
    - Create another duplicate of the original Monthly Charge by Tenure visualization and drop the Multiple Lines dimension into the Color box. We can see the increases in price between plans with no phone service, single phone lines, and multiple phone lines respectively.
    - Create another duplicate of the original Monthly Charge by Tenure visualization and drop the Internet Service dimension into the Color box. This chart shows even starker price differences between plans with no internet service, DSL, and fiber optic respectively.
8. In addition to looking at pricing by demographics and services separately, we can also look at it by both demographics *and* services.
    - Create a highlight table visualization that shows Monthly Charges by Internet Service and Multiple Lines (rows) and Gender and Senior Citizen (columns). Remember to change the Monthly Charge measure to average instead of sum.
    - Add row and column grand totals like we did for prior visualizations.
    - From this perspective, we can see that the prices for the different combination of core services do not differ significantly across demographic features.
9. Let's compare the last visualization with a similar one that shows the number of customers by demographic and service combination.
    - Create a duplicate of the last highlight table visualization.
    - Drag and drop the Number of Records measure to replace Monthly Charges wherever it appears in the Marks section.
    - From this visualization, we can see that the proportion of customers that have fiber optic internet (the highest price service) is higher among seniors than it is among non-seniors. This is likely the cause for the difference in price among those two groups.
10. The final perspective we will analyze this data set from is the number of customers that churn by demographic and service combination.
    - Create another duplicate of the highlight table visualization showing pricing by demographics and services.
    - Create a calculated field called Churned by going to *Analysis > Create Calculated Field* and entering the following formula: `IF [Churn]='Yes' THEN 1 ELSE 0 END`.
    - Drag and drop the newly-created Churned measure to replace Monthly Charges wherever it appears in the Marks section.
    - By default, Tableau will sum the measure which will show us the number of customers that churned in each segment. This is useful, but what we really want to see is the percentage of customers that churned. To see this, click on the drop-down next to the dimension wherever it appears in the Marks section, select *Measure*, and change the value to *Average*.
    - We can see that the churn rates are higher for fiber optic internet across the board than for any other service. We know that fiber is also the highest priced, so perhaps customers aren't happy paying such high prices.
11. Next, we are going to combine all the visualizations we used to explore the data into a Tableau Story.
    - Create a new Story by clicking on *Story > New Story*).
    - Our story should document our journey throughout this lab, so you should create a Story Point for each visualization we have created. You can create a new Story Point by clicking on the *Blank* button under the *New Story Point* heading in the left pane of the workbook.
    - Drag and drop each visualization into a new Story Point.
    - Add a caption for each Story Point that briefly describes the chart. For example, the first one can be captioned *Customer Demographics*, the second one can be captioned *Customers by Service*, etc.
    - Add an annotation to each Story Point describing the insights derived from the visualization. If you're having trouble with what to write, you can copy and paste the insights we have been documenting throughout each of the tasks above.
12. Save your work to Tableau Public, ensure that your workbook is viewable, and copy the URL for the workbook into the deliverables file for this lab.

## Deliverables

- `main.txt` file with a link to your Tableau Public workbook.

## Submission

Upon completion, add your deliverables to git. Then commit git and push your branch to the remote.

## Resources

- [A Beginner's Guide to American Football](https://www.youtube.com/watch?v=3t6hM5tRlfA)

- [American Football Strategy | Wikipedia](https://en.wikipedia.org/wiki/American_football_strategy)

- [Sort Data in a Visualization | Tableau](https://onlinehelp.tableau.com/current/pro/desktop/en-us/sortgroup_sorting_computed_howto.htm)

- [Filter Data From Your Views | Tableau](https://onlinehelp.tableau.com/current/pro/desktop/en-us/filtering.htm)

- [Color Palettes and Effects](https://onlinehelp.tableau.com/current/pro/desktop/en-us/viewparts_marks_markproperties_color.htm)

- [Tableau Training Videos](https://www.tableau.com/learn/training)