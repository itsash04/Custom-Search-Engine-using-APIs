from exa_py import Exa
exa= Exa(api_key="YOUR KEY")

searchquery=input('What do you wanna search? ')

response=exa.search(searchquery, num_results=5, type='keyword',include_domains=['https://www.instagram.com'],)

for result in response.results:
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
