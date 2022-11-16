import random
import math
import statistics
from numpy.random import permutation as randomperm
#======================= Function ================

def fir_gen(N,m,Lo,Hi):
    Population=[]
    for j in m:
        Population[j]=Lo[j]+(Hi[j]-Lo[j])*random.randint(N,1)
        
    return Population

def fit_eval(Population,N,m):
    selection_probability=0
    fit=[]
    ave_fit=0
    max_fit=0
    opt_sol=0
    opt_sol=[]
    
    for in range(1,N):
        x1=Population[i,1]
        x2=Population[i,2]
        
        fit[i]=(1+math.cos(2*math.pi*x1*x2))*math.exp(-(abs(x1))+abs(x2))
        
        selection_probability=fit/sum(fit)
        
        ave_fit=statistics.mean(fit)
        max_fit=max(fit)
        max_loc=max(fit)
        opt_sol=Population(max_loc)
        #=======
        for i in Population:
            
            opt_sol.append(i)
        
        return "??????"
    
def g_roulette_wheel(Population,N,selection_probability):
    
    mating_pool=[]
    cdf=[]
    
    cdf[i]=selection_probability[1]
    
    for i in range(1,N):
        
        cdf[i]=cdf[i-1]+selection_probability[i]
        
        
    for i in range(1,N):
        r=random.randint(0,1)
        
        for j in range(1,N):
            
            if r <= cdf[i]:
                
                mating_pool[i,:]=Population[j,:]
                
                break
            
def g_crossover(mutaing_pool,Pc,N,m,Hi,Lo):
    new_pop=[]
    parent_num=randomperm(N)
    
    for j in range(1,2,N):
        
        pointer1=parent_num[j]
        
        pointer2=parent_num[j+1]
        
        P1=mating_pool[pointer1,:]
        P1=mating_pool[pointer2,:]
        
        
        if rand < Pc:
            
            a=random.randint(1,m)
            
            off1=a*P1+(1-a)*P2 
            off2=a*P2+(1-a)*P1

        else:
            
            off1=P1
            off2=P2 
        
        new_pop[j,:]=off1
        new_pop[j+1,:]=off2
        
    for i in range(1,N):
        
        for j in range(1,m):
            
            if new_pop[i,j]>Hi[j] or new_pop[i,j]<Lo[j]:
                new_pop[i,j]=Lo[j]+(Hi[j]-Lo(j))*random
                
def g_mutation(new_pop,Pm,N,m,scale,Hi,Lo):
    Population=[]
    
    DR=Hi-Lo
    Sigma=DR*scale
    
    Delta="zeros(N,m"
    
    for j in range(1,m):
        Delta[:j]=Sigma[j]*random.randint(N,1)
        
    mask=random.randint(N,m)<= Pm
    
    Population=new_pop+(mask*Delta)
    
    
    for i in range(1,N):
        
        for j in range(1,m):
            
            if Population[i,j]>Hi[j] or Populationp[i,j] < Lo[j]:
                
                Population[i,j]=Lo[j]+(Hi[j]-Lo[j])*random
                
                
    return "???????"                                      
        
    




#========================= End Function =====================
N=50
Pc=0.3
Pm=0.2
scale=0.2
ITER=100
m=2
Lo=[-4,-1.5]
Hi=[2,1]

#================== Main ===============
Population=[]
fir_gen(N,m,Lo,Hi)

best_so_far=[]
Avrage_fitnes=[]
    
for it in ITER:
    
    if it==1:
        best_so_far[it]=max_fit
        final_sol=opt_sol
    
    elif (max_fit>best_so_far[it-1]):
        best_so_far[it]=max_fit
        final_sol=opt_sol
    
    else:
        
        best_so_far[it]=best_so_far=it-1

    Avrage_fitnes[it]=ave_fit
    
    [muting_pool]=g_roulette_wheel(Population,N,selection_probability)
    
    [new_pop]=g_crossover(mating_pool,Pc,N,m,Hi,Lo)
    
    [Population]=g_mutation(new_pop,Pm,N,m,scale,Hi,Lo)

#display("final Solutain    optimum fitnes") 

result=[final_sol_best_so_far[end]]






    
           
        
    