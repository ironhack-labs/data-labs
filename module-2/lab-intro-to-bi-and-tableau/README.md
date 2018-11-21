![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Introduction to BI and Tableau

## Introduction

In this lab, we will practice loading data into Tableau, inspecting and modifying data types, and creating tabular views with metrics based on the information contained in the data set. We will be working with a [liquor store sales data set](https://docs.google.com/spreadsheets/d/1pQ2VFsuuwLqBstYYTY3fcZY32WLigw3Pzxnikkce6IA/edit?usp=sharing) hosted in Google Sheets.

If you get stuck on any of the tasks in this lab, you can reference the excellent training video resources provided on the [Tableau website](https://www.tableau.com/learn/training). We have also referenced specific articles on topics such as binning variables and creating aliases that should be helpful in completing this lab.

## Getting Started

To complete this lab, follow each of the steps below.

1. Open the [data set](https://docs.google.com/spreadsheets/d/1pQ2VFsuuwLqBstYYTY3fcZY32WLigw3Pzxnikkce6IA/edit?usp=sharing) in a browser.
2. Add the data set to your Google Drive.
3. Launch the Tableau Public application.
4. Import the data set from Google Sheets into Tableau.
5. Once the data set has been imported, change the data type for the Year field to string.
6. Create a new field called Quarter by [binning](https://onlinehelp.tableau.com/current/pro/desktop/en-us/calculations_bins.htm) the month field using a bin size of 4.
7. Create a new worksheet, drag the newly-created Quarter field into the Rows section, and drag the Number of Records measure to the center of the view. You will notice that the quarters are currently named labeled 0, 4, 8, 12. [Rename](https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_fieldproperties_aliases_ex1editing.htm) them more intuitively by right-clicking on the Quarter dimension, selecting Aliases and changing their names to Q1, Q2, Q3, and Q4 respectively.
8. Create new worksheets with tabular views for each of the following metrics.
    - Total Retail Sales by Year/Quarter (rows).
    - Average Retail Sales by Year/Quarter (rows).
    - Total Retail Sales by Year/Month (rows) and Item Type (columns).
    - Average Retail Sales by Year/Month (rows) and Item Type (columns).
    - Total Retail Transfers by Year/Quarter (rows).
    - Average Retail Transfers by Year/Quarter (rows).
    - Total Retail Transfers by Year/Month (rows) and Item Type (columns).
    - Average Retail Transfers by Year/Month (rows) and Item Type (columns).
    - Total Warehouse Sales by Year/Quarter (rows).
    - Average Warehouse Sales by Year/Quarter (rows).
    - Total Warehouse Sales by Year/Month (rows) and Item Type (columns).
    - Average Warehouse Sales by Year/Month (rows) and Item Type (columns).
9. Save your work to Tableau Public, ensure that your workbook is viewable, and copy the URL for the workbook into the deliverables file for this lab. It might take several minutes for this workbook to save to Tableau Public due to the number of records in the data set.

## Deliverables

- `main.txt` file with a link to your Tableau Public workbook.

## Submission

Upon completion, add your deliverables to git. Then commit git and push your branch to the remote.

## Resources

- [Google Sheets - Tableau](https://onlinehelp.tableau.com/current/pro/desktop/en-us/examples_googlesheets.htm)

- [Data Types - Tableau](https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_typesandroles_datatypes.htm)

- [Create Bins from a Continuous Measure](https://onlinehelp.tableau.com/current/pro/desktop/en-us/calculations_bins.htm)

- [Create Aliases to Rename Members in the View](https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_fieldproperties_aliases_ex1editing.htm)

- [Tableau Training Videos](https://www.tableau.com/learn/training)