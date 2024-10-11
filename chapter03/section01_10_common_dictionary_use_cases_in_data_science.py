word_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
word_count = {}

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
print(word_count)  # Output: {'apple': 2, 'banana': 3, 'orange': 1}

   
