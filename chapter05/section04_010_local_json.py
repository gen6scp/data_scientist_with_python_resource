import json

# Load JSON
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in the JSON data
for k in json_data.keys():
    print(k + ': ', json_data[k])
