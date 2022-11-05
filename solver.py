from math import ceil

from solution import Solution

bagType_price = [1.7, 1.75, 6, 25, 200]
bagType_co2_production = [30, 24, 36, 42, 60]
bagType_co2_transport = [3, 4.2, 1.8, 3.6, 12]
bagType_reusable = [0, 1, 5, 9, 12]
bagType_washtime = [1, 2, 3, 5, 7]

from solution import Solution


class Solver:
    def __init__(self, game_info):
        self.population = game_info['population']
        self.companyBudget = game_info['companyBudget']
        self.behavior = game_info['behavior']
        self.day = 0
        self.bags = []

    def Solve(self, bagtype, days):
        self.days = days
        self.price = bagType_price[bagtype-1]
        self.co2_prod = bagType_co2_production[bagtype-1]
        self.co2_trans = bagType_co2_transport[bagtype-1]
        self.reusable = bagType_reusable[bagtype-1]
        self.washtime = bagType_washtime[bagtype-1]
        self.solution = Solution('True', 7, 1, bagtype)

        for _ in range(days):
            self.solution.orders.append(self.best())
            self.day += 1
        
        return self.solution


    # Solution 1: "Spend all money day 1"
    def wasteMoney(self, bagtype):
        return int(self.companyBudget / bagType_price[bagtype])

    # Solution 2: "Spend equally money every day"
    def splitMoney(self, bagtype):
        return int(self.companyBudget / bagType_price[bagtype] / self.days)

    # Solution 3: "Everyone get one bag every day"
    def holdMoney(self, bagtype):
        return int(self.companyBudget / bagType_price[bagtype] / self.population / self.days)

    def newStrat(self):
        for i in range(len(self.bags)):
            w, r = self.bags[i]
            self.bags[i] = [w-1, r]

        if not self.bags:
            self.bags.append([self.washtime, self.reusable])
            return self.population * 9 + 7
        
        for i in range(len(self.bags)):
            if self.bags[i][0] == 1:
                r = self.bags[i][1]
                self.bags = self.bags[:i] + self.bags[i+1:]
                if r > 0:
                    self.bags.append([self.washtime, r-1])
                return 0

        self.bags.append([self.washtime, self.reusable])
        return self.population * 9 + 7

    def newNewStrat(self):
        if self.day > 20:
            if self.day % 4 < 2:
                return 19
            return 0
        if self.day > 10:
            if self.day % 4 < 2:
                return 21
            return 0
        if self.day % 4 != 2:
            return 97
        return 0

    def newNewNewStrat(self):
        arr = [
            70,
            70,
            0,
            70,
            70,
            0,
            50,
            0,
            50,
            49,
            43,
            0,
            43,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ]

        return arr[self.day]

    def newNewNewNewStrat(self):
        arr = [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ]

        return arr[self.day]

    def best(self):
        arr = [
            270,
            60,
            60,
            0,
            0,
            60,
            0,
            0,
            60,
            60,
            60,
            60,
            60,
            0,
            0,
            60,
            0,
            0,
            60,
            0,
            60,
            0,
            0,
            60,
            20,
            0,
            0,
            0,
            50,
            0,
            0
        ]

        return arr[self.day]