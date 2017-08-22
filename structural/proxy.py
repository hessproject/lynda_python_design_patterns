import time

class Producer():
    '''Resource intensive object to be instantiated'''
    def produce(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer has time to meet you now!")

class Proxy:
    '''Less resource intensive proxy to use as middleman'''
    def __init__(self):
        self.occupied = False
        self.producer = None

    def produce(self):
        print("Artist checking if Producer is available...")

        if not self.occupied:
            self.producer = Producer()
            time.sleep(2)

            self.producer.meet()

        else: 
            time.sleep(2)
            print("Producer is busy!")

p = Proxy()
p.produce()

p.occupied = True

p.produce()