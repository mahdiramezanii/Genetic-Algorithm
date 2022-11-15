import random
import math
import statistics
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
    
    for in range(1,N):
        x1=Population[i,1]
        x2=Population[i,2]
        
        fit[i]=(1+math.cos(2*math.pi*x1*x2))*math.exp(-(abs(x1))+abs(x2))
        
        selection_probability=fit/sum(fit)
        
        ave_fit=statistics.mean(fit)
        
        




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






    
           
        
    