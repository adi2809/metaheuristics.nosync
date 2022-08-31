from discrete import greedy_local
from continuous import random_walk

import math 

# def test_greedy_local(ub, lb): 
#     func1 = lambda x : (x-math.pi)**2
#     func2 = lambda x : math.sin(x+math.pi/math.e)+2
#     func3 = lambda x : math.sin(x+math.pi/math.e)
#     func4 = lambda x : (x-math.e)**2

#     func = lambda x : (func1(x)*func3(x)+2) + func4(x)/func2(x)
#     solver = greedy_local.GreedyLocal(func, lb, ub)

#     for i in range(20): 
#         local_min = solver.solve()
#         print(f"local minimum at : {local_min}, val : {func(local_min)}")
#         print("\n")
        
# def test_random_walk(ub, lb): 
#     func = lambda x : x**5 - 10*x**4 + 35*x**3 - 50*x**2 + 24*x
#     solver1 = random_walk.RandomWalk(0, 4, func, "six_sigma")
#     solver2 = random_walk.RandomWalk(0, 4, func, "standard")


#     local_min = solver1.solve(100)
#     print(f"the minima found is {local_min} and the value is {func(local_min)}")

#     local_min = solver2.solve(100)
#     print(f"the minima found is {local_min} and the value is {func(local_min)}")

if __name__ == "__main__":
    # test_greedy_local(10, -10)
    # test_random_walk(0, 4)
    pass