import re
from urllib.request import Request, urlopen

url = 'http://pokemondb.net/pokedex/national'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode('UTF8')

poke_names = re.findall(r'<a class="ent-name" href="/pokedex/.*?">(.*?)</a>', html)
print(poke_names)

