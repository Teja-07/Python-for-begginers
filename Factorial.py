'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
num=int(input("Enter the number"))
fact=1
if num<0:
    print("Factorial doesnot exist for negative numbers")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact*=i
        print("The factorial of number is:",fact)