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

Curiously, the CSV file was only supposed to include 20 columns, and my raw_data dataframe had 24 columns. 
The extras were ['original order', 'Unnamed: 22', 'Unnamed: 23']
dropped these columns as a list of column names

['Case Number', 'Case Number.1', Case Number.2'] appeared to be duplicates columns, at least as far as the first 5 rows.
Investigated to confirm.
All have a length of 5,992 rows.
They all three have exactly zero Null values (at least on initial pass, Nulls that pandas recognizes as Nulls)
