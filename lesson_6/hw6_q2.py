class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass


res = Road(20, 5000)
print(res.calc(), 'ton')

