from numpy.random import randint
class GreedyLocal:
    def __init__(self, func, lb, ub): 
        """
        func : discrete function to identify local minima of 
        lb : lower bound of the domain on which minima has to be searched on 
        ub : upper bound of the domain on which minima has to be searched on 
        """
        self.func = func
        self.lb = lb 
        self.ub = ub 

    def neighbourhood_func(self, x): 
        """
        returns the closed neighbourhood of the current point 'x'
        for any point we consider only two points in N(x) = {x-1,
        x+1}
        """
        if (x-1)<self.lb: 
            if(x+1)>self.ub: 
                return self.lb, self.ub 
            else: 
                return self.lb, x+1
        else: 
            if(x+1)>self.ub: 
                return x-1, self.ub 
            else: 
                return x-1, x+1

    def get_initial_point(self): 
        """
        returns a random integer to start search from. 
        """
        return randint(self.lb, self.ub+1)

    def stop_criteria(self, x): 
        """
        returns if we have found a local minima for the function. 
        """
        l, r = self.neighbourhood_func(x)
        fx, fl, fr = self.func(x), self.func(l), self.func(r)
        if(fx<=fl and fx<=fr): 
            return True 
        else:
            return False

    def solve(self): 
        max_iter = 100 
        curr_min = self.get_initial_point()
        print(f"iteration {0} : curr_min = {curr_min}")
        for i in range(max_iter): 
            if(self.stop_criteria(curr_min)):
                break 
            else: 
                l, r = self.neighbourhood_func(curr_min)
                fmin, fl, fr = self.func(curr_min), self.func(l), self.func(r)

                if(fl<=fmin):
                    if(fl<fr):
                        curr_min=l
                    else:
                        curr_min=r
                else:
                    curr_min=r

            print(f"iteration {i+1} : curr_min = {curr_min}, value : {self.func(curr_min)}")

        return curr_min
    


    



    