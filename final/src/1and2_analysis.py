import numpy as np
WATER_COST = [8, 8, 5, 10, 5, 8, 10, 5, 8, 8, 10, 8, 5, 8, 8, 8, 10, 10, 8, 8, 5, 5, 8, 5, 10, 8, 5, 5, 8, 8]
FOOD_COST = [6, 6, 7, 10, 7, 6, 10, 7, 6, 6, 10, 6, 7, 6, 6, 6, 10, 10, 6, 6, 7, 7, 6, 7, 10, 6, 7, 7, 6, 6]
np_water = np.array(WATER_COST)
np_food = np.array(FOOD_COST)

def second_average_cost_compute(path,d1,dm,d2,d2_,d3,T):
    np_path = np.array(path)
    second_cost = (5*np_path*np_water[:T] + 10*np_path*np_food[:T])[d1:T-d3+1].sum()
    second_average_cost = second_cost/((T-d3+1)-d1-1)
    print(second_cost,(T-d3+1)-d1-1,second_average_cost)

# 关卡一
path = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, 2, 2, 2]
d1,dm,d2,d2_,d3,T = 10,7,2,1,3,23
second_average_cost_compute(path,d1,dm,d2,d2_,d3,T)

# 关卡二
path = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2]
d1,dm,d2,d2_,d3,T = 9,13,5,1,2,30
second_average_cost_compute(path,d1,dm,d2,d2_,d3,T)