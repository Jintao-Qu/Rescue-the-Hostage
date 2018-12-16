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
def init_root(root):
    init_pic()
    root.geometry("1000x618")
    root.title(" SMC 拯救人质")
    root.resizable(width=False, height=False)
    root.iconbitmap("img/ico.ico")
    #root['bg'] = '#'
    root.attributes("-toolwindow", 0)  # 工具栏样式
    root.attributes("-transparentcolor", "red")
    root.attributes("-transparentcolor", "blue")
    root.attributes("-alpha", 0.9)
    lw.load_arrow()
    lw.load_rolelable()
    lw.load_music_button()
    lw.load_setting_button()
    lw.load_start_button()
    lw.load_restart_button()
    lw.load_map()


    root.mainloop()
