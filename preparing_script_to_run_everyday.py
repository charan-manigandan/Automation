from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_time = now.strftime("%m%d%y")

website = "https://www.thesun.co.uk/sport/football/"

options = Options()
options.add_argument("--headless=new")

service = Service(r"C:\\Users\\chara_brh5qvm\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get(website)
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').text
    subtitle = container.find_element(by="xpath", value='./a/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
file_name = f'headline-{month_day_time}.csv'
final_path = os.path.join(application_path, file_name)

df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv(final_path)

driver.quit()