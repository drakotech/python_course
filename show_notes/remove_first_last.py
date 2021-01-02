def remove_first_last(list_to_clean):
    _, *content, _ = list_to_clean
    return content

html = ['<h1>', 'some content', '</h1>']

html_2 = ['<h1>', 'some content', 'more', '</h1>']

print(remove_first_last(html))

"""
This works by using the (*) glob method where the glob
grabs everything except the first and last.

Common practice is where when you declare a variabe that is
not going to be called is to assign it into a "_" variable.

"""