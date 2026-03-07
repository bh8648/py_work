# ch15연습문제.py

"""
이터레이터 생성방법
1. iter() 함수 사용
2. 클래스 작성
3. 제너레이터 생성
"""

food = ["김밥", "만두", "양념치킨", "족발", "피자", "쫄면", "라면"]

iter_food = (x for x in food)
print(type(iter_food))

iter_food = iter(food)
print(type(iter_food))

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
        self.position += 1
        return result
iter_food = MyIterator(food)
print(type(iter_food))
for x in iter_food:
    print(x)

print("__iter__" in dir(iter_food))
print("__next__" in dir(iter_food))
print(hasattr(iter_food, "__iter__"))
print(hasattr(iter_food, "__next__"))

print("===========================================================================")
# 제너레이터 생성 방법
# 1. yield
# 2. 제너레이터 컴프리핸션
# 3. 클래스

data = """11
22
33
44
55"""

path = "ch15/iter_test.txt"

def write_file(file_path): 
    with open(file_path, 'w') as file: 
        file.write(data)
        
def read_file(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
        print(text)
        g = (x for x in text)
        print(type(g))
        for x in g:
            print(x.strip())
            

def read_file2(file_path):
    with open(file_path, 'r') as f:
        for line in f.readlines():
            yield line.strip()



write_file(path)
read_file(path)
print("----------------------------------")
lines = read_file2(path)
print(type(lines))
print(next(lines))
print(next(lines))
for line in lines:
    print(line)


