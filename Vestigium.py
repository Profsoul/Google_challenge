# Codejam_problem
#Qualification_Round
#Vestigium

T = int(input())
for x in range(1,T+1):
    N = int(input())
    L = []
    b = []
    for i in range(N):
        L.append(list(map(int,input().split())))
    sm = 0
    rm = rm1 =0
    cm1 = cm =0
    for j in range(N):
        for z in range(N):
            if j== z:
                sm += L[j][z]
            
            if L[j].count(L[j][z])> 1:
                rm += 1
            b.append(L[z][j])    
        if rm > 1:
            rm1 += 1
            
        for a in range(N):
            if b.count(b[a])>1:
                cm += 1
        b = []
                
        if cm > 1:
            cm1 += 1
            cm = 0

    
    print("Case "+"#"+str(x)+": "+str(sm)+" "+str(rm1)+" "+str(cm1))
"""
 #The above code is the solution for the Codejam 2020 Qualification Round.
 ##Vestigium Problem.

   ///////////Soul Corporation////////////

Contact us @profsoul23@gmail.com

"""
