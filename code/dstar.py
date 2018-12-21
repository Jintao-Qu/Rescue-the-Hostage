import global_var as gl
import utils
import tkinter
import time
import lines
import math
from sys import maxsize

class State(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.state = "."
        self.t = "new"
        self.h = 0
        self.k = 0

    def cost(self, state):
        if self.state == "#" or state.state == "#":
            return maxsize
        return math.sqrt(math.pow((self.x - state.x), 2) +
                         math.pow((self.y - state.y), 2))

    def set_state(self, state):
        if state not in ["s", ".", "#", "e", "*"]:
            return
        self.state = state


class Map(object):

    def __init__(self, row, col):
        self.row = int(row)
        self.col = int(col)
        self.map = self.init_map()

    def init_map(self):
        map_list = []
        #print("self", self.row, self.col)
        for i in range(int(self.row)):
            tmp = []
            for j in range(int(self.col)):
                tmp.append(State(i, j))
            map_list.append(tmp)
        return map_list

    def print_map(self):
        for i in range(self.row):
            tmp = ""
            for j in range(self.col):
                tmp += self.map[i][j].state + " "
            print(tmp)
    def draw_map(self, s):
        cv = gl.get_value("cv")
        while s != gl.get_value("end"):
            sxy = utils.index_to_xy([s.x+1, s.y+1])
            spxy = utils.index_to_xy([s.parent.x+1, s.parent.y+1])
            if gl.get_value("if_obs") == True:
                line = cv.create_line(sxy[0], sxy[1], spxy[0], spxy[1], fill="red", width=2)
            else:
                line = cv.create_line(sxy[0], sxy[1], spxy[0], spxy[1], fill="green", width=2)
            lines.lines.append(line)
            #s.set_state("s")
            s = s.parent
        s.set_state("e")
    def get_neighbers(self, state):
        state_list = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if state.x + i < 0 or state.x + i >= self.row:
                    continue
                if state.y + j < 0 or state.y + j >= self.col:
                    continue
                state_list.append(self.map[state.x + i][state.y + j])
        return state_list

    def set_obstacle(self, point_list):
        for x, y in point_list:
            if x < 0 or x >= self.row or y < 0 or y >= self.col:
                continue
            self.map[x][y].set_state("#")
    def erase_obstacle(self, point_list):
        for x, y in point_list:
            if x < 0 or x >= self.row or y < 0 or y >= self.col:
                continue
            self.map[x][y].set_state(".")


class Dstar(object):

    def __init__(self, maps):
        self.map = maps
        self.open_list = set()

    def process_state(self):
        x = self.min_state()
        if x is None:
            return -1
        k_old = self.get_kmin()
        self.remove(x)
        if k_old < x.h:
            for y in self.map.get_neighbers(x):
                if y.h <= k_old and x.h > y.h + x.cost(y):
                    x.parent = y
                    x.h = y.h + x.cost(y)
        elif k_old == x.h:
            for y in self.map.get_neighbers(x):
                if y.t == "new" or y.parent == x and y.h != x.h + x.cost(y) \
                        or y.parent != x and y.h > x.h + x.cost(y):
                    y.parent = x
                    self.insert(y, x.h + x.cost(y))
        else:
            for y in self.map.get_neighbers(x):
                if y.t == "new" or y.parent == x and y.h != x.h + x.cost(y):
                    y.parent = x
                    self.insert(y, x.h + x.cost(y))
                else:
                    if y.parent != x and y.h > x.h + x.cost(y):
                        self.insert(y, x.h)
                    else:
                        if y.parent != x and x.h > y.h + x.cost(y) \
                                and y.t == "close" and y.h > k_old:
                            self.insert(y, y.h)
        return self.get_kmin()

    def min_state(self):
        if not self.open_list:
            return None
        min_state = min(self.open_list, key=lambda x: x.k)
        return min_state

    def get_kmin(self):
        if not self.open_list:
            return -1
        k_min = min([x.k for x in self.open_list])
        return k_min

    def insert(self, state, h_new):
        if state.t == "new":
            state.k = h_new
        elif state.t == "open":
            state.k = min(state.k, h_new)
        elif state.t == "close":
            state.k = min(state.h, h_new)
        state.h = h_new
        state.t = "open"
        self.open_list.add(state)

    def remove(self, state):
        if state.t == "open":
            state.t = "close"
        self.open_list.remove(state)

    def modify_cost(self, x):
        if x.t == "close":
            self.insert(x, x.parent.h + x.cost(x.parent))

    def run(self, start, end):
        self.open_list.add(end) #insert end in open_list
        while True:
            self.process_state()
            if start.t == "close":
                break
        start.set_state("s")
        s = start


        while s != gl.get_value("end"):
            s.set_state("s")
            s = s.parent
        s.set_state("e")

        self.map.print_map()
        print("")
        self.map.draw_map(start)
        print("OK")
        tmp = start
        #self.map.set_obstacle([(2, 1), (2, 2), (2, 3), (2, 4)])
        #self.map.erase_obstacle([(2, 0)])
        flag = False
        while tmp != gl.get_value("end"):

            tmp.set_state("*")
            if gl.get_value("if_moved") != True:
                rkij = gl.get_value("rkij")
                self.map.erase_obstacle(utils.set_obstacle(rkij))
                utils.rk_random_move()
                rkij = gl.get_value("rkij")
                poij = gl.get_value("poij")
                gl.set_value("if_moved", True)
                self.map.set_obstacle(utils.set_obstacle(rkij))
                print("----------------------------------")
            #utils.msgbox()



            nr = gl.get_value("nr")
            nc = gl.get_value("nc")
            poij = gl.get_value("poij")
            lmij = gl.get_value("lmij")
            rkij = gl.get_value("rkij")
            self.map.print_map()
            print("")
            if tmp.parent.state == "#":
                #self.modify(tmp)
                #continue
                utils.obstacle(tmp.x, tmp.y)
                flag = True
                return
            tmp = tmp.parent
            utils.PO_move(tmp.x, tmp.y)

        if flag == False:
            tmp.set_state("e")

    def modify(self, state):
        self.modify_cost(state)
        while True:
            k_min = self.process_state()
            if k_min >= state.h:
                break

'''
if __name__ == '__main__':
    m = Map(5, 5)
    m.set_obstacle([(2, 0), (2, 1), (2, 2), (2, 3)])
    start = m.map[0][0]
    end = m.map[4][4]
    dstar = Dstar(m)
    dstar.run(start, end)
    #m.print_map()
'''