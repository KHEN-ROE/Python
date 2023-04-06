"""
Web Article Text Analysis
You'll use the BeautifulSoup library to extract text from an article
on a news website like the Washington Post,
and then perform the same text analysis as before.
"""

#pip install bs4
#pip install requests

import re
import requests
from bs4 import BeautifulSoup

url = input("enter the url of the news article : ")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.find("article")
paragraphs = article.find_all("p")
text = " ".join(p.get_text() for p in paragraphs)
print('text: ', text)

characters = len(text)
words = re.findall(r'\b\w+\b', text)
word_count = len(words)
sentences = re.findall(r'[.!?]', text)
sentence_count = len(sentences)
average_word_length = sum(len(word) for word in words) / word_count
average_sentence_length = word_count / sentence_count

vowels = "aeiou"
vowel_count = {vowel: text.lower().count(vowel) for vowel in vowels}
total_vowel_count = sum(vowel_count.values())
vowel_percentage = total_vowel_count / characters * 100

word_frequency = {}
for word in words:
    word = word.lower()
    word_frequency[word] = word_frequency.get(word, 0) + 1

print(f"Total characters: {characters}")
print(f"Total words: {word_count}")
print(f"Total sentences: {sentence_count}")
print(f"Average word length: {average_word_length:.2f}")
print(f"Average sentence length: {average_sentence_length:.2f}")
print("\nVowel frequencies and percentages:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count} ({count/characters * 100:.2f}%)")
print("\nWord frequencies:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")

