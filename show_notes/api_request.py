# Overview of the Requests Package in Python to 
# communicate with APIs

import requests
import pprint

r = requests.get('https://api.dailysmarty.com/posts')
r.json()
pprint.pprint(r.json()['posts'][0])
"""
{'associated_topics': ['Django Framework', 'Web Development'],
 'content': '<p>Choosing a web development framework is challenging. But for '
            'most companies, the Django web framework is a popular choice. It '
            'is versatile, powerful, and supports Machine Learning '
            'development. A&nbsp;<a '
            'href="https://www.botreetechnologies.com/django-development">Django '
            'web development company</a>&nbsp;builds scalable applications for '
            'enterprises of all shapes and sizes.</p>\r\n'
            '\r\n'
            '<p>The Django framework architecture is based on Python - the '
            'multi-purpose programming language. The primary purpose of Django '
            'development is to achieve scalability and flexibility while '
            'building web applications.</p>\r\n'
            '\r\n'
            '<p>Django web development framework is perfect for complex '
            'data-driven websites. It&rsquo;s architecture and libraries '
            'support high-level computation and statistical algorithm '
            'development. Therefore, most Django developers are versatile - '
            'they can build a web application and work with scientific '
            'programming.</p>\r\n'
            '\r\n'
            '<p>Source:&nbsp;https://dev.to/botreetechnologies/why-is-the-django-framework-suitable-for-web-development-39he</p>\r\n',
 'created_at': '2020-12-16T11:07:16.910Z',
 'id': 7496,
 'post_links': [{'link_url': 'https://dev.to/botreetechnologies/why-is-the-django-framework-suitable-for-web-development-39he'}],
 'title': 'Why is the Django Framework Suitable for Web Development?',
 'url_for_post': 'http://www.dailysmarty.com/posts/why-is-the-django-framework-suitable-for-web-development'}

"""
pprint.pprint(r.json()['posts'][0]['url_for_post'])
#'http://www.dailysmarty.com/posts/why-is-the-django-framework-suitable-for-web-development'

"""
This will communicate with the api from daily smarty and request
a JSON package. containing loads of data.

"""