import tkinter as tk
from PIL import Image, ImageTk
import global_pic as gc

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
