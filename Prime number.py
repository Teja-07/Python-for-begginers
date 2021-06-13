'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
num=int(input("Enter the number:"))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i==0):
            flag=True
            break
if flag:
    print("not a prime number")
else:
    print("prime number")