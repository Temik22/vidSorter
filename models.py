import os
import subprocess


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

    def run(self):
        if self.path is not None and self.path is not '':
            subprocess.Popen(('start', self.path), shell=True)
        else:
            raise ValueError('Path is not defined')

    def __str__(self):
        return 'Video. Name: {0.name}, Genre: {0.genre}, Seen: {0.seen}, Rate: {0.rate}, Path: {0.path}'.format(self)

    def __repr__(self):
        return 'Video\t{0.name}\t{0.genre}\t{0.duration}\t{0.rate}\t{0.seen}\t{0.path}'.format(self)


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


def create(request):
    if len(request) == 7:
        if request[0] == 'Video':
            for i in range(1, 7):
                if request[i] == 'None':
                    request[i] = None
                elif i == 3:
                    request[i] = int(request[i])
                elif i == 4:
                    request[i] = float(request[i])
                elif i == 5:
                    request[i] = bool(request[i])
                elif i == 6:
                    request[i] = os.path(request[i])
            return Video(*request[1:])
    else:
        raise ValueError


def test():
    pass
    # a = Video('pidor', path=file)

    # a.run()
