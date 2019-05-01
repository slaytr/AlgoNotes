import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.wuxiaworld.com/novel/coiling-dragon-preview/cdp-chapter-1')
print(r.status_code)
soup = BeautifulSoup(r.text, 'lxml')

divs = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['fr-view'])

text = repr(divs)

stack = []
record_paragraph = False
paragraph = ""
test_count = 0

story = []

for letter in text:
    if not record_paragraph:
        if len(stack) == 0 and letter == "<":
            stack.append("<")
        elif len(stack) > 0:
            if letter == ">" and stack[-1] == "<":
                stack = []
                record_paragraph = True
                test_count +=1
    else:
        if len(stack) == 0 and letter == "<":
            stack.append("<")
        elif len(stack) > 0:
            if letter == "/" and stack[-1] == "<":
                stack.append(letter)
            elif letter == ">" and stack[-1] == "/":
                stack = []
                record_paragraph = False
                story.append(paragraph)
                paragraph = ""
        else:
            paragraph = paragraph + letter

for paragraph in story:
    print(paragraph)