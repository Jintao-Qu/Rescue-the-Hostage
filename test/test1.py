import tkinter as tk
cnt = 0
def change():
    global cnt
    global root
    cnt += 1
    text.set(str(cnt))
    root.geometry("100x100")

tag = 0  # tag标记该轮哪家走，0代表黑方，1代表白方
stop = 0
num = 18  # 棋盘网格数量
K = 0.9  # 点击的灵敏度 0~1 之间
mesh = round(400 / num)
Qr = 0.45 * mesh  # 棋子的大小，前面的系数在0~0.5之间选取
px = 5
py = 50
wide = 60
high = 30
key = ["黑方", "白方"]
color = ["black", "white"]
root = tk.Tk()
root.geometry("1000x500")
text = tk.StringVar()
text.set("0")
B = tk.Button(root, text="点击", command=change)
#B.bind("<Button-1>", change)
S = tk.Label(root, bg="green", textvariable=text)
B.pack(side=tk.LEFT)
S.pack(side=tk.RIGHT)
asdf = tk.Canvas(root, width=(num + 1) * mesh + 2 * px, height=(num + 1) * mesh + py + px,bg="red")
asdf.place(x=50, y=50)
root.mainloop()