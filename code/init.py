import tkinter as tk
from PIL import Image, ImageTk
import global_pic as gc
import utils
import pygame
import load_wid as lw
import commands as cmd
import global_var as gl
def init_pic():
    #ARROW
    arrow = Image.open("img/direction.png")
    gc.set_value("arrow", arrow)

    arrow1 = Image.open("img/direction1.png")
    gc.set_value("arrow1", arrow1)
    utils.generate_arrow()

    #POLICE
    police_big = Image.open("img/police_big.png")
    gc.set_value("police_big", police_big)
    police_bigTK = ImageTk.PhotoImage(police_big)
    gc.set_value("police_bigTK", police_bigTK)
    police = Image.open("img/police.png")
    gc.set_value("police", police)
    policeTK = ImageTk.PhotoImage(police)
    gc.set_value("policeTK", policeTK)
    #RK
    rk = Image.open("img/rk.png")
    gc.set_value("rk", rk)
    rkTK = ImageTk.PhotoImage(rk)
    gc.set_value("rkTK", rkTK)

    #block
    board = Image.open("img/board.png")
    gc.set_value("board", board)
    boardTK = ImageTk.PhotoImage(board)
    gc.set_value("boardTK", boardTK)

    #music
    voiceon = Image.open("img/voiceon.png")
    gc.set_value("voiceon", voiceon)
    voiceonTK = ImageTk.PhotoImage(voiceon)
    gc.set_value("voiceonTK", voiceonTK)

    voiceoff = Image.open("img/voiceoff.png")
    gc.set_value("voiceoff", voiceoff)
    voiceoffTK = ImageTk.PhotoImage(voiceoff)
    gc.set_value("voiceoffTK", voiceoffTK)
    #setting
    setting = Image.open("img/setting.png")
    gc.set_value("setting", setting)
    settingTK = ImageTk.PhotoImage(setting)
    gc.set_value("settingTK", settingTK)
    #start
    start = Image.open("img/start.png")
    gc.set_value("start", start)
    startTK = ImageTk.PhotoImage(start)
    gc.set_value("startTK", startTK)
    #restart
    restart = Image.open("img/restart.png")
    gc.set_value("restart", restart)
    restartTK = ImageTk.PhotoImage(restart)
    gc.set_value("restartTK", restartTK)
    #small_pic
    police_s = Image.open("img/police_s.png")
    gc.set_value("police_s", police_s)
    police_sTK = ImageTk.PhotoImage(police_s)
    gc.set_value("police_sTK", police_sTK)

    rk_s = Image.open("img/rk_s.png")
    gc.set_value("rk_s", rk_s)
    rk_sTK = ImageTk.PhotoImage(rk_s)
    gc.set_value("rk_sTK", rk_sTK)

    lm_s = Image.open("img/lm_s.png")
    gc.set_value("lm_s", lm_s)
    lm_sTK = ImageTk.PhotoImage(lm_s)
    gc.set_value("lm_sTK", lm_sTK)
    #exit_pic
    exit = Image.open("img/exit.png")
    gc.set_value("exit", exit)
    exitTK = ImageTk.PhotoImage(exit)
    gc.set_value("exitTK", exitTK)
def init_root(root):
    init_pic()
    root.geometry("1000x618")
    root.title(" SMC 拯救小拉姆")
    root.resizable(width=False, height=False)
    root.iconbitmap("img/ico.ico")
    #root['bg'] = '#'
    root.attributes("-toolwindow", 0)  # 工具栏样式
    root.attributes("-transparentcolor", "red")
    root.attributes("-transparentcolor", "blue")
    root.attributes("-alpha", 0.9)
    lw.load_map()
    lw.load_arrow()
    lw.load_rolelable()
    lw.load_music_button()
    lw.load_setting_button()
    lw.load_start_button()
    lw.load_restart_button()
    lw.load_jintao()
    lw.load_hint()
    lw.load_sel_role()

    #root.mainloop()

def init_var():
    gl.set_value("sp", 1)
    gl.set_value("sr", 1)
    gl.set_value("nr", 5)
    gl.set_value("nc", 7)
    gl.set_value("xx", [0, 1, 1, 1, 0, -1, -1, -1])
    gl.set_value("yy", [1, 1, 0, -1, -1, -1, 0, 1])

    gl.set_value("if_start", False)
    gl.set_value("MODE", 2)