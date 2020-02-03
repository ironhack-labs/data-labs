# Project: API and Web Scraping


### API Scraping

First step - select an API. Chose Superhero API, and signed in with Facebook to generate an Access Token to their API.
Saved this Access Token to my utilitybelt.py file as a variable name, added utilitybelt.py to .gitignore for my repository for security reasons.

API for Reference: https://superheroapi.com/

Checked out the URL using Postman. The data from the API is a JSON, as specified in the Reference Materials.
For example, Aliases of the Superhero is a nested dictionary within the Biography dictionary.
In this case, best to flatten the data for addition to my dataframe.

Tested the API and my dataframe. Confident that I can pull the full list of characters from the API now and work with the data.
Saved the API output to CSV. Lab doesn't ask that we manipulate the data or clean it for this section. Will probably need to do so in next section: Web Scraping

### Web Scraping
Sticking with the superhero theme, found a list of Marvel's Avengers superheroes on Wikipedia. 
Multiple Tables on the page, focused first on List of New Avengers Recruits (2005). 

I've worked with Wikipedia Tables before for lab-web-scraping. 
Investigating this particular page...

While the <span> has a particular id of "New_Avengers_recruits_(2005)", corresponding table underneath is not specific. Table with Class="wikitable".
    Wonder if it would be easier to count the Tables, and just use .find()[index] to grab the table I want, rather than pulling in the whole span and then trying to narrow down the elements within.
    
Opted to count tables, taking first pass.
Opened Chrome Developer Tools, used CTRL+F to find "table", the table I wanted was the 9th table. which would be index 8

That worked. 
I need to create a dataframe to house the data I gather from my BeautifulSoup object.
That dataframe's column names are the table's first row.

Wikipedia identified this header row differently, as "<th>", presumably for TableHeader as opposed to TableRow.
    
As expected, need to remove escape characters after gathering .text attributes for each value in the Header Row.
Completed.

Now inspect the "data rows", the "<td>"
For this particular table, all of the td tags are identical, no differentiation between columns.
Pulled up the Lesson-Web Scraping, where I had practiced with another Wikipedia table
    My notes from that:
    table_rows = table_i_want.find_all('tr') # the list of row content is every instance of <tr> in my table content
    table_rows = [row.text.strip().split("\n") # grab the text out of the row's content, strip whitespace, and throw in line breaks
    for row in table_rows # listcomp to iterate through every row's content
]
    
Will attempt something similar with this one.
Had to follow the same process of pulling the row's data, splitting it along "\n" escape characters, and dropping the empty strings before loading it into the dataframe. Used List Comprehensions to do so.

Saved to CSV same as the APIscrape.

Examined the Webscrape output - looks like for Character Name, since the Wikipedia table was using an <a href> within that <td>, when I pulled the "element.text" from the <td> tag, replacing the "new line" escape character with an empty string, it joined the true "text" with the "link text" from the <a href> resulting in Luke Cageaka and Echoaka values.
    but if I had split on the "\n" instead, so much more work would have been required for data cleaning. 
Taking another pass at it