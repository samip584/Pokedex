import re
from urllib.request import Request, urlopen


pokedex_page_url = 'http://pokemondb.net/pokedex/national'
pokemon_page_url = 'https://pokemondb.net/pokedex/'

poke_name_regex = r'<a class="ent-name" href="/pokedex/.*?">(.*?)</a>'
type_table_regex = r'''<tr>
<th>Type</th>
<td>
(.*?)</td>
</tr>'''
poke_type_regex = r'<a class="type-icon type-.*?" href="/type/.*?">(.*?)</a>'

req = Request(pokedex_page_url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode('UTF8')
poke_names = re.findall(poke_name_regex, html)

poke_url = []
for poke_name in poke_names:
    poke_url = pokemon_page_url + poke_name
    req = Request(poke_url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read().decode('UTF8')

    poke_type_html = re.findall(type_table_regex, html)[0]
    poke_types = re.findall(poke_type_regex, poke_type_html)
    print(poke_name, poke_types)
