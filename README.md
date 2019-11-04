# Wiki-Game-Crawler

Play an automated Wiki Game!

## To Run
```
python3 main.py [--start WIKI_PAGE_URL] [--end WIKI_PAGE_URL] [--limit MAX_PAGE_JUMPS]
```
Please include the full wikipedia url (wrapped in quotes) for --start and --end. If start or end are left blank, they will be given a random Wiki page. You can play totally random games by leaving them both out.

--limit will limit how many page jumps the Web crawler will perform, as the amount of work/memory required will grow exponentially with each page. If you leave limit blank, the default limit is 6 jumps.

### Examples
```
python3 main.py
```
```
python3 main.py --limit 3
```
```
python3 main.py --start 'https://en.wikipedia.org/wiki/English_ship_Constant_Reformation_(1619)'
```
```
python3 main.py --start 'https://en.wikipedia.org/wiki/English_ship_Constant_Reformation_(1619)' --end 'https://en.wikipedia.org/wiki/Marxism' --limit 5
```
```
python3 main.py --end 'https://en.wikipedia.org/wiki/Jesus'
```
