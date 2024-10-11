category_map = {'low': 1, 'medium': 2, 'high': 3}
category_values = ['low', 'medium', 'high', 'medium', 'low']
mapped_values = [category_map[val] for val in category_values]
print(mapped_values)  # Output: [1, 2, 3, 2, 1]
