import re
from urllib.request import Request, urlopen


pokedex_page_url = 'http://pokemondb.net/pokedex/national'
pokemon_page_url = 'https://pokemondb.net/pokedex/'

req = Request(pokedex_page_url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode('UTF8')
poke_names = re.findall(r'<a class="ent-name" href="/pokedex/.*?">(.*?)</a>', html)

poke_url = []
for poke_name in poke_names:
    poke_url = pokemon_page_url + poke_name
    req = Request(poke_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read().decode('UTF8')
    print(html)
