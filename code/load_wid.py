import tkinter as tk
from PIL import Image, ImageTk
import global_pic as gc
import utils
import pygame
import commands as cmd
import global_var as gl

def load_arrow():
    root = gl.get_value("root")
    up = tk.Button(root, image=gc.get_value("up_arrowTK"), relief=tk.FLAT, bd=0, command=cmd.up)
    lef = tk.Button(root, image=gc.get_value("lef_arrowTK"), relief=tk.FLAT, bd=0, command=cmd.lef)
    dwn = tk.Button(root, image=gc.get_value("dwn_arrowTK"), relief=tk.FLAT, bd=0, command=cmd.dwn)
    rig = tk.Button(root, image=gc.get_value("rig_arrowTK"), relief=tk.FLAT, bd=0, command=cmd.rig)
    up1 = tk.Button(root, image=gc.get_value("up_arrow1TK"), relief=tk.FLAT, bd=0, command=cmd.up1)
    lef1 = tk.Button(root, image=gc.get_value("lef_arrow1TK"), relief=tk.FLAT, bd=0, command=cmd.lef1)
    dwn1 = tk.Button(root, image=gc.get_value("dwn_arrow1TK"), relief=tk.FLAT, bd=0, command=cmd.dwn1)
    rig1 = tk.Button(root, image=gc.get_value("rig_arrow1TK"), relief=tk.FLAT, bd=0, command=cmd.rig1)
    up.place(relx=0.8, rely=0.6)
    lef.place(relx=0.731, rely=0.7)
    dwn.place(relx=0.8, rely=0.8)
    rig.place(relx=0.869, rely=0.7)
    up1.place(relx=0.731, rely=0.598)
    lef1.place(relx=0.731, rely=0.81)
    dwn1.place(relx=0.872, rely=0.81)
    rig1.place(relx=0.872, rely=0.598)
def load_start_button():
    root = gl.get_value("root")
    start_button = tk.Button(root, image=gc.get_value("startTK"), relief=tk.FLAT, bd=0, command=cmd.start)
    start_button.place(relx=0.72, rely=0.37)
def load_rolelable():
    root = gl.get_value("root")
    po_cnt = tk.StringVar()
    po_cnt.set("0")
    gl.set_value("po_cnt", po_cnt)
    police_lable_img = tk.Label(root, image=gc.get_value("policeTK"), width=70, height=70)
    police_lable = tk.Label(root, image=gc.get_value("boardTK"), font=("Helvetica", 34, "bold"), textvariable=po_cnt, compound=tk.CENTER, height=60)

    police_lable_img.place(relx=0.7, rely=0.07)
    police_lable.place(relx=0.8, rely=0.07)

    rk_cnt = tk.StringVar()
    rk_cnt.set("0")
    gl.set_value("rk_cnt", rk_cnt)
    rk_lable_img = tk.Label(root, image=gc.get_value("rkTK"), width=50, height=50)
    rk_lable = tk.Label(root, image=gc.get_value("boardTK"), textvariable=rk_cnt, font=("Helvetica", 34, "bold"), compound=tk.CENTER, height=60)
    rk_lable_img.place(relx=0.713, rely=0.21)
    rk_lable.place(relx=0.8, rely=0.2)
def load_restart_button():
    root = gl.get_value("root")
    restart_button = tk.Button(root, image=gc.get_value("restartTK"), relief=tk.FLAT, bd=0, command=cmd.restart)
    gl.set_value("restart_button", restart_button)
    restart_button.place(relx=0.92, rely=0.44)
def load_music_button():
    root = gl.get_value("root")
    music_button = tk.Button(root, image=gc.get_value("voiceoffTK"), relief=tk.FLAT, bd=0, command=cmd.music_on_off)
    gl.set_value("music_ctrl", -1)
    gl.set_value("music_button", music_button)
    music_button.place(relx=0.94, rely=0.38)

def load_setting_button():
    root = gl.get_value("root")
    setting_button = tk.Button(root, image=gc.get_value("settingTK"), relief=tk.FLAT, bd=0, command=cmd.setting)
    setting_button.place(relx=0.94, rely=0.5)
def load_map():
    root = gl.get_value("root")
    cv = tk.Canvas(root, bg='#AFEEEE', width=600, height=500)
    gl.set_value("cv", cv)
    utils.draw_map()
    cv.place(relx=0.04, rely=0.08)

def load_jintao():
    root = gl.get_value("root")
    tao_lable = tk.Label(root, bd=0, font=("Helvetica", 9, "bold"), text="Build by Jintao_Qu, 2018",).place(relx=0.025, rely=0.965)

def load_hint():
    root = gl.get_value("root")
    HINT = tk.StringVar()
    HINT.set("摩尔庄园，快乐童年！")
    gl.set_value("HINT", HINT)
    tao_lable = tk.Label(root, bd=0, font=("Helvetica", 9, "bold"), textvariable=HINT)
    tao_lable.place(relx=0.3, rely=0.965)
def load_sel_role():
    # 0->rk, 1->po, 2->lm
    gl.set_value("sel_role", 0)
    root = gl.get_value("root")
    sel_role_button = tk.Button(root, image=gc.get_value("rk_sTK"), relief=tk.FLAT, bd=0, command=cmd.sel_role)

    gl.set_value("sel_role_button", sel_role_button)
    sel_role_button.place(relx=0.815, rely=0.725)