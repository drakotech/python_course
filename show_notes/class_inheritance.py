# Introduction to Inheritance in Python

class User:
  def __init__(self, email, first_name, last_name):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name

  def greeting(self):
    return f'Hi {self.first_name} {self.last_name}'

class AdminUser(User):
  def active_users(self):
    return '500'


tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')

kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

print(tiffany.active_users())
#500
print(tiffany.greeting())
#Hi Tiffany Hudgens
#print(kristine.active_users())
#AttributeError: 'User' object has no attribute 'active_users'

"""
At a high level: Inheritance is the ability to create specialized
versions of classes. 

As seen above Kristine doesn't have an attribute of active_users
because she was assigned the User class and not AdminUser class.

"""