import requests # type: ignore

from bs4 import BeautifulSoup # type: ignore

url = "https://www.python.org/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)

latest_news = soup.find('div', attrs={'class':"medium-widget blog-widget"})
#print(latest_news)

title_news = latest_news.find_all('a')
#print(title_news)
'''
for item in title_news:
    print(item.get_text)
    print('--'*20)

time_list = latest_news.find_all('time')
for time in time_list:
    print(item.get_text())
    print('--'*20)
'''
conteext = soup.select_one('div.medium-widget.applications-widget.last ul.menu li')    
print(conteext)
for item in conteext:
    print(item.get_text())
    print('--'*20)

ontact_events=soup.select ('div.mdiu-widget event-widget.last ul li time')
print(conteext)
class cconteext_events_itme:
   ...

for item in cconteext_events_itme:
  print(item.get_text())
  print('--'*30)
  
cconteext_events_itme=soup.select('div.medium-widget.event-widget.last ul li time')
for item in cconteext_events_itme:
   print(item.get_text())
   print("-"*30)