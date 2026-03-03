# id2.py

def fk(cb):
    total=0
    for sb in range(0, 3, 1):
        total += cb[sb]
    cb[2] = total
    print("cb_id", id(cb))
    return cb

ca=[10,20,30]
print(ca) # 10,20,30
print("ca_id", id(ca))
cd=fk(ca) # cd=ca  근데 ca는 함수 내부에서 [10, 20, 60]로 바뀜
print("ca_id", id(ca))
print(ca) # 둘이 같은 거 출력
print(cd)


