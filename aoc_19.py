from collections import defaultdict


class AOC:
    memo = {}
    ans = 0
    ore_r_cost = 0
    clay_r_cost = 0
    ob_r_cost = 0
    ge_r_cost = 0
    max_n_ore = 0
    max_n_clay = 0
    max_n_obsid = 0
    final_ans = 1
    count = 0
    hits = 0
    final_ans

    def do_it(self ):
        with open('aoc_19.txt') as my_file:

            for line in my_file:
                self.ans = 0
                self.count += 1

                x = line[:-1].split(" ")
                self.ore_r_cost = (int(x[6]), 0, 0)
                self.clay_r_cost = (int(x[12]), 0, 0)
                self.ob_r_cost = (int(x[18]), int(x[21]), 0)
                self.ge_r_cost = (int(x[27]), 0, int(x[30]))

                self.max_n_ore = max(self.ore_r_cost[0], self.clay_r_cost[0], self.ob_r_cost[0], self.ge_r_cost[0])
                self.max_n_clay = self.ob_r_cost[1]
                self.max_n_obsid = self.ge_r_cost[2]
                print( "Max To build: ", self.ore_r_cost, self.clay_r_cost, self.ob_r_cost, self.ge_r_cost)
                print( "Mats required for robot: ", self.max_n_ore, self.max_n_clay, self.max_n_obsid)

                ans = self.dp(0, 1, 0, 0, 0, 0, 0, 0, 0, {})
                print("answer:" ,ans)

    def dp(self, time, num_ore_robots, num_clay_robots, num_obsi_robots, num_gem_robots, ore, clay, obsid, gems, memo):
        # print(num_ore_robots, num_clay_robots, num_obsi_robots, num_gem_robots,
        #      "mats", ore, clay, obsid, gems, time * " ", time, self.ans)
        # print("Max: ", self.max_n_ore, self.max_n_clay, self.max_n_obsid)
        self.count += 1
        if self.count % 10000000 == 0:
            print(num_ore_robots, num_clay_robots, num_obsi_robots, num_gem_robots,
                  ore, clay, obsid, gems, time * " ", time, self.count, self.hits, self.hits / self.count,
                  self.final_ans)

        vector = (time,
                  num_ore_robots + num_clay_robots * 10 + num_obsi_robots * 100 + num_gem_robots * 1000,
                  ore + clay * 100 + obsid * 10000 + gems * 1000000)
        if vector in memo:
            self.hits += 1
            return memo[vector]

        ret = 0

        if time == 32:
            return gems

        if ore >= self.ore_r_cost[0] and num_ore_robots < self.max_n_ore:
            ret = max(ret, self.dp( time + 1,
                    num_ore_robots + 1, num_clay_robots, num_obsi_robots, num_gem_robots,
                    ore + num_ore_robots - self.ore_r_cost[0], clay + num_clay_robots,
                    obsid + num_obsi_robots, gems + num_gem_robots, memo))

        if ore >= self.clay_r_cost[0] and num_clay_robots < self.max_n_clay:
            ret = max(ret, self.dp( time + 1,
                    num_ore_robots, num_clay_robots + 1, num_obsi_robots, num_gem_robots,
                    ore + num_ore_robots - self.clay_r_cost[0], clay + num_clay_robots,
                    obsid + num_obsi_robots, gems + num_gem_robots, memo))

        if ore >= self.ob_r_cost[0] and clay >= self.ob_r_cost[1] and num_obsi_robots < self.max_n_obsid:
            ret = max(ret, self.dp( time + 1,
                    num_ore_robots, num_clay_robots, num_obsi_robots + 1, num_gem_robots,
                    ore + num_ore_robots - self.ob_r_cost[0], clay + num_clay_robots - self.ob_r_cost[1],
                    obsid + num_obsi_robots, gems + num_gem_robots, memo))

        if ore >= self.ge_r_cost[0] and obsid >= self.ge_r_cost[2] :
            ret = max(ret, self.dp( time + 1,
                    num_ore_robots, num_clay_robots, num_obsi_robots, num_gem_robots + 1,
                    ore + num_ore_robots - self.ge_r_cost[0], clay + num_clay_robots,
                    obsid + num_obsi_robots - self.ge_r_cost[2], gems + num_gem_robots, memo))

        ret = max(ret, self.dp(time + 1,
                num_ore_robots, num_clay_robots, num_obsi_robots, num_gem_robots,
                ore + num_ore_robots, clay + num_clay_robots,
                obsid + num_obsi_robots, gems + num_gem_robots, memo))

        memo[vector] = ret
        self.final_ans = max(self.final_ans, ret)
        return ret


'''
4 ore/robot
1:
0 1 and 0

2: 
6 2r and 3o

2 ore/robot
1:

2:
4 2r and 3o
4 1 1 and 2 1

'''