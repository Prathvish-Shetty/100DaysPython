from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
articles = soup.find_all(name="a", class_="storylink")
# print(articles)
articles_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0])for score in soup.find_all(name="span", class_="score")]
# print(articles_texts)
# print(article_links)
# print(article_upvotes)
# print(article_upvotes[0])

largest_number = max(article_upvotes)
largest_number_index = article_upvotes.index(largest_number)
print(articles_texts[largest_number_index])
print(article_links[largest_number_index])


# /robots.txt