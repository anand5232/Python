'''for i in range(1,11):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
'''
# using only one loop
'''for i in range(1,100):
        print('*'*i)'''

# making a euilateral triangular with star symbol
'''for i in range(1,11):
    n=40;
    print(' '*n, '*'*(i))
    n-=1'''
# program to display the number from 1 to 100
for x in range(1,11):
    for y in range(1,11):
        print('{:8}'.format(x*y))
    print()
