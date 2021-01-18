# Using Polymorphism to Build an HTML Generator in Python

class Html:
    def __init__(self, content):
        self.content = content

    def render(self):             
        raise NotImplementedError("Subclass must implement render method")


class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'


class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'


tags = [Div('Some content'), Heading('My Amazing Heading'), Div('Another div')]

for tag in tags:
    print(str(tag) + ': ' + tag.render())
    #<__main__.Div object at 0x000002C326921FD0>: <div>Some content</div>
    #<__main__.Heading object at 0x000002C326921F70>: <h1>My Amazing Heading</h1>
    #<__main__.Div object at 0x000002C326921AF0>: <div>Another div</div>


"""
Polymorphism means many changes or one item can have many forms.
Polymorphism is closely associated with inheritance.

In this example the html class is an abstract parent class that
has multiple child classes that can perform different tasks.

"""
