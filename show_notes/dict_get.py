#Guide to Using the get Function in Python Dictionaries to Configure Fallback Lookup Values

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}

featured_team_mets = teams.get('mets', 'No featured team')
# No featured team

featured_team = teams.get('yankees', 'No featured team')
# ['Judge', 'Stanton']

print(featured_team_mets)
print(featured_team)

"""
Notes: Get gives you the ability to avoid stopping the script
with a KeyError: 'mets' and instead return the string: 
"No fearured team"

"""