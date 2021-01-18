# Building Polymorphic Functions in Python

class Heading:
    def __init__(self, content):
      self.content = content

    def render(self):
      return f'<h1>{self.content}</h1>'

class Div:
  def __init__(self, content):
    self.content = content

  def render(self):
    return f'<div>{self.content}</div>'

div_one = Div('Some content')
heading = Heading('My Amazing Heading')
div_two = Div('Another div')

def html_render(tag_object):
  print(tag_object.render())

html_render(div_one)
#<div>Some content</div>
html_render(div_two)
#<div>Another div</div>
html_render(heading)
#<h1>My Amazing Heading</h1>   
