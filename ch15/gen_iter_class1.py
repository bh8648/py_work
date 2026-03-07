# gen_iter_class1.py

class MyIterator:
    def __init__(self):
        self.data = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.data >= 6:
            raise StopIteration
        result = self.data**2
        self.data +=1
        return result


my_iter = MyIterator()
print(type(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
for i in my_iter:
    print(i)





print("=============================================================================================")

