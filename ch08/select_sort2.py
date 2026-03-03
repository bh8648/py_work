# select_sort2.py

def fselsort(ca):
    for i in range(len(ca)):
        mina=ca[i]
        minix=i
        for sb in range(i, len(ca)):
            if mina > ca[sb]:
                mina=ca[sb]
                minix=sb
        temp=ca[i]
        ca[i]=ca[minix]
        ca[minix]=temp
        print(f"{i}번째 순회한 배열{ca}")

ca=[21,10,11,15,13]
fselsort(ca)

print("==================")
print(ca)
