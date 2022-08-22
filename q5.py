# 5. Write a python script to print first N odd natural numbers in reverse order

n=int(input("Enter the number: "))

i=2*n-1
while(i>0):
    print(i,end=' ')
    i-=2