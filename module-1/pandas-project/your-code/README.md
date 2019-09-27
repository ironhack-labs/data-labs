### My experience with the Pandas Project - Data Cleaning and Manipulation

I attempted to read the CSV directly from the Kaggle website with the urlOpen function, but I kept getting this error
ParserError: Error tokenizing data. C error: Expected 1 fields in line 6, saw 2

Printing the output from the urlOpen function returned "<http.client.HTTPResponse object at 0x11f0440b8>", so I know it recognizes it as a URL object

I attempted to read the CSV directly via pandas, skipping the urllib library
raw_data = pd.read_csv('the url'), but this still gave me ParserError: Error tokenizing data. C error: Expected 1 fields in line 6, saw 2

Reviewing Stack Overflow, attempted to adjust the Delimiter optional argument sep=, the optional argument for headers, the optional argument for encoding='utf-8'. 

Gave up and downloaded the CSV file.

Reading that gave a new error
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x92 in position 1: invalid start byte
while someone suggested changing the optional argument engine= from 'c' to 'python', another user recommended against it for working-memory reasons. Since I have what I believe to be a large file (20MB for a CSV), I decided not to go this route.

But after other efforts proved fruitless. I ran it and it worked.

### Step 1 - Examine data for potential issues
used .head() to visually inspect an extremely small subset of the data
used .describe() method to get the column names and their datatypes
used .isnull().sum() to review how many columns have null values (that pandas recognizes on first pass), and how many null values are present in those columns

Curiously, the CSV file was only supposed to include 20 columns, and my raw_data dataframe had 24 columns. 
The extras were ['original order', 'Unnamed: 22', 'Unnamed: 23']
dropped these columns as a list of column names

['Case Number', 'Case Number.1', Case Number.2'] appeared to be duplicates columns, at least as far as the first 5 rows.
Investigated to confirm.
All have a length of 5,992 rows.
They all three have exactly zero Null values (at least on initial pass, Nulls that pandas recognizes as Nulls)


I noticed during Exploratory Data Analysis (EDA) that the Date series contained some incongruent reported values, 
showing "Reported dd-Mon-yyyy" as opposed to "dd-Mon-yy"
I want to convert all of those.
They are an object, hopefully a string object. so replace with stripping non-numeric characters from the beginning. basically, only look within each cell's string until you hit a number, and then ignore the rest. 
Regex will be my focus. couldn't figure it out, had to move on to more important issues with the data set, come back to that later.

Dropped columns that did not add relevant data.

First pass - clean up the 'Type' column. ['Provoked', 'Unprovoked', 'Invalid']
will need to use .loc[] to replace the values within the 'Type' column. Also, do .lower() to ask if the type is in the list, so that a capitalization error does not remove a confirmed shark attack.
then drop the rows with invalid - if we can't confirm a shark was involved, the data can be removed.


## Start over
#### Question to answer:
Given in the US, and given that the victom is Female, is a shark attack more likely to be reported as Provoked or Unprovoked? 
Does age of victim have anything to do with it? 

### Step 1 - Examine data for potential issues
used .head() to visually inspect an extremely small subset of the data
used .describe() method to get the column names and their datatypes
used .isnull().sum() to review how many columns have null values (that pandas recognizes on first pass), and how many null values are present in those columns

Curiously, the CSV file was only supposed to include 20 columns, and my raw_data dataframe had 24 columns. 
The extras were ['original order', 'Unnamed: 22', 'Unnamed: 23']
dropped these columns as a list of column names

Dropped the following columns that did not add relevant data
['Case Number.1', 'Case Number.2', 'pdf', 'href formula', 'href']


Bin the ages into Adolescent/Child, Adult, Senior at 0-18, 19-54, 55+
I should do this AFTER I have dropped data

### Step 2 - Subset the data by a condition

I want to drop the rows that do not have either "provoked" or "unprovoked" as the Type of attack.
Easier than dropping the rows, just filter/subset the data into a new dataframe!
That dropped ~1,050 rows! 

Checking the null values following this subset: 
I see that Country still has 30 null values. will need to drop those.
Sex has 227 Null values. drop those.
Age has 1928 null values. drop the nulls before Binning them with pd.cut (wonder if the victim age is normally distributed. if not, possible reasons - age of victim not reported for the elderly? (that's my assumption/bias, check the DATA first). perhaps certain age ranges are more likely to be in areas where shark attacks are possible?)





