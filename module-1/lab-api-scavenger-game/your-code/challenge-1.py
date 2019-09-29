from keyring import github_token
import json
import requests
import pandas as pd
from pandas.io.json import json_normalize

# url = 'https://api.github.com/repos/ironhack-labs/data-labs'
# response = requests.get(url)
# result = response.json()
# print(result)

# specifically, look at the forks per the challenge
# url = 'https://api.github.com/repos/ironhack-labs/data-labs/forks'
# response = requests.get(url)
# result = response.json()
# forks_from_ironhack = pd.DataFrame(result)
# print(forks_from_ironhack.dtypes)
# print(list(forks_from_ironhack))
# print(forks_from_ironhack['language'])

# langs_of_ironhack = forks_from_ironhack['language'] # this was correct from the beginning, I just was only looking at the first five rows
# print(langs_of_ironhack.head(20))

# langs_of_ironhack = forks_from_ironhack.groupby(['language'])
# print(langs_of_ironhack.head())
# print(langs_of_ironhack.describe())
# returns that of those that have forked from the Ironhack Data Labs Repo, there are 2 programming languages used. 1 use of HTML, and 17 uses of Jupyter Notebook

# print(len(forks_from_ironhack['language'].values)) # only returns 30. i'm not looking at all the data

# Github API documentation on working with pagination
# in terminal, ran `curl -I "url below"`
# retrieved that rel="last" shows page 4. 
# so I have 4 pages, and the documentation shows that calls to /repos/ will default to 30 items per page
# but I want to be able to call this dynamically. found PyGitHub, the equivalent of tweepy for GitHub.
# from github import Github # need to play with this more, documentation here: https://pygithub.readthedocs.io/en/latest/index.html

# url = 'https://api.github.com/repos/ironhack-labs/data-labs/forks'
# response = requests.get(url)
# result = response.json()
# forks_from_ironhack = pd.DataFrame(result)

page_data = []
for i in range(1, 5):
    url = f'https://api.github.com/repos/ironhack-labs/data-labs/forks?&page={i}'
    response = requests.get(url)
    result = response.json()
    flattened_data = json_normalize(result)
    page_data.append(pd.DataFrame(flattened_data))

lang_data = pd.concat(page_data)
# print(lang_data.head())

# print(lang_data.dtypes)
# print(list(lang_data))

total_langs = lang_data.groupby(['language'])
print(total_langs.describe())
# print(lang_data['language'].values) # shows that apart from nulls, there's only HTML and Jupyter notebook

