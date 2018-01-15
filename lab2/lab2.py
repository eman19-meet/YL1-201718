#execise 1:
a=[5,10,15,20,25]
b=[]
def eman():
    b.append(a[0])
    b.append(a[-1])
eman()
print(b)

#exercise 2:
a=[1,1,2,3,5,8,13,21,34,55,89]
for i in range(len(a)):
    if a[i]<5:
        print(a[i])

c=[]       
for i in range(len(a)):
    if a[i]<5:
        c.append(a[i])
print(c)

k=[]
def hi(p):
    for i in range(len(a)):
        if a[i]<p:
        k.append(a[i])

#exercise 3:
x=[1,1,2,3,5,8,13,21,34,55,89]
y=[1,2,3,4,5,6,7,8,9,10,11,12,13]
z=[]
def hello():
    for i in range(len(y)):
        if x[i]==y[i]:
            z.append(x[i])

#exercise 4:
m=[1,2,3,4,5,6,7,8,9]
counter=0
def prime(n):
    for i in range(len(m):
        if n%m[i]!=0:
            counter++
    if counter>2:
        print("its not a prime number")
    else:
        print("its a prime number")

