from dstar import *
import global_var as gl
import utils
import lines
def mode0():
    nr = gl.get_value("nr")
    nc = gl.get_value("nc")
    poij = gl.get_value("poij")
    lmij = gl.get_value("lmij")
    rkij = gl.get_value("rkij")
    print(nr, nc)
    m = Map(int(nr), int(nc))
    m.set_obstacle(utils.set_obstacle(rkij))
    start = m.map[poij[0]-1][poij[1]-1]
    end = m.map[lmij[0]-1][lmij[1]-1]
    gl.set_value("end", end)
    dstar = Dstar(m)
    dstar.run(start, end)
    utils.msgbox()

def mode1():
    return
def mode2():
    return
