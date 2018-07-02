from urllib.request import Request, urlopen
lis = []
pokelis = []
i = 0
l = 0
url = 'http://pokemondb.net/pokedex/national'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode('UTF8')
print(html)
string = 'ent-name" href="/pokedex/'
lis.append(html.find(string,0))
l = lis[i]+len(string)
while(html[l]!='"'):
	l += 1
pokelis.append(html[(lis[i]+len(string)):l])
while(i != 806):
	i = i + 1
	lis.append(html.find(string,lis[i-1]+1))
	l = lis[i]+len(string)
	while(html[l]!='"'):
		l += 1
	pokelis.append(html[(lis[i]+len(string)):l])
print(pokelis)

