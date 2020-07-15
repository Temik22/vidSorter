class Video:
    verified = False

    def __init__(self, name, genre=None, duration=0,
                 rate=None, seen=False, path=None):
        self.name = name
        self.genre = genre
        self.duration = duration
        self.seen = seen
        self.rate = rate
        self.path = path

    def __str__(self):
        return 'Video. Name: {0.name}, Genre: {0.genre}, Seen: {0.seen}, Rate: {0.rate}'.format(self)

    def __repr__(self):
        return 'Video. Name: {0.name}, Genre: {0.genre}, Seen: {0.seen}, Rate: {0.rate}'.format(self)


class Series:
    vids = {}
    addedVids = 0
    seenVids = 0

    def __init__(self, name, genre=None,
                 numberOfSeries=0, seen=False, rate=None):
        self.name = name
        self.genre = genre
        self.numberOfSeries = numberOfSeries
        self.seen = seen
        self.rate = rate

    def add(self, addable, number):
        if addable.__class__ == Video:
            print('its a video')
        else:
            print('its not a video')

    def __str__(self):
        return 'Series. Name: {0.name}'


def test():
    s = Series('Series')
    v = Video('Film')
    s.add(v, 1)
