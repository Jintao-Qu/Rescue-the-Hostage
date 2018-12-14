import tkinter as tk
cnt = 0
def change(event):
    global cnt
    cnt += 1
    text.set(str(cnt))

root = tk.Tk()
B = tk.Button(root, text="点击")
B.bind("<Button-1>", change)
text = tk.StringVar()
text.set("0")
S = tk.Label(root, bg="green", textvariable=text)
B.pack(side=tk.LEFT)
S.pack(side=tk.RIGHT)
root.mainloop()