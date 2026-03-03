# func2.py

na = 10
nb = 11
print("na", na, end=" ")
print("nb", nb)

def swap(pa, pb):
    buf = pa
    pa = pb
    pb = buf

    return pa, pb

swap(na, nb)
print("==========")
print("na", na, end=" ")
print("nb", nb)

na, nb = swap(na,nb)
print("==========")
print("na", na, end=" ")
print("nb", nb)

na, nb = nb, na
print("==========")
print("na", na, end=" ")
print("nb", nb)