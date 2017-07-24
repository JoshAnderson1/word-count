#shows the 10 most used words on a website.
import requests
from bs4 import BeautifulSoup
word_count = dict()
print("returns the 10 most used words on a website.")
website = input("What website: ")
#requests website
page = requests.get(website)
#makes a "soup" using the BeautifulSoup lib
soup = BeautifulSoup(page.content, "html.parser")
words = soup.find_all('body')[0].get_text()
words = words.split()
#making the dict of words in the website
for word in words:
    words = word.split()[0]
    if words in word_count:
        word_count[words] = word_count[words] + 1
    else:
        word_count[words] = 1
#loop for finding the word that appears most often
most_word = list()
for key, val in list(word_count.items()):
    most_word.append((val, key))
most_word.sort(reverse = True)
print(most_word[:10])
