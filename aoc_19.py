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

    opt = [0 ,0]
    for i in range(1,50):
        opt.append(i + opt[i])
    print(opt)

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
                print( "To build: ", self.ore_r_cost, self.clay_r_cost, self.ob_r_cost, self.ge_r_cost)
                print( "Max Mats required: ", self.max_n_ore, self.max_n_clay, self.max_n_obsid)
                self.dp(0, 1, 0, 0, 0, 0, 0, 0, 0)
                print("answer:" ,self.ans)
                self.final_ans = self.final_ans * self.ans
        print("final answer:", self.final_ans)

    def dp(self, time, num_ore_robots, num_clay_robots, num_obsi_robots, num_gem_robots, ore, clay, obsid, gems):
        # print(time * "  ",time, n_o, n_c, n_ob, n_g, o, c, ob, g, "   ", len(memo))

        # print("Max: ", self.max_n_ore, self.max_n_clay, self.max_n_obsid)

        self.count += 1
        if self.count % 10000000 == 0:
            print(num_ore_robots, num_clay_robots, num_obsi_robots, num_gem_robots, ore, clay, obsid, gems, time * "  ", time, self.ans)

        if time == 32:
            if self.count % 1000000 == 0:
                print(num_ore_robots, num_clay_robots, num_obsi_robots, num_gem_robots, "mats", ore, clay, obsid, gems, time * " ", time, self.ans)
            if gems>self.ans:
                print(gems)
            self.ans = max(gems, self.ans)
            return

        t = 32 - time
        if self.ans >= num_gem_robots * t + gems + self.opt[t]:
            return

        if ore >= self.ge_r_cost[0] and obsid >= self.ge_r_cost[2]:
            self.dp(time + 1,
                    num_ore_robots, num_clay_robots, num_obsi_robots, num_gem_robots + 1,
                    ore + num_ore_robots - self.ge_r_cost[0], clay + num_clay_robots,
                    obsid + num_obsi_robots - self.ge_r_cost[2], gems + num_gem_robots)
        if ore >= self.ore_r_cost[0] and num_ore_robots < self.max_n_ore:
            self.dp(time + 1,
                    num_ore_robots + 1, num_clay_robots, num_obsi_robots, num_gem_robots,
                    ore + num_ore_robots - self.ore_r_cost[0], clay + num_clay_robots,
                    obsid + num_obsi_robots, gems + num_gem_robots)
        if ore >= self.clay_r_cost[0] and num_clay_robots < self.max_n_clay:
            self.dp(time + 1,
                    num_ore_robots, num_clay_robots + 1, num_obsi_robots, num_gem_robots,
                    ore + num_ore_robots - self.clay_r_cost[0], clay + num_clay_robots,
                    obsid + num_obsi_robots, gems + num_gem_robots)
        if ore >= self.ob_r_cost[0] and clay >= self.ob_r_cost[1] and num_obsi_robots < self.max_n_obsid:
            self.dp(time + 1,
                    num_ore_robots, num_clay_robots, num_obsi_robots + 1, num_gem_robots,
                    ore + num_ore_robots - self.ob_r_cost[0], clay + num_clay_robots - self.ob_r_cost[1],
                    obsid + num_obsi_robots, gems + num_gem_robots)

        # if (ore < self.ore_r_cost[0] and ore < self.clay_r_cost[0] and
        #     ore < self.ob_r_cost[0] and clay < self.clay_r_cost[1] and
        #     ore < self.ge_r_cost[0] and obsid < self.ge_r_cost[2]
        # ):
        self.dp(time + 1,
                num_ore_robots, num_clay_robots, num_obsi_robots, num_gem_robots,
                ore + num_ore_robots, clay + num_clay_robots,
                obsid + num_obsi_robots, gems + num_gem_robots)
        return
