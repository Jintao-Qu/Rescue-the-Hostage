import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import global_pic as gc
import global_var as gl
import commands as cmd
import random
import lines
from dstar import *
import time

def generate_arrow():
    #ARROW
    arrow = gc.get_value("arrow")
    right_arrow = gc.get_value("arrow")
    gc.set_value("rig_arrow", right_arrow)
    right_arrowTK = ImageTk.PhotoImage(right_arrow)
    gc.set_value("rig_arrowTK", right_arrowTK)

    up_arrow = arrow.rotate(90)
    gc.set_value("up_arrow", up_arrow)
    up_arrowTK = ImageTk.PhotoImage(up_arrow)
    gc.set_value("up_arrowTK", up_arrowTK)

    lef_arrow = arrow.rotate(180)
    gc.set_value("lef_arrow", lef_arrow)
    lef_arrowTK = ImageTk.PhotoImage(lef_arrow)
    gc.set_value("lef_arrowTK", lef_arrowTK)

    dwn_arrow = arrow.rotate(270)
    gc.set_value("dwn_arrow", dwn_arrow)
    dwn_arrowTK = ImageTk.PhotoImage(dwn_arrow)
    gc.set_value("dwn_arrowTK", dwn_arrowTK)

    #ARROW1
    arrow1 = gc.get_value("arrow1")
    right_arrow1 = arrow1.rotate(45)
    gc.set_value("rig_arrow1", right_arrow1)
    right_arrow1TK = ImageTk.PhotoImage(right_arrow1)
    gc.set_value("rig_arrow1TK", right_arrow1TK)

    up_arrow1 = arrow1.rotate(135)
    gc.set_value("up_arrow1", up_arrow1)
    up_arrow1TK = ImageTk.PhotoImage(up_arrow1)
    gc.set_value("up_arrow1TK", up_arrow1TK)

    lef_arrow1 = arrow1.rotate(225)
    gc.set_value("lef_arrow1", lef_arrow1)
    lef_arrow1TK = ImageTk.PhotoImage(lef_arrow1)
    gc.set_value("lef_arrow1TK", lef_arrow1TK)

    dwn_arrow1 = arrow1.rotate(315)
    gc.set_value("dwn_arrow1", dwn_arrow1)
    dwn_arrow1TK = ImageTk.PhotoImage(dwn_arrow1)
    gc.set_value("dwn_arrow1TK", dwn_arrow1TK)

def draw_map():
    cv = gl.get_value("cv")
    nr = int(gl.get_value("nr"))
    nc = int(gl.get_value("nc"))

    ver_int = int((460 - nr)/(nr - 1))
    gl.set_value("ver_int", ver_int)
    aux = 460 - (ver_int * (nr - 1) + nr)
    top_lef = int(aux/2 + 20)
    gl.set_value("top_lef", top_lef)
    btm_lef = int(aux - top_lef + 20)

    lev_int = int((560 - nc)/(nc - 1))
    gl.set_value("lev_int", lev_int)
    aux = 560 - (lev_int * (nc - 1) + nc)
    lef_lef = int(aux/2 + 20)
    gl.set_value("lef_lef", lef_lef)
    rig_lef = int(aux - lef_lef + 20)


    snr = top_lef + 1
    snc = lef_lef
    for i in range(nr):
        snc = lef_lef+1
        for j in range(nc - 1):
            cv.create_line(snc, snr, snc+lev_int, snr, fill="black", width=1)
            snc = snc + lev_int + 1
        snr = snr + ver_int + 1

    snc = lef_lef + 1
    snr = top_lef
    for i in range(nc):
        snr = top_lef + 1
        for j in range(nr - 1):
            cv.create_line(snc, snr, snc, snr + ver_int, fill="black", width=1)
            snr = snr + ver_int + 1
        snc = snc + lev_int + 1

    init_role_position()
    cv.place(relx=0.04, rely=0.08)

def index_to_xy(p):
    #[1, 1] to [nr, nc]
    xi = p[0]
    yi = p[1]
    ver_int = gl.get_value("ver_int")
    top_lef = gl.get_value("top_lef")
    lev_int = gl.get_value("lev_int")
    lef_lef = gl.get_value("lef_lef")
    x = lef_lef + yi + lev_int*(yi - 1)
    y = top_lef + xi + ver_int*(xi - 1)
    return [x, y]

def init_role_position():
    cv = gl.get_value("cv")
    nr = int(gl.get_value("nr"))
    nc = int(gl.get_value("nc"))
#init rk's position

    rk_i = random.randint(1, nr)
    rk_j = random.randint(1, nc)
    while(rk_i == nr and rk_j == nc):
        rk_i = random.randint(1, nr)
        rk_j = random.randint(1, nc)
    rkxy = index_to_xy([rk_i, rk_j])
    gl.set_value("rkij", [rk_i, rk_j])
    #print("RK position", [rk_i, rk_j])
#init police's position
    po_i = random.randint(1, nr)
    po_j = random.randint(1, nc)

    while(if_catch(rk_i, rk_j, po_i, po_j) or (rk_i == po_i and rk_j ==po_j) or (po_i == nc and po_j == nr)):
        po_i = random.randint(1, nr)
        po_j = random.randint(1, nc)

    poxy = index_to_xy([po_i, po_j])
    gl.set_value("poij", [po_i, po_j])
    #print("PO position", [po_i, po_j])
# init lm's position
    lm_i = random.randint(1, nr)
    lm_j = random.randint(1, nc)
    while(lm_i == po_i and lm_j == po_j) or (lm_i == rk_i and lm_j == rk_j) or (lm_i == nr and lm_j == nc):
        lm_i = random.randint(1, nr)
        lm_j = random.randint(1, nc)
    lmxy = index_to_xy([lm_i, lm_j])
    gl.set_value("lmij", [lm_i, lm_j])
    #print("LM position", [lm_i, lm_j])
    RK = cv.create_image(rkxy[0], rkxy[1], image=gc.get_value("rk_sTK"))
    PO = cv.create_image(poxy[0], poxy[1], image=gc.get_value("police_sTK"))
    LM = cv.create_image(lmxy[0], lmxy[1], image=gc.get_value("lm_sTK"))
    EX = cv.create_image(565, 465, image=gc.get_value("exitTK"))

    gl.set_value("RK", RK)
    gl.set_value("PO", PO)
    gl.set_value("LM", LM)
    gl.set_value("EX", EX)

def if_catch(rk_i, rk_j, po_i, po_j):
    xx = gl.get_value("xx")
    yy = gl.get_value("yy")
    for i in range(8):
        if (rk_i + xx[i] == po_i) and (rk_j + yy[i] == po_j):
            return True
    return False
def if_in_range(x, y):
    if (x >= 1) and (x <= int(gl.get_value("nr"))) and (y >= 1) and (y <= int(gl.get_value("nc"))):
        return True
    else:
        return False

def move(role, xx, yy):
    cv = gl.get_value("cv")
    if role == 0:

        rkij = gl.get_value("rkij")
        poij = gl.get_value("poij")
        RK = gl.get_value("RK")

        if gl.get_value("if_start") == True:
            #rk_cnt = gl.get_value("rk_cnt")
            #rk_cnt.set(int(rk_cnt.get())+1)
            if if_in_range(rkij[0] + xx, rkij[1] + yy) == True:
                aux = index_to_xy([rkij[0] + xx, rkij[1] + yy])
                cv.coords(RK, (aux[0], aux[1]))
                gl.set_value("rkij", [rkij[0] + xx, rkij[1] + yy])
        else:
            if if_in_range(rkij[0] + xx, rkij[1] + yy) == True and if_catch(rkij[0] + xx, rkij[1] + yy, poij[0],
                                                                            poij[1]) == False:
                aux = index_to_xy([rkij[0] + xx, rkij[1] + yy])
                cv.coords(RK, (aux[0], aux[1]))
                gl.set_value("rkij", [rkij[0] + xx, rkij[1] + yy])


    elif role == 1:
        poij = gl.get_value("poij")
        PO = gl.get_value("PO")
        rkij = gl.get_value("rkij")

        if gl.get_value("if_start") == True:
            po_cnt = gl.get_value("po_cnt")
            po_cnt.set(int(po_cnt.get())+1)
            if if_in_range(poij[0] + xx, poij[1] + yy) == True:
                aux = index_to_xy([poij[0] + xx, poij[1] + yy])
                cv.coords(PO, (aux[0], aux[1]))
                gl.set_value("poij", [poij[0] + xx, poij[1] + yy])
        else:
            if if_in_range(poij[0] + xx, poij[1] + yy) == True and if_catch(rkij[0], rkij[1], poij[0] + xx,
                                                                            poij[1] + yy) == False:
                aux = index_to_xy([poij[0] + xx, poij[1] + yy])
                cv.coords(PO, (aux[0], aux[1]))
                gl.set_value("poij", [poij[0] + xx, poij[1] + yy])
    elif role == 2:
        lmij = gl.get_value("lmij")
        LM = gl.get_value("LM")
        if if_in_range(lmij[0] + xx, lmij[1] + yy) == True:
            aux = index_to_xy([lmij[0] + xx, lmij[1] + yy])
            cv.coords(LM, (aux[0], aux[1]))
            gl.set_value("lmij", [lmij[0] + xx, lmij[1] + yy])
        if gl.get_value("if_escape") == True:
            lm_cnt = gl.get_value("lm_cnt")
            lm_cnt.set(int(lm_cnt.get()) + 1)
            gl.set_value("lm_cnt", lm_cnt)

def loop_role():
    sel_role = gl.get_value("sel_role")
    if gl.get_value("is_start"):
        sel_role += 1
        sel_role %= 2
        gl.set_value("sel_role", sel_role)
        HINT = gl.get_value("HINT")
        sel_role_button = gl.get_value("sel_role_button")
        if sel_role == 0:
            sel_role_button.config(image=gc.get_value("rk_sTK"))
            HINT.set("RK移步")
        elif sel_role == 1:
            sel_role_button.config(image=gc.get_value("police_sTK"))
            HINT.set("警察移步")
def msgbox():
    rkij = gl.get_value("rkij")
    poij = gl.get_value("poij")
    lmij = gl.get_value("lmij")
    cv = gl.get_value("cv")
    if if_catch(rkij[0], rkij[1], poij[0], poij[1]):
        messagebox.showwarning("ohno!", "被抓住了，再试一次吧！")
        cmd.restart()
    elif lmij[0] == poij[0] and lmij[1] == poij[1]:
        PO = gl.get_value("PO")
        cv.delete(PO)
        messagebox.showwarning("ohyeh!", "与人质相遇！向出口前进！")
        gl.set_value("if_escape", True)
def msgbox_escape():
    if gl.get_value("if_start") == True:
        rkij = gl.get_value("rkij")
        lmij = gl.get_value("lmij")
        nr = gl.get_value("nr")
        nc = gl.get_value("nc")
        cv = gl.get_value("cv")

        if lmij[0] == int(nr) and lmij[1] == int(nc):
            messagebox.showwarning("ohyeh!", "恭喜！成功解救人质！！")
            cmd.restart()
        elif lmij[0] == rkij[0] and lmij[1] == rkij[1]:
            messagebox.showwarning("ohno!", "被追上了，再试一次吧！")
            cmd.restart()
def set_obstacle(rkij):
    i = rkij[0]-1
    j = rkij[1]-1
    #return [(i-2, j-2), (i-2, j-1), (i-2, j), (i-2, j+1), (i-2, j+2),
    #       (i - 1, j - 2), (i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i - 1, j + 2),
    #       (i, j - 2), (i, j - 1), (i, j), (i, j + 1), (i, j + 2),
    #       (i + 1, j - 2), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1), (i + 1, j + 2),
    #       (i + 2, j - 2), (i + 2, j - 1), (i + 2, j), (i + 2, j + 1), (i + 2, j + 2)]
    return [
        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
        (i, j - 1), (i, j), (i, j + 1),
        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
                ]
def rk_random_move():
    #time.sleep(0.5)
    rkij = gl.get_value("rkij")
    lmij = gl.get_value("lmij")
    poij = gl.get_value("poij")
    RK = gl.get_value("RK")
    xx = gl.get_value("xx")
    yy = gl.get_value("yy")
    r = random.randint(0, 7)
    pos = index_to_xy([rkij[0]+xx[r], rkij[1]+yy[r]])
    cv = gl.get_value("cv")
    #pos = index_to_xy([rkij[0]+1, rkij[1]+1])
    #cv.coords(RK, pos[0], pos[1])

    if if_in_range(rkij[0]+xx[r], rkij[1]+yy[r]):
        if(rkij[0]+xx[r]!=lmij[0] and rkij[1]+yy[r]!=lmij[1]):
            if(rkij[0]+xx[r]!=poij[0] and rkij[1]+yy[r]!=poij[1]):
                cv = gl.get_value("cv")
                cv.coords(RK, pos[0], pos[1])
                gl.set_value("rkij", [rkij[0]+xx[r], rkij[1]+yy[r]])

def erase_lines():
    cv = gl.get_value("cv")
    for i in lines.lines:
        cv.delete(i)
    lines.lines = []

def PO_move(i, j):
    aux = index_to_xy([i+1, j+1])
    cv = gl.get_value("cv")
    PO = gl.get_value("PO")
    po_cnt = gl.get_value("po_cnt")
    po_cnt.set(int(po_cnt.get())+1)
    cv.coords(PO, (aux[0], aux[1]))
    gl.set_value("poij", [i+1, j+1])
def order(t):
    if t > 0:
        return 1
    if t < 0:
        return -1
    return 0

def rk_follow():
    rkij = gl.get_value("rkij")
    poij = gl.get_value("poij")
    lmij = gl.get_value("lmij")
    RK = gl.get_value("RK")
    cv = gl.get_value("cv")
    add_row = order(lmij[0] - rkij[0])
    add_col = order(lmij[1] - rkij[1])
    if if_in_range(rkij[0] + add_row, rkij[1] + add_col):
        aux = index_to_xy([rkij[0] + add_row, rkij[1] + add_col])
        cv.coords(RK, (aux[0], aux[1]))
        gl.set_value("rkij", [rkij[0] + add_row, rkij[1] + add_col])

def obstacle(x, y):
    gl.set_value("if_obs", True)
    print("in utils.obs")
    nr = gl.get_value("nr")
    nc = gl.get_value("nc")
    rkij = gl.get_value("rkij")
    lmij = gl.get_value("lmij")
    poij = gl.get_value("poij")
    m = Map(int(nr), int(nc))
    m.set_obstacle(utils.set_obstacle(rkij))
    start = m.map[poij[0] - 1][poij[1] - 1]
    end = m.map[lmij[0] - 1][lmij[1] - 1]
    gl.set_value("end", end)
    lines.lines = []
    dstar = Dstar(m)
    dstar.run(start, end)


    #print("dstar.run...")
    dstar.run(start, end)

