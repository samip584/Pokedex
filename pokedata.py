import re
from urllib.request import Request, urlopen


url = 'http://pokemondb.net/pokedex/national'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode('UTF8')
link = 'https://pokemondb.net/pokedex/'
poke_names = re.findall(r'<a class="ent-name" href="/pokedex/.*?">(.*?)</a>', html)

poke_url=[]
for poke_name in poke_names:
    poke_url = link + poke_name
    req = Request(poke_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read().decode('UTF8')
    print(html)
