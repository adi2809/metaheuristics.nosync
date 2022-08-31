from statistics import NormalDist
from numpy.random import randint, rand
class RandomWalk: 
    def __init__(self, lb, ub, func, mode):
        

        if(mode in ['six_sigma', 'standard']): 
            self.mode = mode
        else: 
            raise ValueError("choose modes from the solver choices")

        self.lb = lb 
        self.ub = ub
        self.func = func 
        self.dist = NormalDist(0, 1)

    def step_func(self): 
        if self.mode == "standard": 
            return self.dist.samples(1)[0]-0.5
        else: 
            return self.dist.inv_cdf(rand())/6 

    def solve(self, max_iter): 
        curr_min = randint(self.lb, self.ub+1)
        for i in range(max_iter): 
            
            new_min = curr_min + self.step_func() * (self.ub-self.lb)
            print(new_min, self.func(new_min))
            print("\n")

            if(new_min<self.lb or new_min > self.ub or self.func(new_min)>self.func(curr_min)): 
                for i in range(max_iter): 
                    new_min = curr_min + self.step_func() * (self.ub-self.lb)
                    print(new_min, self.func(new_min))

                    if not (new_min<self.lb or new_min > self.ub or self.func(new_min)>self.func(curr_min)): 
                        break 
                

            curr_min = new_min

        return curr_min


            

            


        