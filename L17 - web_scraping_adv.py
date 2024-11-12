import requests
from bs4 import BeautifulSoup

w3_page = requests.get('https://www.w3schools.com/tags/ref_colornames.asp')
soup = BeautifulSoup(w3_page.content, 'html.parser')

# TASK: teach HTML structure [id, value, attr, class, style, a tag href vs target]
# HTML structure:
#<div>
#   <span class="colornamespan">
#       <a target="_blank" href="">Color name</a>
#   </span>
#   <span class="colorhexspan">
#       <a target="_blank" href="">Color hex</a>
#   </span>
#</div>

color_table = soup.find(id='colornamestable')
span_list = color_table.find_all('span')

color_dict = {}
color_name = ''

for span in span_list:
    # step 1:
    #print(span.a.text)
    #print(span['class'][0])

    # step 2:
    if span['class'] == ['colornamespan']:
        # hold this temporarily
        color_name = span.a.text
    elif span['class'] == ['colorhexspan']:
        # store the pair in the dictionary (previous value, current value)
        color_dict[color_name] = span.a.text
    # no else needed, ignore any other spans

print('Found {} colors'.format(len(color_dict)))

# TODO: find the longest name, shortest name, count the number of 'F' characters in the hex values
#   or any other exploration as needed
