# In python Dictionaries act as Hash Tables or Hash Map.

# Normal Dictionary
character = {"name": ["ritik","batman"], "age": 22, "power": "super strength"}

print(character["name"][0])

# Adding
character["rank"] = 1

print(character)

# Updating
character["name"] = [character["name"][0], character["name"][1], "alex"]
# OR
character["name"].append("robin")


print(character)

print("name" in character)