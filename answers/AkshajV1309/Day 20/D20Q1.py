T,F=int(input('Enter test cases: ')),[]
while(T>0):
    N=list(input('Enter Number: '))
    S=[]
    for i in range(len(N)):
        if i>0 and int(N[i])==int(N[i-1]):
            i+=1
        else:
            S.append(N[i])
            i+=1
    F.append("".join(S))
    T-=1
for i in F:
    print('Output:',i)
