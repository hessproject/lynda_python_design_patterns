class Korean:
    '''Korean speaker'''
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong!"

class British: 
    '''English speaker'''
    def __init__(self):
        self.name = "British"
        
    def speak_english(self):
        return "Hello!"

class Adapter:
    '''Changes the geenric method name to individualized method names'''

    def __init__(self, obj, **adapted_method):
        self._object = obj
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        '''Return the rest of the attributes'''
        return getattr(self._object, attr)


objects = []
k = Korean()
b = British()

#Map the individual speak_* methods to the generic speak method with the adapter
objects.append(Adapter(k, speak=k.speak_korean))
objects.append(Adapter(b, speak=b.speak_english))

for obj in objects:
    print('{} says "{}"\n'.format(obj.name, obj.speak()))