import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

# titles = soup.find_all("a", class_="govuk-link gem-print-link govuk-link--no-underline")

# for title in titles:
#    print(title.string)

#Get all titles with gem-c-document-list__item-title class
bs_titles = soup.find_all("a", class_="govuk-link gem-print-link govuk-link--no-underline")
 
for title in bs_titles:
   print(title.string)

#Get all descriptions with class gem-c-document-list__item-description
bs_descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
 

#Save titles and descriptions as lists of strings
titles = []
for title in bs_titles:
	titles.append(title.string)

# descriptions = []
# for desc in bs_descriptions:
# 	descriptions.append(desc.string)
