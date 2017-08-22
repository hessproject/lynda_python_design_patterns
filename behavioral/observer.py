class Subject(object):
    '''Abstract class'''
    def __init__(self):
        self._observers = [] #References to all observers. This a one-to-many relationship. One subject observed by multiple observers

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Core(Subject):
    '''Concrete class'''
    def __init__(self, name=''):
        Subject.__init__(self)
        self._name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp
    
    @temp.setter
    def temp(self, temp):
        self._temp = temp
        self.notify()

class TempViewer:
    def __init__(self,name=''):
        self._name = name

    def update(self, subject):
        print('Temperature Viewer {}: {} has temperature {}'.format(self._name, subject._name, subject._temp))

c1 = Core('Core 1')
c2 = Core('Core 2')

o1 = TempViewer('1')
o2 = TempViewer('2')

c1.attach(o1)
c1.attach(o2)

c1.temp = 80
c1.temp = 90
