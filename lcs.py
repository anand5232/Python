# program for LCS
def lcs(X,Y):
    m=len(X)
    n=len(Y)
    L=[[0]*(n+1) for i in range(m+1)]
    print(L)
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0
                elif x[i-1]==y[j-1]:
                    L[i][j]=L[i-1][j-1]+1
                    else:
                        L[i][j]=max
                        (L[i-1][j])
                    return L[m][n]
X="bisect"
Y="trisect"
print(" length of the lcs is ",lcs(x,y))
                
            
