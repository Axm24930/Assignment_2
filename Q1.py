n=int(input("Enter the star pattern range:"))
for i in range( 1,n+1):
    print('*'*i)
j=range(n)[::-1]
for i in j:
    print('*'* i)
