class House(object):
    def accept(self, visitor):
        '''Interface to accept a visitor'''
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print('{} worked on by {}'.format(self, hvac_specialist))

    def work_on_electricity(self, electrician):
        print('{} worked on by {}'.format(self, electrician))

    def __str__(self):
        return self.__class__.__name__

class Visitor(object):
    '''Abstract visitor'''
    def __str__(self):
        return self.__class__.__name__

class HvacSpecialist(Visitor):
    '''Concrete visitor 1'''
    def visit(self, house):
        house.work_on_hvac(self)

class Electrician(Visitor):
    '''Concrete visitor 2'''
    def visit(self, house):
        house.work_on_electricity(self)

hvac = HvacSpecialist()
elec = Electrician()

house = House()

house.accept(hvac)
house.accept(elec)