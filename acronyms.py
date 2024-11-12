import requests
# Terminal window: pip install requests (windows)
#                   pip3 install requests (mac)

# download the acronyms file from Github (comma-separated values)
response = requests.get('https://raw.githubusercontent.com/krishnakt031990/Crawl-Wiki-For-Acronyms/master/AcronymsFile.csv')

# print(response.text)
# break up the file into one acronym per line
text_lines = response.text.split('\n')
# each string in the list is an acronym with its meaning
print(len(text_lines))  # how many lines in the file? 5843

# # look at just one line:
# print( text_lines[15] )
# # break up one line by " - " (space dash space)
# one_line = text_lines[15].split(' - ')
# acro_part = one_line[0].strip()
# meaning_part = one_line[1].strip()
# print(acro_part)
# print(meaning_part)

# create a dictionary variable BEFORE the loop
acronyms = {}
# do the same thing for EVERY line in the file
for line in text_lines:
    # split up each line into its components
    components = line.split('-', 1)   # split on "dash", but only 1 time
    if len(components) > 1: # could also use "== 2"
        acro = components[0].strip()
        mng = components[1].strip()
        # print('Acro: {}, meaning: {}'.format(acro, mng))
        # store those values together in a dictionary
        # add a new item to a dictionary: dictionary[key] = value
        acronyms[acro] = mng

# AFTER the loop (and OUTSIDE the loop)
print('Found {} acronyms in the file'.format( len(acronyms) ))

# from here on, don't use text_lines anymore. That's the file
# just use the acronyms dictionary
# TODO: print the meaning of the acronym "ACCD"
# print( acronyms['ACCD'] )
# challenge: turn this into an app
# prompt the user for any acronym, we print it
# that is homework 4

# more code down here (not needed for the homework)
# TODO: find the longest acronym
longest_acro = ''
# TODO: find the shortest meaning (definition)
shortest_meaning = 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT'
# TODO: find the meaning with the most alternates
#       find the acronym with the most possible meanings (same thing)
most_meanings = ''

for k,v in acronyms.items():
    # every dictionary has 3 built-in lists: .keys(), .values(), .items()
    # simultaneously filling both k and v from each item in the dictionary
    # k,v represent each key and each value, one pair at a time
    if len(k) > len(longest_acro):
        # k becomes the new winner
        longest_acro = k
    if len(v) < len(shortest_meaning):
        # v becomes the new winner
        shortest_meaning = v
    if v.count(',') > most_meanings.count(','):
        # v becomes the new winner
        most_meanings = v

# OUTSIDE the loop
print(longest_acro)
print(shortest_meaning)
print(most_meanings)