import tkinter as tk
from PIL import Image, ImageTk
import global_pic as gc
import utils
import pygame
import commands as cmd
import global_var as gl

def load_arrow():
    root = gl.get_value("root")
    up = tk.Button(root, image=gc.get_value("up_arrowTK"), relief=tk.FLAT, bd=0)
    lef = tk.Button(root, image=gc.get_value("lef_arrowTK"), relief=tk.FLAT, bd=0)
    dwn = tk.Button(root, image=gc.get_value("dwn_arrowTK"), relief=tk.FLAT, bd=0)
    rig = tk.Button(root, image=gc.get_value("rig_arrowTK"), relief=tk.FLAT, bd=0)
    up1 = tk.Button(root, image=gc.get_value("up_arrow1TK"), relief=tk.FLAT, bd=0)
    lef1 = tk.Button(root, image=gc.get_value("lef_arrow1TK"), relief=tk.FLAT, bd=0)
    dwn1 = tk.Button(root, image=gc.get_value("dwn_arrow1TK"), relief=tk.FLAT, bd=0)
    rig1 = tk.Button(root, image=gc.get_value("rig_arrow1TK"), relief=tk.FLAT, bd=0)
    up.place(relx=0.8, rely=0.6)
    lef.place(relx=0.731, rely=0.7)
    dwn.place(relx=0.8, rely=0.8)
    rig.place(relx=0.869, rely=0.7)
    up1.place(relx=0.731, rely=0.598)
    lef1.place(relx=0.731, rely=0.81)
    dwn1.place(relx=0.872, rely=0.81)
    rig1.place(relx=0.872, rely=0.598)

def load_rolelable():
    root = gl.get_value("root")
    police_lable_img = tk.Label(root, image=gc.get_value("policeTK"), width=70, height=70)
    police_lable = tk.Label(root, image=gc.get_value("boardTK"), font=("Helvetica", 34, "bold"), text="125", compound=tk.CENTER, height=60)
    police_lable_img.place(relx=0.7, rely=0.07)
    police_lable.place(relx=0.8, rely=0.07)

    rk_lable_img = tk.Label(root, image=gc.get_value("rkTK"), width=50, height=50)
    rk_lable = tk.Label(root, image=gc.get_value("boardTK"), text="89", font=("Helvetica", 34, "bold"), compound=tk.CENTER, height=60)
    rk_lable_img.place(relx=0.713, rely=0.21)
    rk_lable.place(relx=0.8, rely=0.2)

def load_music_button():
    root = gl.get_value("root")
    music_button = tk.Button(root, image=gc.get_value("voiceoffTK"), relief=tk.FLAT, bd=0, command=cmd.music_on_off)
    gl.set_value("music_ctrl", -1)
    gl.set_value("music_button", music_button)
    music_button.place(relx=0.94, rely=0.4)

def load_setting_button():
    root = gl.get_value("root")
    setting_button = tk.Button(root, image=gc.get_value("settingTK"), relief=tk.FLAT, bd=0, command=cmd.setting)
    setting_button.place(relx=0.94, rely=0.5)
