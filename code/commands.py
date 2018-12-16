import tkinter as tk
import winsound
import global_var as gl
import pygame
import global_pic as gc

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
    top.geometry("250x155")
    top.attributes()
    top.resizable(width=False, height=False)
    top.iconbitmap("img/ico.ico")
    gl.set_value("top", top)
    buchang = tk.Label(top, text="速度：", bd=0)
    buchang.place(relx=0.08, rely=0.08)


    pol_sped_lable = tk.Label(top, image=gc.get_value("policeTK"), width=20, height=20)
    pol_sped_lable.place(relx=0.1, rely=0.22)
    pol_sped = tk.Spinbox(top, bd=0, from_=1, to=2, increment=1, width=6)
    gl.set_value("pol_sped",pol_sped)
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
    gl.set_value("col",col)

    okbutton = tk.Button(top, text="OK！", relief=tk.RAISED, bd=1, command=setting_config)
    okbutton.place(relx=0.8, rely=0.8)

def setting_config():
    pol_sped = gl.get_value("pol_sped")
    rk_sped = gl.get_value("rk_sped")
    row = gl.get_value("row")
    col = gl.get_value("col")

    gl.set_value("sp", pol_sped.get())
    gl.set_value("sr", rk_sped.get())
    gl.set_value("nr", row.get())
    gl.set_value("nc", col.get())

    top = gl.get_value("top")
    top.destroy()
