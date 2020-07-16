import models
import os


class GeneratorError(Exception):
    pass

class searchRequest():
    def __init__(self, searchType, text):
        # request can be 4 types: name, genre, seen, rate
        self.searchType = searchType
        self.text = text


class Collection:
    data = {}  # data here have id as a key
    lastId = 0
    freeIds = set()
    archiveName = 'data.mda'

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
            print(self.freeIds)
        else:
            raise ValueError('this id is unused: {}'.format(index))

    def __str__(self):
        # this is just for test, because gui doesnt need such method
        result = []
        for k, v in self.data.items():
            result.append('{}: {}'.format(k, v))
        result = ';\n'.join(result)
        return '[{0}]\nlast:{1.lastId}, free: {1.freeIds}'.format(result, self)

    def __repr__(self):
        return "bla bla bla bla"

    def search(self, requests):
        searchFuncs = {
            'name': lambda x, y: x.lower() in y.name.lower(),
            'genre': lambda x, y: x.lower() == y.genre.lower(),
            'seen': lambda x, y: x == y.seen,
            'rate': lambda x, y: float(x) <= y.rate
        }
        temp = self.data.copy()
        result = {}
        for request in requests:
            if request.__class__ == searchRequest:
                func = searchFuncs[request.searchType]
                for k, v in temp.items():
                    if func(request.text, v):
                        result[k] = v
            else:
                raise ValueError(
                    'Search method get wrong type of request: need to be class searchRequest')
            temp = result.copy()
            result.clear()
        return temp

    def generateList(self):
        result = []
        for v in self.data.values():
            result.append(str(v))
        return result

    def getFromList(self, index):
        return list(self.data.values())[index]

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

    def reload(self, file=None):
        if file is None:
            file = self.archiveName
        print('Reloading collection from {}...'.format(file))
        with open(file, 'r') as f:
            s = f.readline()
            self.lastId = int(s)
            s = set(list(map(int, f.readline().strip()[1:-1].split(', '))))
            self.freeIds = s
            s = f.readlines()
            for el in s:
                temp = el.strip().split('\t')
                self.data[int(temp[0])] = models.create(temp[1:])
        print('Reloading completed.')


def test():
    # a = []
    # for i in range(4):
    #     a.append(models.Video('name' + str(i)))

    col = Collection()
    # for el in a:
    #     col.add(el)

    # print(col)
    # col.remove(2)
    # col.remove(3)
    # print(col)
    # col.archive()

    col.reload()
    print(col)
    print('Done')
