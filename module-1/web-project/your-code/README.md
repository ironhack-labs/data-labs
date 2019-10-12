

## API:

As suggested I used the API List given. I choose to use NASA's, as you might have heard on October 3rd, we were going to possibly be hit by an asteroid. I got to request a list of all asteroids that could be coming close to earth between Sept 28th and Oct 3rd. I created a DataFrame with the results, then I looped through the results to make sure the variable within called "is_potentially_hazardous_asteroid:" was either TRUE or FALSE. And send a request to print a funny message.


## WEB SCRAPING:

As I worked on asteroids and possible impact on earth, I decided to use WIKIPEDIA, and study the impact_event. The website had a table with the impact events in Jupyter, which I extracted and save in a dataframe as well, I cleaned it and finally saved it in a CSV file. 

## OBSTACLES:

Creating several DataFrames, as I thought JSON_normalize will be a better tool. David, kindly explained it was better to get the data by DataFrames instead of the JSON. 

