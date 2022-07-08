import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/12016/Desktop/WebDrover/chromedriver.exe")
driver.get('https://www.thesound.co.nz/home/other/2020/09/rolling-stone-releases-500-greatest-albums-of-all-time.html')
results = []
content = driver.page_source
soup = BeautifulSoup(content)

for element in soup.findAll(attrs='text parbase section'):
    name = element.find('b')
    if name not in results:
        results.append(name.text)

df = pd.DataFrame({'Name':results})
df.to_csv('names.csv',index=False , encoding="utf-8")
print(results)