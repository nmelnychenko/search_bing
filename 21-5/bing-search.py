import requests
from decouple import config

subscription_key = config('subscription_key', default='')

search_url = "https://api.bing.microsoft.com/v7.0/search"

search_term = 'ноутбук 16Гб + SSD + Acer + 50000 + Україна'
search_term = search_term.rstrip()

# Copied from the Bing documentation on page
# [https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/quickstarts/rest/python]
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

pages = search_results['webPages']
results = pages['value']

print(type(results))

for elem in search_results:
  print(elem)
  # single_res = results[elem]
  # text = single_res['snippet']

  # print(text)

