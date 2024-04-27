a=[1,2,3,4]
b=[10,20,30]

def f(x,y):
    return x+y

L=map(f,a,b)
print(list(L))