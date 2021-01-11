from itertools import permutations, compress
import numpy as np
from math import floor

# global constant
WAIT,WALK,WORK = 1,2,3
SUN,HOT,SAND = 5,8,10
START,FACTORY,SHOP,END = 0,1,2,3
WEIGHT_BOUND = 1200

# global constant arrays: weather, pathS, graph 
WATER_COST = [8, 8, 5, 10, 5, 8, 10, 5, 8, 8, 10, 8, 5, 8, 8, 8, 10, 10, 8, 8, 5, 5, 8, 5, 10, 8, 5, 5, 8, 8]
FOOD_COST =  [6, 6, 7, 10, 7, 6, 10, 7, 6, 6, 10, 6, 7, 6, 6, 6, 10, 10, 6, 6, 7, 7, 6, 7, 10, 6, 7, 7, 6, 6]
weather =  WATER_COST 

# all possible paths
paths1 = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 8], [0, 1, 2, 3, 8], [0, 1, 8], [0, 8]]
paths2 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15], [0, 1, 2, 3, 4, 5, 6, 7, 8, 15], [0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15], [0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 15], [0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 15], [0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 15], [0, 1, 2, 3, 4, 5, 6, 9, 10, 15], [0, 1, 2, 3, 4, 5, 6, 9, 15], [0, 1, 2, 3, 4, 5, 6, 15], [0, 1, 2, 3, 4, 9, 10, 11, 12, 13, 14, 15], [0, 1, 2, 3, 4, 9, 10, 11, 12, 13, 15], [0, 1, 2, 3, 4, 9, 10, 11, 12, 15], [0, 1, 2, 3, 4, 9, 10, 11, 15], [0, 1, 2, 3, 4, 9, 10, 15], [0, 1, 2, 3, 4, 9, 15], [0, 1, 2, 3, 4, 15], [0, 1, 2, 9, 10, 11, 12, 13, 14, 15], [0, 1, 2, 9, 10, 11, 12, 13, 15], [0, 1, 2, 9, 10, 11, 12, 15], [0, 1, 2, 9, 10, 11, 15], [0, 1, 2, 9, 10, 15], [0, 1, 2, 9, 15], [0, 1, 2, 15]]
paths = [paths1, paths2]

# adjacent matrices 
graph1 = [[0, 6, 0, 0, 0, 0, 0, 0, 3], [0, 0, 2, 0, 0, 0, 0, 0, 3], [0, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 3], [0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0, 3], [0, 0, 0, 0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 3]]
graph2 = [[0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
graphs = [graph1, graph2]

# key_vertices
hash1 = {0:START, 1:SHOP, 2:FACTORY, 3:SHOP, 4:FACTORY, 5:SHOP, 6:FACTORY, 7:SHOP, 8:END}
hash2 = {0:START, 1:FACTORY, 2:SHOP, 3:FACTORY, 4:SHOP, 5:FACTORY, 6:SHOP,7:FACTORY, 8:SHOP, 9:FACTORY, 10:SHOP, 11:FACTORY, 12:SHOP, 13:FACTORY, 14:SHOP, 15:END}


# some helper functions
def raw_path_length(path, graph):
    sum = 0
    if graph == 1:    
        for i in range(len(path)-1):
            sum += graph1[path[i]][path[i+1]]
    else:
        for i in range(len(path)-1):
            sum += graph2[path[i]][path[i+1]]
    return sum

def count_key_vertices(key,graph,path):
    count = 0
    if graph == 1:
        for i in path:
            if hash1[i] == key:
                count += 1
    else:
        for i in path:
            if hash2[i] == key:
                count += 1            
    return count
        

class exhaust_k_days: 
    def __init__(self,k,path,graph):
        self.k = k
        self.path = path
        self.graph = graph
        self.basic_length = raw_path_length(self.path,self.graph)
        # can be reduced by considering sand 
        self.space0 = list(permutations(list(range(k - self.basic_length)), count_key_vertices(FACTORY,graph,path)))
        

    def rough_cleaning(self):
        permutations_sum = [sum(i) for i in self.space0]
        total_sand = weather[:self.k].count(SAND)
        low, high = self.k - total_sand - self.basic_length, self.k - total_sand
        mask = [True if i >= low and i <= high else False for i in permutations_sum]
        self.space0 = list(compress(self.space0,mask))


class permutation:
    def __init__(self,mine_days,k,raw_path,graph):
        self.k = k
        self.raw_path = raw_path
        self.graph = graph
        self.mine_days = mine_days
        self.shop = []
        self.end = []
        self.cost = 0

    def translate(self):
        # _path: compute from the first day
        _path = []
        ptr_factory = 0
        if self.graph == 1:
            for i in range(1,len(self.raw_path)):
                _path += [2]*graph1[self.raw_path[i-1]][self.raw_path[i]]
                self.shop += [0]*graph1[self.raw_path[i-1]][self.raw_path[i]]
                self.end += [0]*graph1[self.raw_path[i-1]][self.raw_path[i]]
                if hash1[self.raw_path[i]] == SHOP:
                    self.shop[-1] = 1
                elif hash1[self.raw_path[i]] == FACTORY:
                    _path += [3]*self.mine_days[ptr_factory]
                    self.shop += [0]*self.mine_days[ptr_factory]
                    self.end += [0]*self.mine_days[ptr_factory]
                    ptr_factory += 1
        else:
            for i in range(1,len(self.raw_path)):
                _path += [2]*graph2[self.raw_path[i-1]][self.raw_path[i]]
                self.shop += [0]*graph2[self.raw_path[i-1]][self.raw_path[i]]
                self.end += [0]*graph2[self.raw_path[i-1]][self.raw_path[i]]
                if hash2[self.raw_path[i]] == SHOP:
                    self.shop[-1] = 1
                elif hash2[self.raw_path[i]] == FACTORY:
                    _path += [3]*self.mine_days[ptr_factory]
                    self.shop += [0]*self.mine_days[ptr_factory]
                    self.end += [0]*self.mine_days[ptr_factory]
                    ptr_factory += 1  
        self.days = _path
        self.end[-1] = 1

    def wait_insert(self):
        flag = 1
        for k in range(6):
            if not flag or len(self.days) > self.k: 
                break
            for i,state in enumerate(self.days):
                flag = 0
                try:
                    if state == WALK and weather[i] == SAND:
                        self.days.insert(i,1)
                        self.shop.insert(i,0)
                        self.end.insert(i,0)
                        flag = 1
                        break
                except:
                    print(i,len(self.days))

    def length_check(self):
        return self.k == len(self.days)

    def weight_check(self,x):
        np_days  = np.array(self.days)
        r_water = (np_days * np.array(WATER_COST[:self.k]))[::-1]
        r_food  = (np_days * np.array(FOOD_COST[ :self.k]))[::-1]

        r_shop = self.shop[::-1]
        r_weight = r_water * 3 + r_food * 2

        shop_num = sum(self.shop)

        water_block = []
        food_block = []
        low = 0
        for c in range(shop_num):
            high = r_shop.index(1)
            r_shop[high] = 0
            tmp_water = r_water[low:high].sum()
            tmp_food = r_food[low:high].sum()
            tmp = tmp_water*3 + tmp_food*2

            if tmp > WEIGHT_BOUND:
                return False
            else:
                water_block.append(tmp_water)
                food_block.append(tmp_food)
                low = high 

        tmp = r_weight[low:].sum()
        tmp_water = r_water[low:].sum()
        tmp_food = r_food[low:].sum()
        y = floor((1200 - 3*x)/2)
        if tmp > WEIGHT_BOUND or x < tmp_water or y < tmp_food:
            return False
        else:
            water_block.append(tmp_water)
            food_block.append(tmp_food)

            water_block = water_block[::-1]
            food_block = food_block[::-1]

        if x < y:
            for i in range(len(food_block)-1):
                if y - food_block[i] > food_block[i+1]:
                    if (y - food_block[i])*2 + water_block[i+1]*3 > 1200:

                        return False 
                    y = y - food_block[i]
            y = floor((1200 - 3*x)/2)
        else:
            for i in range(len(water_block)-1):
                if x - water_block[i] > water_block[i+1]:
                    if (x - water_block[i])*2 + food_block[i+1]*3 > 1200:
                        return False 
                    x = x - water_block[i]
        
        return True



    def total_cost(self,x):
        y = floor((1200 - 3*x)/2)
        cost_0 = x*5 + y*10
        np_days  = np.array(self.days)
        return cost_0 + ((np_days*np.array(WATER_COST[:self.k])).sum()-x)*10 + ((np_days*np.array(FOOD_COST[:self.k])).sum()-y)*20
                
    def total_gain(self):
        return sum([1 if i == 3 else 0 for i in self.days])*1000


if __name__ == "__main__":
    print("===================================================")
    print("Graph 1")
    print("===================================================")
    for path in paths1:
        print("Finding optimal solution for one path......")
        path_clean_gain  = 0
        path_final_path = []
        path_x = 0

        for k in range(20,31):
            a = exhaust_k_days(k,path,1)
            a.rough_cleaning()
            k_clean_gain  = 0
            k_final_path = []
            k_x = 0

            for perm in a.space0:
                b = permutation(perm,k,path,1)
                b.translate()
                b.wait_insert()
                perm_clean_gain = -100000
                perm_final_path = []
                perm_x = 0

                if b.length_check() and len(b.end) == k and count_key_vertices(FACTORY,1,path):
                    perm_gain = b.total_gain()
                    perm_min_cost = 1000000
                    for x in range(98,241):
                        if b.weight_check(x):
                            x_min_cost = b.total_cost(x)
                            if x_min_cost < perm_min_cost:   
                                perm_min_cost = x_min_cost
                                perm_clean_gain = perm_gain - x_min_cost
                                perm_final_path = b.days
                                perm_x = x

                if perm_clean_gain > k_clean_gain:
                    k_clean_gain = perm_clean_gain
                    k_final_path = perm_final_path
                    k_x = perm_x



            if k_clean_gain > path_clean_gain:
                path_clean_gain = k_clean_gain
                path_final_path = k_final_path
                path_x = k_x


        if (path_clean_gain != 0):
            print("For path",path,":")
            print("Total gain = ",path_clean_gain+10000,",Total day = ", len(path_final_path),",Initial x = ", path_x)
            print()
        else:
            print("NO SOLUTION")
            print()


    print("===================================================")
    print("Graph 2")
    print("===================================================")
    for path in paths2:
        print("Finding optimal solution for one path......")
        path_clean_gain  = 0
        path_final_path = []
        path_x = 0

        for k in range(18,31):
            a = exhaust_k_days(k,path,2)
            a.rough_cleaning()
            k_clean_gain  = 0
            k_final_path = []
            k_x = 0
            k_perm = 0

            for perm in a.space0:
                # print("==========================================================")
                b = permutation(perm,k,path,2)
                b.translate()
                b.wait_insert()
                perm_clean_gain = -100000
                perm_final_path = []
                perm_x = 0

                if b.length_check() and len(b.end) == k and count_key_vertices(FACTORY,2,path):
                    perm_gain = b.total_gain()
                    perm_min_cost = 1000000
                    for x in range(130,318):
                        if b.weight_check(x):
                            x_min_cost = b.total_cost(x)
                            if x_min_cost < perm_min_cost:   
                                perm_min_cost = x_min_cost
                                perm_clean_gain = perm_gain - x_min_cost
                                perm_final_path = b.days
                                perm_x = x



                if perm_clean_gain > k_clean_gain:
                    k_clean_gain = perm_clean_gain
                    k_final_path = perm_final_path
                    k_x = perm_x
                    k_perm = perm
                    # print(k_clean_gain,k_final_path,len(k_final_path),k_x)



            if k_clean_gain > path_clean_gain:
                path_clean_gain = k_clean_gain
                path_final_path = k_final_path
                path_x = k_x
                path_perm = k_perm
                # print(path_clean_gain,path_final_path,len(path_final_path),path_x)


        if (path_clean_gain != 0):
            print("For path",path,":")
            print("Total gain = ",path_clean_gain+10000,",Total day = ", len(path_final_path),",Initial x = ", path_x)
            print()
        else:
            print("NO SOLUTION")
            print()