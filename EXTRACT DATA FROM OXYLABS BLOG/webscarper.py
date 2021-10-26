import pandas as pd
from bs4 import BeautifulSoup 
from selenium import webdriver

driver=webdriver.Chrome(executable_path='C:/Users/Klaus/Downloads/software/chromedriver/chromedriver.exe')
driver.get("https://oxylabs.io/blog")

title_results=[]
date_results=[]
author_results=[]
content=driver.page_source
soup=BeautifulSoup(content, features="html.parser")
driver.quit()

for a in soup.find_all(attrs='blog-card__content-wrapper'):
    name=a.find('h2')
    if name not in title_results:
        title_results.append(name.text)


for b in soup.find_all(attrs='blog-card__date-wrapper'):
    date=b.find('p')
    if date not in date_results:
        date_results.append(date.text)

        
for c in soup.find_all(attrs='blog-card__user-info__wrapper'):
    author=c.find('p')
    if author not in author_results:
        author_results.append(author.text)



#this variable will create a two-dimensional table
df=pd.DataFrame({'Names':title_results, 'Dates':date_results, 'Author':author_results})
df.to_csv('OlylabsBlog.csv', index=False, encoding='utf-8')
