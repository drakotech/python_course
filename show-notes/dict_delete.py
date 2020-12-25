# Overview of the Multiple Methods for Deleting Items in a 
# Python Dictionary

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

del teams['angels']
"""
{
    'astros': ['Altuve', 'Correa', 'Bregman'], 
    'yankees': ['Judge', 'Stanton'], 
    'red sox': ['Price', 'Betts']
}

"""
removed_team = teams.pop('mets', 'Team not found')

print(teams)
print(removed_team)
#Team not found

"""
Notes: Similar to how the get function works to handle errors
safely, the pop function also works the same way when deleting.
However the popped return needs to be stored to get its value
otherwise will return nothing.

"""