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
