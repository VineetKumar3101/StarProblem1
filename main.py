print("==========================================================")
N=int(input("Enter the number of line:"))
for I in range(1,N+1): #(1:N)
    for J in range(1,I+1):
        print('*',end='')
    print()

print("==========================================================")

q=int(input("Enter the Number of lines:")) #10
for k in range(0,q): #0-10
    for S in range(0,q-k-1): #0-4
        print(end=" ")
    for m in range(0,k+1):
        print('*',end=" ")
    print()


print("==========================================================")
w=int(input("Enter the Number of lines:"))
for e in range(0,w):
    for r in range(0,w-1-I):
        print(end=" ")
    for t in range(0,e+1):
        print('*',end='')
    print()

print("==========================================================")

x=int(input("Enter the Number of lines:"))
for c in range(0,x):
    for v in range(0,c+1):
        print('* ',end="")
    print()


print("==========================================================")

b=int(input("Enter the Number of lines:"))
for l in range(0,b):
    for h in range(0,l+1):
        print('* ',end="")
    print()
for l in range(b,1,-1):#5-2
    for h in range(1,l):
        print('* ',end="")
    print()

print("==========================================================")