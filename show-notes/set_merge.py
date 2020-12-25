# Various Methods for Merging Python Sets

tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

# merged tags
merged_tags = tags_one | tags_two
print(merged_tags)
#{'development', 'python', 'coding', 'tutorials', 'ruby'}

# tags in tags_one but not in tags_two
exclusive_to_tag_one = tags_one - tags_two
print(exclusive_to_tag_one)
#{'python'}

# tags in tags_two but not in tags_one
exclusive_to_tag_two =  tags_two - tags_one
print(exclusive_to_tag_two)
#{'development', 'ruby'}

# tags found in both tags_one and tags_two
universal_tags = tags_one & tags_two
print(universal_tags)
#{'coding', 'tutorials'}

"""
Merging them with the 'pipe char' | will return a set with all 
duplicates removed

Left side of the - symbol will only find what is unique to its
set opposed to whats on the right of it.

"""