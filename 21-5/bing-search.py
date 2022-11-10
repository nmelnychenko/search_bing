import requests
from bs4 import BeautifulSoup
from decouple import config

subscription_key = config('subscription_key', default='')

search_url = "https://api.bing.microsoft.com/v7.0/search/"

search_term = 'ноутбук 16Гб + SSD + 50000 + Україна -site:.ru'
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

def is_meta_description(tag):
    return tag.name == 'meta' and tag['name'] == 'description'

for result in results[:10]:
  url = result['url']

  try:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('title').get_text()

    # TODO: define what content from the page we want to parse

    # TODO: fix the errors with description.
    # Probably some sites don't have this or define description in different ways

    # meta_tag = soup.find(is_meta_description)
    # meta_description = meta_tag['content']

    possible_output = {
      'url': url,
      'title': title,
      # 'meta_description': meta_description
    }

    print(possible_output)
  except:
    print("Something went wrong")
  else:
    continue

