import collection as col
import models

c = col.Collection()

a = []
a.append(models.Video(name='the name', genre='triller', rate=8.4, seen=False))
a.append(models.Video(name='die nigga die',
                      genre='triller', rate=9.2, seen=True))
a.append(models.Video(name='the king of the jungle',
                      genre='comedy', rate=7.3, seen=False))
a.append(models.Video(name='king Arthur', genre='fantasy', rate=5.5, seen=True))
a.append(models.Video(name='Arthur is nigga',
                      genre='comedy', rate=10, seen=False))

for el in a:
	c.add(el)

print(c)

b = []
b.append(col.searchRequest('name', 'arthur'))
b.append(col.searchRequest('genre', 'comedy'))
b.append(col.searchRequest('rate', 8))
b.append(col.searchRequest('seen', False))

result = c.search(b)

print(result)
