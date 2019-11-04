import requests
import re
from collections import deque

BASE_URL = 'https://en.wikipedia.org/wiki/'
RANDOM_URL = 'https://en.wikipedia.org/wiki/Special:Random'

def end_game(start,end,path):
    print('{} -> {} in {} hops'.format(start,end,len(path)))
    print(' --> '.join(path),'-->',end)
    exit(0)

def play(start,end,limit):
    Q = deque()
    checked = set()
    print('Play!')

    start = get_subject(start) if start else get_subject(get_random_page())
    end = get_subject(end) if end else get_subject(get_random_page())

    print('{} -> {}'.format(start,end))
    Q.append((start,[]))

    while len(Q) > 0:
        title, path = Q.popleft()
        print('Searching page: {}'.format(title))
        checked.add(title)
        
        page = requests.get(BASE_URL+title).text
        links = set(get_links(page))
        
        if end in links:
            end_game(start,end,path+[title])
        
        new_urls = [(found_url, path+[title]) for found_url in links if found_url not in checked]
        checked = checked.union(links)

        Q.extend(new_urls)
        
        if len(path) > limit:
            print('\n\nPath not found within {} jumps :(\n'.format(limit))
            exit()
    

def get_links(page):
    link_list = re.findall(r'<a href="(.*?)</a>', page)
    return [get_subject(l) for l in link_list if l[:6] == '/wiki/' and not 'Wikipedia' in l]

def get_subject(url):
    wiki_find = url.find('/wiki/')+6
    end_find = url[wiki_find:].find('"')+wiki_find if '"' in url else len(url)

    return url[wiki_find:end_find]
    
def get_random_page():
    page = requests.get(RANDOM_URL).url
    # print(page)
    return page

