# Lab | Introduction to BI and Tableau

Complete the steps below and record your answers where appropriate.

1. Open the [data set](https://docs.google.com/spreadsheets/d/1pQ2VFsuuwLqBstYYTY3fcZY32WLigw3Pzxnikkce6IA/edit?usp=sharing) in a browser.
2. Add the data set to your Google Drive.
3. Launch the Tableau Public application.
4. Import the data set from Google Sheets into Tableau.
5. Once the data set has been imported, inspect the data types for each field. Are there any that are incorrect? What should they be changed to?
    
    Year and Month should be strings instead of numeric.

6. Change the field data types you identified as incorrect to the correct data type.
7. From the fields in the data set, come up with 5 Key Performance Indicators (KPIs) that would help provide the company insight into its performance. You don't need to actually create the KPIs at this point, just list what they are.

    Possible answers include:
    - Total/Average Retail Sales by Month/Item Type
    - Total/Average Warehouse Sales by Month/Item Type
    - Total/Average Sales by Month/Item Type
    - Ratio of Retail Sales to Warehouse Sales
    - Total/Average Retail Transfers by Month/Item Type
    - Number of Unique Items Sold by Month/Item Type
    - Average Sale per Unique Item Sold by Month/Item Type
    - Percent of Total Sales by Month/Item Type

8. What additional fields could be created from the existing fields that would be informative?

    - You could parse the volume from the description.
    - You could attempt to extract the type of liquor from the description to get more granular item categories.
    - You could score items and/or suppliers based on desirable sales/transfer activity so that you can rank them.
