# pip/pip3 install beautifulsoup4
# already have "requests" module

import requests
from bs4 import BeautifulSoup

# TASK: teach HTML [angle bracket, tag, a tag (and href), img (and src), span, div, h1, h2, h3, p]

# # get all images from the sc.edu main page
# sc_page = requests.get('https://sc.edu/')
# soup = BeautifulSoup(sc_page.content, 'html.parser')

# img_list = soup.find_all('img')
# for img in img_list:
#     print(img.get('src'))

#############################################################

# # get all hyperlinks from the wikipedia main page
# wiki_page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
# soup = BeautifulSoup(wiki_page.content, 'html.parser')

# link_list = soup.find_all('a')
# for link in link_list:
#     print(link.get('href'))

#############################################################

# get from fake jobs
fake_jobs_page = requests.get('https://realpython.github.io/fake-jobs/')
soup = BeautifulSoup(fake_jobs_page.content, 'html.parser')
# container with all of the cards
results = soup.find(id="ResultsContainer")
# all cards in a list
job_elements = results.find_all("div", class_="card-content")
# # Version 1
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element)
#     print(company_element)
#     print(location_element)
# # Version 2
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
# Version 3
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title").text.strip()
    company_element = job_element.find("h3", class_="company").text.strip()
    location_element = job_element.find("p", class_="location").text.strip()
    print('{} with {} ({})'.format(title_element, company_element, location_element))