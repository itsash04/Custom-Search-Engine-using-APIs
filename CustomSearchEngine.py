from exa_py import Exa
exa= Exa(api_key="d800e108-b97d-45f9-8c1a-11f4228ee303")

searchquery=input('What do you wanna search? ')

response=exa.search(searchquery, num_results=5, type='keyword',include_domains=['https://www.instagram.com'],)

for result in response.results:
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
