import tkinter as tk
from PIL import Image, ImageTk
import global_pic as gc
import global_var as gl

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
    aux = 460 - (ver_int * (nr - 1) + nr)
    top_lef = int(aux/2 + 20)
    btm_lef = int(aux - top_lef + 20)

    lev_int = int((560 - nc)/(nc - 1))
    aux = 560 - (lev_int * (nc - 1) + nc)
    lef_lef = int(aux/2 + 20)
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
    cv.place(relx=0.04, rely=0.08)