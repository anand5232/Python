def quicksort(alist,first,last):
    if first<last:
        splitpoint=partition(alist,first,last)
        quicksort(alist,first,splitpoint-1)
        quicksort(alist,splitpoint+1,last)
def partition(alist,first,last):
    pivotvalue=alist(first)
    left=first+1
    right=last
    done=false
    while not done :
        print(alist)
        while left<=right and alist (left)<=pivotvalue:
            print('left :',left,alist[left],'right',right,alist[right])
            print(alist[left],'=',pivotvalue,'so left is increamented by 1')
            left=left+1
            print('new left and its value',left,alist[left])
        while alist[right] >= pivotvalue and right  >=left:
            print(alist[right]'>=',pivotvalue)
            print('alist[right] >= pivotvalue and right >= left,so right is incremented by 1')
            right=right-1
            print(" new right and its value",right,alist[right])
        if right<left:
            done=True
        else:
            print(" right",right ,'and','left',left,'right is not less than left')
            
        
            
                  
    
        
