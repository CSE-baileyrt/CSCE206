import requests

# Tasks:
# 1. Download the scrabble dictionary
#       Verbs: GET, PUT, POST, DELETE
# 2. Store the data (list of words)
# 3. Analyze that data

response = requests.get(
    'https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt'
)
text_lines = response.text.split('\n')
# full text content:
#print(text_lines)
# word count:
#print(len(text_lines))

longest_word = ''   # the longest word in the list
max_len = 0         # the length of that word ^
shortest_word = ''
min_len = 10
num_words = len(text_lines)
sum_letters = 0

for word in text_lines:
    #print(word)
    # longest word routine:
    # 1. look at the current word
    # 2. if the current word is longer than longest_word, do the following:
    #   a. overwrite longest_word, replacing it with the current word
    #   b. overwrite max_len, replacing it with the length of current word
    # 3. ignore everything smaller than max_len
    if len(word) > max_len:
        longest_word = word
        max_len = len(word)
        #print('The longest word so far is {}, with {} characters'.format(word, max_len))

    # shortest word routine:
    # invert the logic from the longest word
    if len(word) < min_len:
        shortest_word = word
        min_len = len(word)
    
    # for the average
    sum_letters += len(word)
    #same as: sum_letters = sum_letters + len(word)

# after the loop, after looking at all 178,000 words
print('The longest is {}, with {} characters'.format(longest_word, max_len))
print('The shortest is {}, with {} characters'.format(shortest_word, min_len))
print('There are {} words total and {} characters total'.format(num_words, sum_letters))
print('The average word length is {}'.format(sum_letters / num_words))
