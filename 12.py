#for python, try not to inherient from the build-in types(list, dict, etc)
#try use the collection module, like collections.UserDict, collections.UserList, collections.UserString

#this is the inherient from build-in type
class Dopper(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

dd = Dopper(a = 1)  #inherient from dict class
dd.update(b = 2)    #inherient from dict class
dd['c'] = 3         #inherient from Dopper Class
dd #hope result is {'a':1, 'b':2, 'c':6}

#this is the inherient from collection module
import collections

class Dopper2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)
    def __contains__(self, item):       #this is not necessary, which is the same as the super class
       super().__contains__(item)

ee = Dopper2(a = 1)
ee.update(b = 2)
ee['c'] = 3
ee #hope result is {'a':2, 'b':4, 'c':6}
class a():
    pass

print(a.mro())

pass
