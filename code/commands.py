import tkinter as tk
import winsound
import global_var as gl
import pygame
import commands as cmd
import global_pic as gc
import utils
def up():
    if gl.get_value("if_start") == False:
        utils.move(gl.get_value("sel_role"), -1, 0)

def up1():
    if gl.get_value("if_start") == False:
        utils.move(gl.get_value("sel_role"), -1, -1)

def lef():
    if gl.get_value("if_start") == False:
        utils.move(gl.get_value("sel_role"), 0, -1)

def lef1():
    if gl.get_value("if_start") == False:
        utils.move(gl.get_value("sel_role"), 1, -1)
    return

def dwn():
    if gl.get_value("if_start") == False:
        utils.move(gl.get_value("sel_role"), 1, 0)

def dwn1():
    if gl.get_value("if_start") == False:
        utils.move(gl.get_value("sel_role"), 1, 1)

def rig():
    if gl.get_value("if_start") == False:
        utils.move(gl.get_value("sel_role"), 0, 1)

def rig1():
    if gl.get_value("if_start") == False:
        utils.move(gl.get_value("sel_role"), -1, 1)

def music_on_off():
    cnt = gl.get_value("music_ctrl")
    gl.set_value("music_ctrl", cnt * (-1))
    if cnt * (-1) > 0:
        filename = 'music/Farm.wav'
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(loops=-1, start=0.0)
        music_button = gl.get_value("music_button")
        music_button.config(image=gc.get_value("voiceonTK"))
    else:
        pygame.mixer.music.stop()
        music_button = gl.get_value("music_button")
        music_button.config(image=gc.get_value("voiceoffTK"))


def setting():
    top = tk.Toplevel()
    top.title("游戏设置")
    top.geometry("255x160")
    top.attributes()
    top.resizable(width=False, height=False)
    top.iconbitmap("img/ico.ico")
    gl.set_value("top", top)
    buchang = tk.Label(top, text="速度：", bd=0)
    buchang.place(relx=0.08, rely=0.08)


    pol_sped_lable = tk.Label(top, image=gc.get_value("policeTK"), width=20, height=20)
    pol_sped_lable.place(relx=0.1, rely=0.22)
    pol_sped = tk.Spinbox(top, bd=0, from_=1, to=2, increment=1, width=6)
    gl.set_value("pol_sped", pol_sped)
    pol_sped.place(relx=0.23, rely=0.24)

    rk_sped_lable = tk.Label(top, image=gc.get_value("rkTK"), width=20, height=20)
    rk_sped_lable.place(relx=0.55, rely=0.22)
    rk_sped = tk.Spinbox(top, bd=0, from_=1, to=2, increment=1, width=6)
    gl.set_value("rk_sped",rk_sped)
    rk_sped.place(relx=0.68, rely=0.24)

    dituguimo = tk.Label(top, text="地图规模：", bd=0)
    dituguimo.place(relx=0.08, rely=0.45)

    hang = tk.Label(top, text="行：", bd=0)
    hang.place(relx=0.08, rely=0.61)
    row = tk.Spinbox(top, bd=0, from_=5, to=10, increment=1, width=6)
    row.place(relx=0.23, rely=0.61)
    gl.set_value("row",row)

    lie = tk.Label(top, text="列：", bd=0)
    lie.place(relx=0.53, rely=0.61)
    col = tk.Spinbox(top, bd=0, from_=7, to=14, increment=1, width=6)
    col.place(relx=0.68, rely=0.61)
    gl.set_value("col", col)

    doublebutton = tk.Button(top, text="双人游戏", relief=tk.RAISED, bd=1, command=setting_config_double)
    doublebutton.place(relx=0.6, rely=0.8)
    singlebutton = tk.Button(top, text="自动营救", relief=tk.RAISED, bd=1, command=setting_config_single)
    singlebutton.place(relx=0.2, rely=0.8)

def setting_config_double():
    pol_sped = gl.get_value("pol_sped")
    rk_sped = gl.get_value("rk_sped")
    row = gl.get_value("row")
    col = gl.get_value("col")

    gl.set_value("sp", pol_sped.get())
    gl.set_value("sr", rk_sped.get())
    gl.set_value("nr", row.get())
    gl.set_value("nc", col.get())

    gl.set_value("MODE", 2)
    cmd.redraw()
    top = gl.get_value("top")
    top.destroy()
def setting_config_single():
    pol_sped = gl.get_value("pol_sped")
    rk_sped = gl.get_value("rk_sped")
    row = gl.get_value("row")
    col = gl.get_value("col")

    gl.set_value("sp", pol_sped.get())
    gl.set_value("sr", rk_sped.get())
    gl.set_value("nr", row.get())
    gl.set_value("nc", col.get())

    gl.set_value("MODE", 1)
    cmd.redraw()
    top = gl.get_value("top")
    top.destroy()
def redraw():
    root = gl.get_value("root")
    cv = tk.Canvas(root, bg='#AFEEEE', width=600, height=500)
    gl.set_value("cv", cv)
    utils.draw_map()

def start():
    HINT = gl.get_value("HINT")
    HINT.set("游戏开始！")
    gl.set_value("if_start", True)

def sel_role():
    sel_role = gl.get_value("sel_role")
    sel_role = (sel_role + 1) % 3
    gl.set_value("sel_role", sel_role)
    HINT = gl.get_value("HINT")
    sel_role_button = gl.get_value("sel_role_button")

    if(gl.get_value("if_start")==False):
        if sel_role == 0:
            sel_role_button.config(image=gc.get_value("rk_sTK"))
            HINT.set("设置RK的位置")
        elif sel_role == 1:
            sel_role_button.config(image=gc.get_value("police_sTK"))
            HINT.set("设置警察的位置")
        elif sel_role == 2:
            sel_role_button.config(image=gc.get_value("lm_sTK"))
            HINT.set("设置小拉姆的位置")



