from discrete import greedy_local
import math 

def test_greedy_local(ub, lb): 
    func1 = lambda x : (x-math.pi)**2
    func2 = lambda x : math.sin(x+math.pi/math.e)+2
    func3 = lambda x : math.sin(x+math.pi/math.e)
    func4 = lambda x : (x-math.e)**2

    func = lambda x : (func1(x)*func3(x)+2) + func4(x)/func2(x)
    solver = greedy_local.GreedyLocal(func, lb, ub)

    for i in range(20): 
        local_min = solver.solve()
        print(f"local minimum at : {local_min}, val : {func(local_min)}")
        print("\n")
        

if __name__ == "__main__":
    test_greedy_local(10, -10)
