n=int(input("Enter the number of tasks/inputs\n"))
print("Enter the numbers\n")
for i in range(n):
    i=int(input())
    t=1
    s=0
    queue=[]
    while i>(s+(2**t)):#using permutation to eliminate some previous numbers and calculate the number of digits in this paticular number
        s=s+(2**t)
        t+=1#counting number of digits

    for j in range(t):
        queue.append(1)
    
    d=t-1
    while d > 0:
        if (i > s + (2 ** d)):
            queue[t - 1 - d] = 2
            s = s + (2 ** d) + 1
            print(s)
        d = d - 1
    if i == s + 1:
        queue[t - 1] = 2
    print(queue)
       



