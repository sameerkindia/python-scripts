import requests
from bs4 import BeautifulSoup
import pprint


def multipage_data(pages=1):
    links = []
    subtext = []

    for num in range(pages):
        res = requests.get(f'https://news.ycombinator.com/news?page={num + 1}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links.extend(soup.select('.titleline > a'))
        subtext.extend(soup.select('.subtext'))

    return links, subtext

# multipage_data(2)


links, subtext = multipage_data()


# print(links)

# votes = soup.select('.score')
# print(soup)
# print(links)
# print(votes)

def short_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    # print(links)
    hn = []
    for idx, item in enumerate(links):

        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))

            if points > 99:
                hn.append({'title': title, 'href': href, 'votes': points})

    return short_stories_by_votes(hn)


# create_custom_hn(links, subtext)
pprint.pprint(create_custom_hn(links, subtext))
