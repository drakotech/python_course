#Using the join Function in Python to Build a URL Query String

# https://www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}'

print(query_uri)

#Notes: Whatever goes before the .join is what will be used to separate the strings.
