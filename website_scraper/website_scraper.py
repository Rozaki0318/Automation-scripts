import urllib3
from bs4 import BeautifulSoup

def get_upcoming_events(url):
    req = urllib3.PoolManager()
    res = req.request('GET', url)
    soup = BeautifulSoup(res.data, 'html.parser')

    events = soup.find_all('span', {'class': 'titleline'})
    print(events)

    for event in events:
        event_details = dict()
        event_details['title'] = event.find('a').text
        event_details['link'] = event.find('a').get('href')
        print(event_details)

get_upcoming_events('https://news.ycombinator.com/')
