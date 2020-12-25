# Three Ways to Remove Elements from a Python Tuple

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing elements from end
post = post[:-1]
#('Python Basics', 'Intro guide to Python', 'Some cool python content')

# Removing elements from beginning
post = post[1:]
#('Intro guide to Python', 'Some cool python content', 'published')

# Removing specific element (messy/not recommended)
post = list(post)
post.remove('published')
post = tuple(post)

print(post)
#('Python Basics', 'Intro guide to Python', 'Some cool python content')
