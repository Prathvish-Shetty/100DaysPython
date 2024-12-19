from bs4 import BeautifulSoup

# import lxml
# lxml.parser

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)  # gives first a tag
all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

class_is_heading = soup.find_all(class_="heading")
# print(class_is_heading)

h3_headings = soup.find_all("h3", class_="heading")
print(h3_headings)

headings = soup.select(".heading")
print(headings)