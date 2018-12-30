# while loop

n=0
while(n<1000):
    print(n)
    n=n+1

# for loop
for i in range(10,1000):
    print(i)
    i=i+1

# for loop in collection of the element

days=['sunday','monday','tuesday','wednesday','friday','saturday']
for j ,d in days:
    print(j)

# break
# continue

for i in range(0,10):
    if(i==5 or i==7):
        break
    if(i%2==0):
        continue
    print(i)


