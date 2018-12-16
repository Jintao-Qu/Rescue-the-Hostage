import tkinter as tk
import init
import global_pic as gc
import global_var as gl
gl._init_globalar()
gc._init_globalpic()
root = tk.Tk()
gl.set_value("root", root)
init.init_var()
init.init_root(root)
root.mainloop()