from keyring import github_token
import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
from datetime import datetime, timedelta



# url = 'https://api.github.com/repos/Ironhack-labs/data-labs/commits?'
# ran the below in the Terminal
# curl -I "https://api.github.com/repos/Ironhack-labs/data-labs/commits"
# checking link, see that there are 15 pages.
# at 30 per page, that should be 450 records. is 30 still the default? 
# ran the Terminal command again with 'per_page=90' in the URL, and got a 5-page (so =450)

# looking for just the past week
# SINCE is the parameter to use
# YYYY-MM-DDTHH:MM:SSZ

# bet I can do this dynamically with datetime
# print(datetime.datetime(2019, 9, 22).isoformat('T'))
seven_days_ago = (datetime.now() - timedelta(days=7)).isoformat('T')
# print(seven_days_ago)

page_data = []
for i in range(1, 15+1):
    url = f'https://api.github.com/repos/Ironhack-labs/data-labs/commits?since={seven_days_ago}&page={i}'
    response = requests.get(url)
    flat_results = json_normalize(response.json())
    page_data.append(pd.DataFrame(flat_results))

commit_data = pd.concat(page_data)
# print(commit_data.head())
print("The total number of commits made in the past week is: " + str(len(commit_data['sha'])))


