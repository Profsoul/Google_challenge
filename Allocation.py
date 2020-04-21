# Kickstart_Problem
#Round_A_2020
#Allocation

T = int(input())
for x in range(1,T+1):
    N,C = map(int,input().split())
    A = list(map(int,input().split()))
    A = sorted(A)
    count = 0
    for  i in A:
        C -= i
        if C >= 0:
            count+=1
        else:
            pass
    print("Case "+"#{}".format(x)+": "+str(count))

"""
 #The above code is the solution for the KickStart 2020 Round_A.
 ##Allocation Problem.

   ///////////Soul Corporation////////////

Contact us @profsoul23@gmail.com

"""
