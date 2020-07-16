import models


class GeneratorError(Exception):
    pass


class searchRequest():
    def __init__(self, searchType, text):
        # request can be 4 types: name, genre, seen, rate
        self.searchType = searchType
        self.text = text

    def __repr__(self):
        return 'Request: {0.searchType}, {0.text}'.format(self)


class Collection:
    data = {}  # data here have id as a key
    lastId = 0
    freeIds = set()
    archiveName = 'data.txt'

    def generateId(self):
        if len(self.freeIds) == 0:
            self.lastId += 1
            return self.lastId - 1
        else:
            return self.freeIds.pop()

    def add(self, addable):
        # now adding will be able if addable is not verified
        # todo verification
        index = self.generateId()
        if self.data.get(index) is None:
            self.data[index] = addable
        else:
            raise GeneratorError('id is already used: {}'.format(index))

    def remove(self, index):
        if self.data.get(index) is not None:
            del self.data[index]
            self.freeIds.add(index)
        else:
            raise ValueError('this id is unused: {}'.format(index))

    def __str__(self):
        # this is just for test, because gui doesnt need such method
        result = []
        for k, v in self.data.items():
            result.append('{}: {}'.format(k, v))
        result = ';\n'.join(result)
        return '[{0}]\nlast:{1.lastId}, free: {1.freeIds}'.format(result, self)

    def search(self, requests):
        result = []
        for k, v in self.data.items():
            if self.check(requests, v):
                result.append(k)

        return result

    def check(self, requests, current):
        searchFuncs = {
            'name': lambda x, y: x.lower() in y.name.lower(),
            'genre': lambda x, y: x.lower() == y.genre.lower(),
            'seen': lambda x, y: x == y.seen,
            'rate': lambda x, y: float(x) <= y.rate
        }
        count = 0
        for req in requests:
            if req.__class__ == searchRequest:
                if searchFuncs[req.searchType](req.text, current):
                    count += 1
            else:
                raise ValueError(
                    'Search method get wrong type of request: need to be class searchRequest')
        return count == len(requests)

    def generateList(self):
        result = []
        for v in self.data.values():
            result.append(str(v))
        return result

    def getIndexFromList(self, index):
        return list(self.data.keys())[index]

    def archive(self, file=None):
        if file is None:
            file = self.archiveName
        print('Archiving to {}...'.format(file))
        with open(file, 'w') as f:
            f.write('{0.lastId}\n'.format(self))
            f.write('{}\n'.format(self.freeIds))
            for k, v in self.data.items():
                f.write('{}\t{}\n'.format(k, v.__repr__()))
        print('Archivation completed.')

    def reload(self, f):
        print('Reloading collection from {}...'.format(f.name))
        s = f.readline()
        self.lastId = int(s)
        s = f.readline()
        if s.strip() == 'set()':
            s = set()
        else:
            s = set(list(map(int, s.strip()[1:-1].split(', '))))
        self.freeIds = s
        s = f.readlines()
        for el in s:
            temp = el.strip().split('\t')
            self.data[int(temp[0])] = models.create(temp[1:])
        print('Reloading completed.')
