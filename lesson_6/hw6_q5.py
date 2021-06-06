class Stationery:
    def __init__(self):
        self.title = 'title'

    def draw(self):
        print('Start rendering')


class Pen(Stationery):
    def draw(self):
        print('Start pen rendering')


class Pencil(Stationery):
    def draw(self):
        print('Start pencil rendering')


class Handle(Stationery):
    def draw(self):
        print('Start handle rendering')


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()
