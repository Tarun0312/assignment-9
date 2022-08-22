# 7. Write a python script to print first N even natural numbers in reverse order


N=int(input("Enter the number: "))

i=N

while(i>0):
    print(2*i,end=' ')
    i-=1