# FinancialResourceAllocation

This project aims to form a Genetic algorithm for financial resource allocation for victims of a disaster.

Parameters for availing financial help: Economic background, Age, Amount of loss occured

Objectives: 
1. Maximise the number of individuals receiving financial help.

Ob1 = n(S) where S = {x : 1<= x <= n & Chr[x] != 0}

2. Maximise the number of individuals who have poor economic background / Minimise the economic fitness of individuals receiving financial help.

Ob2 = Σeco[i] ∀ i ϵ S

3. Maximise the number of senior citizens and kids.

Ob3 = n(M) where M = {x : x ϵ S and (Age[x] < 18 or Age[x] >= 60)

4. Maximise the amount given out as help.

Ob4 =  Σcost[i] ∀ i ϵ S

5. Maximise the loss incurred for recipients.

Ob5 = Σloss[i] ∀ i ϵ S

Fitness Of a Chromosome

Since we’ve to maximise Ob1,3,4,5 and minimise Ob2
Fitness = (Ob1 + Ob3 + Ob4 + Ob5) / (1 + Ob2)

Constraints: Total aiding amount should be less than or equal to the amount of money at disposal.
