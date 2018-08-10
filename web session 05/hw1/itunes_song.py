from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url = 'https://www.apple.com/itunes/charts/songs/'
connection = urlopen(url)
raw_data =connection.read()
text = raw_data.decode('unicode_escape')

soup = BeautifulSoup(text, 'html.parser')
div_new =soup.find('div','main')
sec_new = div_new.find('section','section chart-grid')
div_new2 = sec_new.find('div','section-content')
ul_new =div_new2.find('ul')
li_list = ul_new.find_all('li')
new_items = []
for li in li_list:
    b = li.h3.a
    c= li.h4.a
    link1 = url +b['href']
    title1 = b.text
    link2 = url +c['href']
    title2 = c.text
    item = {
        'Artists' :title1,
        'Link1': link1,
        'Song' :title2,
        'Link2':link2
    }
    new_items.append(item)

import pyexcel
pyexcel.save_as(records = new_items, dest_file_name = 'itunesong.xlsx')

