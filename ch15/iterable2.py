# iterable2.py

# 클래스로 이터레이터 생성

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position +=1
        return result

if __name__ == "__main__":
    item = MyIterator([1,2,3])
    
    # print(next(item))
    # print(next(item))
    # print(next(item))
    # print(next(item)) # StopIteration

    print(type(item))

    for i in item:
        print(i)

print("================================================================")

# ReverseIterator

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result

if __name__ == "__main__":
    item = ReverseIterator([1,2,3,4])
    print(type(item))
    print(next(item))
    print("aa")
    for i in item:
        print(i)


# dir() : 객체의 속성을 보여주는 함수
print(dir(item))
print("__iter__" in dir(item))
